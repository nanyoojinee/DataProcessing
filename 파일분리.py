import os
import json
from PIL import Image

# 이미지 파일이 있는 상위 폴더 경로
parent_folder = r'C:\Users\opera\OneDrive\바탕 화면\롯데정보통신\새 폴더'

# 이미지 파일 및 해당 json 파일 불러오기
image_files = [file for file in os.listdir(parent_folder) if file.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
json_files = [file for file in os.listdir(parent_folder) if file.endswith('.json')]

# 하위 폴더 이름 리스트
output_subfolders = ["split_cam1", "split_cam2", "split_cam3", "split_cam4", "split_cam5", "split_cam6"]

# 이미지 분할 및 정보 이동
for image_file in image_files:
    # 이미지 파일 이름에서 확장자 제거
    image_name = os.path.splitext(image_file)[0]

    # 해당 이미지에 대한 json 파일 찾기
    json_file = next((file for file in json_files if file.startswith(image_name)), None)

    if json_file:
        # 해당 json 파일 불러오기
        json_path = os.path.join(parent_folder, json_file)
        with open(json_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        # 이미지 불러오기
        image_path = os.path.join(parent_folder, image_file)
        merged_image = Image.open(image_path)

        # 각 하위 폴더에 이미지 저장
        for idx, subfolder in enumerate(output_subfolders):
            folder_path = os.path.join(parent_folder, subfolder)
            os.makedirs(folder_path, exist_ok=True)

            # 이미지를 6등분하여 저장
            image_width, image_height = merged_image.size
            split_width = image_width // 3
            split_height = image_height // 2

            left = (idx % 3) * split_width
            top = (idx // 3) * split_height
            right = left + split_width
            bottom = top + split_height

            split_image = merged_image.crop((left, top, right, bottom))

            # 저장할 파일명 생성
            output_filename = f"{image_name}_{idx + 1}.jpg"
            output_path = os.path.join(folder_path, output_filename)

            # 이미지 저장
            split_image.save(output_path)

            # 해당 분할 이미지의 좌표값 조정하여 json 정보를 이동
            for item in json_data:
                x1 = item['coordinates']['x1'] * image_width
                y1 = item['coordinates']['y1'] * image_height
                x2 = item['coordinates']['x2'] * image_width
                y2 = item['coordinates']['y2'] * image_height

                # 좌표가 분할된 이미지 내에 있을 경우에만 정보 이동
                if left <= x1 < right and top <= y1 < bottom and left <= x2 < right and top <= y2 < bottom:
                    item['coordinates']['x1'] -= left / image_width
                    item['coordinates']['y1'] -= top / image_height
                    item['coordinates']['x2'] -= left / image_width
                    item['coordinates']['y2'] -= top / image_height

                    # 수정된 json 정보를 저장할 파일명 생성
                    output_json_filename = f"{image_name}_{idx + 1}.json"
                    output_json_path = os.path.join(folder_path, output_json_filename)

                    # 수정된 json 정보 저장
                    with open(output_json_path, 'w', encoding='utf-8') as json_output:
                        json.dump(json_data, json_output)

print("이미지를 성공적으로 나누어 저장하고 정보를 옮겼습니다.")