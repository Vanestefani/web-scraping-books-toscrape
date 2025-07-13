
# Book Scraper - Books to Scrape

Este proyecto realiza web scraping sobre el sitio [Books to Scrape](https://books.toscrape.com/) para extraer información relevante de libros, como el **título**, **precio** y **stock**, y guardarla en un archivo CSV.

## 📌 Requisitos

- Python 3.x
- Librerías especificadas en `requirements.txt`

## 🛠 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/nombre_repositorio.git
   cd nombre_repositorio
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Ejecución

Ejecuta el script principal:

```bash
python main.py
```

Esto generará un archivo `libros.csv` con los datos recolectados.

## 📁 Archivos generados

- `libros.csv`: archivo con los datos de todos los libros procesados.

## 🧩 Tecnologías

- `requests` para realizar las solicitudes HTTP.
- `BeautifulSoup` para parsear y analizar el HTML.

---

**Sitio objetivo:** [Books to Scrape](https://books.toscrape.com/)  
**Propósito:** Proyecto educativo para prácticas de scraping.
