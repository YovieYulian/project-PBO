import sqlite3
connection = sqlite3.connect("E:/Kuliah/Python/PBO/dbbaru.db")

class user:
    def __init__ (self) :
        self.__Username = None
        self.__Password = None
        self.__TanggaLahir = None 
        self.__Gender= None 
        self.__Tinggi = None
        self.__BeratBadan = None 
        self.__Nik = None 
        self.__NomorHP = None
        self.__Alamat = None 
        self.__NilaiUN = None 
        self.__AsalSekolah = None 
        self.__jurusan = None  
        self.__NamaAyah = None 
        self.__NamaIbu = None 
        self.__KerjaAyah = None 
        self.__KerjaIbu = None 
        self.__JmlhSaudara = None 
        self.__status = None 
        self.__Pekerjaan = None
        self.__Sekolah = None
          
    def AddDataUser(self):
        self.__Username = input ("masukan Username Baru : ")
        self.__Password = input ("masukan password baru : ")
        self.__Nama = input ("masukan nama  : " )
        self.__TanggaLahir =input ("masukan Tanggal Lahir : " )
        for row in connection.execute('SELECT * FROM Gender'):
            print(row)
        self.__Gender= input("masukan ID Gender : " )   
        self.__Tinggi =input ("masukan Tinggi : " )
        self.__BeratBadan =input ("masukan Berat : " ) 
        self.__nik =input ("masukan NIK  : " ) 
        self.__NomorHP =input ("masukan NomorHP  : " )
        self.__Alamat = input ("masukan alamat : ") 
        self.__NilaiUN =input ("masukan Nilai UN  : " )
        for row in connection.execute('SELECT * FROM AsalSekolah'):
            print(row)
        self.__AsalSekolah =input ("masukan ID Asal Sekolah : " )
        for row in connection.execute('SELECT * FROM Jurusan'):
            print(row)
        self.__jurusan =input ("masukan ID Jurusan : " )   
        self.__NamaAyah =input ("masukan Nama Ayah : " ) 
        self.__NamaIbu =input ("masukan Nama Ibu : " )
        for row in connection.execute('SELECT * FROM Pekerjaan'):
            print(row)
        self.__KerjaAyah =input ("masukan Pekerjaan Ayah : " )
        for row in connection.execute('SELECT * FROM Pekerjaan'):
            print(row)
        self.__KerjaIbu =input ("masukan Nama Ibu : " )   
        self.__JmlhSaudara = input ("masukan Jumlah saudara : " )
        for row in connection.execute('SELECT * FROM StatusSiswa'):
            print(row)
        self.__status = input ("masukan ID status : " ) 

        query = f'INSERT INTO User(Username,Password,Nama,tglLahir,Gender,tinggiBadan,beratBadan,NIK,noHP,Alamat,nilaiUN,asalSekolah,jurusanPilihan,namaAyah,namaIbu,pekerjaanAyah,pekerjaanIbu,jmlSaudara,status) VALUES ("{self.__Username}", "{self.__Password}","{self.__Nama}",{self.__TanggaLahir},{self.__Gender},"{self.__Tinggi}","{self.__BeratBadan}","{self.__nik}","{self.__NomorHP}","{self.__Alamat}",{self.__NilaiUN},{self.__AsalSekolah},{self.__jurusan},"{self.__NamaAyah}","{self.__NamaIbu}",{self.__KerjaAyah},{self.__KerjaIbu},"{self.__JmlhSaudara}",{self.__status})'
        connection.execute(query)
        connection.commit() 
    
    def AddStatus(self) : 
        self.__status = input ("masukan Status  : " )
        query = f'INSERT INTO StatusSiswa(Status) VALUES ("{self.__status}")'
        connection.execute(query)
        connection.commit()
    
    def AddAsalSekolah (self):
        self.__Sekolah =input ("masukan Asal Sekolah : " )
        query = f'INSERT INTO AsalSekolah(SekolahAsal) VALUES ("{self.__Sekolah}")'
        connection.execute(query)
        connection.commit()
    
    def AddPekerjaan (self):
        self.__Pekerjaan = input ("masukan nama pekerjaan : ")
        query = f'INSERT INTO Pekerjaan(Pekerjaan) VALUES ("{self.__Pekerjaan}")'
        connection.execute(query)
        connection.commit()
    
    def Addjurusan(self):
        self.__jurusan = input ("masukan Jurusan : ")
        query = f'INSERT INTO Jurusan(JurusanPilihan) VALUES ("{self.__jurusan}")'
        connection.execute(query)
        connection.commit()
    
    def AddGender(self) :
        self.__Gender = input ("masukan Gender  : ")
        query = f'INSERT INTO Gender(Gender) VALUES ("{self.__Gender}")'
        connection.execute(query)
        connection.commit()
    
    def ubahNama(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        setNama = input('Masukkan nama: ')
        connection.execute(f'UPDATE User SET Nama = "{setNama}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahTglLahir(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        setTgl = input('Masukkan tanggal lahir: (format YYYY-MM-DD)')
        connection.execute(f'UPDATE User SET tglLahir = "{setTgl}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahGender(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        for row in connection.execute('SELECT * FROM Gender'):
            print(row)
        setGender = input('Masukkan jenis kelamin: ')
        connection.execute(f'UPDATE User SET Gender = "{setGender}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahTinggi(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        setTinggi = input('Masukkan tinggi badan: ')
        connection.execute(f'UPDATE User SET tinggiBadan = "{setTinggi}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahBerat(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        setBerat = input('Masukkan berat badan: ')
        connection.execute(f'UPDATE User SET beratBadan = "{setBerat}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahNik(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        setNik = input('Masukkan NIK: ')
        connection.execute(f'UPDATE User SET NIK = "{setNik}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahNoHp(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        setNoHp = input('Masukkan nomer HP: ')
        connection.execute(f'UPDATE User SET noHp = "{setNoHp}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahAlamat(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        setAlamat = input('Masukkan Alamat: ')
        connection.execute(f'UPDATE User SET Alamat = "{setAlamat}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahNilai(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        setNilai = input('Masukkan NilaiUN : ')
        connection.execute(f'UPDATE User SET nilaiUN = "{setNilai}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahAsalSekolah(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        for row in connection.execute('SELECT * FROM AsalSekolah'):
            print(row)
        setSekolah = input('Masukkan ID sekolah: ')
        connection.execute(f'UPDATE User SET asalSekolah = "{setSekolah}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahJurusan(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        for row in connection.execute('SELECT * FROM Jurusan'):
            print(row)
        setJurusan = input('Masukkan Jurusan pilihan: ')
        connection.execute(f'UPDATE User SET jurusanPilihan = "{setJurusan}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahNamaAyah(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        setNamaAyah = input('Masukkan nama Ayah: ')
        connection.execute(f'UPDATE User SET namaAyah = "{setNamaAyah}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahNamaIbu(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        setNamaIbu = input('Masukkan nama Ibu: ')
        connection.execute(f'UPDATE User SET namaIbu = "{setNamaIbu}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahPekerjaanAyah(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        setPekerjaanAyah = input('Masukkan pekerjaan Ayah: ')
        connection.execute(f'UPDATE User SET pekerjaanAyah = "{setPekerjaanAyah}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahPekerjaanIbu(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        setPekerjaanIbu = input('Masukkan pekerjaan Ibu: ')
        connection.execute(f'UPDATE User SET pekerjaanIbu = "{setPekerjaanIbu}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahJmlSaudara(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        setSaudara = input('Masukkan jumlah saudara: ')
        connection.execute(f'UPDATE User SET jmlSaudara = "{setSaudara}" WHERE idUser = {idSearch}')
        connection.commit()

    def ubahStatus(self):
        idSearch = input('Masukkan id siswa yang akan dirubah datanya: ')
        for row in connection.execute('SELECT * FROM StatusSiswa'):
            print(row)
        setStatus = input('Tetapkan status calon siswa: ')
        connection.execute(f'UPDATE User SET status = "{setStatus}" WHERE idUser = {idSearch}')
        connection.commit()

    def DeleteUser(self):
        for row in connection.execute('SELECT * FROM User'):
            print(row)
        idDelete = input('Masukkan id Siswa yang akan dihapus: ')
        connection.execute(f'DELETE * FROM User  WHERE idUser ={idDelete}')
        connection.commit()
        
    def ShowDataUser (self) :
        for row in connection.execute('SELECT Nama, tglLahir, Genders.GenderDetail, tinggiBadan, beratBadan, NIK, noHP, Alamat, nilaiUN, AsalSekolah.SekolahAsal, Jurusan.JurusanPilihan, namaAyah, namaIbu, pekerjaanAyah, pekerjaanIbu, jmlSaudara, StatusSiswa.Status FROM User JOIN Genders on User.Gender = Genders.idGender, AsalSekolah on User.asalSekolah = AsalSekolah.idSekolah, Jurusan on User.jurusanPilihan = Jurusan.idJurusan, Pekerjaan on User.pekerjaanAyah AND User.pekerjaanIbu = Pekerjaan.idPekerjaan,StatusSiswa on User.status = StatusSiswa.idStatus'):
            print(row)

    def ShowSelfUser (self) :
        print('Nama: ')
        #for row in connection.execute(f'SELECT * FROM User JOIN Gender on User.Gender = Gender.idGender, AsalSekolah on User.asalSekolah = AsalSekolah.idSekolah, Jurusan on User.jurusanPilihan = Jurusan.idJurusan, Pekerjaan on User.pekerjaanAyah AND User.pekerjaanIbu = Pekerjaan.idPekerjaan,StatusSiswa on User.status = StatusSiswa.idStatus WHERE Username = "{Username}"'):
        #   print(row)
        for row in connection.execute(f'SELECT Nama From User WHERE Username = "{Username}"'):
            print(row)
        print('Tangal Lahir: ')
        for row in connection.execute(f'SELECT tglLahir From User WHERE Username = "{Username}"'):
            print(row)
        print('Gender: ')
        for row in connection.execute(f'SELECT Genders.GenderDetail From User JOIN Genders on User.Gender = Genders.idGender WHERE Username = "{Username}"'):
            print(row)
        print('Tinggi Badan: ')
        for row in connection.execute(f'SELECT tinggiBadan From User WHERE Username = "{Username}"'):
            print(row)
        print('Berat Badan: ')
        for row in connection.execute(f'SELECT beratBadan From User WHERE Username = "{Username}"'):
            print(row)
        print('NIK: ')
        for row in connection.execute(f'SELECT NIK From User WHERE Username = "{Username}"'):
            print(row)
        print('Nomer HP: ')
        for row in connection.execute(f'SELECT noHP From User WHERE Username = "{Username}"'):
            print(row)
        print('Alamat: ')
        for row in connection.execute(f'SELECT Alamat From User WHERE Username = "{Username}"'):
            print(row)
        print('Nilai UN: ')
        for row in connection.execute(f'SELECT nilaiUN From User WHERE Username = "{Username}"'):
            print(row)
        print('Asal Sekolah: ')
        for row in connection.execute(f'SELECT AsalSekolah.SekolahASal From User JOIN AsalSekolah on User.asalSekolah = AsalSekolah.idSekolah WHERE Username = "{Username}"'):
            print(row)
        print('Jurusan Pilihan: ')
        for row in connection.execute(f'SELECT Jurusan.JurusanPilihan From User JOIN Jurusan on User.jurusanPilihan = Jurusan.idJurusan WHERE Username = "{Username}"'):
            print(row)
        print('Nama Ayah: ')
        for row in connection.execute(f'SELECT namaAyah From User WHERE Username = "{Username}"'):
            print(row)
        print('Nama Ibu: ')
        for row in connection.execute(f'SELECT namaIbu From User WHERE Username = "{Username}"'):
            print(row)
        print('Pekerjaan Ayah: ')
        for row in connection.execute(f'SELECT Pekerjaan.Pekerjaan From User JOIN Pekerjaan on User.pekerjaanAyah = Pekerjaan.idPekerjaan WHERE Username = "{Username}"'):
            print(row)
        print('Pekerjaan Ibu: ')
        for row in connection.execute(f'SELECT Pekerjaan.Pekerjaan From User JOIN Pekerjaan on User.pekerjaanIbu = Pekerjaan.idPekerjaan WHERE Username = "{Username}"'):
            print(row)
        print('Jumlah Saudara: ')
        for row in connection.execute(f'SELECT jmlSaudara From User WHERE Username = "{Username}"'):
            print(row)
        print('Status Penerimaan: ')
        for row in connection.execute(f'SELECT StatusSiswa.Status From User JOIN StatusSiswa on User.status = StatusSiswa.idStatus WHERE Username = "{Username}"'):
            print(row)
        
    
    #def ShowDataUser (self) :
    #    for row in connection.execute('SELECT * FROM User JOIN Gender on User.Gender = Gender.idGender,AsalSekolah on User.asalSekolah = AsalSekolah.idSekolah,Jurusan on User.jurusanPilihan = Jurusan.idJurusan,Pekerjaan on User.pekerjaanAyah AND User.pekerjaanIbu = Pekerjaan.idPekerjaan,StatusSiswa on User.status = StatusSiswa.idStatus'):
    #        print(row)
        
class panitia (user) :
    def __init__ (self) :
        self.__Nip = None
        self.__Nama = None
        self.__Username = None
        self.__Password = None
    
    def AddDataPanitia (self) :
        self.__Username = input ("masukan Username Baru : ")
        self.__Password = input ("masukan password baru : ")
        self.__Nama = input ("masukan nama : ")
        self.__Nip =  input("masukan NIP : ")
        query = f'INSERT INTO Panitia(Username,Password,Nama,NIP) VALUES ("{self.__Username}","{self.__Password}","{self.__Nama}","{self.__Nip}")'
        connection.execute(query)
        connection.commit()
print("----Login----")
print("""
Siapkah anda ??
1. Panitia
2. siswa
""")
login = input ("masukan pilihan anda : ")
if login == "1" :
    obj=panitia()
    Username = input ("Username : ")
    Password = input ("Password : ")
    cur = connection.cursor()
    cur.execute('SELECT * from Panitia WHERE Username="%s" AND Password="%s"' % (Username, Password))
    if (len(list(cur)) > 0):
        while True :
            print(""" 
            Menu : 
                1. Melihat data Siswa
                2. Menambah Data Siswa
                3. Mengubah Data Siswa
                4. Menghapus Data Siswa
                5. Exit
            """)

            masukan = input ()
            if masukan == "1" :
                obj.ShowDataUser()
            if masukan == "2" :
                obj.AddDataUser()
            if masukan == "3" :
                obj.ShowDataUser()
                while True :
                    print(""" 
                    apa yang akan di edit
                    1. Nama || 2. TanggalLahir || 3. Gender || 4. Tinggi badan || 5. Berat badan ||
                    6. NIK || 7. No HP || 8. Alamat || 9. Nilai UN || 10. Asal Sekolah ||
                    11. Jurusan Pilihan || 12. Nama Ayah || 13. Nama Ibu || 14. Pekerjaan Ayah || 15. Pekerjaan Ibu ||
                    16. Jumlah Saudara || 17. Status Penerimaan || 18. Back
                    """)
                    Edit = input("")
                    if Edit == "1" :
                        obj.ubahNama()
                    elif Edit == "2":
                        obj.ubahTglLahir()
                    elif Edit == "3":
                        obj.ubahGender()
                    elif Edit == "4":
                        obj.ubahTinggi()
                    elif Edit == "5":
                        obj.ubahBerat()
                    elif Edit == "6":
                        obj.ubahNik()
                    elif Edit == "7":
                        obj.ubahNoHp()
                    elif Edit == "8":
                        obj.ubahAlamat()
                    elif Edit == "9":
                        obj.ubahNilai()
                    elif Edit == "10":
                        obj.ubahAsalSekolah()
                    elif Edit == "11":
                        obj.ubahJurusan()
                    elif Edit == "12":
                        obj.ubahNamaAyah()
                    elif Edit == "13":
                        obj.ubahNamaIbu()
                    elif Edit == "14":
                        obj.ubahPekerjaanAyah()
                    elif Edit == "15":
                        obj.ubahPekerjaanIbu()
                    elif Edit == "16":
                        obj.ubahJmlSaudara()
                    elif Edit == "17":
                        obj.ubahStatus()
                    elif Edit == "18":
                        break
                    else:
                        continue

            if masukan == "4" :
                obj.DeleteUser()
            if masukan == "5" :
                break
            
    else:
        print ("Login failed")
if login == "2":
    obj=user()
    Username = input ("Username : ")
    Password = input ("Password : ")
    cur = connection.cursor()
    cur.execute('SELECT * from User WHERE Username="%s" AND Password="%s"' % (Username, Password))
    if (len(list(cur)) > 0):
        obj.ShowSelfUser()
    else:
        print('Login Gagal')
