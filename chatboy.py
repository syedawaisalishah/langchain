from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
import streamlit as st
load_dotenv()

st.header("Chat with tthe Google Gemini-2.5-flash")
text=st.text_input("Ask me anything about France!")
st.write("You asked: "+text)

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.8)
result=llm.invoke("What is the capital of France?")
print(result)