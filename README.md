# MDFILECONVERT


**mdfileconvert** es una biblioteca de Python que convierte varios tipos de archivos a Markdown, facilitando su uso para documentación, indexación y análisis de texto.

### 🚀 **Características**

Actualmente soporta la conversión de:

- 📄 **PDF** (`.pdf`) – Extrae texto, tablas e imágenes.
- 📜 **Word** (`.docx`)
- 📊 **Excel** (`.xlsx`)
- 🖼️ **Power Point** (`.pptx`)
- 📑 **Archivos de texto** (`.csv`, `.json`, `.xml`, etc.)
---

📂 **Salida Esperada**
Cada archivo se convertirá en un archivo .md con su contenido formateado en Markdown. 🎯

¡Ahora mdfileconvert está listo para usarse de manera eficiente con cualquier tipo de archivo soportado! 🚀😃

---
🛠️ **Mejoras Futuras**
📌 Soporte para imágenes en Markdown (para PDF, PPT).
📌 Mejor manejo de estructuras JSON complejas.

---

## 📥 **Instalación**

Puedes instalar `mdfileconvert` con:

```sh
pip install mdfileconvert
```

## ⚡Uso

#### 📄 Convertir PDF a Markdown

```sh
from mdfileconvert.converter import pdf_to_markdown

with open("archivo.pdf", "rb") as pdf_file:
    markdown_text = pdf_to_markdown(pdf_file)

# Guardar la salida en un archivo Markdown
output_filename = "archivo.md"
with open(output_filename, "w", encoding="utf-8") as md_file:
    md_file.write(markdown_text)

print(f"Markdown guardado en {output_filename}")
```

#### 📜 Convertir Word (DOCX) a Markdown

```sh
from mdfileconvert.converter import docx_to_markdown

markdown_text = docx_to_markdown("documento.docx")

# Guardar la salida en un archivo Markdown

output_filename = "documento.md"
with open(output_filename, "w", encoding="utf-8") as md_file:
    md_file.write(markdown_text)

print(f"Markdown guardado en {output_filename}")
```

#### 📊 Convertir Excel (XLSX) a Markdown

```sh
from mdfileconvert.converter import excel_to_markdown

markdown_text = excel_to_markdown("datos.xlsx")

# Guardar la salida en un archivo Markdown
output_filename = "datos.md"
with open(output_filename, "w", encoding="utf-8") as md_file:
    md_file.write(markdown_text)

print(f"Markdown guardado en {output_filename}")
```

#### 🖼️ Convertir PowerPoint (PPTX) a Markdown

```sh
from mdfileconvert.converter import pptx_to_markdown

markdown_text = pptx_to_markdown("presentacion.pptx")

# Guardar la salida en un archivo Markdown
output_filename = "presentacion.md"
with open(output_filename, "w", encoding="utf-8") as md_file:
    md_file.write(markdown_text)

print(f"Markdown guardado en {output_filename}")
```

#### 📑 Convertir CSV a Markdown

```sh
from mdfileconvert.converter import csv_to_markdown

markdown_text = csv_to_markdown("datos.csv")

# Guardar la salida en un archivo Markdown
output_filename = "datos_csv.md"
with open(output_filename, "w", encoding="utf-8") as md_file:
    md_file.write(markdown_text)

print(f"Markdown guardado en {output_filename}")
```

#### 🔗 Convertir JSON a Markdown

```sh
from mdfileconvert.converter import json_to_markdown

markdown_text = json_to_markdown("datos.json")

# Guardar la salida en un archivo Markdown
output_filename = "datos_json.md"
with open(output_filename, "w", encoding="utf-8") as md_file:
    md_file.write(markdown_text)

print(f"Markdown guardado en {output_filename}")
```

#### 🏗️ Convertir XML a Markdown

```sh
from mdfileconvert.converter import xml_to_markdown

markdown_text = xml_to_markdown("datos.xml")

# Guardar la salida en un archivo Markdown
output_filename = "datos_xml.md"
with open(output_filename, "w", encoding="utf-8") as md_file:
    md_file.write(markdown_text)

print(f"Markdown guardado en {output_filename}")
```


## Contribuciones

**Si deseas contribuir a este proyecto, sigue estos pasos:**

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature-nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Sube los cambios a la rama (`git push origin feature-nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto

- Leandro Rivera: <leo.232rivera@gmail.com>
- Linkedin: <https://www.linkedin.com/in/leandrorivera/>

### ¡Feliz Codificación! 🚀

Si encuentras útil este proyecto, ¡dale una ⭐ en GitHub! 😊
