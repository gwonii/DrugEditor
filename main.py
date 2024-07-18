import os
import pandas as pd
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

import Util.Converter as uconvert


chat = ChatOpenAI(temperature=0.1)
template = ChatPromptTemplate.from_messages([
    ("system", "Your task is to create an csv_string that meets the specified requirements."),
    ("system", "1. You need to fill in the blanks of ```{reference_empty}``` to create a result in the form of a csv_string."),
    ("system", "2. To fill in the empty data, read the {target_csv_string} and list it according to the names of similar columns."),
    ("human", "Create a csv file according to the requirements.")
])

chain = template | chat 

# chain = template | chat

response = chain.invoke({
    "reference_empty":uconvert.convert_csv_to_string("./reference_empty.csv"),
    "target_csv_string":uconvert.convert_csv_to_string("./after/result_gy.csv")
})

print(response.content)
uconvert.convert_csv_to_xlsx(response.content.strip("```"), "./result/output2.xlsx")