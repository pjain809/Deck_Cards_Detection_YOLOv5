
import os
import sys
import shutil
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, render_template, Response
from YOLO_Object_Detection.pipeline.training_pipeline import TrainPipeline
from YOLO_Object_Detection.constants.application import APP_HOST, APP_PORT
from YOLO_Object_Detection.utils.main_utils import encodeImageIntoBase64, decodeImage


app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"


@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successful"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods = ['POST', 'GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)

        os.system("python yolov5/detect.py --weights yolov5/best.pt --img 416 --conf 0.5 --source data/inputImage.jpg")
        opencodedbase64 = encodeImageIntoBase64("yolov5/runs/detect/exp/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}
        shutil.rmtree("yolov5/runs")

    except ValueError as val:
        print(val)
        return Response("Request does not contain expected value.")
    except KeyError:
        return Response("Request does not contain expected key.")
    except Exception as e:
        print(e)
        result = "Invalid Input"

    return jsonify(result)


@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:
        os.system("python yolov5/detect.py --weights yolov5/best.pt --img 416 --conf 0.5 --source 0")
        shutil.rmtree("yolov5/runs")
        return "Camera Starting"

    except ValueError as val:
        print(val)
        return Response("Request does not contain expected value.")


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST,
            port=APP_PORT)
