from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st 
import os 
from dotenv import load_dotenv

load_dotenv()

# Ensure API keys are set
#os.environ["OPEN_API_KEY"] = os.getenv("OPEN_API_KEY")
#os.environ["LANGCHAIN_TRACING_V3"] = "true"
#os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries"),
    ("user", "Question: {question}")
]
)

# Streamlit framework
st.title('LangChain Demo With Open API')
input_text = st.text_input("Search the topic you want")

llm = Ollama(model="llama2")
output_parser = StrOutputParser()

# Combine the prompt, language model, and output parser into a chain
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({'question': input_text})
    st.write(response)
