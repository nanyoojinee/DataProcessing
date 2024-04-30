import pandas as pd
import re

# 엑셀 파일 로드
file_path = r'C:\Users\정유진\Desktop\코난테크놀로지\코난테크놀로지_DS사업부_뉴스기사데이터_240423\코난테크놀로지_DS사업부_뉴스기사데이터_240423\IT\output(2).xlsx'  # 엑셀 파일 경로
df = pd.read_excel(file_path)

# "Summary" 열의 따옴표 안의 문장을 추출하고 "Body" 열에 존재하는지 확인
for index, row in df.iterrows():
    # "Summary" 열에서 따옴표 안의 문장 추출
    summary_quotes = re.findall(r'"([^"]*)"', row['Summary'])
    # 모든 따옴표 내 문장이 "Body" 열에 있는지 확인
    if not all(quote in row['body'] for quote in summary_quotes):
        # 하나라도 "Body" 열에 없는 경우, 그 "Summary" 열을 프린트
        print(f'Missing in body, Summary (Index {index}): {row["Summary"]}')
