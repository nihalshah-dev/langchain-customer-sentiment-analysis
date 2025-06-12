import json

from typing import List
from pprint import pprint

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_core.pydantic_v1 import BaseModel, Field

# Setup LLM
base_url = 'http://llama:8000/v1'
model = 'meta/llama-3.1-8b-instruct'
llm = ChatNVIDIA(base_url=base_url, model=model, temperature=0)

# Define the output model for the assessment
class AssessmentOutput(BaseModel):
    most_complained_category: str = Field(..., description="The category of product with most complaints")
    most_complained_location: str = Field(..., description="The store location with most complaints")

# Load customer emails
with open('data/emails.json', 'r') as f:
    emails = json.load(f)

# Setup Output Parser
parser = JsonOutputParser(pydantic_object=AssessmentOutput)

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an intelligent assistant helping analyze customer feedback to determine complaint patterns."
    ),
    (
        "human",
        """
Here is a list of customer emails from different store locations. Each email is either a praise or complaint about a product.

Your task:
1. Identify all emails with a **negative** sentiment.
2. For each negative email:
   - Extract the product mentioned and categorize it into a general category (like "clothing", "electronics", etc.)
   - Record the store location.
3. Count:
   - Which product category received the most complaints.
   - Which store location received the most complaints.

Only consider **negative emails** for this.

Return your answer in this **JSON format** only:
{{
  "most_complained_category": "...",
  "most_complained_location": "..."
}}

Emails:
{emails}
"""
    )
])

# Combine into Chain
chain = prompt | llm | parser

# Print the chain graph for debugging
print(chain.get_graph().draw_ascii())

# Run chain and print output
output = chain.invoke({"emails": emails})
print(output)