import json


def create_json_file(destination_file_name: str, source_dict: dict):
    with open(destination_file_name, "w") as outfile:
        json.dump(source_dict, outfile)
