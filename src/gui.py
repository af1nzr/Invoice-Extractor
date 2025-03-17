import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from src.pdf_processor import extract_text_from_pdf
from src.image_processor import extract_text_from_image
from src.data_extractor import extract_invoice_data
from src.utils import (
    ensure_output_directory_exists,
    log_extracted_text,
    log_processing_steps,
    save_to_txt,
    save_to_pdf,
    save_to_csv,
    save_to_excel,
)
import pandas as pd
import os

# Custom colors and fonts
BG_COLOR = "#2E3440"  # Dark blue-gray
FG_COLOR = "#D8DEE9"  # Light gray
BUTTON_COLOR = "#5E81AC"  # Soft blue
BUTTON_HOVER_COLOR = "#81A1C1"  # Lighter blue
FONT = ("Helvetica", 12)
TITLE_FONT = ("Helvetica", 16, "bold")

def upload_file():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf"), ("Image Files", "*.png *.jpg")])
    if file_paths:
        all_data = []
        for file_path in file_paths:
            try:
                if file_path.endswith(".pdf"):
                    text = extract_text_from_pdf(file_path)
                else:
                    text = extract_text_from_image(file_path)
                
                # Log the extracted text for debugging
                print("Extracted Text:")
                print(text)
                
                log_extracted_text(text)  # Log extracted text
                data = extract_invoice_data(text)
                log_processing_steps(data)  # Log processed data

                if data["Invoice Number"]:
                    all_data.append(data)
                else:
                    messagebox.showerror("Error", f"No invoice data found in {file_path}")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
                messagebox.showerror("Error", f"Failed to process file {file_path}. Check logs for details.")

        if all_data:
            # Ensure the outputs directory exists
            ensure_output_directory_exists()

            # Save data to Excel, CSV, PDF, and/or TXT based on user selection
            df = pd.DataFrame(all_data)
            
            # Debug: Print the DataFrame
            print("DataFrame:")
            print(df)
            
            output_files = []
            if excel_var.get():
                excel_path = "outputs/output.xlsx"
                save_to_excel(df, excel_path)
                output_files.append(excel_path)
            if csv_var.get():
                csv_path = "outputs/output.csv"
                save_to_csv(df, csv_path)
                output_files.append(csv_path)
            if pdf_var.get():
                pdf_path = "outputs/output.pdf"
                save_to_pdf(all_data[0], pdf_path)  # Save the first invoice as PDF
                output_files.append(pdf_path)
            if txt_var.get():
                txt_path = "outputs/output.txt"
                save_to_txt(all_data[0], txt_path)  # Save the first invoice as TXT
                output_files.append(txt_path)

            # Show success message with output paths
            success_message = "Extraction successful! Files saved at:\n"
            success_message += "\n".join([os.path.abspath(path) for path in output_files])
            messagebox.showinfo("Success", success_message)

            # Preview data in a new window
            preview_data(df)

def preview_data(df):
    preview_window = tk.Toplevel()
    preview_window.title("Extracted Data Preview")
    preview_window.geometry("600x400")

    # Create a Treeview widget to display the data
    tree = ttk.Treeview(preview_window, columns=list(df.columns), show="headings")
    
    # Add columns to the Treeview
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Adjust column width as needed
    
    # Insert data into the Treeview
    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    
    # Add a scrollbar
    scrollbar = ttk.Scrollbar(preview_window, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    
    # Pack the Treeview
    tree.pack(fill="both", expand=True)

def start_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Invoice Processing Bot")
    root.geometry("500x400")  # Set window size
    root.configure(bg=BG_COLOR)

    # Add a title label
    title_label = tk.Label(
        root,
        text="Invoice Processing Bot",
        font=TITLE_FONT,
        bg=BG_COLOR,
        fg=FG_COLOR,
        pady=20
    )
    title_label.pack()

    # Add output format selection
    global excel_var, csv_var, pdf_var, txt_var
    excel_var = tk.BooleanVar(value=True)
    csv_var = tk.BooleanVar(value=True)
    pdf_var = tk.BooleanVar(value=False)
    txt_var = tk.BooleanVar(value=False)

    format_frame = tk.Frame(root, bg=BG_COLOR)
    format_frame.pack(pady=10)

    excel_check = tk.Checkbutton(
        format_frame,
        text="Save as Excel",
        variable=excel_var,
        font=FONT,
        bg=BG_COLOR,
        fg=FG_COLOR,
        selectcolor=BG_COLOR  # Background of the checkbox
    )
    excel_check.pack(side=tk.LEFT, padx=10)

    csv_check = tk.Checkbutton(
        format_frame,
        text="Save as CSV",
        variable=csv_var,
        font=FONT,
        bg=BG_COLOR,
        fg=FG_COLOR,
        selectcolor=BG_COLOR  # Background of the checkbox
    )
    csv_check.pack(side=tk.LEFT, padx=10)

    pdf_check = tk.Checkbutton(
        format_frame,
        text="Save as PDF",
        variable=pdf_var,
        font=FONT,
        bg=BG_COLOR,
        fg=FG_COLOR,
        selectcolor=BG_COLOR  # Background of the checkbox
    )
    pdf_check.pack(side=tk.LEFT, padx=10)

    txt_check = tk.Checkbutton(
        format_frame,
        text="Save as TXT",
        variable=txt_var,
        font=FONT,
        bg=BG_COLOR,
        fg=FG_COLOR,
        selectcolor=BG_COLOR  # Background of the checkbox
    )
    txt_check.pack(side=tk.LEFT, padx=10)

    # Add a stylish button
    upload_button = tk.Button(
        root,
        text="Upload Invoice(s)",
        command=upload_file,
        font=FONT,
        bg=BUTTON_COLOR,
        fg=FG_COLOR,
        activebackground=BUTTON_HOVER_COLOR,
        activeforeground=FG_COLOR,
        relief=tk.FLAT,
        padx=20,
        pady=10
    )
    upload_button.pack(pady=20)

    # Add hover effect to the button
    def on_enter(e):
        upload_button.config(bg=BUTTON_HOVER_COLOR)

    def on_leave(e):
        upload_button.config(bg=BUTTON_COLOR)

    upload_button.bind("<Enter>", on_enter)
    upload_button.bind("<Leave>", on_leave)

    # Add a footer label
    footer_label = tk.Label(
        root,
        text="© 2023 Invoice Processing Bot",
        font=("Helvetica", 10),
        bg=BG_COLOR,
        fg=FG_COLOR,
        pady=10
    )
    footer_label.pack(side=tk.BOTTOM)

    # Run the GUI
    root.mainloop()