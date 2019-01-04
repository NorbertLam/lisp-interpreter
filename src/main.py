import argparse
import sys
from tokenizer import tokenize
from tokenParser import evaluate_multiple_expression
from evaluator import evaluate


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--command')
parser.add_argument('filename', nargs='?', type=argparse.FileType('r'))
args = parser.parse_args()

if args.filename:
    print(evaluate(evaluate_multiple_expression(tokenize(args.filename.read()))))
elif args.command:
    print(evaluate(evaluate_multiple_expression(tokenize(args.command))))
else:
    sys.stderr.write("Usage: python main.py exp")
    sys.exit(1)
