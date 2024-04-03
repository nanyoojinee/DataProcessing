import os
import shutil

# A 폴더와 B 폴더의 경로 설정
a_folder = r"C:\Users\정유진\Desktop\도로 및 유도선 Json-20231031T083748Z-001\도로 및 유도선 Json\json"
b_folder = r"C:\Users\정유진\Desktop\도로 및 유도선 Image-20231031T083748Z-001\도로 및 유도선 Image\1차 데이터(5,000장)\분기점_5000장_1"

# A 폴더 파일 이름 목록 가져오기 (확장자 제외)
a_files = [os.path.splitext(f)[0] for f in os.listdir(a_folder)]

# B 폴더 내 모든 하위 경로를 검색하며 파일 목록 가져오기
for root, _, files in os.walk(b_folder):
    for file in files:
        b_file_name = os.path.splitext(file)[0]  # 확장자를 제외한 파일 이름
        # 파일 이름이 A 폴더의 파일 이름과 같다면 복사
        if b_file_name in a_files:
            a_file_name = b_file_name + ".json"  # .json 확장자 추가
            a_file_path = os.path.join(a_folder, a_file_name)
            b_file_path = os.path.join(root, file)
            # 복사 작업 수행
            shutil.copy2(a_file_path, b_file_path)
            print(f"파일 '{a_file_name}'을 복사했습니다: {a_file_path} -> {b_file_path}")
