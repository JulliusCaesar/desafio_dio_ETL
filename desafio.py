import requests
from urllib import request
import pandas as pd

df = pd.read_csv("links.csv")

url = "https://api.pdfendpoint.com/v1/convert"


def generation_pdf(link):
    payload = {
        "url": link,
        "sandbox": True,
        "orientation": "vertical",
        "page_size": "A4",
        "margin_top": "2cm",
        "margin_bottom": "2cm",
        "margin_left": "2cm",
        "margin_right": "2cm"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 03f9a882e2e575de8567493c39c6349e53d66ac64b"
    }

    return requests.request("POST", url, json=payload, headers=headers)

#print(response.content)

for link in range(0, len(df)):
    get_response = generation_pdf(df['url'][link])
    resposta = get_response.json()
    file_url = resposta['data']['url']
    file = df['site'][link] + ".pdf"
    request.urlretrieve(file_url, file)