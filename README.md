
# Rule Engine with Abstract Syntax Tree (AST)

## Overview
This project implements a dynamic rule engine application that uses an Abstract Syntax Tree (AST) to determine user eligibility based on various attributes like age, department, income, and experience. The rule engine supports creating, combining, modifying, and evaluating rules in real time. 

## Features
- **Create Rules:** Users can define rules using logical expressions (e.g., `"age > 30 AND department = 'Sales'"`).
- **Combine Rules:** Multiple rules can be combined into one AST for efficient evaluation.
- **Evaluate Rules:** Evaluate the rules against user data to check if conditions are met.
- **Dynamic Rule Modifications:** Modify existing rules with ease.
- **Error Handling:** Robust handling of invalid rule strings and conditions.
- **REST API:** Backend API endpoints to create, modify, delete, and evaluate rules.

## Project Structure
rule_engine/ ├── app.py # Flask server and API endpoints ├── ast.py # AST Node implementation ├── rule_parser.py # Rule parsing and AST creation ├── database.py # Database setup and interaction ├── tests.py # Unit tests for the rule engine ├── static/ # Static files (JavaScript, CSS) │ ├── app.js # JavaScript for handling frontend functionality │ └── style.css # Basic styling ├── templates/ # HTML templates │ └── index.html # Main frontend page └── README.md # Documentation (this file)

markdown
Copy code

## Technologies Used
- **Backend:** Python, Flask
- **Frontend:** HTML, JavaScript, CSS
- **Database:** SQLite
- **Other Libraries:** APScheduler (for background tasks), requests (if needed for HTTP requests)

## Setup Instructions

### Prerequisites
- Python 3.x
- `pip` (Python package installer)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/rule-engine-with-ast.git
   cd rule-engine-with-ast
Install the required dependencies:

bash
Copy code
pip install flask requests apscheduler
Initialize the database: The database will be created automatically when running the application, but you can manually create it by running:

bash
Copy code
python -c "from database import init_db; init_db()"
Run the application: Start the Flask server using:

bash
Copy code
python app.py
The server will be available at http://localhost:5000.

Running the Tests
To run unit tests:

bash
Copy code
python -m unittest tests.py
Usage Guide
1. Create a Rule
Send a POST request to /create_rule with a JSON body containing:

json
Copy code
{
    "rule_string": "(age > 30 AND department = 'Sales') OR (salary > 50000)",
    "rule_name": "Sales Eligibility"
}
Response:

201 Created if the rule is successfully created.
400 Bad Request for invalid input.
500 Internal Server Error if there is an unexpected issue.
2. Evaluate a Rule
Send a POST request to /evaluate_rule with a JSON body containing:

json
Copy code
{
    "rule_data": {
        "age": 35,
        "department": "Sales",
        "salary": 60000
    }
}
Response:

200 OK with the result (true or false).
400 Bad Request for invalid input.
500 Internal Server Error if there is an unexpected issue.
3. Combine Rules
The API can be extended to combine multiple rules using logical operators (AND, OR). This would require additional endpoints (e.g., /combine_rules).

Architecture
1. AST (Abstract Syntax Tree)
Node Structure: Represents logical expressions with operators (AND/OR) and conditions (e.g., age > 30).
Tree Traversal: Used for evaluating user data against the rules.
2. Flask API
Endpoints:
/create_rule: To create a rule and store it in the database.
/evaluate_rule: To evaluate user data against a specified rule.
3. Database
SQLite: Used for storing rules and their AST representations.
Tables:
rules: Stores rule metadata and serialized AST.
Frontend
Templates
templates/index.html: The main HTML file with forms for creating and evaluating rules.
JavaScript (static/app.js)
Handles form submissions for creating and evaluating rules.
Communicates with the Flask backend via fetch API.
Styling (static/style.css)
Basic CSS styling for forms and buttons.
Advanced Features (Optional)
1. Rule Modification
Extend the system to allow users to update existing rules, change operators, or add/remove conditions.

2. User-Defined Functions
Implement custom functions to handle complex conditions beyond basic comparisons.

3. Error Handling
Add detailed error messages for different scenarios (e.g., unsupported operators, invalid data types).

Limitations and Future Enhancements
Current Limitation: The system does not yet support nested conditions beyond a basic level. A more sophisticated parser could be implemented.
Future Enhancement: Add support for more data types and conditions (e.g., date comparisons).
Example Use Cases
Eligibility Check: Check if a user qualifies for a loan based on age, income, and credit score.
Access Control: Determine if a user has the required permissions based on role and department.
Sales Target Achievement: Evaluate if a salesperson meets the criteria for a bonus based on sales figures.
Troubleshooting
Database Issues: Ensure that rules.db is present in the project root. You can reinitialize it using the init_db() function.
Server Errors: Check the server logs in the console where the Flask app is running for detailed error messages.
References
Flask Documentation
SQLite Documentation
Abstract Syntax Tree (AST) Concepts
Contributing
Feel free to open issues or submit pull requests for any enhancements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

The above README provides a detailed guide for setting up and using Application 1. It covers the project overview, features, setup instructions, usage, architecture, and more. Let me know if any specific details need to be added or modified!
