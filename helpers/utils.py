import json


def create_json_file(destination_file_name: str, source_dict: dict):
    """
    Creates a json file and writes it to the destination provided.

    :param destination_file_name: Destination file name
    :param source_dict: Source dictionary
    :return: None
    """
    with open(destination_file_name, "w") as outfile:
        json.dump(source_dict, outfile)
