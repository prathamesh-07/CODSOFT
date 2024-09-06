import re

def extract_header_info(raw_input):
    patterns = {
        "Message ID": r"Message ID\s*[:\t ]+\s*(<[^>]+>)",
        "Created on": r"Created on\s*[:\t ]+\s*(.+?)(?=(From|To|Subject|SPF|DKIM|DMARC|$))",
        "From": r"From\s*[:\t ]+\s*(.+?)(?=(To|Subject|SPF|DKIM|DMARC|$))",
        "To": r"To\s*[:\t ]+\s*(.+?)(?=(Subject|SPF|DKIM|DMARC|$))",
        "Subject": r"Subject\s*[:\t ]+\s*(.+?)(?=(SPF|DKIM|DMARC|$))",
        "SPF": r"SPF\s*[:\t ]+\s*(.+?)(?=(DKIM|DMARC|$))",
        "DKIM": r"DKIM\s*[:\t ]+\s*(.+?)(?=(DMARC|$))",
        "DMARC": r"DMARC\s*[:\t ]+\s*(.+)",
    }
    
    header_info = {}
    
    for key, pattern in patterns.items():
        match = re.search(pattern, raw_input, re.DOTALL)
        if match:
            header_info[key] = match.group(1).strip()
        else:
            header_info[key] = "Not Found"
    
    return header_info

def analyze_email_header():
    raw_input = input("Enter the full email header details:\n")
    header_info = extract_header_info(raw_input)
    spf_pass = 'PASS' in header_info['SPF'].upper()
    dkim_pass = 'PASS' in header_info['DKIM'].upper()
    dmarc_pass = 'PASS' in header_info['DMARC'].upper()
    is_authentic = spf_pass and dkim_pass and dmarc_pass
    
    print("\nEmail Details:")
    for key, value in header_info.items():
        print(f"{key}: {value}")
    
    if is_authentic:
        print("\nThe email is authentic based on SPF, DKIM, and DMARC checks.")
    else:
        print("\nThe email is NOT authentic based on SPF, DKIM, and DMARC checks.")

analyze_email_header()
