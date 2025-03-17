import pandas as pd
from fpdf import FPDF

def ensure_output_directory_exists():
    import os
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

def log_extracted_text(text):
    with open("outputs/extracted_text.log", "a") as log_file:
        log_file.write(text + "\n\n")

def log_processing_steps(data):
    with open("outputs/processing_steps.log", "a") as log_file:
        log_file.write(str(data) + "\n\n")

def save_to_txt(data, file_path):
    with open(file_path, "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

def save_to_pdf(data, file_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
    pdf.output(file_path)

def save_to_csv(df, file_path):
    df.to_csv(file_path, index=False)

def save_to_excel(df, file_path):
    df.to_excel(file_path, index=False)