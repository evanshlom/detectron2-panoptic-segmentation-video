from Detector import *

detector = Detector(model_type="PS")

detector.onImage("images/1.jpg")

# use ctrl+C in terminal to stop video (it will hog all your CPU memory)
detector.onVideo("videos/A.mp4")