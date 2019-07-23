import numpy as np
import tensorflow as tf
from PIL import Image
from keras.models import load_model
from keras.preprocessing.image import img_to_array

graph = tf.get_default_graph()


# This function loads the model in memory
def get_model():
    global model
    model = load_model('myapp/model.h5')  # here we should put the file name of the model.h5
    print("\n\t\t***Model loaded!***\n")


# This function takes the image entered by the user and adjust it to be suitable for the model
# 1- RGB check, 2- resizing with 244, 3- convert to numpy array, 4- expand the dimensions of the image!!
def preprocess_image(image):
    if image.mode != 'RGB':
        image = image.convert('RGB')

    width = 224
    height = 224
    image = image.resize((width, height), Image.NEAREST)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    return image


print("\n\t\t***Loading model***\n")
get_model()  # Load model in memory


# This function take the image as a PIL image object
# Here w pass the preprocessed image to model.predict()
# model.predict returns a numpy array with the predicted values so we should convert it to a normal integer list
def predict(img):
    with graph.as_default():
        prediction = model.predict(preprocess_image(img)).tolist()

    return prediction
