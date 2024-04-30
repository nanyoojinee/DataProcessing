import pandas as pd
import json
import os

# 엑셀 파일 로드
file_path = r'C:\Users\정유진\Desktop\코난테크놀로지\코난테크놀로지_DS사업부_뉴스기사데이터_240423\코난테크놀로지_DS사업부_뉴스기사데이터_240423\economy\eco_55_output1.xlsx'
df = pd.read_excel(file_path)

# JSON 파일들이 있는 폴더
json_folder_path = r'C:\Users\정유진\Desktop\코난테크놀로지\코난테크놀로지_DS사업부_뉴스기사데이터_240423\코난테크놀로지_DS사업부_뉴스기사데이터_240423\economy\eco_set1 - 복사본'

json_files = sorted(os.listdir(json_folder_path))  # JSON 파일 목록을 정렬

# JSON 파일과 엑셀 데이터를 순서대로 매핑
for idx, json_filename in enumerate(json_files):
    if json_filename.endswith('.json'):
        json_file_path = os.path.join(json_folder_path, json_filename)
        
        # 엑셀 데이터프레임의 해당 행 읽기
        if idx < len(df):
            row = df.iloc[idx]
            with open(json_file_path, 'r', encoding='utf-8-sig') as file:
                data = json.load(file)
            
            # 데이터 추가
            data['extractive_summary'] = [s.strip() for s in row['extractive_summary'].split('"') if s.strip()]
            data['keywords'] = [k.strip() for k in row['keywords'].split(',')]
            data['ner_tags'] = [n.strip() for n in row['ner_tags'].split(',')]

            # JSON 파일을 업데이트된 데이터로 다시 저장
            with open(json_file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            print(f"No corresponding row in Excel for {json_file_path} (index {idx})")