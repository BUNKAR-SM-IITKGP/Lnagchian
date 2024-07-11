from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPEN_API_KEY"]=os.getenv("OPEN_API_KEY")

##langsmith tracking 
os.environ["LANGCHAIN_TRACING_V3"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


##Promt Template
promat=ChatPromptTemplate.from_messages(
    ("system","You are a helpful assistant . Please  response to the user queries"),("user","Question:{question}")
    
    
)

## streamlit framework 

st.title('Langchian Demo With Open API')
input_text=st.text_input("Search the topic u want")


## openAI llm

llm=ChatOpenAI(model="gpt-3.5-turbo")
ouput_parser=StrOutputParser()
chain =promat|llm|ouput_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
    







