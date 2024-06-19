# Database Query Generator
This Streamlit app converts natural language prompts into SQL queries and executes them on a MySQL database using LangChain's PromptTemplate and LLMChain, and the Ollama LLM model.

# Features
Natural Language to SQL: Converts prompts into SQL queries.

Query Execution: Runs the generated SQL query on a MySQL database.

Results Display: Shows query results in a table.

# Requirements

Python 3.7+

Streamlit

LangChain

Ollama

MySQL Connector

Installation

# Install dependencies:

pip install streamlit langchain mysql-connector-python

# Set up MySQL database:

CREATE DATABASE atulmanjhi;

USE atulmanjhi;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(255),
    city VARCHAR(50),
    join_date DATE
);


# Update database connection in app.py if necessary:

con = ms.connect(host="localhost", user="root", password="root", database="atulmanjhi")

# Usage

Run the app:

streamlit run app.py

Enter a prompt, e.g., "Get all customers who joined in the last year."

Click "Find Data" to generate and execute the SQL query, displaying the results.

# Example Prompts

"List all customers from New York."

"Show customers who joined after January 1, 2023."

"Find the email addresses of all customers with the first name John."

# Code Overview

data_analyst_template: Template for generating SQL queries.

data_analyst_prompt_template: Instance of PromptTemplate.

gemma: Instance of the Ollama LLM model.

llm_chain: Instance of LLMChain.

query_llm(prompt): Generates SQL query from prompt.

extract_sql_code(input_string): Extracts SQL code from response.

query_db(sql_query): Executes SQL query and returns results.

