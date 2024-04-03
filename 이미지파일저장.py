import xlwings as xw
import os

# 엑셀 파일의 경로 설정
excel_file_path = r"C:\Users\정유진\Desktop\보도자료\test\이거이거요.xlsx"

# 이미지를 저장할 경로 설정
image_folder_path = r"C:\Users\정유진\Desktop\보도자료\test\파일입니다"

# 이미지 저장할 폴더 생성 (없으면)
if not os.path.exists(image_folder_path):
    os.makedirs(image_folder_path)

# 엑셀 파일 열기
app = xw.App(visible=False)  # 엑셀을 숨김 모드로 열기
workbook = app.books.open(excel_file_path)

# 원하는 워크시트 선택
worksheet = workbook.sheets['s1']

# 워크시트에서 이미지 추출 및 저장
for shape in worksheet.shapes:
    if shape.type == 3:  # 이미지 형태인 경우
        image_data = shape.image
        image_filename = f"판매_{shape.row}.jpg"  # 파일명 생성
        image_file_path = os.path.join(image_folder_path, image_filename)
        image_data.save(image_file_path)

# 엑셀 파일 닫기
workbook.close()
app.quit()

print("이미지 추출 및 저장이 완료되었습니다.")
