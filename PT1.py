import tkinter as tk    # Mengimpor modul tkinter untuk membuat GUI (Graphical User Interface).

def prediksi_prodi():    # Mendefinisikan fungsi prediksi_prodi yang akan dipanggil ketika tombol ditekan.
    hasil_label.config(text="Prodi: Teknologi Informasi")    # Mengubah teks dari label hasil_label menjadi "Prodi: Teknologi Informasi".


root = tk.Tk()    # Membuat jendela utama aplikasi dengan tkinter.
root.title("Aplikasi Prediksi Prodi Pilihan") #mengatur judul jendela aplikasi.


judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"), fg="black", bg="pink") #Mengatur jenis huruf, ukuran (16), dan ketebalan huruf (bold).
judul_label.grid(row=0, column=0, columnspan=2, pady=10)    # Menempatkan label di grid pada baris 0, kolom 0, membentang dua kolom (columnspan=2), dan memberikan jarak vertikal 10 piksel di atas dan bawah.


input_labels = []
input_entries = []
for i in range(10):      #membuat 10 pasang label dan entry (kotak input)
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i + 1}")        #Membuat label untuk setiap mata pelajaran
    label.grid(row=i+1, column=0, padx=5, pady=5, sticky="e")   # Menempatkan label pada grid.
    entry = tk.Entry(root)        # Membuat kotak input di mana pengguna dapat memasukkan nilai.
    entry.grid(row=i+1, column=1, padx=5, pady=5) # Menempatkan kotak input pada grid.
    input_labels.append(label) #Append Menyimpan referensi label dan entry ke dalam list 
    input_entries.append(entry) # Menyimpan referensi entry ke dalam list input_entries.


prediksi_button = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi)    # Membuat tombol prediksi.
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)   # Menempatkan tombol di grid.


hasil_label = tk.Label(root, text="Prodi: ", font=("Arial", 16, "bold"), fg="black", bg="pink") # Membuat label hasil prediksi.
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)   # Menempatkan label di grid.


root.mainloop() # Menjalankan loop utama aplikasi untuk menjaga jendela tetap terbuka.