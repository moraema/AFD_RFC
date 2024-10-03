import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from docx import Document
from automata_RFC import AFDValidorRFC
import PyPDF2

class AFDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AFD: Análisis y Extracción de Patrones")
        
        self.root.configure(bg="#AAF9BD")
        self.load_button = tk.Button(root, text="Cargar archivo", command=self.reset,  bg="#4CAF50", fg="white", font=("Arial", 12))
        self.load_button.pack(pady=20)

        self.result_area = tk.Text(root, height=20, width=80, bg="#ffffff", fg="#333333", font=("Arial", 10))
        self.result_area.pack(pady=10)

        self.save_button = tk.Button(root, text="Guardar resultados en CSV", command=self.save_results, bg="#2196F3", fg="white", font=("Arial", 12))
        self.save_button.pack(pady=10)
        
        self.exit_buttom = tk.Button(root, text="Salir", command=root.quit, bg="#f44336", fg="white", font=("Arial", 12))
        self.exit_buttom.pack(pady=20)
       
        self.results = []
        self.rfc_validator = AFDValidorRFC()

    def load_file(self):
        file = filedialog.askopenfilename(filetypes=[
            ("Archivos permitidos", "*.xlsx;*.csv;*.xls;*.pdf;*.docx"),
            ("Todos los archivos", "*.*")
        ])
        
        if file:
            try:
                if file.endswith('.xlsx') or file.endswith('.xls'):
                    df = pd.read_excel(file, engine='openpyxl')
                    self.process_excel(df)
                elif file.endswith('.csv'):
                    df = pd.read_csv(file)
                    self.display_dataframe(df)
                elif file.endswith('.docx'):
                    doc = Document(file)
                    self.process_rfc(doc)
                elif file.endswith('.pdf'):
                    self.process_pdf(file)
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar archivo: {e}")

    def process_rfc(self, doc):
        all_valid_rfc = []
        self.rfc_validator.reset()
    
        for parrafo_idx, parrafo in enumerate(doc.paragraphs):
            texto = parrafo.text
            rfc_encontrados = self.rfc_validator.procesar(texto)
    
            for rfc in rfc_encontrados:
                start_idx = texto.find(rfc)
                if start_idx != -1:
                    columna = start_idx + 1
                else:
                    columna = 1
    
                all_valid_rfc.append({
                    'rfc': rfc,
                    'fila': parrafo_idx + 1,
                    'columna': columna
                })
    
        if all_valid_rfc:
            self.result_area.insert(tk.END, "RFC válidos encontrados: \n")
            for item in all_valid_rfc:
                self.result_area.insert(tk.END, f"Fila: {item['fila']} - Columna: {item['columna']} - RFC: {item['rfc']}\n")
            self.results.extend(all_valid_rfc)
            print(f"RFCs válidos encontrados: {all_valid_rfc}")
        else:
            self.result_area.insert(tk.END, "No se encontró ningún RFC válido.\n")
    
    def process_pdf(self, file):
        all_valid_rfc = []
        self.rfc_validator.reset()
        
        with open(file, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                texto = page.extract_text()
                rfc_encontrados = self.rfc_validator.procesar(texto)
                
                for rfc in rfc_encontrados:
                    start_idx = texto.find(rfc)
                    if start_idx != -1:
                        columna = start_idx + 1
                    else:
                        columna = 1
    
                    all_valid_rfc.append({
                        'rfc': rfc,
                        'fila': page_num + 1,
                        'columna': columna
                    })
    
        if all_valid_rfc:
            self.result_area.insert(tk.END, "RFC válidos encontrados: \n")
            for item in all_valid_rfc:
                self.result_area.insert(tk.END, f"Página: {item['fila']} - Columna: {item['columna']} - RFC: {item['rfc']}\n")
            self.results.extend(all_valid_rfc)
            print(f"RFCs válidos encontrados: {all_valid_rfc}")
        else:
            self.result_area.insert(tk.END, "No se encontró ningún RFC válido.\n")

    def process_excel(self, df):
        all_valid_rfc = []
        self.rfc_validator.reset()
        
        for idx, row in df.iterrows():
            for col in df.columns:
                texto = str(row[col])
                rfc_encontrados = self.rfc_validator.procesar(texto)
                
                for rfc in rfc_encontrados:
                    all_valid_rfc.append({
                        'rfc': rfc,
                        'fila': idx + 1,
                        'columna': col
                    })

        if all_valid_rfc:
            self.result_area.insert(tk.END, "RFC válidos encontrados: \n")
            for item in all_valid_rfc:
                self.result_area.insert(tk.END, f"Fila: {item['fila']} - Columna: {item['columna']} - RFC: {item['rfc']}\n")
            self.results.extend(all_valid_rfc)
            print(f"RFCs válidos encontrados: {all_valid_rfc}")
        else:
            self.result_area.insert(tk.END, "No se encontró ningún RFC válido.\n")

    def save_results(self):
        if not self.results:
            messagebox.showinfo("Información", "No hay resultados para guardar.")
            return
        
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        
        if save_path:
            try:
                df = pd.DataFrame(self.results, columns=['fila', 'columna', 'rfc'])
                df.to_csv(save_path, index=False)
                messagebox.showinfo("Éxito", f"Resultados guardados en {save_path}")
                self.result_area.delete(1.0, tk.END)
                self.results.clear()
            except Exception as e:
                messagebox.showerror("Error", f"Error al guardar archivo: {e}")

    def reset(self):
        self.reset_pantalla()
        self.load_file()

    def reset_pantalla(self):
        self.result_area.delete(1.0, tk.END)
        self.results.clear()