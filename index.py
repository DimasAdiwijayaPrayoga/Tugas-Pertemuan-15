#XOR untuk enkripsi
def encrypt(teks, kunci):
  ciphertext = ""
  for i in range(len(teks)):
    ciphertext += chr(ord(teks[i]) ^ ord(kunci[i % len(kunci)]))
  return ciphertext

# Trial enkripsi dan deskripsi
teks = "Saya harus lulus tepat waktu dan menjadi sarjana"
kunci = "12345"

print("__Tugas Enkripsi__")
print("Plaintext : ", teks)
ciphertext = encrypt(teks, kunci)
print("Encryption :", ciphertext)