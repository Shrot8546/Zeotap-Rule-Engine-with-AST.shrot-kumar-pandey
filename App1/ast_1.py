# ast.py
class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # "operator" (AND/OR) or "operand" (condition)
        self.value = value  # Value for operand, or None for operators
        self.left = left  # Left child node
        self.right = right  # Right child node

    def to_dict(self):
        """Convert Node to a dictionary format for serialization."""
        return {
            'type': self.type,
            'value': self.value,
            'left': self.left.to_dict() if self.left else None,
            'right': self.right.to_dict() if self.right else None
        }
# ast.py
def evaluate_ast(node, data):
    if node.type == "operand":
        # Check if data matches the operand condition
        return eval_condition(node.value, data)
    elif node.type == "operator":
        left_result = evaluate_ast(node.left, data)
        right_result = evaluate_ast(node.right, data)
        if node.value == "AND":
            return left_result and right_result
        elif node.value == "OR":
            return left_result or right_result
    return False

def eval_condition(condition, data):
    # Parse and evaluate the condition (e.g., "age > 30")
    # against the given data
    pass  # Implement actual comparison logic
