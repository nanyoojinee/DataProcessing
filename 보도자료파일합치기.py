import pandas as pd
import os

# 합칠 CSV 파일들이 있는 폴더 경로
folder_path = r'C:\Users\정유진\Desktop\플리옥션납품'

# 빈 데이터프레임을 생성하여 데이터를 추가할 준비
combined_data = pd.DataFrame()

# 파일 순서대로 읽어와 합치기
for i in range(1, 18):  # 1부터 17까지의 파일을 합칩니다.
    filename = f'보도자료_{i}.csv'
    file_path = os.path.join(folder_path, filename)

    if os.path.exists(file_path):
        # 파일을 'utf-8' 인코딩으로 읽기
        data = pd.read_csv(file_path, encoding='utf-8', header=None, skiprows=1)  # 1행을 제외하고 읽기
        combined_data = pd.concat([combined_data, data], ignore_index=True)  # 데이터를 합칩니다.

# 새로운 CSV 파일로 저장
combined_file_path = r'C:\Users\정유진\Desktop\플리옥션납품\합친_파일2.csv'
# 파일을 'utf-8' 인코딩으로 저장
combined_data.to_csv(combined_file_path, index=False, header=False, encoding='utf-8')  # 1행과 인덱스를 제외하고 저장
