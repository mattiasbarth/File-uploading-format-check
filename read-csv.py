import os

import pandas as pd


path = 'C:/Users/tilda/lisa/realpython/fastapi-web-apis'

def my_func():
    file_path = os.path.join(path, 'files/image.csv')

    df = pd.read_csv(file_path)

    image_template = df["Template"].dropna()
    for temp in iter(e for e in image_template if e != "nan"):
        if type(temp) != str:
            print(temp, type(temp))

    return ', '.join(image_template)

print(my_func())