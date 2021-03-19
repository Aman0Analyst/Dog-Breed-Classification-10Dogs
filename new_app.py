from flask import Flask,jsonify,request
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.applications.resnet import preprocess_input
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow import keras
import numpy as np
import base64
from io import BytesIO
from PIL import Image

def preprocess_image(file):
    image_64_decoded = base64.decodebytes(bytes(file,'Utf-8')) 
    image = np.array(Image.open(BytesIO(image_64_decoded)))
    image = preprocess_input(image)
    image = np.expand_dims(image,axis = 0)
    return image


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/predict', methods = ['POST'])    
def predict():
    data = request.get_json()
    img  = preprocess_image(data['image'])
    Model = load_model('Resnet50_10dogs.h5')
    predictions = Model.predict(img).ravel()

    Label_map = {0: 'beagle',
                1: 'chihuahua',
                2: 'doberman',
                3: 'french_bulldog',
                4: 'golden_retriever',
                5: 'malamute',
                6: 'pug',
                7: 'saint_bernard',
                8: 'scottish_deerhound',
                9: 'tibetan_mastiff'}
    
    Dog_breed = Label_map[np.argmax(predictions)]
    confidence = predictions[np.argmax(predictions)]

    output = {'breed': Dog_breed,'score' : str(confidence)}
    return jsonify(output)


if __name__ == "__main__":
    app.run()    