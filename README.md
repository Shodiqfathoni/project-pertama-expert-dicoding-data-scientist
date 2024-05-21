# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

### Permasalahan Bisnis

tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%. sehingga dibutuhkan alat untuk memprediksi apakah karyawa tersebut akan keluar atau tetap bertahan, sehingga karyawan yang terindikasi ingin keluar bisa segera ditangani dan dicari solusinya

### Cakupan Proyek

1. menyiapkan data dari "postgresql://postgres.zyjmkzlykunzxtxdxzio:cHBjk9uP9A3kC9lq@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres"

2. menganalisis data 

3. membuat dashboard untuk departemen HR https://lookerstudio.google.com/reporting/8bbe9f0e-ed27-47dc-8590-204d9a075f10

4. membuat model machine learning

5. membuat kesimpulan dan saran

### Persiapan

Sumber data: "postgresql://postgres.zyjmkzlykunzxtxdxzio:cHBjk9uP9A3kC9lq@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres"

Setup environment:

mkdir proyek_pertama_expert
cd proyek_pertama_expert
pipenv install
pipenv shell
pip install -r requirements.txt

## cara penggunaan model machine learning :
ada dua cara untuk menjalankan machine learning yaitu local maupun cloud

1.menjalankan machine learning secara lokal dimulai dengan cara memilih berkas Attrition_app.py, kemudian run code tersebut nanti di terminal akan mucul Warning: to view this Streamlit app on a browser, run it with the following command,setelah itu ikuti command yang ditunjukkan oleh warning tersebut dan run command tersebut di terminal,kemudian akan muncul tulisan local url dan juga network url,kemudian pilih local url,kemudian anda akan muncul sebuah app prediksi

2.menjalankan machine learning lewat cloud anda harus mempunyai akun streamlit cloud dan github kemudian deploy lewat creat app isi apa saja yang diminta oleh creat app kemudian pencet deploy dan tunggu hingga proses selesai,nanti akan muncul di bagian your app untuk menjalankannya tinggal klik app yang baru dibuat tadi atau bisa langsung mengakses link ini: https://projectpertamaexpert-nk66q6dzqnjrmrgjseftfc.streamlit.app/

3.cara menggunakan prototype app tersebut cukup mudah,anda hanya perlu memilih parameter yang anda inginkan sudah tersedia dimasing masing kolom tersebut,jika sudah memilih parameter tersebut kemudian pada bagian bawah ada view the raw data,ini adalah tampilan parameter anda yang sudah dipilih dari kolom yang diatas, silahkan periksa apakah data yang tercantum di view raw data tersebut sesuai dengan pilihan anda,kemudian tekan predict dan data yang tadi anda pilih akan diproses, anda bisa melihat prosesnya di kolom view preprocesed data kemudian paling bawah akan muncul status prediction salah satu dari stay atau out kemudian tahapan pun selesai

## Business Dashboard

dashboard yang saya buat adalah analisis attrition rate menggunakan looker studiountuk mendapatkan attrition rate saya menggunakan rumus SUM(Attrition)/COUNT_DISTINCT(EmployeeId) dan membuat kolom baru kemudian dari situ saya analisis dari departement sampai overtime untuk link dashboardnya : https://lookerstudio.google.com/reporting/8bbe9f0e-ed27-47dc-8590-204d9a075f10

## Conclusion

kesimpulan dari dashboard yang saya buat adalah attrition rate dipengaruhi oleh faktor kenyamanan dalam bekerja baik lingkungan ataupun pekerjaan mereka,kemudian untuk pendapatan bulanan lumayan berpengaruh terhadap attrition rate karena pendapatan kecil bisa membuat karyawan menjadi tertekan apalagi ditambah dengan bekerja melebihi waktu yang membuat mereka tambah tertekan dalam pekerjaan sehingga masuk akal jika mereka keluar atau mengundurkan diri dari perusahaan 

### Rekomendasi Action Items (Optional)

ada beberapa saran rekomendasi untuk menurunkan attrition rate:

1.Peningkatan Kondisi Kerja: Perhatikan kembali kondisi kerja di departemen Sales, terutama dalam hal kenyamanan kerja. Tingkatkan komunikasi antara manajemen dan karyawan untuk memahami permasalahan yang ada dan upayakan untuk meningkatkan lingkungan kerja agar lebih nyaman dan memotivasi karyawan.

2.Evaluasi Kebijakan Gaji: Perhatikan kembali kebijakan gaji perusahaan, terutama untuk departemen Sales. Pastikan bahwa gaji yang ditawarkan sesuai dengan tingkat pekerjaan dan memberikan insentif yang cukup untuk mempertahankan karyawan yang berkinerja baik.

3.Program Retensi Karyawan: Implementasikan program-program retensi karyawan, seperti program pengembangan karyawan, peluang kenaikan jabatan, dan insentif kinerja, untuk memotivasi karyawan agar tetap tinggal dan berkinerja baik di perusahaan.

4.Penilaian Lingkungan Kerja: Lakukan penilaian mendalam terhadap lingkungan kerja di seluruh departemen. Identifikasi faktor-faktor yang menyebabkan tingkat kenyamanan kerja rendah dan upayakan untuk memperbaikinya.

5.Pengembangan Karyawan: Berikan pelatihan dan pengembangan kepada karyawan, terutama yang berada di departemen Sales, untuk meningkatkan keterampilan mereka dan memberikan mereka rasa kepemilikan terhadap pekerjaan mereka.

6.Peninjauan Kebijakan Umur dan Lama Kerja: Tinjau kembali kebijakan perusahaan terkait umur pensiun dan penghargaan bagi karyawan yang telah bekerja dalam perusahaan selama jangka waktu tertentu. Pastikan bahwa kebijakan tersebut memotivasi karyawan untuk tetap tinggal dan berkontribusi dalam jangka waktu yang lebih panjang.

7.Fokus pada High-Performing Roles: Berikan perhatian khusus pada posisi-posisi yang telah terbukti menjadi penyumbang karyawan high performance, seperti Research Scientist dan Sales Executive. Identifikasi faktor-faktor yang membuat posisi-posisi ini berhasil dan upayakan untuk menerapkan strategi yang sama pada posisi lain dalam perusahaan.
