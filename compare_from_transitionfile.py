

import os
import json
import shutil
transition_directory="transitionfiles"
compare_dir = "compare_results"
save_dir = "save"
summary_dir = "_summary"
files = os.listdir(transition_directory)
validator_path = "/home/dev/.fhir/validators/validator_cli_v5_6_89-SNAPSHOT-at2.jar"
ressources_unable_to_process = {'OperationDefinition', 'CodeSystem','NamingSystem','ValueSet'}

def create_folder(fname):
     if not os.path.exists(fname):
        print("[INFO] Creating folder {0}".format(fname))
        os.makedirs(fname)


def getProfileName(url):
    url_split = os.path.split(url)
    profileName = url_split[-1]
    return profileName

def copy_compare_results():
    shutil.rmtree(save_dir)
    shutil.copytree(compare_dir, os.path.join(save_dir, compare_dir), symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=False)

def copy_summary_content():
    for top_fhir_dir in os.listdir(compare_dir):
        current_dir = os.path.join(compare_dir, top_fhir_dir)
        #1. Delete all dirs except _summary
        for profile_dir in os.listdir(current_dir):
            if (profile_dir != summary_dir):
                shutil.rmtree(os.path.join(current_dir, profile_dir))
        #2. Copy content of _summary one level up
        for new_profile_dir in os.listdir(os.path.join(current_dir, summary_dir)):
            shutil.move(os.path.join(current_dir, summary_dir, new_profile_dir), current_dir)

        shutil.rmtree(os.path.join(current_dir, summary_dir))

# Loop to print each filename separately
for filename in files:
    print("[INFO] Reading file '{0}'".format(filename) )
    with open(os.path.join(transition_directory,filename)) as f:
        json_data = json.load(f)
        print("[INFO] Processing File for {0} in Version {1}" .format(json_data['meta']['content']['name'], json_data['meta']['content']['version']))
        #for dependency in json_data['dependencies']:
        #    os.system("fhir install {0} {1} --here".format(dependency['package']['name'],dependency['package']['version'] ))
        for transition in json_data['transitions']:
            try:
                left = transition['transition'][0]['ressource']
                right = transition['transition'][1]['ressource']
                if left['type'] in ressources_unable_to_process:
                    print("[INFO] Type is '{0}'. Skipping".format(left['type']))
                else:
                    print("[INFO] Comparing file {0} v{1} with file {2} v{3}...".format(left['name'],left['version'],right['name'],right['version']))
                    destination_to = "./compare_results/{0}/{1}".format(right['package'],getProfileName(right['url']), left['name'])
                    packages = "-ig {0}#{1} -ig {2}#{3}".format(left['package'],left['version'],right['package'],right['version'])
                    left_string = "{0}|{1}".format(left['url'],left['version'])
                    right_string = "{0}|{1}".format(right['url'],right['version'])

                    executestring_to = "java -jar {0} -compare -tx n/a -proxy 192.168.110.10:3128 -dest \"{1}\" -version 4.0.1 {2} -left \"{3}\" -right \"{4}\"".format(validator_path, destination_to, packages,left_string,right_string)


                    create_folder(destination_to+"/script")
                    f = open(os.path.join(destination_to+"/script/"+ "execute_script.sh"),"w")
                    f.writelines("#!/bin/bash\n")
                    f.writelines(executestring_to +"\n")
                    f.close()
                    if not os.path.isfile(destination_to+"/index.html" ):
                        os.system(executestring_to)

                    else:
                        print("[INFO] index.html file found. Skipping")
            except KeyboardInterrupt:
                print('interrupted!')
                break

# Copy the results to save folder
copy_compare_results()

# Run Compress script
os.system("compress_result.py")

# Copy _summary-content to level up
copy_summary_content()