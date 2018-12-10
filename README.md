# lisp-interpreter
 A Lisp interpreter written in python. Takes in an expression and converts it into tokens to be evaluated. 
 Supports mathematical calculations, booleans, definitions, and conditionals. 
 Tests are written with python unittest and ran with a bash script.

# Usage
```
python3 main.py expression
```

# Examples
```
python3 main.py "(not #t)"
False

python3 main.py "(+ 10 (* 2 (/ 72 (- 6 3))))"
58

python3 main.py "(define cats 5)(define dogs 6)(define birds 5)(cond [(eq? cats birds)(+ cats birds)] [(eq? cats dogs)(+ cats dogs)] [else 0])"
10
```

# Running Tests
```
./test
```
