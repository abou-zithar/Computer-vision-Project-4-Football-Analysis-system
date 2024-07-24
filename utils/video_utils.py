import cv2 as cv

def read_video(video_path):
    cap = cv.VideoCapture(video_path)
    frames = []
    while True:
        # ret is flag means is there a next frame or the video ended
        ret, frame =cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames,output_video_path):
    fourcc = cv.VideoWriter.fourcc(*'XVID')
    out = cv.VideoWriter(output_video_path,fourcc,24.0,(output_video_frames[0].shape[1],output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()