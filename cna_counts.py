import pandas as pd
import numpy as np
import os

# IO
os.chdir('/Users/JMin/COTA')
counts = pd.ExcelFile('cna_counts.xlsx')
total = counts.parse('Total')
lymphoma = counts.parse('Lymphoma')
leukemia = counts.parse('Leukemia')
head_neck = counts.parse('Head Neck')
gyno = counts.parse('Gynecologic')
genitourinary = counts.parse('Genitourinary')
thoracic = counts.parse('Thoracic')
breast = counts.parse('Breast')
gi = counts.parse('Gastrointestinal')
blood = counts.parse('Blood')
endocrine = counts.parse('Endocrine')
unknown_primary = counts.parse('Unknown Primary')
neuro = counts.parse('Neurooncology')
myeloma = counts.parse('Myeloma')
sarcoma = counts.parse('Sarcoma')

# Start plotting


'''
myeloma_count = {}
myeloma_xl = pd.ExcelFile('Multiple Myeloma Outline 040814.xls')
for sheet_name in myeloma_xl.sheet_names:
    df = myeloma_xl.parse(sheet_name, skiprows=1)
    myeloma_count[sheet_name] = df.shape[0]

sarcoma_count = {}
sarcoma_xl = pd.ExcelFile('Final Skin Sarcoma COTA Nodal Addresses.xls')
for sheet_name in sarcoma_xl.sheet_names:
    df = sarcoma_xl.parse(sheet_name, skiprows=1)
    sarcoma_count[sheet_name] = df.shape[0]

neuro_count = {}
neuro_xl1 = pd.ExcelFile('Neuro Oncology Outline 040814.xls')
for sheet_name in neuro_xl1.sheet_names:
    df = neuro_xl1.parse(sheet_name, skiprows=1)
    neuro_count[sheet_name] = df.shape[0]
'''
