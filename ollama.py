from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

# Define the prompt template
promt=ChatPromptTemplate.from_messages(
   [("system","you are a helpful assistant. please response to the user"),
     ("user","Question:{question}")
        
    ]
)
# Set up Streamlit app
st.title("langchain demo with ollama")
input_text=st.text_input("search the topic you want")

# Set up the llm 
llm=Ollama(model='llama2',temperature=0)

# Define the output parser
output_parser=StrOutputParser()
#define the chain

chain=promt|llm|output_parser
if input_text:
    st.write(chain.invoke({"question":input_text}))
