import os

# 작업 디렉토리 경로 설정
folder_path = r'C:\Users\정유진\Documents\카카오톡 받은 파일\유한비_보도자료\유한비_보도자료 - 복사본'

# 폴더 내의 파일 목록을 얻습니다.
file_list = os.listdir(folder_path)

# 파일 이름 변경
for file_name in file_list:
    # 파일의 절대 경로
    file_path = os.path.join(folder_path, file_name)

    # 파일명을 '_'로 분리
    parts = file_name.split('_')

    # 파일명이 언더바로 분리되고, 두 부분으로 나누어질 경우 변경
    if len(parts) > 1:
        new_file_name = f"보도자료_{parts[1]}"
        os.rename(file_path, os.path.join(folder_path, new_file_name))

print('파일 이름 변경이 완료되었습니다.')
