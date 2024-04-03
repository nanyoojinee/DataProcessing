import json
import pandas as pd
import os

# 폴더 경로
folder_path = r"C:\Users\정유진\Downloads\롯데어쩌고저쩌고"

# 경계선 정의
boundary_x = [1 / 3, 2 / 3]
boundary_y = 1 / 2

# 폴더 내의 모든 JSON 파일 찾기
json_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.json')]

all_boundary_coordinates = []
file_data_counts = []  # 파일별 데이터 개수 저장

for json_path in json_files:
    file_name = os.path.basename(json_path)

    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 파일별 데이터 개수 추가
    file_data_counts.append({
        'file_name': file_name,
        'data_count': len(data)
    })

    for item in data:
        x1 = item['coordinates']['x1']
        x2 = item['coordinates']['x2']
        y1 = item['coordinates']['y1']
        y2 = item['coordinates']['y2']

        section_nums = set()

        if y1 < boundary_y:
            if x1 < boundary_x[0]:
                section_nums.add(1)
            if x2 > boundary_x[0] and x1 < boundary_x[1]:
                section_nums.add(2)
            if x2 > boundary_x[1]:
                section_nums.add(3)
        if y2 > boundary_y:
            if x1 < boundary_x[0]:
                section_nums.add(4)
            if x2 > boundary_x[0] and x1 < boundary_x[1]:
                section_nums.add(5)
            if x2 > boundary_x[1]:
                section_nums.add(6)

        if len(section_nums) > 1:
            all_boundary_coordinates.append({
                'file_name': file_name,
                'x1': x1,
                'x2': x2,
                'y1': y1,
                'y2': y2,
                'section_nums': list(section_nums)
            })

# 모든 결과를 하나의 엑셀 파일에 저장
df = pd.DataFrame(all_boundary_coordinates)
excel_file_path = os.path.join(folder_path, "compiled_boundary_coordinates_with_sections.xlsx")
df.to_excel(excel_file_path, index=False)

# 파일별 데이터 개수를 엑셀 파일에 저장
df_counts = pd.DataFrame(file_data_counts)
counts_excel_file_path = os.path.join(folder_path, "json_file_data_counts.xlsx")
df_counts.to_excel(counts_excel_file_path, index=False)

print(f"모든 JSON 파일에서 처리된 데이터를 하나의 엑셀 파일로 출력했습니다: {excel_file_path}")
print(f"각 JSON 파일별 데이터 개수를 나타내는 엑셀 파일을 생성했습니다: {counts_excel_file_path}")
