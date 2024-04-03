
import os
import json

def process_coordinates(data):
    for item in data:
        coordinates = item.get('coordinates', None)
        if coordinates:
            coordinates['x1'] *= 1920
            coordinates['x2'] *= 1920
            coordinates['y1'] *= 1080
            coordinates['y2'] *= 1080
    return data

def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                processed_data = process_coordinates(data)
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(processed_data, f, indent=4, ensure_ascii=False)

# 사용 예시:
folder_path =r'C:\Users\정유진\Downloads\롯데어쩌고저쩌고'  # 폴더의 실제 경로로 바꿔주세요
process_folder(folder_path)
