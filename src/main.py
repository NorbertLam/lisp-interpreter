from tokenizer import tokenize
from evaluator import evaluate_multiple_expression
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--command')
parser.add_argument('filename', nargs='?', type=argparse.FileType('r'))
args = parser.parse_args()

if args.filename:
    with args.filename as file:
        for line in file:
            print(evaluate_multiple_expression(tokenize(line)))
elif args.command:
    print(evaluate_multiple_expression(tokenize(args.command)))
