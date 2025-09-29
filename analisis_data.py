import pandas as pd

# Baca data hasil integrasi
df_integrasi = pd.read_csv("data_integrasi.csv")

# Analisis
produk_per_kategori = df_integrasi['kategori'].value_counts()
rata_harga = df_integrasi.groupby('kategori')['harga'].mean()
total_stok = df_integrasi.groupby('kategori')['stok'].sum()

# Simpan hasil analisis ke file
df_analysis = pd.DataFrame({
    "Jumlah Produk": produk_per_kategori,
    "Rata-rata Harga": rata_harga,
    "Total Stok": total_stok
})

df_analysis.to_csv("data_analysis.csv")

print("=== Hasil analisis disimpan di data_analysis.csv ===")
