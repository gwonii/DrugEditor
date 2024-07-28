import io
import os
import pandas as pd
import chardet

def convert_csv_to_string(csv_file_path):
    with open(csv_file_path, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']

    df = pd.read_csv(csv_file_path, encoding=encoding).drop_duplicates()
    csv_string = df.to_csv(index=False)
    return csv_string

def convert_csv_to_xlsx(content, output_path):
    df = pd.read_csv(io.StringIO(content)).drop_duplicates()
    df.to_excel(output_path, index=False)

def convert_csv_to_string_list(csv_files_path):
    csv_strings = []
    
    # 디렉토리 내의 모든 파일 탐색
    for filename in os.listdir(csv_files_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(csv_files_path, filename)
            
            # CSV 파일 읽기
            df = pd.read_csv(file_path).drop_duplicates()

            # DataFrame을 문자열로 변환
            csv_string = df.to_string()
            
            # 문자열 배열에 추가
            csv_strings.append(csv_string)
    
    return csv_strings

# result = convert_csv_to_string_list("./after")
# print(result[0])


# response = """
# 년월,제품명,규격,요양기관기호,표준코드,구분,매출처명,사업자번호,우편번호,상세주소,수량,단가,금액
# """

# print(convert_csv_to_xlsx(response, "./result/output1.xlsx"))
