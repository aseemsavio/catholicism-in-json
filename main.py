import json
import pickle
from operator import itemgetter


def read_canon_law() -> list:
    canon_law = pickle.load(open("pickles/canon.pickle", 'rb'))
    law_numbers = [law for law in canon_law]

    canon_law_list = []
    sorted_canon_law_list = []

    for law_num in law_numbers:
        law = canon_law[law_num]

        is_list = law[0]

        if is_list:
            sub_laws = law[1]

            sub_law_numbers = [sub_law for sub_law in sub_laws]

            individual_sub_laws = []

            for n in sub_law_numbers:
                individual_sub_law = {
                    "sub_law_id": int(n),
                    "sub_law_text": sub_laws[n]
                }
                individual_sub_laws.append(individual_sub_law)

            sorted_individual_sub_laws = sorted(individual_sub_laws, key=itemgetter('sub_law_id'))
            law_object = {
                "law_id": int(law_num),
                "sub_laws": sorted_individual_sub_laws
            }

            canon_law_list.append(law_object)

        else:
            law_text = law[1]
            law_object = {
                "law_id": int(law_num),
                "law_text": law_text
            }
            canon_law_list.append(law_object)

    sorted_canon_law_list = sorted(canon_law_list, key=itemgetter("law_id"))
    return sorted_canon_law_list


if __name__ == '__main__':
    canon = read_canon_law()
    with open("canon.json", "w") as outfile:
        json.dump(canon, outfile)
