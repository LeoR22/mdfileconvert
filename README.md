# MDFILECONVERT


**mdfileconvert** es una biblioteca de Python que convierte varios tipos de archivos a Markdown, facilitando su uso para documentación, indexación y análisis de texto.

### 🚀 **Características**

Actualmente soporta la conversión de:

- 📄 **PDF** (`.pdf`) – Extrae texto, tablas e imágenes.

### **Futuras versiones**
Se espera que pueda realizar lo mismo en diferentes formatos como:
- 📜 **Word** (`.docx`)
- 📊 **Excel** (`.xlsx`)
- 🖼️ **Power Point** (`.pptx`)
- 📑 **Archivos de texto** (`.csv`, `.json`, `.xml`, etc.)
---

## 📥 **Instalación**

Puedes instalar `mdfileconvert` con:

```sh
pip install mdfileconvert
```

## ⚡Uso
Como API en python
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

Leandro Rivera: <leo.232rivera@gmail.com>
Linkedin: <https://www.linkedin.com/in/leandrorivera/>

### ¡Feliz Codificación! 🚀

Si encuentras útil este proyecto, ¡dale una ⭐ en GitHub! 😊
