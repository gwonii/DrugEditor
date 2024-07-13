import pandas as pd
import os

def convert_excel_to_csv(excel_file_path, output_directory):
    # 파일 확장자에 따라 Excel 파일을 읽습니다.
    file_extension = os.path.splitext(excel_file_path)[1]
    if file_extension not in ['.xls', '.xlsx']:
        raise ValueError("지원하지 않는 파일 형식입니다: {}".format(file_extension))
    
    # Excel 파일 읽기
    excel_data = pd.ExcelFile(excel_file_path)

    first_sheet_name = excel_data.sheet_names[0]
    df = pd.read_excel(excel_file_path, sheet_name=first_sheet_name)
        
        # CSV 파일 경로 생성
    csv_file_name = f"result_{os.path.splitext(os.path.basename(excel_file_path))[0]}.csv"
    csv_file_path = os.path.join(output_directory, csv_file_name)
        
        # DataFrame을 CSV 파일로 저장
    df.to_csv(csv_file_path, index=False)
    print(f"저장 완료: {csv_file_path}")

def convert_all_excels_in_folder(input_folder, output_folder):
    # 입력 폴더 내 모든 파일을 확인
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        # 파일이 Excel 형식인 경우 변환 수행
        if os.path.isfile(file_path) and file_name.endswith(('.xls', '.xlsx')):
            convert_excel_to_csv(file_path, output_folder)

# 사용 예시
input_folder = './before'  # Excel 파일들이 있는 폴더
output_folder = './after'  # CSV 파일을 저장할 폴더

# 출력 폴더가 존재하지 않으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

convert_all_excels_in_folder(input_folder, output_folder)


