import os
import pandas as pd
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

import Util.Converter as uconvert
import transformer as transformer

# chat = ChatOpenAI(temperature=0.1)
chat = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)

systemMessage = """
Your task is to create an csv format string

Constraint
1. Write `일자` as day/month/year. If the day is missing, use month/year. If both day and month are missing, use year. Exclude any values that cannot be displayed, but display all possible day/month/year values. 
2. Each header column meaning `일자: date, 제품명: Product Name, 규격: Specification, 요양기관기호: Institution Code, 표준코드: Standard Code, 구분: Division, 매출처명: Vendor name, 사업자번호: Business Registration Number, 우편번호: Postal Code, 주소: Address, 수량: Quantity, 단가: Unit Price, 매출액: Total Sales Amount
3. `구분` row value type is `원내` or `도매`. If there is no corresponding `구분` column, enter an empty string.
4. Use only the values from the corresponding column, and if the content is empty, do not attempt to guess or fill in values from other columns.
5. Define numbers as Int values without decimal points. Everything else should be represented as String.
6. Please enclose all field values in double quotes ("").
7. Only write `csv string`

Instructions
1. Write the following header row in CSV format as the first row: `일자, 제품명, 규격, 요양기관기호, 표준코드, 구분, 매출처명, 사업자번호, 우편번호, 주소, 수량, 단가, 매출액`.
2. In ```csv{target_csv_string}```, Referencing the constraints, find header row and then identify the columns in the header row that most closely match each of the provided headers (`일자, 제품명, 규격, 요양기관기호, 표준코드, 구분, 매출처명, 사업자번호, 우편번호, 주소, 수량, 단가, 매출액`).
3. For each row from 2 to n in the source CSV, place the values into the new CSV under the matched headers.
4. Ensure that the new CSV file has exactly 13 columns as per the header row.
5. If a corresponding value for any header is not found, enter an empty string `""` in that position.
"""

template = ChatPromptTemplate.from_messages([
    ("system", systemMessage),
    ("human", "Work according to the instructions. `{target_csv_string}`")
])

chain = template | chat 

response = chain.invoke({
    "target_csv_string":uconvert.convert_csv_to_string("./target_input/result_original6.csv")
})

content = response.content.replace("`csv", "").replace("`", "").strip()
print(content)
uconvert.convert_csv_to_xlsx(content, "./result/output.xlsx")