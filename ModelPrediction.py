import pickle
from pyexpat import model
import pandas as pd
import json 
import numpy as np 
import math 

class ModelPrediction: 
    def loadModel(self,filename):

        model = pickle.load(open(filename, 'rb'))
        print('leido pickle')
        return model
    def predict(self,model,data):
        #calculo
        datos = data.copy()
        df = pd.DataFrame(datos)
        #df = df.set_index('DateObserved)
        print(df.info)
        #realizo predicción y calculo distancia 
        iso_prediction = model.predict(df)
        iso_score = model.score_samples(df)
        # calculo si es una anomalia y su probabilidad
        df['anomaly']=(iso_prediction[0]==-1)
        df['probability'] = iso_score[0]*100*-1*df['anomaly']

        return df 