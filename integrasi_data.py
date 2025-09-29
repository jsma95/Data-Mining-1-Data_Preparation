import pandas as pd

# ===============================
# INTEGRASI DATA
# ===============================

# Membaca data utama
df = pd.read_csv("produk e-commerce.csv")

# Contoh data tambahan
data_tambahan = {
    "produk_id": [101, 102],
    "nama_produk": ["Smartwatch X", "Headset Gaming"],
    "kategori": ["Elektronik", "Aksesoris"],
    "harga": [550000, 350000],
    "stok": [50, 80]
}

df_tambahan = pd.DataFrame(data_tambahan)

# Integrasi data
df_integrasi = pd.concat([df, df_tambahan], ignore_index=True)

# Simpan hasil integrasi agar bisa dipakai file lain
df_integrasi.to_csv("data_integrasi.csv", index=False)

print("=== Hasil Integrasi Data (5 teratas) ===")
print(df_integrasi.head())
