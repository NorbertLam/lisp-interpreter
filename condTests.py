import unittest
from tokenizer import tokenize
from parse import evaluate


class TestCond(unittest.TestCase):

    def test_cond_basic(self):
        exp = tokenize("(define cats 5)(define dogs 6)(define birds 5)"
                       "(cond [(eq? cats birds) (+ cats birds)]"
                       "[(eq? cats dogs) (+ cats dogs)][else 0])")
        result = evaluate(exp)
        expected = 10
        self.assertEqual(result, expected)

    def test_cond_else(self):
        exp = tokenize("(define cats 1)(define dogs 2)(define birds 3)"
                       "(cond [(eq? cats birds) (+ cats birds)]"
                       "[(eq? cats dogs) (+ cats dogs)][else 0])")
        result = evaluate(exp)
        expected = 0
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
