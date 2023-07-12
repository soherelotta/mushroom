import cv2
import numpy as np
from keras.models import load_model

def predict_class(image_path, model_path):
    # モデルの読み込み
    model = load_model(model_path)

    # 画像の前処理
    img = cv2.imread(image_path)
    img = cv2.resize(img, dsize=(150, 150))
    img = img.astype('float32')
    img /= 255.0
    img = img[None, ...]

    # 予測
    result = model.predict(img)
    np.set_printoptions(precision=3, suppress=True)
    result *= 100
    pred = result.argmax()

    return pred

