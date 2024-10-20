# database.py
import sqlite3
import json

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_name TEXT NOT NULL,
            rule_ast TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_rule(rule_name, rule_ast):
    """Save a rule in the database."""
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO rules (rule_name, rule_ast) VALUES (?, ?)', 
                   (rule_name, json.dumps(rule_ast.to_dict())))
    conn.commit()
    conn.close()
