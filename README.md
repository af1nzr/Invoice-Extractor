<h1 align="center">Invoice Extractor</h1>

<p align="center">
    AI-powered tool for extracting structured data from invoices
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
    <img src="https://img.shields.io/badge/Framework-Tkinter-orange.svg" alt="Tkinter">
    <img src="https://img.shields.io/badge/OCR-Pytesseract-green.svg" alt="Pytesseract">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
</p>

---

## **Overview**
**Invoice Extractor** is a Python-based tool designed to **automate the extraction of structured data from invoices** in PDF or image formats.  
It uses **OCR (Optical Character Recognition)** and **regex-based parsing** to extract key details such as:
- **Invoice Number**
- **Date**
- **Billing & Shipping Information**
- **Product/Service Details** (Description, Quantity, Unit Price, Total)
- **Total Amount**

The tool features a **Tkinter-based GUI** for easy file upload and data preview, and it supports exporting extracted data to **Excel, CSV, PDF, or TXT** formats.

---

## **Key Features**
✅ **Multi-Format Support** – Works with **PDFs and images** (PNG, JPG)  
✅ **Structured Data Extraction** – Automatically parses invoice details into a structured format  
✅ **User-Friendly GUI** – Built with **Tkinter** for easy file upload and data preview  
✅ **Export Options** – Save extracted data to **Excel, CSV, PDF, or TXT**  
✅ **Spelling Correction** – Automatically corrects common spelling mistakes in extracted text  

---

## **Installation & Setup**
### **Prerequisites**
Ensure the following dependencies are installed:
- **Python 3.8+**
- **Tesseract OCR** (for text extraction from images)

### **Installation Steps**
```sh
# Clone the repository
git clone https://github.com/af1nzr/Invoice-Extractor.git
cd Invoice-Extractor

# Set up a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py


Usage Guide

1. Launch the GUI by running:
  python main.py

2. Upload Invoices:
 - Click the Upload Invoice(s) button to select PDF or image files.
 - The application will extract and display the data in a preview window.

3. Save Extracted Data:
 - Choose the output format (Excel, CSV, PDF, or TXT).
 - The extracted data will be saved in the outputs folder.

Technologies & Frameworks Used

Python – Core programming language
Tkinter – GUI framework for a user-friendly experience
PyPDF2 – Text extraction from PDF files
Pytesseract – OCR for text extraction from images
Pandas – Data manipulation and export to Excel/CSV
FPDF – Generating PDF files from extracted data
Regex – Parsing and extracting structured data from text

Ethical Considerations & Disclaimer

Invoice Extractor is intended for educational and professional use only.
 - Ensure you have the right to access and process the invoices you upload.
 - The author assumes no responsibility for misuse or violations of privacy.

Future Enhancements

 - Support for More File Formats – Add support for additional formats like DOCX.
 - Machine Learning – Use ML models to improve text extraction accuracy.
 - Cloud Integration – Save extracted data directly to cloud storage (e.g., Google Drive, Dropbox).

License

This project is licensed under the MIT License.
See LICENSE for details.

Contact

For questions or feedback, feel free to reach out:
GitHub: af1nzr
Email: af1nzr07@gmail.com

Acknowledgments

PyPDF2 – For PDF text extraction.
Pytesseract – For OCR-based text extraction from images.
Tkinter – For building the GUI.
Pandas – For data manipulation and export.