# AFD: Análisis y Extracción de Patrones

Este proyecto implementa un autómata finito determinista (AFD) para validar y extraer RFCs (Registro Federal de Contribuyentes) de varios tipos de archivos, incluyendo `.xlsx`, `.csv`, `.xls`, `.pdf` y `.docx`.

## Requisitos

- Python 3.x
- Librerías necesarias:
  - `tkinter`
  - `pandas`
  - `python-docx`
  - `PyPDF2`
  - `openpyxl`

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/moraema/AFD_RFC.git
   cd AFD_RFC

2. Instala las dependencias
   ```sh
   pip install pandas python-docx PyPDF2 openpyxl

## Uso

1. Ejecuta el script principal:
   ```sh
   python main.py

2. En la interfaz gráfica, haz clic en "Cargar archivo" para seleccionar un archivo de los tipos permitidos (.xlsx, .csv, .xls, .pdf, .docx).

3. Los RFCs válidos encontrados se mostrarán en el área de resultados.

4. Puedes guardar los resultados en un archivo CSV haciendo clic en "Guardar resultados en CSV".