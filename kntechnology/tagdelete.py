import pandas as pd
import re

# 엑셀 파일 로드
file_path = r'C:\Users\정유진\Desktop\코난테크놀로지\코난테크놀로지_DS사업부_뉴스기사데이터_240423\코난테크놀로지_DS사업부_뉴스기사데이터_240423\economy\eco_40.xlsx'  # 엑셀 파일 경로
df = pd.read_excel(file_path)

# 8번째 열('H' 열)에서 한글, 따옴표, 대시 제거
df['Tags'] = df['Tags'].apply(lambda x: re.sub(r"[가-힣'-]", '', str(x)))

# 결과를 새로운 엑셀 파일로 저장
output_path = r'C:\Users\정유진\Desktop\코난테크놀로지\코난테크놀로지_DS사업부_뉴스기사데이터_240423\코난테크놀로지_DS사업부_뉴스기사데이터_240423\economy\eco_40(1).xlsx'
df.to_excel(output_path, index=False)

print("Completed! The modified data has been saved to", output_path)
