import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
import mysql.connector as ms


data_analyst_template = """You are a data analyst. You are working on a database named atulmanjhi, 
which has a table named customers and the table has the following columns,customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(255),
    city VARCHAR(50),
    join_date DATE
    \n Your job is to perform the given task {prompt} by converting the prompt into sql queries.
    The result should be the sql query in single line string format excluding. 
    Result: 
    """

data_analyst_prompt_template = PromptTemplate(
    input_variables=["prompt"],
    template=data_analyst_template
)

gemma = Ollama(model="gemma")

llm_chain = LLMChain(llm=gemma,prompt=data_analyst_prompt_template)

def query_llm(prompt):
    return llm_chain.invoke({"prompt":prompt})["text"]

def extract_sql_code(input_string):
    sql_code = input_string.replace("```sql", "").replace("```", "").strip()
    return sql_code

def query_db(sql_query):
    con = ms.connect(host="localhost",user="root",password="root",database="atulmanjhi")
    cursor = con.cursor()
    
    cursor.execute(sql_query)
    data = cursor.fetchall()
    
    cursor.close()
    con.close()
    return data


st.title("Database Query Generator")
user_input = st.text_input("Enter the Prompt....")

if st.button("Find Data"):
    result = query_llm(user_input)
    sql_query = extract_sql_code(result)
    st.write(sql_query)
    print(sql_query)
    st.table(query_db(sql_query))