import json
import pandas as pd

# JSON dosyasını okuma
with open('veriler.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Tüm anahtarları al
keys = list(data.keys())

# Anahtarları DataFrame'e aktar
df = pd.DataFrame({'Keys': keys})

# Excel dosyasına yazma
df.to_excel('keys.xlsx', index=False)
