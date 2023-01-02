import os
import re
from pathlib import Path
import shutil



usual_files = {'template-comparison-CodeSystem.html',
'template-comparison-ValueSet.html',
'template-comparison-index.html',
'template-comparison-CapabilityStatement.html',
'template-comparison.html',
'template-comparison-Profile.html',
'template-comparison-set.html',
'index.html',
'x1ver-paths-r2.json',
'validation-summary.json',
'xver-paths-1.4.json',
'xver-paths-3.0.json',
'ig-r4.json',
'validation-oo.json',
'xver-paths-r2.json',
'xver-paths-5.0.json',
'xver-paths-4.0.json',
'xver-paths-1.0.json'
}


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_data_from_file(file_path):
    text_file = open(file_path, "r")
    data = text_file.read()
    text_file.close()
    return data

def write_data_to_file(data, newfilename ):
    with open(newfilename, "w") as text_file:
        text_file.write(data)
    print("Written file {0}".format(newfilename))

def parse_table_from_index(file_path, subfolder):
    data = get_data_from_file(file_path)
    pat = r"(.*)<table class=\"grid\">(.*)</table>(.*)"
    result = re.match(pat, data, re.DOTALL)
    if result is not None:
        table = result.group(2)
        table = table.replace('<a href="','<a href="' + str(subfolder) + "/")
        return table


def create_new_detailfile(file_path, newfilename):
    data = get_data_from_file(file_path)
    replaced_data = data.replace('href="fhir.css"/>', 'href="../res/fhir.css"/>')
    replaced_data = replaced_data.replace('<img src="', '<img src="../res/')
    write_data_to_file(replaced_data, newfilename)

def write_index_file(index_tables, summary_file):
    document = """<!DOCTYPE HTML>

            <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
            <head>
            <title>Comparing Profiles</title>
            <link rel="stylesheet" href="res/fhir.css"/>
            </head>
            <body>

            <p>Comparing Profiles</p>

            <ul>"""
    for table in index_tables:
        if table is not None:
            document += '<table class="grid">' + table + '</table>'
    document += """"
                </ul>
                </body>
                </html>

                <ul>
                </ul>"""
    write_data_to_file(document, summary_file)

def work_directory(walk_dir):
    print('walk_dir = ' + walk_dir)
    summary_directory = os.path.join(walk_dir,'_summary/')
    summary_file = os.path.join(summary_directory,'index.html')
    create_directory(summary_directory)
    index_tables = []
    for root, _, files in os.walk(walk_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            subfolder =os.path.basename(os.path.dirname((file_path)))
            new_directory = os.path.join(summary_directory,subfolder)
            if filename == "index.html":
                #print("subfolder: {0}".format(subfolder))
                #print(filename)
                index_tables.append(parse_table_from_index(file_path, subfolder))
            elif filename.endswith(".html") and filename not in usual_files:
                create_directory(new_directory)
                new_filename = os.path.join(summary_directory,subfolder,filename)
                create_new_detailfile(file_path, new_filename)
            elif filename.endswith(".json") and filename not in usual_files:
                create_directory(new_directory)
                new_filename = os.path.join(summary_directory,subfolder,filename)
                if file_path != new_filename:
                    shutil.copyfile(file_path, new_filename)


    if(len(index_tables) > 0):
        create_directory(summary_directory)
        write_index_file(index_tables, summary_file)
        if not os.path.exists(os.path.join(summary_directory,'res')):
            shutil.copytree('res/', os.path.join(summary_directory,'res'))

res_dir = 'res/'
root_dir= 'compare_results/'
for fname in os.listdir(root_dir):
    walk_dir = os.path.join(root_dir, fname)
    if os.path.isdir(walk_dir):
        print(walk_dir)
        work_directory(walk_dir)
        continue


