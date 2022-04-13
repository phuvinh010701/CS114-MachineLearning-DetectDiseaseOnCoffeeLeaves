#from crypt import methods
from ctypes import resize
from email.mime import image
from flask import Flask,render_template,request
import cv2
import random
import json
app = Flask(__name__,static_url_path='/static')
with open('static/json/solve.json') as json_file:
    solve = json.load(json_file)

class YoloV4:
    def __init__(self):
        self.net = cv2.dnn.readNetFromDarknet("model/yolov4.cfg","model/yolov4.weights")
        self.model = cv2.dnn_DetectionModel(self.net)
        self.classes = {
            0 : "Sau ve bua",
            1 : "Phan trang",
            2 : "Nam ri sat",
            3 : "Dom rong"
        }
        self.color = {
            1 : (0,255,0),
            2 : (255,0,0),
            3 : (0,0,255)
        }
    def load_model(self):
        self.model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
    def predict(self,path):
        img = cv2.imread(path)
        h = img.shape[0]
        w = img.shape[1]
        # img = cv2.resize(img,(416,416))
        i = 0
        classIds, scores, boxes = self.model.detect(img, confThreshold=0.25, nmsThreshold=0.4)
        for (classId, score, box) in zip(classIds, scores, boxes):
            index = random.randint(1,3)
            cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                    color=self.color[index], thickness=2)
    
            text = '%s: %.2f' % (self.classes[classIds[i]], score)
            print(classId)
            if box[1] < 100:
                cv2.rectangle(img,(box[0],box[1] + box[3]),(box[0]+300, box[1] + box[3]+ 30),self.color[index],-1)
                cv2.putText(img, text, (box[0], box[1] + box[3]+ 20), cv2.FONT_HERSHEY_SIMPLEX, 1,
                color=(255,255,255), thickness=2)
            else:
                cv2.rectangle(img,(box[0],box[1]-30),(box[0]+300, box[1]),self.color[index],-1)
                cv2.putText(img, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                color=(255,255,255), thickness=2)
            i += 1
        name = path.split(".jpg")
        imgDetected = "{}.jpg".format(name[0]+"_detected")
        img = cv2.resize(img,(w,h))
        cv2.imwrite(imgDetected,img)
        return classIds,imgDetected
m = YoloV4()
m.load_model()
@app.route("/")
def index():
    print(solve["0"]["treatment"][0])
    return render_template("index.html")

@app.route("/detect",methods=['POST','GET'])
def detect():
    if request.method == "POST":
        imgFile = request.files['file'];
        # imgFile = request.args.get("img")
        imgPath =   "./static/images/" + imgFile.filename
        imgFile.save(imgPath)
        classIds,path = m.predict(imgPath)
        res = '{'
        for i in range(0,len(classIds)):
            tmp = '{' + '"name":' + '"' +solve[str(classIds[i])]["name"] + '"' + ',' +'"treatment":'+'["'+ solve[str(classIds[i])]["treatment"][0] +'","' + solve[str(classIds[i])]["treatment"][1]+ '"]'
            tmp = tmp + ',' +'"image":'+'"'+ solve[str(classIds[i])]["image"][0] +'"' + ',' + '"guide":' + '"' + solve[str(classIds[i])]["guide"] + '"' +'}'
            res = res + '"{}":{},'.format(str(i),tmp)
            # res = res + str(i) + ":" + str(classIds[i]) + ","
        res = res + '"{}":"{}"'.format("path",path) + '}'
        return res
        # return "<img src='"+path+"'/>"
if __name__ == "__main__":
    app.run(debug=False)
