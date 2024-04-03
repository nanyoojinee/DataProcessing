import os
import re

# 파일이 들어있는 폴더 경로 설정
folder_path = r'C:\Users\정유진\Desktop\이미지파일\이은석_협업\협업'

# 폴더 내의 파일 목록을 얻습니다.
file_list = os.listdir(folder_path)

# 파일명에서 숫자를 추출하여 숫자 순서대로 정렬합니다.
file_list.sort(key=lambda x: int(re.search(r'_(\d+)\.', x).group(1)) if re.search(r'_(\d+)\.', x) else float('inf'))

# 순서대로 파일명 변경
for i, file_name in enumerate(file_list, start=1):
    match = re.search(r'_(\d+)\.', file_name)
    if match:
        old_number = match.group(1)
        new_file_name = file_name.replace(f'_{old_number}.', f'_{i}.')

        # 파일명 변경
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

        print(f'Renamed: {file_name} -> {new_file_name}')
    else:
        print(f'Skipped: {file_name} (No matching pattern)')

print('파일명 변경이 완료되었습니다.')

