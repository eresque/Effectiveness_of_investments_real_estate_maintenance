import os

import numpy as np
from matplotlib import pyplot as plt
import csv

from fastapi import FastAPI, File, UploadFile

app=FastAPI(
    title="back for cbcase"
)

@app.post("/upload")
def upload(file: UploadFile=File(...)):
    try:
        contents=file.file.read()
        with open(file.filename,'wb') as f:
            f.write(contents)
            exp=str(f).split("'")[1].split('.')[1]
            if exp!=("csv"):
                raise Exception("not a csv file")
    except Exception:
        return {"message":"there was an error uploading file"}
    finally:
        file.file.close()
    os.rename(str(f).split("'")[1], "temp.csv")

    return {"message":f"Successfuly uploaded {file.filename}"}

def getGraph():
    try:
        X = []
        Y = []
        Y2 = []
        with open('growth.csv', 'r') as datafile:
            plotting = csv.reader(datafile, delimiter=';')

            for ROWS in plotting:
                X.append(float(ROWS[0]))
                Y.append(float(ROWS[1].replace(',','.')))
                Y2.append(float(ROWS[2].replace(',','.')))
        plt.bar(X,Y,align='edge',color='#00bbe6')
        plt.bar(X,Y2,align='edge',color='#b3b3b3')
        plt.xticks(np.arange(1,19,1))
        plt.title('График прироста цен по месяцам')
        plt.xlabel('Месяц')
        plt.ylabel('Цена')
        return plt
    except Exception:
        return {"message":"error in generating plot"}


@app.get("/test")
def getInfo():
    getGraph().savefig('growth.png')
    templates={"message":"generated succesfully"}
    return templates

