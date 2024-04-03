import openpyxl

# 엑셀 파일 경로 설정
excel_file_path = r'C:\Users\정유진\Desktop\숫자세기\숫자세기.xlsx'

# 엑셀 파일 열기
wb = openpyxl.load_workbook(excel_file_path)

# 시트 선택 (예: 첫 번째 시트 선택)
sheet = wb.active

# A열에서 숫자를 읽어서 중복을 제외한 숫자의 총 개수를 세기
numbers = set()
for cell in sheet['A']:
    if cell.value is not None and isinstance(cell.value, (int, float)):
        numbers.add(cell.value)

count = len(numbers)

print(f'A열에 있는 숫자의 총 개수: {count}')
