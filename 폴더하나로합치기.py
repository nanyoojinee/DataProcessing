import os
import shutil


def merge_folders(input_directory, output_directory):
    # 결과 디렉토리가 없으면 생성
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 작업 디렉토리 내의 모든 파일 찾기
    for folder, _, file_list in os.walk(input_directory):
        for file_name in file_list:
            source_path = os.path.join(folder, file_name)
            destination_path = os.path.join(output_directory, file_name)

            # 파일을 결과 디렉토리로 복사
            shutil.copy(source_path, destination_path)

    print("작업 완료")


# 함수를 호출하여 작업 수행
merge_folders(r"C:\Users\정유진\Desktop\난유지니\난유지니", r"C:\Users\정유진\Desktop\난유지니\결과")
