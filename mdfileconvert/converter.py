import pdfplumber
import re
import io
import os
from PIL import Image
import docx
import pandas as pd
import json
import xml.etree.ElementTree as ET
from pptx import Presentation

# Umbrales mínimos (en puntos) para considerar una imagen "grande y entendible"
MIN_WIDTH = 100
MIN_HEIGHT = 100

def pdf_to_markdown(pdf_file):
    """Convierte un archivo PDF a Markdown con texto, tablas e imágenes."""
    output = io.StringIO()
    os.makedirs("temporal", exist_ok=True)

    with pdfplumber.open(pdf_file) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            output.write(f"## Página {page_num}\n\n")

            # Extraer y formatear el texto
            text = page.extract_text()
            if text:
                output.write(text + "\n\n")

            # Extraer tablas
            tables = page.extract_tables()
            if tables:
                output.write("### Tablas extraídas:\n\n")
                for table in tables:
                    if table:
                        df = pd.DataFrame(table)
                        output.write(df.to_markdown(index=False) + "\n\n")

            # Extraer imágenes
            im = page.to_image()
            for i, bbox in enumerate(page.images):
                x0, top, x1, bottom = bbox["x0"], bbox["top"], bbox["x1"], bbox["bottom"]
                width, height = x1 - x0, bottom - top
                if width >= MIN_WIDTH and height >= MIN_HEIGHT:
                    cropped = im.original.crop((x0, top, x1, bottom))
                    image_filename = f"temporal/imagen_{page_num}_{i}.png"
                    cropped.save(image_filename, format="PNG")
                    output.write(f"![Imagen de página {page_num}, imagen {i}]({image_filename})\n\n")

    return output.getvalue()

def docx_to_markdown(docx_file):
    """Convierte un archivo Word (.docx) a formato Markdown."""
    doc = docx.Document(docx_file)
    output = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            style_name = getattr(para.style, "name", "").lower()
            if "heading" in style_name:
                level = re.search(r"\d+", style_name)
                level = int(level.group()) if level else 2
                output.append("#" * level + " " + text)
            else:
                output.append(text)

    return "\n\n".join(output)

def xlsx_to_markdown(xlsx_file):
    """Convierte un archivo Excel (.xlsx) a formato Markdown."""
    output = []
    xls = pd.ExcelFile(xlsx_file)

    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)
        output.append(f"## Hoja: {sheet_name}\n")
        if hasattr(df, "to_markdown"):
            output.append(df.to_markdown(index=False))
        else:
            output.append(df.to_csv(sep="|", index=False))

    return "\n\n".join(output)

def json_to_markdown(json_file):
    """Convierte un archivo JSON a Markdown como bloque de código."""
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return "```json\n" + json.dumps(data, indent=4, ensure_ascii=False) + "\n```"

def xml_to_markdown(xml_file):
    """Convierte un archivo XML a formato Markdown."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    def parse_element(element, level=0):
        md = "#" * (level + 2) + f" {element.tag}"
        if element.attrib:
            md += " " + json.dumps(element.attrib, indent=4, ensure_ascii=False)
        md += "\n"
        if element.text and element.text.strip():
            md += f"{element.text.strip()}\n"
        for child in element:
            md += parse_element(child, level + 1)
        return md

    return parse_element(root)
