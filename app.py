import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.models import Sequential, load_model
from tensorflow import keras
from werkzeug.utils import secure_filename
import numpy as np


ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
UPLOAD_FOLDER = 'uploads'
Model = load_model('Resnet50_10dogs.h5')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def preprocess_image(path):
    from tensorflow.keras.applications.resnet import preprocess_input
    from tensorflow.keras.preprocessing.image import load_img,img_to_array
    import numpy as np

    image = load_img(path,target_size=(299,299,1))
    image = img_to_array(image)
    image = np.expand_dims(image,axis = 0)
    image = preprocess_input(image)
    return image

def predict(file):
    img  = preprocess_image(file)
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

    output = {'Dog_breed :': Dog_breed,              'confidence': confidence}
    return output

app = Flask(__name__, template_folder='Templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def template_test():
    return render_template('home.html', label='', imagesource='file://null')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            output = predict(file_path)
    return render_template("home.html", label=output, imagesource=file_path)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == "__main__":
    app.run(threaded=False)
