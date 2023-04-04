import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model

model=load_model('BackEnd/Algorithm/BackEnd/Algorithm/save_models/best_sign_cnn.h5')
path='D:/本科/毕设/数据/CRWU/12k Drive End Bearing Fault Data/Ball/0014/B014_0.mat'
predict=model.predict('D:/本科/毕设/数据/CRWU/12k Drive End Bearing Fault Data/Ball/0014/B014_0.mat')
