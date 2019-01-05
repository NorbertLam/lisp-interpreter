

def evaluate(tree_list):
    values = []

    for tree in tree_list:
        tree_value = evaluate_tree(tree)

        if tree_value:
            values.append(tree_value)

    return values


def evaluate_tree(tree):
    return tree.evaluate()
