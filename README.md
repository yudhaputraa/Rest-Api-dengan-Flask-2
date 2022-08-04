# Rest-Api-dengan-Flask-2
- Folder/File
    - Folder venv/env
    Lingkungan tempat aplikasi berjalan. Flask dan ekstensi dapat mengaktifkan perilaku berdasarkan lingkungan, seperti mengaktifkan mode debug. Atribut envmemetakan ke kunci konfigurasi ini. Ini diatur olehFLASK_ENVvariabel lingkungan dan mungkin tidak berperilaku seperti yang diharapkan jika diatur dalam kode.
    - Folder src
    utk menampung semua kode aplikasi
    - Folder config
    akan menampung semua kekosongan, meningkatkan konfigurasi
    - Folder constants
    utk variabel yg tdk kita inginkan contoh http
    - Folder static
    utk tempat css,js
    - Folder services
    Direktori Services berisi berbagai layanan "helper" yang dibutuhkan aplikasi Anda untuk berfungsi. Misalnya, layanan Registrar untuk memvalidasi dan membuat pengguna baru aplikasi Anda.
    - Folder tests
    utk kumpulan code pengetesan
    - File .flaskenv dan .env 
    Dengan diperkenalkannya antarmuka baris perintah Flask, salah satu hal yang lebih mengganggu yang harus Anda lakukan selama pengembangan adalah mengatur variabel lingkungan setiap kali Anda mengerjakan aplikasi Anda, yaitu FLASK_ENV dan FLASK_APP. Nah, Flask punya cara agar kamu bisa menangani hal-hal tersebut dengan cara yang hanya perlu kamu lakukan sekali. Dan melalui fungsi yang sama, Anda juga dapat menambahkan variabel lingkungan lain untuk proyek Anda. Dalam artikel ini, saya akan menunjukkan cara menggunakan python-dotenv agar variabel lingkungan Anda dimuat dan siap digunakan setiap kali Anda menjalankan aplikasi.


- Penjelasan configurasi pd flask di init.py
    - instance_relative_config 
    utk didefinisikan dalam beberapa file di luar sini src. Karena objek config menyediakan pemuatan file konfigurasi dari nama file relatif, kami memungkinkan untuk mengubah pemuatan melalui nama file menjadi relatif terhadap jalur instance jika diinginkan. Perilaku jalur relatif dalam file konfigurasi dapat dibalik antara "relatif ke root aplikasi" (default) ke "relatif ke folder instance" melalui sakelar instance_relative_config ke konstruktor aplikasi.
    - SECRET_KEY 
    digunakan oleh Flask dan ekstensi untuk menjaga keamanan data. Ini diatur untuk 'dev'memberikan nilai yang nyaman selama pengembangan, tetapi harus diganti dengan nilai acak saat digunakan.