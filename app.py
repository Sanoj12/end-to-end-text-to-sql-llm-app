from dotenv import load_dotenv

load_dotenv() #load all the envirnoments variable


import streamlit as st
import os

import sqlite3

import google.generativeai as genai
#


###configure our API KEY

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


##function to load google gemini model and provide sql query as response

def get_gemini_response(question,prompt):

    model = genai.GenerationConfig('gemini-pro')

    response = model.generate_content([prompt[0],question])

    return response.text 



### function to retrieve query from the sequential data

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    

    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return row


###prompt 


prompt = [
    """
    you are an expert in converting questions to sql query!
    the sql database has the name STUDENT and has the following 
    columns-NAME,CLASS,SECTION and MARKS \n \n
    example 1-how many entries of records are present in record
    the sql command will be something like this SELECT COUNT(*) FROM STUDENT
"""
]

###streamlit

st.set_page_config(page_title="I can Retrieve any sql query")

st.header("llm app to retreive SQL Data")

question = st.text_input("input:",key="input")
submit= st.button("ask the question")


#####if submit

if submit:
    response = get_gemini_response(question,prompt)
    print(response)

    data = read_sql_query(response,"student.db")
    st.subheader("The Response is")

    for row in data:
        print(row)
        st.header(row)

      
       