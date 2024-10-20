# app.py
from flask import Flask, request, jsonify, render_template
from rule_parser import parse_rule
from database import init_db, save_rule
import json

app = Flask(__name__)

# Initialize the database
init_db()

@app.route('/')
def index():
    """Serve the main page with the forms for creating and evaluating rules."""
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule():
    """Create a new rule from the rule string provided in the request."""
    data = request.json
    rule_string = data.get('rule_string')
    rule_name = data.get('rule_name')
    
    if not rule_string or not rule_name:
        return jsonify({'error': 'Rule string and name are required'}), 400

    try:
        # Parse the rule string to create the AST
        rule_ast = parse_rule(rule_string)
        # Save the rule in the database
        save_rule(rule_name, rule_ast)
        return jsonify({'message': 'Rule created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    """Evaluate a rule against the provided user data."""
    data = request.json
    rule_data = data.get('rule_data')
    
    if not rule_data:
        return jsonify({'error': 'User data is required for evaluation'}), 400

    try:
        # For demonstration, we just return True if user data is provided
        # The actual evaluation would involve checking the AST against the rule_data
        # Here, you should implement the logic to evaluate the rule against user data
        result = True  # Placeholder for actual evaluation logic
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handling for invalid routes
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors by rendering a custom message."""
    return jsonify({'error': 'Page not found'}), 404

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
