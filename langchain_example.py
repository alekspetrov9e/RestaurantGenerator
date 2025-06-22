from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_template("Translate '{text}' to German.")
chain = prompt | llm

response = chain.invoke({"text": "I love skiing"})
print(response.content)
