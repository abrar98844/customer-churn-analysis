import pandas as pd
IBM_file=pd.read_csv(r"C:\Users\Arabmac Os\OneDrive\Desktop\anlays\I_file")
IBM_file["SeniorCitizen"].dtype
IBM_file["MonthlyCharges"].dtype
#print(IBM_file["TotalCharges"].dtype)
IBM_file["TotalCharges"]=pd.to_numeric(IBM_file["TotalCharges"], errors="coerce")
IBM_file.isna().sum()
IBM_file["TotalCharges"]=IBM_file["TotalCharges"].fillna(value=0)
IBM_file.isnull().all(axis=1).sum()
IBM_file.duplicated().sum()
IBM_file.apply(lambda col: col.astype(str).str.contains(r"^\s|\s$", regex=True).any())
IBM_file.apply(lambda col: col.astype(str).str.fullmatch(r"\s*").sum())
varr=IBM_file.to_csv("IBM_csv")
print(varr)
