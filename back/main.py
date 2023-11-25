import os

import numpy as np
from matplotlib import pyplot as plt
import csv

from fastapi import FastAPI, File, UploadFile
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(
    title="back for cbcase"
)
origins = [
    'http://localhost:3000',
    'http://localhost:5173',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:5173'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/uploadmany")
def uploadMany(files: List[UploadFile] = File(...)):
    try:
        u=0
        for i, file in enumerate(files):
            try:
                contents = file.file.read()
                with open(file.filename, 'wb') as f:
                    f.write(contents)
                    exp=(str(f).split("'")[1].split('.'))[len(str(f).split("'")[1].split('.'))-1]
                    if exp!=("csv"):
                        raise Exception("not a csv file")
            except Exception:
                return {"message": "There was an error uploading the file(s)"}
            finally:
                file.file.close()
                os.replace(str(f).split("'")[1], f"temp{i}.csv")
            u=i+1
        if u!=3:
            raise Exception("not enough or to many files")
    except Exception:
        return {"message": "There was an error uploading the file(s)"}

    return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}


@app.post("/uploadone")
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
        plt.bar(X,Y,align='edge',color='#0088cc')
        plt.bar(X,Y2,align='edge',color='#686e7a') 
        plt.xticks(np.arange(1,19,1))
        plt.title('График прироста цен по месяцам')
        plt.xlabel('Месяц')
        plt.ylabel('Цена')
        return plt
    except Exception:
        return {"message":"error in generating plot"}


def getInfo():
    getGraph().savefig('growth.png')
    templates={"message":"generated succesfully"}
    return templates

