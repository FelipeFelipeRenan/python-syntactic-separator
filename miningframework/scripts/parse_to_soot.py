# This script receives as input the path to a directory generated by the miningframework, it reads the output files and creates a [output]/data/results-soot.csv with the output in a format suported by a SOOT analysis framework

import sys
from csv import DictReader, writer
import os

CLASS_NAME = "className"
METHOD = "method"
LEFT_MODIFICATIONS = "left modifications"
RIGHT_MODIFICATIONS = "right modifications"
COMMIT_SHA = "merge commit"
PROJECT_NAME = "project"
HAS_BUILD = "has_build"

output_path = sys.argv[1].rstrip("/") # get output path passed as cli argument
def export_csv():
    print ("Running parse to soot")
    scenarios = read_output(output_path)
    
    for scenario in scenarios:
        base_path = get_scenario_base_path(scenario)

        if scenario[HAS_BUILD] == "true":
            left_modifications = parse_modifications(scenario[LEFT_MODIFICATIONS])
            right_modifications = parse_modifications(scenario[RIGHT_MODIFICATIONS])
            class_name = scenario[CLASS_NAME]
            method = scenario[METHOD]

            result = []
            result_reverse = []

            for line in left_modifications:
                result.append([class_name, "sink", line])
                result_reverse.append([class_name, "source", line])

            for line in right_modifications:
                result.append([class_name, "source", line])
                result_reverse.append([class_name, "sink", line])

            if result:
                class_method_folder = base_path + "/changed-methods/" + class_name + "/" + method

                if not os.path.exists(class_method_folder):
                    os.makedirs(class_method_folder)

                with open(class_method_folder + "/left-right-lines.csv", "w") as soot, open(class_method_folder + "/right-left-lines.csv", "w") as soot_reverse:
                    soot_writer = writer(soot, delimiter=",")
                    soot_reverse_writer = writer(soot_reverse, delimiter=",")

                    soot_writer.writerows(result)
                    soot_reverse_writer.writerows(result_reverse)



def read_output(output_path):
    with open(output_path + "/data/results-with-build-information.csv", "r") as output_file:
        return list(DictReader(output_file, delimiter=";"))

def parse_modifications(modifications):
    trimmed_input = modifications.strip("[]").replace(" ", "")
    if (len (trimmed_input) > 0):
        return trimmed_input.split(",")
    return []

def get_scenario_base_path(scenario):
    return output_path + "/files/" + scenario[PROJECT_NAME] + "/" + scenario[COMMIT_SHA]

export_csv()