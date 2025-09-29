import pandas as pd

# Baca data hasil integrasi
df_integrasi = pd.read_csv("data_integrasi.csv")

# Validasi
# Hapus duplikat
df_validasi = df_integrasi.drop_duplicates()

# Hapus data dengan harga <= 0 atau stok < 0
df_validasi = df_validasi[(df_validasi['harga'] > 0) & (df_validasi['stok'] >= 0)]

# Simpan hasil validasi
df_validasi.to_csv("data_validation.csv", index=False)

print("=== Data setelah validasi disimpan di data_validation.csv ===")
