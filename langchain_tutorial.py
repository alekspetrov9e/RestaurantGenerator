import os
from dotenv import load_dotenv

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.9)

# First PromptTemplate
prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to create a name for my {cuisine} restaurant. Suggest a nice name for it"
)

# First LLMChain with output_key "restaurant_name"
name_chain = LLMChain(
    llm=llm,
    prompt=prompt_template_name,
    output_key="restaurant_name"
)

# Second PromptTemplate
prompt_template_items = PromptTemplate(
    input_variables=['restaurant_name'],
    template="Suggest some menu items for {restaurant_name}. Only the names of the items. Return it as a comma separated list"
)

# Second LLMChain with output_key "menu_items"
food_items_chain = LLMChain(
    llm=llm,
    prompt=prompt_template_items,
    output_key="menu_items"
)

# SequentialChain that connects both
chain = SequentialChain(
    chains=[name_chain, food_items_chain],
    input_variables=["cuisine"],
    output_variables=["restaurant_name", "menu_items"]
)

response = chain({"cuisine": "Bulgarian"})
#print(response)
def generate_restaurant_name_and_items(cuisine):
    return chain({"cuisine":cuisine})
