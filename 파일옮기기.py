import os
import shutil

# A 폴더와 B 폴더의 경로 설정
a_folder = r"C:\Users\정유진\Desktop\도로 및 유도선 Json-20231031T083748Z-001\도로 및 유도선 Json\json"
b_folder = r"C:\Users\정유진\Desktop\도로 및 유도선 Image-20231031T083748Z-001\도로 및 유도선 Image\1차 데이터(5,000장)\분기점_5000장_1"

# A 폴더 내 파일 목록 가져오기
a_files = os.listdir(a_folder)

# B 폴더 내 파일과 디렉토리 목록 가져오기
for root, _, files in os.walk(b_folder):
    for file in files:
        b_file_path = os.path.join(root, file)
        # 파일 이름이 A 폴더 파일과 같다면 이동
        if file in a_files:
            a_file_path = os.path.join(a_folder, file)
            # 이동 작업 수행
            shutil.move(a_file_path, b_file_path)
            print(f"파일 '{file}'을 이동했습니다: {a_file_path} -> {b_file_path}")
