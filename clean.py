import pandas as pd
data = pd.read_csv(r"C:\Users\arsha\Downloads\drive-download-20240410T120549Z-001\IPL_Ball_by_Ball_2008_2022.csv")
df = pd.DataFrame(data, index = None)
result = df.sort_values(by = ['id','inning','over','ball'])
result.to_csv(r"C:\Users\arsha\Downloads\cleaned.csv", index = False)
print(result)