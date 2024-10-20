# tests.py
import unittest
from rule_parser import parse_rule

class RuleEngineTest(unittest.TestCase):
    def test_create_rule(self):
        rule_string = "age > 30 AND department = 'Sales'"
        ast = parse_rule(rule_string)
        self.assertIsNotNone(ast)
        self.assertEqual(ast.type, 'AND')

if __name__ == '__main__':
    unittest.main()
