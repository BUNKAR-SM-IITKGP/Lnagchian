from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription= "A simple API Server"
)

#model=ChatOpenAI()
##olma lllam2
llm=Ollama(model="llama2")
prompt1=ChatPromptTemplate.from_template("Write me an code for finding  {number} in python")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words")


add_routes(
    app,
    prompt1|llm,
    path="/essay"
)
add_routes(
    app,
    prompt2|llm,
    path="/poem"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
    
