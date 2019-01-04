

def evaluate(tree_list):
    output = None
    for tree in tree_list:
        output = evaluate_tree(tree)
    return output


def evaluate_tree(tree):
    return tree.evaluate()
