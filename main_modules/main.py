import face_recognition
import os
import cv2
import numpy as np

"""
    [Modules] 스트림으로 측정 되는 얼굴이 등록된 얼굴 인지 여부를 확인 하는 모듈
    - 존재 할 경우 파일명으로 이름이 그려지고
    - 존재하지 않을 경우 Unknown으로 이름이 그려집니다. 
"""

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# STEP1: 저장된 이미지 모든 리스트(ALL)를 가져온다.
# TODO: 추후 S3 혹은 저장된 공간에서 이미지를 가져 올 예정.
images = os.listdir("images")
print(images)

# STEP2: 저장된 이미지를 인코딩 및 이름을 각각 지정 하는 배열
known_face_encodings = []
known_face_names = []

# STEP3: Loop를 수행 하면서 비교 대상 파일 && 비교 대상 파일을 인코딩 함
for image in images:
    file_name = image.split('.')[0]         # 파일 명
    file_ext = image.split('.')[1]          # 파일 확장자

    # STEP4: 디렉토리 내에 이미지인 경우만 수행을 한다.
    if file_ext == 'png' or file_ext == 'jpeg' or file_ext == 'jpg':

        # STEP 4-1: 각각의 파일을 하나씩 가져옴
        current_image = face_recognition.load_image_file("images/" + image)

        # STEP 5: 불러 온 사진의 랜드마크를 찍어서 얼굴 탐지 여부를 체크
        face_landmarks_list = face_recognition.face_landmarks(current_image)

        # STEP 6: 얼굴을 탐지한 경우 - 얼굴의 랜드마크가 존재 하는 경우
        if len(face_landmarks_list) > 0:
            # STEP 6-1: 이미지 인코딩
            current_image_encoded = face_recognition.face_encodings(current_image)[0]
            # STEP 6-2: 등록된 사용자 이미지 (인코딩 값)를 배열에 넣음
            known_face_encodings.append(current_image_encoded)
            # STEP 6-3: 등록된 사용자 이름을 배열에 넣음
            known_face_names.append(file_name)
        else:
            print(" ============== 얼굴을 탐지 못 하였습니다 ==============> ", image)
    else:
        print("============== 이미지 파일이 아닙니다.==============")


# 변수 초기화
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# STEP4: 반복 하여 스트림과 등록된 이미지를 비교한다.
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the images from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []

        # 등록된 이미지(known_face_encodings)와 스트림으로 찍히는 얼굴(face_encoding)을 비교한다.
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting images
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
