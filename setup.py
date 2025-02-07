from setuptools import setup, find_packages

setup(
    name="pdf2md",
    version="1.0.0",
    author="Leandro Rivera Ríos",
    author_email="leo.232rivera@gmail.com",
    description="Convierte archivos PDF a formato Markdown extrayendo texto, tablas e imágenes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LeoR22/pdf2md",
    packages=find_packages(),
    install_requires=[
        "pdfplumber",
        "Pillow"
    ],
    license="MIT",
    license_files=["LICEN[CS]E*"],
)