import os

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import pandas as pd
import magic
from PIL import Image
from typing import List


path = "C:/Users/tilda/lisa/realpython/fastapi-web-apis"

def media_type():
    file_path = os.path.join(path, 'files/image.csv')

    df = pd.read_csv(file_path)

    image_template = df["Template"].dropna()

    return ', '.join(image_template)

#media_type = media_type()

app = FastAPI()


# media_type = "image/png, image/jpeg"

# print(type(media_type))


@app.get("/")
def index():
    return {"media_type": media_type}

@app.get("/fire")
def fire():
    img = Image.open('files-for-testing/fire-0.jpg')
    return {"format": img.format, "image": img}

@app.post("/fire")
def upload_fire(images: List[UploadFile] = File(...)):
    for image in images:
        # TODO solve for content type
        image = image.read()
        mime = magic.Magic(mime=True)
        # print(image)
        print(mime.from_file(image))


        # print(image.content_type)
        # print(image)
