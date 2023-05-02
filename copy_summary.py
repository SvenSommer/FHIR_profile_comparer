import os, shutil

compare_dir = "compare_results"
save_dir = "save"
summary_dir = "_summary"

def copy_summary_content():
    for top_fhir_dir in os.listdir(compare_dir):
        current_dir = os.path.join(compare_dir, top_fhir_dir)

        if (not os.path.isdir(current_dir)):
            break

        #1. Delete all dirs except _summary
        for profile_dir in os.listdir(current_dir):

            lower_dir = os.path.join(current_dir, profile_dir)

            if (not os.path.isdir(lower_dir)):
                break

            if (profile_dir != summary_dir):
                shutil.rmtree(lower_dir)

        #2. Copy content of _summary one level up
        for new_profile_dir in os.listdir(os.path.join(current_dir, summary_dir)):
            shutil.move(os.path.join(current_dir, summary_dir, new_profile_dir), current_dir)

        shutil.rmtree(os.path.join(current_dir, summary_dir))

copy_summary_content()