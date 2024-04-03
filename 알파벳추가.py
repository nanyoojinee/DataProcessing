
import os

folder_path = r"C:\Users\정유진\Desktop\보도자료_노충완_완료"  # 작업할 폴더 경로를 입력하세요

# 폴더 내의 파일 목록을 가져옵니다.
file_list = os.listdir(folder_path)

# 파일 이름 앞에 추가할 접두사
prefix = "보도자료_F-"

# 파일 이름을 수정하여 변경된 파일 이름으로 파일을 이동합니다.
for filename in file_list:
    try:
        # 기존 파일 경로와 새 파일 경로를 설정합니다.
        old_file_path = os.path.join(folder_path, filename)
        new_filename = prefix + filename
        new_file_path = os.path.join(folder_path, new_filename)

        # 파일 이름을 변경합니다.
        os.rename(old_file_path, new_file_path)

        print(f"파일 이름 변경: {filename} -> {new_filename}")
    except Exception as e:
        print(f"파일 이름 변경 실패: {filename}, 오류: {str(e)}")
