import os

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import pandas as pd
#import magic
from PIL import Image
from typing import List


path = "C:/Users/tilda/lisa/realpython/fastapi-web-apis"

def media_type():
    file_path = os.path.join(path, 'files/image.csv')

    df = pd.read_csv(file_path)

    image_template = df["Template"].dropna()

    return ', '.join(image_template)

#media_type = media_type()

MAGIC_NUMBERS = {"png": bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
                 "jpg": bytes([0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0x01])}
MAX_READ_SIZE = max(len(key) for key in MAGIC_NUMBERS.values())

app = FastAPI()


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
        image = image.file.read(MAX_READ_SIZE)

        print(type(image))


        if any([image.startswith(magic) for magic in MAGIC_NUMBERS.values()]):
            print("HURRAY!")
            # TODO compare image.file and magic_number key
        else:
            print("No")

