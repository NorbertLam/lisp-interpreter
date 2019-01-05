import argparse
import sys
from tokenizer import tokenize
from tokenParser import parse_multiple_expression
from evaluator import evaluate


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--command')
parser.add_argument('filename', nargs='?', type=argparse.FileType('r'))
args = parser.parse_args()

if args.filename:
    evaluation = evaluate(parse_multiple_expression(
        tokenize(
            args.filename.read()
        )))

    for value in evaluation:
        print(value)

elif args.command:
    evaluation = evaluate(parse_multiple_expression(tokenize(args.command)))

    for value in evaluation:
        print(value)

else:
    sys.stderr.write("Usage: python main.py exp")
    sys.exit(1)
