import sqlite3
connection = sqlite3.connect("E:/data kuliah/semester 3/PBO/project/coding/database.db")

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
        self.__Tinggi =input ("masukan Tinggi : " )
        self.__BeratBadan =input ("masukan Berat : " ) 
        self.__nik =input ("masukan NIK  : " ) 
        self.__NomorHP =input ("masukan NomorHP  : " ) 
        self.__NilaiUN =input ("masukan Nilai UN  : " )   
        self.__NamaAyah =input ("masukan Nama Ayah : " ) 
        self.__NamaIbu =input ("masukan Nama Ibu : " )   
        self.__JmlhSaudara = input ("masukan Jumlah saudara : " ) 

        query = f'INSERT INTO User(Username,Password,Nama,tglLahir,tinggiBadan,beratBadan,NIK,noHP,Alamat,nilaiUN,jurusanPilihan,namaAyah,namaIbu,pekerjaanAyah,pekerjaanIbu,jmlSaudara) VALUES ("{self.__Username}", {self.__Password},{self.__Nama},{self.__TanggaLahir},{self.__Tinggi},{self.__BeratBadan},{self.__nik},{self.__NomorHP},{self.__NilaiUN},{self.__NamaAyah},{self.__NamaIbu},"{self.__JmlhSaudara}")'
        connection.execute(query)
        connection.commit() 
    def AddStatus(self) : 
        self.__status = input ("masukan Status  : " ) 
    
    def SetStatus(self):
        for row in connection.execute('SELECT * FROM StatusSiswa'):
            print(row)
        self.__status = input ("masukan ID status : " )
        query = f'INSERT INTO User(status) VALUES ("{self.__status}")'
        connection.execute(query)
        connection.commit()
         

    def AddAsalSekolah (self):
        self.__Sekolah =input ("masukan Asal Sekolah : " )
        query = f'INSERT INTO AsalSekolah(SekolahAsal) VALUES ("{self.__Sekolah}")'
        connection.execute(query)
        connection.commit()

    def SetAsalSekolah (self):
        for row in connection.execute('SELECT * FROM AsalSekolah'):
            print(row)
        self.__AsalSekolah =input ("masukan ID Asal Sekolah : " )
        query = f'INSERT INTO User(asalSekolah) VALUES ("{self.__AsalSekolah}")'
        connection.execute(query)
        connection.commit()

    def SetGender (self) :
         for row in connection.execute('SELECT * FROM Gender'):
            print(row)
        self.__Gender=input ("masukan ID Gender : " ) 
        query = f'INSERT INTO User(Gender) VALUES ("{self.__Gender}")'
        connection.execute(query)
        connection.commit()

    def SetJurusan(self) :
        for row in connection.execute('SELECT * FROM Jurusan'):
            print(row)
        self.__jurusan =input ("masukan ID Jurusan : " )
        query = f'INSERT INTO User(jurusanPilihan) VALUES ("{self.__jurusan}")'
        connection.execute(query)
        connection.commit()
    
    def AddPekerjaan (self):
        self.__Pekerjaan = input ("masukan nama pekerjaan : ")
        query = f'INSERT INTO Pekerjaan(Pekerjaan) VALUES ("{self.__Pekerjaan}")'
        connection.execute(query)
        connection.commit()
    
    def SetPekerjaanAyah (self):
        for row in connection.execute('SELECT * FROM Pekerjaan'):
            print(row)
        self.__KerjaAyah =input ("masukan Pekerjaan Ayah : " )
        query = f'INSERT INTO User(pekerjaanAyah) VALUES ("{self.__KerjaAyah}")'
        connection.execute(query)
        connection.commit()

    def SetPekerjaanIbu (self):
        for row in connection.execute('SELECT * FROM Pekerjaan'):
            print(row)
        self.__KerjaIbu =input ("masukan Nama Ibu : " )
        query = f'INSERT INTO User(pekerjaanIbu) VALUES ("{self.__KerjaIbu}")'
        connection.execute(query)
        connection.commit()
        

class panitia (user) :
    def __init__ (self) :
        self.__Nip = None
        self.__Nama = None
    def AddDataPanitia (self) :
        self.__Username = input ("masukan Username Baru : ")
        self.__Password = input ("masukan password baru : ")
        self.__Nip =  input("masukan NIP : ")
        
obj= panitia()
obj.SetStatus()
