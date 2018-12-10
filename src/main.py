import sys
from tokenizer import tokenize
from evalTokens import evaluate_tokens

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(evaluate_tokens(tokenize(sys.argv[1])))
    else:
        sys.stderr.write("Usage: python main.py exp")
        sys.exit(1)
