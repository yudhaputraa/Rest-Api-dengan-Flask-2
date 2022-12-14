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
    - Cara membuat Bookmark.db 
    buka terminal, masuk env, lalu ketik flask shell, ketik from src.database import db, db.create_all(). jika ingin hapus db.drop_all()


- Penjelasan configurasi pd flask di init.py
    - instance_relative_config 
    utk didefinisikan dalam beberapa file di luar sini src. Karena objek config menyediakan pemuatan file konfigurasi dari nama file relatif, kami memungkinkan untuk mengubah pemuatan melalui nama file menjadi relatif terhadap jalur instance jika diinginkan. Perilaku jalur relatif dalam file konfigurasi dapat dibalik antara "relatif ke root aplikasi" (default) ke "relatif ke folder instance" melalui sakelar instance_relative_config ke konstruktor aplikasi.
    - SECRET_KEY 
    digunakan oleh Flask dan ekstensi untuk menjaga keamanan data. Ini diatur untuk 'dev'memberikan nilai yang nyaman selama pengembangan, tetapi harus diganti dengan nilai acak saat digunakan.
    - register_blueprint() 
    Untuk menggunakan Flask Blueprint, Anda harus mengimpornya dan mendaftarkannya ke dalam aplikasi menggunakan register_blueprint() . Saat Flask Blueprint didaftarkan, aplikasi diperpanjang dengan isinya. Saat aplikasi sedang berjalan, buka http://localhost:5000 menggunakan browser web Anda. Cetak biru Flask membantu Anda membuat instance aplikasi yang dapat digunakan kembali. Ia melakukannya dengan mengatur proyek Anda dalam modul. Modul-modul tersebut kemudian didaftarkan sebagai aplikasi utama. Mereka membantu dalam membuat pabrik aplikasi.
    - SQLALCHEMY_TRACK_MODIFICATIONS 
    Jika disetel ke True (default) Flask-SQLAlchemy akan melacak modifikasi objek dan memancarkan sinyal. Ini membutuhkan memori ekstra dan dapat dinonaktifkan jika tidak diperlukan.


- Penjelasan yang Terinstall di pip
    - Fungsi Blueprint 
    secara fungsi sih sama-sama bisa menambah routing aplikasi. Fungsi Blueprint ini lebih terasa jika digunakan dalam projek skala menengah ke besar. Yaitu bisa pisah-pisahin file routing, lalu di-import di app.py.
    - Fungsi request 
    Untuk mengakses data yang masuk di Flask, Anda harus menggunakan objek request. Objek permintaan menampung semua data yang masuk dari permintaan, antara lain termasuk mimetype, pengarah, alamat IP, data mentah, metode HTTP, dan header.
    - Fungsi jsonify 
    jsonify adalah fungsi dalam Flask. modul json. jsonify membuat serial data ke format JavaScript Object Notation (JSON), membungkusnya dalam objek Response dengan aplikasi/json mimetype. Perhatikan bahwa jsonify terkadang diimpor langsung dari modul flask alih-alih dari flask.
    - validators 
    Dalam konteks ini, memvalidasi data berarti memverifikasi input dan memeriksa apakah memenuhi harapan atau kriteria tertentu. Validasi data dapat dilakukan di bagian depan dan belakang.
    - Flask-JWT-Extended 
    Flask-JWT-Extended tidak hanya menambahkan dukungan untuk menggunakan JSON Web Tokens (JWT) ke Flask untuk melindungi rute, tetapi juga banyak fitur bermanfaat (dan opsional) yang dibangun untuk membuat bekerja dengan JSON Web Tokens lebih mudah. Ini termasuk: Menambahkan klaim khusus ke Token Web JSON. Pemuatan pengguna otomatis ( current_user ).