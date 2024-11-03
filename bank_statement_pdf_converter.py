from PyPDF2 import PdfReader
import pandas as pd
import numpy as np

#Current Month(s)
l = '09/'
t = '10/'

#PDF File
pdf = "BANK-STATEMENT.PDF"

#Read file
reader = PdfReader(pdf)
totalPages = len(reader.pages)

#Get the text
segments = 0
transaction = ''
all_transactions = []

#Get the transactions

for p in range(0, totalPages):
    page = reader.pages[p]
    text = page.extract_text().split("\n")
    segments = len(text)
    for i in range(0, segments):
        if 'Beginning Balance' in text[i]:
            continue
        elif 'Ending Balance' in text[i]:
            continue
        elif 'For additional information' in text[i]:
            continue
        elif 'Statement Period' in text[i]:
            continue
        elif l in text[i]:
            transaction = text[i]
            all_transactions.append(transaction)
        elif t in text[i]:
            transaction = text[i]
            all_transactions.append(transaction)
        else:
            continue

df = pd.DataFrame(all_transactions)
df.to_csv('bankstatement.csv', index=False)
