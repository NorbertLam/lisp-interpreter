import argparse
import sys
from tokenizer import tokenize
from evaluator import evaluate_multiple_expression


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--command')
parser.add_argument('filename', nargs='?', type=argparse.FileType('r'))
args = parser.parse_args()

if args.filename:
    print(evaluate_multiple_expression(tokenize(args.filename.read())))
elif args.command:
    print(evaluate_multiple_expression(tokenize(args.command)))
else:
    sys.stderr.write("Usage: python main.py exp")
    sys.exit(1)
