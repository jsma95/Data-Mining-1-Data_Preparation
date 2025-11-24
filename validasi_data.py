import pandas as pd

# Baca data hasil integrasi
df_integrasi = pd.read_csv("integrasi_data.csv")

# Validasi
# Hapus duplikat
df_validasi = df_integrasi.drop_duplicates()

# Hapus data dengan Price <= 0 atau Stock < 0
df_validasi = df_validasi[(df_validasi['Price'] > 0) & (df_validasi['Stock'] >= 0)]

# Simpan hasil validasi
df_validasi.to_csv("data_validation.csv", index=False)

print("=== Data setelah validasi disimpan di data_validation.csv ===")


