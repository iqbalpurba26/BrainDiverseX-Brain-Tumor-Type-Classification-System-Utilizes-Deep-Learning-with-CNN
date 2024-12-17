"""endpoint.py"""
import numpy as np
import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from util.format_predict import get_formatted_predict_result
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
model = tf.keras.models.load_model('tumor-brain.h5')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
def predict(image: UploadFile = File(...)):
    """
    The enpoint that will be called

    Arg:
    image: An image scan MRI

    Return:
    Classification tumor
    """

    try:
        image_pil = Image.open(image.file).convert('RGB')

        expected_size = (150,150)
        resized_image_pil = image_pil.resize(expected_size)

        image_array = np.array(resized_image_pil)/255.0
        batched_rescaled_image_array = np.expand_dims(image_array, axis=0)

        result = model.predict(batched_rescaled_image_array)
        classification = get_formatted_predict_result(result)

        return {"classification": classification}
    except Exception as e:
        return {"error": str(e)}