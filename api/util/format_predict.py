"""format_predict.py"""
import numpy as np

def get_formatted_predict_result(predict_result):
    """
    This function to create a format prediction

    Arg:
    predict_result: Result prediction from model (0,1,2)

    Return:
    class_index: A string from the predict_result
    """
    class_indexes = {
        0: "Meningioma",
        1: "Glioma",
        2: "Pituitari"
    }

    process_predict_result = predict_result[0]
    max_index = np.argmax(process_predict_result)
    return class_indexes[max_index]