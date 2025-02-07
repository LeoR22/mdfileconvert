# pdf2md

pdf2md es una librería de Python para convertir archivos PDF a Markdown, extrayendo texto, tablas e imágenes.

## Instalación

```sh
pip install pdf2md
```

## Uso

```sh
from pdf2md.converter import pdf_to_markdown

with open("archivo.pdf", "rb") as pdf_file:
    markdown_text = pdf_to_markdown(pdf_file)

print(markdown_text)
```
