# rule_parser.py
import re
from ast import Node

def tokenize(rule_string):
    """Convert the rule string into individual tokens."""
    tokens = re.findall(r'\w+|[()=><!&|]', rule_string)
    return tokens

def parse_expression(tokens):
    """Recursively parse tokens to create an AST."""
    # Implement parsing logic for AND, OR, comparisons
    pass

def parse_rule(rule_string):
    tokens = tokenize(rule_string)
    return parse_expression(tokens)
