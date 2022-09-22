import json
import pickle
from operator import itemgetter

from helpers.utils import create_json_file


def read_canon_law() -> list:
    """
    Reads the canon.pickle file.
    :return: a list of Canon Law
    """
    canon_law_from_pickle = pickle.load(open("pickles/canon.pickle", 'rb'))
    law_numbers = [law for law in canon_law_from_pickle]

    canon_law_list = []

    for law_num in law_numbers:
        law = canon_law_from_pickle[law_num]

        is_list = law[0]

        if is_list:
            sub_laws = law[1]

            sub_law_numbers = [sub_law for sub_law in sub_laws]

            individual_sub_laws = []

            for n in sub_law_numbers:
                individual_sub_law = {
                    "id": int(n),
                    "text": sub_laws[n]
                }
                individual_sub_laws.append(individual_sub_law)

            sorted_individual_sub_laws = sorted(individual_sub_laws, key=itemgetter('id'))
            law_object = {
                "id": int(law_num),
                "sub_laws": sorted_individual_sub_laws
            }

            canon_law_list.append(law_object)

        else:
            law_text = law[1]
            law_object = {
                "id": int(law_num),
                "text": law_text
            }
            canon_law_list.append(law_object)

    sorted_canon_law_list = sorted(canon_law_list, key=itemgetter("id"))
    return sorted_canon_law_list


def read_catechism() -> list:
    """
    Reads the catechism.pickle file.
    :return: a list of catechism paragraphs.
    """
    catechism_from_pickle = pickle.load(open("pickles/catechism.pickle", 'rb'))
    catechism_paragraph_numbers = [number for number in catechism_from_pickle]

    catechism_list = []

    for paragraph_number in catechism_paragraph_numbers:
        paragraph = catechism_from_pickle[paragraph_number]
        text = paragraph[0]
        paragraph_object = {
            "id": int(paragraph_number),
            "text": text
        }
        catechism_list.append(paragraph_object)

    return sorted(catechism_list, key=itemgetter("id"))


def read_general_instruction_of_the_roman_missal() -> list:
    """
    Reads the girm.pickle file.
    :return: List of girm paragraphs
    """
    girm_from_pickle = pickle.load(open("pickles/girm.pickle", 'rb'))
    girm_ids = [girm_id for girm_id in girm_from_pickle]

    girm_list = []

    for girm_id in girm_ids:
        single_girm_object = girm_from_pickle[girm_id]
        text = single_girm_object[0]
        girm_object = {
            "id": int(girm_id),
            "text": text
        }
        girm_list.append(girm_object)

    return sorted(girm_list, key=itemgetter("id"))


if __name__ == '__main__':
    canon = read_canon_law()
    create_json_file("canon.json", canon)

    catechism = read_catechism()
    create_json_file("catechism.json", catechism)

    girm = read_general_instruction_of_the_roman_missal()
    create_json_file("girm.json", girm)
