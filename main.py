
# Importaciones
# requests: es una biblioteca estándar para realizar solicitudes HTTP. Permite enviar peticiones a servidores web y obtener respuestas, como HTML, JSON, etc.
# BeautifulSoup: es una clase del módulo bs4, usada para analizar y extraer información de documentos HTML o XML de forma estructurada.
import csv
import requests
from bs4 import BeautifulSoup
'''
Pasos practica
1. Obtener el maquetado HTML
    -Si el archivo html no exite de forma local crearlo
    -Si el archivo html  exite de forma local obtener contenido
2.Obtener la informacion 
    -titulo
    - precio
    -stock
3.Generar un archivo CSV
'''
BASE_URL="https://books.toscrape.com/catalogue/page-{}.html"

# Reaizar peticion para obtener maquetado
def get_books_content(url):
    headers={
     'User-Agent':'Mozilla/5.0'   
    }
    response =requests.get(url,headers=headers)
 
    if  response.status_code==200:
        return response.text
    return None
 # crear archivo de forma local
def create_file (content):
    try :
        with open('books.html','w') as file:
            file.write(content)
    except :
        pass

## Leer archivo local
def get_file ():
    content:None
    try :
        with open('books.html','r', encoding='utf-8') as file:
            content= file.read()
    except :
        pass
    return content

def create_book(tag):
    
    
    titulo = tag.h3.a['title']  
    precio = tag.find('p', class_='price_color').text
    stock = tag.find('p', class_='instock').text.strip()
    print(f'Título: {titulo} | Precio: {precio}| Stock: {stock}\n') 
    return (titulo,precio,stock)

def create_book(tag):
    
    
    titulo = tag.h3.a['title']  
    precio = tag.find('p', class_='price_color').text
    stock = tag.find('p', class_='instock').text.strip()
    return (titulo,precio,stock)


def main():
    page_number = 1
    libros = []
    while True:
        url = BASE_URL.format(page_number)
        print(f"Procesando página {page_number}: {url}")
        
        content = get_books_content(url)  # <--- Aquí cambiamos la función
        if content is None:
            print("Fin del catálogo o error en la petición.")
            break
        
        soup = BeautifulSoup(content, 'html.parser')
        article_tag = soup.find_all('article', class_='product_pod')
        if not article_tag:
            break
        
        for tag in article_tag:
            libro = create_book(tag)
            libros.append(libro)
        
        page_number += 1
    with open('libros.csv','w', encoding='utf-8', newline='') as file:
        writes=csv.writer(file)
        for libro in libros :
                writes.writerow(libro)
 
# Este bloque evalúa si el script se está ejecutando directamente (no importado como módulo).
if __name__ == '__main__' :  
    main()