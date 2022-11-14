import pandas as pd
import re


def file():
    filepath = r'D:\Download\out_22047.csv'
    return filepath


df = pd.read_csv(file())


def condition(row):
    out = []
    if row.BLEMISH == 'Y':
        out.append("HOLD")
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
    return out


df['Dispo_Option'] = df.apply(condition, axis=1)
df.to_csv(file(), sep='\t', encoding='utf-8')

if __name__ == '__main__':
    pass
