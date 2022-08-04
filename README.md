# Rest-Api-dengan-Flask-2
- Folder
    - venv/env
    Lingkungan tempat aplikasi berjalan. Flask dan ekstensi dapat mengaktifkan perilaku berdasarkan lingkungan, seperti mengaktifkan mode debug. Atribut envmemetakan ke kunci konfigurasi ini. Ini diatur olehFLASK_ENVvariabel lingkungan dan mungkin tidak berperilaku seperti yang diharapkan jika diatur dalam kode.
    - src
    utk menampung semua kode aplikasi
    - config
    akan menampung semua kekosongan, meningkatkan konfigurasi
    - constants
    utk variabel yg tdk kita inginkan contoh http
    - static
    utk tempat css,js
    - services
    Direktori Services berisi berbagai layanan "helper" yang dibutuhkan aplikasi Anda untuk berfungsi. Misalnya, layanan Registrar untuk memvalidasi dan membuat pengguna baru aplikasi Anda.
    - tests
    utk kumpulan code pengetesan


- Penjelasan configurasi pd flask di __init__.py
    - instance_relative_config 
    utk didefinisikan dalam beberapa file di luar sini src. Karena objek config menyediakan pemuatan file konfigurasi dari nama file relatif, kami memungkinkan untuk mengubah pemuatan melalui nama file menjadi relatif terhadap jalur instance jika diinginkan. Perilaku jalur relatif dalam file konfigurasi dapat dibalik antara "relatif ke root aplikasi" (default) ke "relatif ke folder instance" melalui sakelar instance_relative_config ke konstruktor aplikasi.