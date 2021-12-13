Nama : Lucky Pradana
       , Kevin Octaviano
       , Muhammad Arif

Host  : Universitas Gadjah Mada (UGM-04), Kelompok 2

#Penjelasan

Web app ini dibuat berdasarkan dari model yang telah di training menggunakan dataset yang didapatkan dari tugas kuliah monitoring parameter suhu dan kualitas udara di daerah Tanjung Uban, Kepulauan Riau. Dengan menggunakan model LSTM (Long Short Term Memory) kita dapat memprediksi suhu pada keesokan harinya
di daerah tersebut. Web app ini menggunakan 'streamlit' ( https://streamlit.io/ ) sebagai fondasi dasar mulai dari front-end web hingga hosting web app.

#Penggunaan Aplikasi

https://share.streamlit.io/luckyprdn/lstm-temp-predict/main/app.py -- Link Model yang telah di deploy

Dengan mengklik link tersebut, maka pengguna akan diarahkan ke web app.
Langkah selanjutnya pengguna cukup mengetikkan parameter suhu di isian, kemudian tekan tombol "predict". Maka kemudian web app akan menampilkan prediksi suhu berdasarkan model yang sudah di training sebelumnya.

#Penjelasan File
1. Procfile         -- File yang akan dijalankan pertama kali pada web app
2. app.py           -- File yang berisikan kode program library 'streamlit'
3. cleaned_iot.csv  -- Dataset yang sudah di cleaning dan preprocessing
4. model.pkl        -- Model yang telah diserialisasikan menggunakan 'pickle'
5. Requirements.txt -- Library yang diperlukan web app
6. setup.sh         -- Dibutuhkan untuk menjalankan web app
7. streamlit.ipynb  -- Notebook yang berisikan kode debugging pembuatan web app menggunakan 'streamlit'
8. training.ipynb   -- Notebook yang berisikan kode pembuatan dan pelatihan model hingga siap digunakan
9. unclean_iot.csv  -- Dataset yang belum di cleaning dan preprocessing
