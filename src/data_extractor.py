import re

def preprocess_text(text):
    """
    Preprocesses the extracted text to make it easier to parse.
    """
    # Correct spelling mistakes
    text = text.replace("cr eate", "create")
    text = text.replace("y our", "your")
    text = text.replace("It' s", "It's")
    
    return text

def extract_invoice_data(text):
    """
    Extracts invoice data from the given text using a state-based approach.
    """
    # Preprocess the text
    text = preprocess_text(text)
    
    # Split the text into lines
    lines = text.split('\n')
    
    # Initialize variables
    data = {
        "Date": "Unknown Date",
        "Invoice Number": "Unknown Invoice Number",
        "Billing Name": "Unknown Billing Name",
        "Shipping Name": "Unknown Shipping Name",
        "Billing Address": "Unknown Billing Address",
        "Shipping Address": "Unknown Shipping Address",
        "Billing City": "Unknown Billing City",
        "Shipping City": "Unknown Shipping City",
        "Phone Number": "Unknown Phone Number",
        "Email": "Unknown Email",
        "Products": [],
        "Total Amount": "Unknown Total Amount"
    }
    
    # State variables
    is_billing_section = False
    is_shipping_section = False
    is_product_section = False
    product_buffer = ""
    
    # Iterate through each line
    for line in lines:
        line = line.strip()
        
        # Extract date
        if re.match(r'\d{2}/\d{2}/\d{4}', line):
            data["Date"] = line
        
        # Extract invoice number
        if "Sample Inv" in line:
            match = re.search(r'(\w+)\s*Sample Inv', line)
            if match:
                data["Invoice Number"] = match.group(1)
        
        # Extract billing information
        if "Billing Information" in line:
            is_billing_section = True
            is_shipping_section = False
            is_product_section = False
            continue
        
        if is_billing_section:
            if "Shipping Information" in line:
                is_billing_section = False
                is_shipping_section = True
                continue
            if not data["Billing Name"]:
                data["Billing Name"] = line
            elif not data["Billing Address"]:
                data["Billing Address"] = line
            elif not data["Billing City"]:
                data["Billing City"] = line
        
        # Extract shipping information
        if is_shipping_section:
            if "Phone Number" in line:
                is_shipping_section = False
                continue
            if not data["Shipping Name"]:
                data["Shipping Name"] = line
            elif not data["Shipping Address"]:
                data["Shipping Address"] = line
            elif not data["Shipping City"]:
                data["Shipping City"] = line
        
        # Extract phone number
        if "Phone Number" in line:
            match = re.search(r'\((.*?)\)', line)
            if match:
                data["Phone Number"] = match.group(1)
        
        # Extract email
        if "Email" in line:
            match = re.search(r'([\w\.-]+@[\w\.-]+)', line)
            if match:
                data["Email"] = match.group(1)
        
        # Extract product details
        if "Description Quantity Unit Price Total" in line:
            is_product_section = True
            continue
        
        if is_product_section:
            if "Total:" in line:
                is_product_section = False
                # Extract total amount
                match = re.search(r'Total:\s*(\d+)', line)
                if match:
                    data["Total Amount"] = match.group(1)
                continue
            if "Product/Service" in line:
                if product_buffer:
                    # Process the buffered product line
                    parts = product_buffer.split()
                    try:
                        description = " ".join(parts[2:-3])
                        quantity = parts[-3]
                        unit_price = parts[-2]
                        total = parts[-1]
                        data["Products"].append({
                            "description": description,
                            "quantity": quantity,
                            "unit_price": unit_price,
                            "total": total
                        })
                    except IndexError:
                        print(f"Skipping malformed product line: {product_buffer}")
                # Start a new product buffer
                product_buffer = line
            else:
                # Append to the current product buffer
                product_buffer += " " + line
    
    # Process the last product buffer
    if product_buffer:
        parts = product_buffer.split()
        try:
            description = " ".join(parts[2:-3])
            quantity = parts[-3]
            unit_price = parts[-2]
            total = parts[-1]
            data["Products"].append({
                "description": description,
                "quantity": quantity,
                "unit_price": unit_price,
                "total": total
            })
        except IndexError:
            print(f"Skipping malformed product line: {product_buffer}")
    
    return data