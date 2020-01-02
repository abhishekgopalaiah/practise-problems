"""
This is a sample code snippet
removes non ascii char from the csv file
Chardet: The Universal Character Encoding Detector
"""
import chardet
import pandas as pd
import numpy as np


def csv_encoder(input_file):
    with open(input_file, 'rb') as f:
        result = chardet.detect(f.read())

    df = pd.read_csv(input_file, encoding=result['encoding'])
    # remove unicode chars for entire df
    for col in df.columns:
        series = df[col]
        df[col] = [s.encode('ascii', 'ignore').strip()
                   for s in series.str.decode('unicode_escape')]

    # vectorised str.decode to decode byte strings into ordinary strings:
    str_df = df.select_dtypes([np.object])

    str_df = str_df.stack().str.decode('utf-8').unstack()

    encoded_file = 'utf-8_file.csv'
    str_df.to_csv(encoded_file, encoding='utf-8', index=False)
