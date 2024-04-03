import os

folder_path = r'C:\Users\정유진\Desktop\이미지파일\4.판매항목_이은석'  # 폴더 경로를 여기에 입력하세요.

# 폴더 내의 모든 파일에 대해 반복합니다.
for filename in os.listdir(folder_path):
    if '.' in filename:  # 파일 이름에 '.'이 있는 경우에만 처리합니다.
        new_filename = filename.replace('.', '_', 1)  # 첫 번째 '.'만 '_'로 대체합니다.
        # 새 파일 이름으로 파일을 이동합니다.
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        print(f'파일 이름 변경: {filename} -> {new_filename}')
