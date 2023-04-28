from itertools import permutations

from nltk.tree import *


def get_paraphrases(syntax_tree, limit):
    trees = {"paraphrases": []}
    tree = Tree.fromstring(syntax_tree)
    positions = tree.treepositions()
    for pos in positions:
        try:
            i = tree[pos]
            if not isinstance(i, str):
                if i.label() == "NP":
                    np_counter = 0
                    del_counter = 0
                    for k in i:
                        if k.label() == "NP":
                            np_counter += 1
                        elif k.label() == "," or k.label() == "CC":
                            del_counter += 1

                    if np_counter > 1 and del_counter > 1:
                        el_positions = i.treepositions()

                        np_positions = []
                        np_dct = {}
                        for el_pos in el_positions:
                            el = i[el_pos]

                            if not isinstance(el, str):
                                if el.label() == "NP":
                                    np_positions.append(el_pos)
                                    np_dct[el_pos] = el.copy()

                        combinations = [*permutations([*np_positions[1:]])][1:]

                        for c in combinations:
                            p_tree = tree.copy()
                            for i_el, c_el in zip(np_positions[1:], c):
                                p_tree[pos][i_el] = np_dct[c_el]

                            if len(trees["paraphrases"]) < limit:
                                parse_string = ' '.join(str(p_tree).split())
                                t_dict = {"tree": parse_string}
                                trees["paraphrases"].append(t_dict)
                            else:
                                return trees

        except Exception as ex:
            print(ex)
    return trees
