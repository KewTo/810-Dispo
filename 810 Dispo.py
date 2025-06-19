import pandas as pd
import re
import numpy as np


def file():
    filepath = r'C:\Users\kevinto\OneDrive - Intel Corporation\Desktop\Python Dispatch.xlsx'
    return filepath


df = pd.read_excel(file())


def condition(row):
    out = []
    if row.BLEMISH == 'Y':
        out.append("HOLD")
    elif re.match(r'BEUVF(\d*)', row.LOT):
        out.append('HOLD')
    elif row.BLEMISH == 'N':
        if re.match(r'.*PCAR', row.RESIST):
            if row.CLN_CNT > 2:
                out.append("DOWNGRADE")
            elif row.CLN_CNT < 2:
                out.append("CLE")
        elif re.match(r'.*P37', row.RESIST):
            if row.DAYS_AT_OPERATION > 15:
                out.append("TRASH")
            elif row.DAYS_AT_OPERATION < 15:
                out.append("DOWNGRADE")
        elif re.match(r'.*N19', row.RESIST):
            if row.CLN_CNT > 2:
                out.append("DOWNGRADE")
            elif row.CLN_CNT < 2:
                out.append("CLE")
        elif re.match(r'.*P53', row.RESIST):
            if row.DAYS_AT_OPERATION > 15:
                out.append("TRASH")
            elif row.DAYS_AT_OPERATION < 15:
                out.append("DOWNGRADE")
    out = (", ".join(out))
    return out


df = df.replace(np.nan, '', regex=True)
pd.set_option('display.show_dimensions', False)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df['Dispo'] = df.apply(condition, axis=1)
print(df)


def excel():
    from openpyxl import load_workbook
    wb = load_workbook(file())
    ws = wb.active
    ws.delete_cols(1)
    wb.save(file())


if __name__ == '__main__':
    main()
