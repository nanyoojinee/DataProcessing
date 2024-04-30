import pandas as pd
import re

# 엑셀 파일 로드
file_path = r'C:\Users\정유진\Desktop\코난테크놀로지\코난테크놀로지_DS사업부_뉴스기사데이터_240423\코난테크놀로지_DS사업부_뉴스기사데이터_240423\economy\eco_55_output.xlsx'  # 엑셀 파일 경로
df = pd.read_excel(file_path)

# "Keywords" 열의 데이터에서 따옴표 안의 텍스트만 추출
df['Summary'] = df['Summary'].apply(lambda x: ' '.join(re.findall(r'(".*?")', x)))

# 변경된 데이터프레임을 새로운 엑셀 파일로 저장
df.to_excel(r'C:\Users\정유진\Desktop\코난테크놀로지\코난테크놀로지_DS사업부_뉴스기사데이터_240423\코난테크놀로지_DS사업부_뉴스기사데이터_240423\economy\eco_55_output1.xlsx', index=False)
