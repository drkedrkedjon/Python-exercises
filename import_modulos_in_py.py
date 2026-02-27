#    IMPORTACION DE MODULOS EXTERNOS EN PYTHON

# ---------- Importacion de modulos incrustados en el mismo python
import math
print(math.sqrt(3))

# ---------- Importacion de function desde el otro modulo y TAMBIEN importacion de TODAS las functiones del dicho modulo
from modulos.helper import greeting
import modulos.helper
print(greeting("Sasha"))
print(modulos.helper.greeting("Sasha"))
print(modulos.helper.shitting("Sasha"))

# ---------- Install NUMPY using PIP and use it to make 4x4 arrays nested in array
import numpy as np
num_range = np.arange(16)
reshaped = num_range.reshape(4, 4)
print(reshaped)

# ---------- API connection usando Request Package
# https://jsonplaceholder.typicode.com/ 
# https://jsonplaceholder.typicode.com/posts
import requests
import pprint

api_data = requests.get("https://jsonplaceholder.typicode.com/posts")
# pprint.pprint(api_data.json()[0]["title"])

# ----------- Build web scrapper shit using some shity libraries
# 1. download web page
# 2. selectionar y extraer enlaces
# 3. Convertir enlaces en Titulos

import inflection
from bs4 import BeautifulSoup


def web_scrapper(url):
  api_data = requests.get(url)
  titles = []
  
  html_data = api_data.text
  soup_data = BeautifulSoup(html_data, "html.parser")

  for link in soup_data.find_all("a"):
    href = link.get("href")
    if href and href.startswith("/servicios/"):
      slug = href.split("/servicios/")[-1].strip("/")
      if slug:
        title = inflection.titleize(slug.replace("-", " "))
        titles.append(title)

  return titles
# print(web_scrapper("https://blancodent.com/servicios/servicios"))

