
import openpyxl
from collections import Counter

# 엑셀 파일 열기
workbook = openpyxl.load_workbook("C:\\Users\\정유진\\Desktop\\작가번호.xlsx")
sheet = workbook.active

# A 열의 값을 읽어서 리스트에 저장
values_in_a_column = [cell.value for cell in sheet['A']]

# 1부터 2684까지의 숫자 중에서 없는 숫자 찾기
all_numbers = set(range(1, 1895))
existing_numbers = set(values_in_a_column)
missing_numbers = sorted(list(all_numbers - existing_numbers))

# 중복된 숫자 찾기
counted_numbers = Counter(values_in_a_column)
duplicates = [num for num, count in counted_numbers.items() if count > 1]

# 출력
print("없는 숫자들 개수:", len(missing_numbers))
print("없는 숫자들:", missing_numbers)
print("중복된 숫자들 개수:", len(duplicates))
print("중복된 숫자들:", duplicates)

# 엑셀 파일 닫기
workbook.close()

# import os
#
# folder_path = r"C:\Users\정유진\Desktop\이미지파일\보도자료_한비유\보도자료_한비유"  # 작업할 폴더 경로를 입력하세요
#
# # 폴더 내의 파일 목록을 가져옵니다.
# file_list = os.listdir(folder_path)
#
# # 파일 이름에서 '6.' 뒤에 있는 띄어쓰기를 없애는 함수 정의
# def remove_whitespace_after_6(filename):
#     index = filename.find('6.')
#     if index != -1 and len(filename) > index + 2:
#         new_filename = filename[:index + 2] + filename[index + 2:].replace(" ", "")
#         return new_filename
#     else:
#         return filename
#
# # 파일 이름을 수정하고 이동합니다.
# for filename in file_list:
#     old_path = os.path.join(folder_path, filename)
#     new_filename = remove_whitespace_after_6(filename)
#     new_path = os.path.join(folder_path, new_filename)
#
#     # 파일 이름 수정
#     os.rename(old_path, new_path)
#     print(f"변경된 파일 이름: {new_filename}")

# import os
#
# folder_path = r"C:\Users\정유진\Desktop\알바 사진 자료\알바 사진 자료"  # 작업할 폴더 경로를 입력하세요
#
# # 1부터 1080까지의 숫자를 포함하는 집합을 생성합니다.
# all_numbers = set(range(1, 436))
#
# # 폴더 내의 파일 목록을 가져옵니다.
# file_list = os.listdir(folder_path)
#
# # 파일 이름에서 숫자 부분을 추출하고 집합에서 제거합니다.
# missing_numbers = []
# for filename in file_list:
#     try:
#         start_index = filename.index('_') + 1
#         end_index = filename.rfind('.')
#         number = int(filename[start_index:end_index])
#         if number in all_numbers:
#             all_numbers.remove(number)
#     except ValueError:
#         pass  # '_숫자' 형식을 찾지 못한 경우 무시합니다.
#
# # 누락된 숫자 목록과 개수를 출력합니다.
# missing_numbers = sorted(all_numbers)
# missing_count = len(missing_numbers)
# print(f"누락된 숫자: {missing_numbers}")
# print(f"누락된 숫자 개수: {missing_count}")

# import os
#
# folder_path = r'C:\Users\정유진\Desktop\보도자료_유한비_완료'  # 폴더 경로를 적절히 수정해주세요.
#
# # 폴더 내의 모든 파일 검사
# for filename in os.listdir(folder_path):
#     if filename.startswith('6.'):
#         new_filename = filename.replace('6.', '', 1)
#         os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
#         print(f'{filename} 파일의 이름이 {new_filename}으로 변경되었습니다.')
#
#
