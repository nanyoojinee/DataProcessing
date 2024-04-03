# import os
#
# # 폴더 경로 설정
# folder_path = r'C:\Users\정유진\Desktop\나는정유지니야\나는정유지니야'
#
# # 폴더 내의 파일 목록을 얻습니다.
# file_list = os.listdir(folder_path)
#
# # '보도자료_'를 삭제한 파일 이름으로 변경
# for file_name in file_list:
#     if file_name.startswith('보도자료_'):
#         new_file_name = file_name.replace('보도자료_', '')
#         os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
#         print(f'Renamed: {file_name} -> {new_file_name}')
#
# print('파일명 변경이 완료되었습니다.')
import os

# 폴더 경로 설정
folder_path = r'C:\Users\정유진\Desktop\나는정유지니야\나는정유지니야'

# 폴더 내의 파일 목록을 얻습니다.
file_list = os.listdir(folder_path)

# '보도자료_'를 추가한 파일 이름으로 변경
for file_name in file_list:
    new_file_name = '보도자료_' + file_name
    os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
    print(f'Renamed: {file_name} -> {new_file_name}')

print('파일명 변경이 완료되었습니다.')
