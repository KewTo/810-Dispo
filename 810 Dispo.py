import pandas as pd
import re


# Grab location of file
def file():
    filepath = r'C:\Users\kevinto\OneDrive - Intel Corporation\Desktop\out_22047.csv'
    return filepath


# Read Excel file
df = pd.read_csv(file())


# Disposition option for various resist types and their conditions
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


# Apply the conditions and add the option to the Excel files as a new column
df['Dispo'] = df.apply(condition, axis=1)
print(df)
df.to_csv(file(), encoding='utf-8')


# Save the Excel file with new disposition option
def main():
    from openpyxl import load_workbook
    wb = load_workbook(file())
    ws = wb.active
    ws.delete_cols(1)
    wb.save(file())


if __name__ == '__main__':
    main()
