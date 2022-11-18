from flask import Flask,render_template,request
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf
app = Flask(__name__)
@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/about')
def upload_file1():
    return render_template('predict.html')

@app.route('/upload')
def upload_file2():
    return render_template('predict.html')

@app.route('/upload', methods = ['POST'])
def upload_image_file():
    if request.method=='POST':
        img = Image.open(request.files['file'].stream).convert("L")
        img = img.resize((28,28))
        img2arr = np.array(img)
        img2arr = img2arr.reshape(1,28,28,1)
        model = load_model('mnistCNN.h5')
        #y_pred = model.predict_classes(img2arr)
        y_pred = np.argmax(model.predict(img2arr), axis=1)
        print(y_pred)
        if(y_pred == 0):
            return render_template("predict.html",msg="0")
        elif(y_pred == 1):
            #return render_template("1.html",shoechase = str(y_pred))
            return render_template("predict.html",msg="1")
        elif(y_pred == 2):
            #return render_template("2.html",shoechase = str(y_pred))
            return render_template("predict.html",msg="2")
        elif(y_pred == 3):
            #return render_template("3.html",shoechase = str(y_pred))
            return render_template("predict.html",msg="3")
        elif(y_pred == 4):
            #return render_template("4.html",shoechase = str(y_pred))
            return render_template("predict.html",msg="4")
        elif(y_pred == 5):
            #return render_template("5.html",shoechase = str(y_pred))
            return render_template("predict.html",msg="5")
        elif(y_pred == 6):
            #return render_template("6.html",shoechase = str(y_pred))
            return render_template("predict.html",msg="6")
        elif(y_pred == 7):
            #return render_template("7.html",shoechase = str(y_pred))
            return render_template("predict.html",msg="7")
        elif(y_pred == 8):
            #return render_template("8.html",shoechase = str(y_pred))
            return render_template("predict.html",msg="8")
        else:
            #return render_template("9.html",shoechase = str(y_pred))
            return render_template("predict.html",msg="9")
    else:
        return None
    
if __name__=='__main__':
    app.run()