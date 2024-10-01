# Delicate - Skincare and Make Up

Ini merupakan repository **Delicate**, sebuah aplikasi e-commerce yang dikembangkan untuk **Tugas Pemrograman Berbasis Platform**.

<details>
  <summary>Tugas 2</summary>

## Deskripsi Proyek
Aplikasi Delicate adalah aplikasi e-commerce yang menjual skincare dan makeup dan memungkinkan pengguna untuk melihat daftar produk dengan atribut **nama**, **harga**, dan **deskripsi**. Proyek ini dibuat dengan menggunakan framework Django dan mengimplementasikan konsep **Model-View-Template (MVT)**.

## Link Aplikasi
Aplikasi yang sudah dideploy dapat diakses melalui tautan berikut:
[Delicate - Aplikasi E-Commerce](http://safira-salma-delicates.pbp.cs.ui.ac.id/)

## Implementasi Langkah-demi-Langkah
Berikut adalah langkah-langkah yang saya lakukan untuk menyelesaikan checklist tugas ini:

1. **Membuat proyek Django baru:**  Pertama memulai dengan membuat proyek baru menggunakan perintah `django-admin startproject delicate`.
2. **Membuat aplikasi dengan nama `main`:** Lalu, membuat aplikasi bernama `main` dengan perintah `python manage.py startapp main`.
3. **Melakukan routing pada proyek:** Routing dilakukan dengan menambahkan URL aplikasi `main` ke dalam `urls.py` proyek utama, agar aplikasi dapat diakses.
4. **Membuat model `Product`:** Membuat model `Product` pada `models.py` dengan atribut wajib `name` (CharField), `price` (IntegerField), dan `description` (TextField).
5. **Membuat fungsi pada `views.py`:** Saya menambahkan fungsi yang menampilkan nama aplikasi, serta nama dan kelas saya, kemudian mengembalikannya ke template HTML.
6. **Membuat routing pada `urls.py` di aplikasi `main`:** Routing ditambahkan pada `urls.py` di aplikasi `main` untuk memetakan fungsi yang telah dibuat di `views.py`.
7. **Deployment ke PWS:** Aplikasi di deploy ke PWS agar bisa diakses secara online.

## Bagan Request-Response Django
Berikut adalah bagan alur request client ke web aplikasi berbasis Django dan responnya:

![Diagram](image/diagram.png)


- **urls.py**: Menerima request dari client dan memetakan ke fungsi yang sesuai di `views.py`.
- **views.py**: Mengambil data dari `models.py` jika diperlukan, lalu merender template HTML untuk dikirim ke client.
- **models.py**: Mengelola data yang diambil dari database menggunakan ORM Django.
- **templates**: File HTML yang dirender oleh `views.py` untuk ditampilkan kepada pengguna.

## Fungsi Git dalam Pengembangan Perangkat Lunak
Git berfungsi sebagai sistem kontrol versi yang memungkinkan pengembang melacak perubahan kode, berkolaborasi dengan tim, dan kembali ke versi kode sebelumnya jika terjadi kesalahan. Dengan Git, pengembang juga bisa bekerja secara paralel melalui branching dan merging.

## Mengapa Django Digunakan dalam Pembelajaran?
Django dipilih sebagai framework untuk pembelajaran karena memiliki struktur yang jelas (Model-View-Template) dan dilengkapi dengan banyak fitur bawaan yang mempermudah pengembangan aplikasi. Django juga memiliki dokumentasi yang baik dan komunitas yang besar, sehingga cocok untuk pemula.

## Mengapa Model di Django Disebut ORM?
Model di Django disebut sebagai **Object-Relational Mapping (ORM)** karena memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python. Dengan ORM, kita tidak perlu menulis query SQL secara langsung, melainkan menggunakan metode yang lebih sederhana dan aman dalam bentuk query berbasis objek.

</details>


<details>
  <summary>Tugas 3</summary>

### 1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
   Data delivery penting karena memungkinkan pertukaran informasi antara klien dan server. Ini membantu platform menjadi dinamis dengan menyediakan informasi real-time, mengelola permintaan pengguna, dan memberikan respons yang diperlukan. Tanpa data delivery, platform tidak bisa mengelola interaksi antara pengguna dan server secara efisien, dan tidak dapat berfungsi secara penuh.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
   JSON dianggap lebih baik daripada XML dalam banyak kasus karena lebih sederhana dan mudah dibaca. JSON lebih ringkas, sehingga menghemat bandwidth dan lebih cepat di-parse oleh browser. JSON juga lebih populer karena lebih mudah digunakan bersama dengan JavaScript, yang banyak digunakan dalam pengembangan aplikasi web modern. XML, meskipun fleksibel, cenderung lebih verbose dan kompleks dibandingkan JSON.

### 3. Fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
   Method `is_valid()` pada Django digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form memenuhi kriteria validasi yang telah didefinisikan. Kita memerlukan method ini untuk memastikan bahwa input dari pengguna sesuai dengan tipe data yang diharapkan dan bebas dari kesalahan sebelum data tersebut diproses lebih lanjut atau disimpan ke dalam database.

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
   `csrf_token` (Cross-Site Request Forgery token) diperlukan untuk melindungi aplikasi dari serangan CSRF, di mana penyerang dapat membuat pengguna yang terautentikasi melakukan tindakan yang tidak diinginkan di aplikasi tanpa sepengetahuan mereka. Jika kita tidak menambahkan `csrf_token` pada form, penyerang bisa memanfaatkan kelemahan ini untuk mengirimkan permintaan berbahaya atas nama pengguna. CSRF token memastikan bahwa setiap permintaan yang diajukan ke server berasal dari pengguna yang sah dan formulir yang benar.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   - Pertama, buat `forms.py` untuk membuat form berdasarkan model `Product`.
   - Tambahkan fungsi di `views.py` untuk menangani form dan menampilkan data. Dalam file, kita import forms, HTTPResponse, redirect dan serializers.
   -Buat fungsi `create_item_entry` untuk menambahkan item dengan POST.
   - Buat file HTML baru untuk form, tambahkan `{% csrf_token %}` dan tombol submit.
   - Buat 4 fungsi di `views.py` untuk menampilkan data dalam format **JSON** dan **XML**.
   - Tambahkan routing di `urls.py` untuk mengakses form, serta melihat data dalam format **JSON** dan **XML**.

##Screenshot Postman
![Postman JSON](imagetugas3/Screenshot%20(829).png)
![Postman JSON ID](imagetugas3/Screenshot%20(830).png)
![Postman XML](imagetugas3/Screenshot%20(831).png)
![Postman XML ID](imagetugas3/Screenshot%20(832).png)

 </details>


<details>
  <summary>Tugas 4</summary>

### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
- HttpResponseRedirect() adalah class bawaan Django yang mengirimkan respons HTTP dengan kode status 302 untuk melakukan redirect. Kode ini membutuhkan URL lengkap yang harus diberikan sebagai argumen.

- redirect() adalah shortcut function yang mempermudah proses redirect dengan cara yang lebih fleksibel. Django akan secara otomatis menentukan URL tujuan, baik dari nama URL (seperti yang didefinisikan di urlpatterns), objek, atau model. Ini membuat kode lebih mudah dibaca dan di-maintain.

### 2. Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan antara model Item dan User dilakukan melalui relasi ForeignKey. Setiap Item terhubung dengan satu User, yang berarti satu pengguna bisa memiliki banyak Item (one-to-many). Relasi ini didefinisikan dengan menggunakan atribut ForeignKey di model Item, di mana User menjadi referensi. Jika pengguna dihapus, maka semua Item yang dimilikinya akan ikut dihapus karena pengaturan on_delete=models.CASCADE.

### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah proses untuk memverifikasi identitas pengguna, yaitu memastikan bahwa pengguna yang login adalah benar-benar pengguna yang sah. Di Django, ini dilakukan dengan memvalidasi username dan password pengguna.

Authorization adalah proses untuk menentukan hak akses pengguna terhadap sumber daya tertentu, seperti akses ke halaman atau fitur tertentu di aplikasi. Setelah pengguna login, Django menggunakan authorization untuk memutuskan apakah pengguna tersebut berhak mengakses bagian tertentu.

Saat pengguna login:
1. Django memverifikasi identitas pengguna dengan mencocokkan username dan password.
2. Jika cocok, Django mencatat pengguna sebagai authenticated dan menyimpan informasi ini dalam session.
3. Authorization digunakan untuk menentukan akses apa saja yang dapat dilakukan oleh pengguna yang sudah login.

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan session, yang diidentifikasi oleh session ID yang disimpan di dalam cookie pada browser pengguna. Setiap kali pengguna mengunjungi aplikasi, browser mengirimkan cookie dengan session ID ini ke server, dan server bisa mengenali pengguna berdasarkan session tersebut.

Kegunaan lain dari cookies termasuk:
- Menyimpan preferensi pengguna, seperti bahasa yang dipilih atau item yang terakhir dilihat.
- Melacak aktivitas pengguna di situs web (misalnya, untuk analitik).

Namun, tidak semua cookies aman. Cookies bisa disalahgunakan oleh serangan seperti cross-site scripting (XSS). Django menyediakan pengaturan keamanan seperti HttpOnly untuk mencegah JavaScript mengakses cookie, dan Secure agar cookie hanya dikirimkan melalui koneksi HTTPS.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat Fungsi Registrasi, Login, dan Logout:
Saya menggunakan UserCreationForm untuk registrasi, dan AuthenticationForm untuk login. Setelah pengguna berhasil login, session dibuat untuk pengguna tersebut. Fungsi logout menghapus session dan cookies terkait.

2. Membuat Dummy Data untuk Setiap Pengguna:
Saya membuat dua akun pengguna dan tiga item skincare dummy untuk masing-masing pengguna menggunakan model Item, yang dihubungkan ke pengguna melalui relasi ForeignKey.

##Screenshot User Page
![USER 1](imagetugas4/user1.png)
![USER 2](imagetugas4/user2.png)

3. Menghubungkan Model Item dengan User:
Di model Item, saya menambahkan atribut user dengan tipe ForeignKey yang merujuk ke model User, memastikan setiap item terkait dengan pengguna yang memilikinya.

4. Menampilkan Username dan Menggunakan Cookie:
Saya menampilkan username pengguna yang login di halaman utama menggunakan request.user.username dan mencatat waktu login terakhir menggunakan cookie bernama last_login. Cookie ini dihapus saat pengguna logout.

5. Menyimpan dan Memastikan Push ke GitHub:
Setelah semuanya berfungsi dengan baik, saya memastikan semua perubahan di-commit dan di-push ke GitHub sesuai dengan checklist.

</details>


<details>
  <summary>Tugas 5</summary>

### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas CSS selector diatur berdasarkan **specificity** sebagai berikut:

- **Inline styles** (misalnya: `style="color: red;"`) memiliki spesifisitas tertinggi.
- **ID selectors** (misalnya: `#header`) memiliki spesifisitas lebih tinggi daripada class atau elemen.
- **Class, attribute, atau pseudo-class selectors** (misalnya: `.container`, `[type="text"]`, `:hover`) memiliki spesifisitas lebih rendah dari ID.
- **Element selectors** (misalnya: `div`, `p`) memiliki spesifisitas paling rendah.

Jika ada beberapa aturan CSS yang memiliki spesifisitas yang sama, aturan yang ditulis terakhir akan diterapkan.

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web?
Responsive design sangat penting karena pengguna mengakses aplikasi web dari berbagai perangkat dengan ukuran layar berbeda, mulai dari desktop hingga smartphone. Dengan responsive design, tampilan web dapat menyesuaikan ukuran layarnya, sehingga pengguna mendapatkan pengalaman yang optimal di semua perangkat.

**Contoh aplikasi yang menerapkan responsive design**: Facebook, Twitter.
**Contoh aplikasi yang belum menerapkan responsive design**: Beberapa situs web lama yang masih menggunakan layout fixed-width.

### 3. Jelaskan perbedaan antara margin, border, dan padding!
- **Margin**: Ruang di luar border yang memisahkan elemen dengan elemen lain.
- **Border**: Garis yang mengelilingi konten elemen dan padding.
- **Padding**: Ruang di dalam border yang memisahkan konten elemen dari border.

### 4. Jelaskan Konsep Flexbox dan Grid Layout serta Kegunaannya
- Flexbox: Flexbox adalah layout satu dimensi yang digunakan untuk menyusun elemen secara fleksibel dalam baris atau kolom. Flexbox sangat berguna untuk layout responsif yang dinamis, karena memudahkan pengaturan item dalam container dengan penyesuaian yang mudah, misalnya dengan menyusun item secara horizontal (baris) atau vertikal (kolom).

Kegunaannya: Flexbox digunakan untuk membuat layout yang mudah menyesuaikan ukuran elemen dan container-nya, misalnya dalam menata card produk atau elemen navigasi.

- Grid Layout: Grid layout adalah sistem layout dua dimensi yang memungkinkan pengaturan elemen dalam bentuk baris dan kolom. Ini sangat berguna untuk membuat layout yang lebih kompleks, seperti dashboard atau galeri gambar, karena kita bisa menentukan lebar kolom dan tinggi baris dengan mudah.

Kegunaannya: Grid layout sangat cocok untuk tata letak yang presisi dan detail, seperti pembuatan layout multi-kolom dengan konten yang beragam.

### 5. Implementasi Checklist secara Step-by-Step
1. Saya menambahkan tailwind ke aplikasi.
2. Menambahkan fitur "Edit" untuk edit item yang sudah di-add.
3. Menambahkan fitur "Delete" untuk menghapus item yang sudah di-add.
4. Menambahkan navbar dengan design awal yang hanya berisi button logout dan welcome user.
5. Konfigurasi static files 
6. Membuat sketch tampilan aplikasi rancangan saya melalui aplikasi canva.
6. Menambahkan styles pada app dengan tailwind dan css. Pada tahap ini saya styling halaman login, regoster, home, create item entry, dan edit mood.
7. Lalu, saya design navbar dengan beberapa button pilihan yaitu:
-home : mengarah ke main.html
-sale : mengarah ke sale.html
-shop by categories : berisi dropdown skincare yang mengarah ke skincare.html dan makeup yang mengarah ke makeup.html
8. Terakhir saya push ke github dan pws.

</details>

## Author
Nama: Safira Salma Humaira -
NPM: 2306245850 -
Kelas: PBP F

