from ultralytics import YOLO

model = YOLO('Models/best.pt')


results = model.predict('input_vedios\\08fd33_0.mp4',save=True)


print(results[0])
print("==========")
for box in results[0].boxes:
    print(box)