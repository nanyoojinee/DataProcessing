import os
import json
import pandas as pd

def read_json_files(folder_path):
    data_frames = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8-sig') as file:
                    data = json.load(file)
                    # Check if 'body' key exists
                    if 'body' in data and isinstance(data['body'], list):
                        data['body'] = '\n'.join(data['body'])
                    else:
                        print(f"Skipping {filename}: 'body' key is missing or not a list")
                        continue  # Skip this file and move to the next
                    df = pd.DataFrame([data])
                    data_frames.append(df)
            except json.JSONDecodeError as e:
                print(f"Error reading {filename}: {e}")
    if data_frames:
        return pd.concat(data_frames, ignore_index=True)
    else:
        return pd.DataFrame()


def save_to_excel(data_frame, output_path):
    # Excel 파일로 저장
    data_frame.to_excel(output_path, index=False)

# 사용 예시
folder_path = r'C:\Users\정유진\Desktop\코난테크놀로지\코난테크놀로지_DS사업부_뉴스기사데이터_240423\코난테크놀로지_DS사업부_뉴스기사데이터_240423\politics\pol_set1'  # 폴더 경로 설정
output_excel_path = r'C:\Users\정유진\Desktop\코난테크놀로지\코난테크놀로지_DS사업부_뉴스기사데이터_240423\코난테크놀로지_DS사업부_뉴스기사데이터_240423\politics\pol_set1.xlsx'  # 출력 파일 경로 설정
df = read_json_files(folder_path)
save_to_excel(df, output_excel_path)
