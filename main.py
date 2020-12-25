class account :
    def __init__ (self):
        self.__Nama = None
        self.__Username = None
        self.__Password = None
    def AddDataAcount (self) :
        self.__Nama : input ("masukan nama baru : " )
        self.__Username : input ("masukan Username Baru : ")
        self.__Password : input ("masukan password baru : ")

class user (account) :
    def __init__ (self) :
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
    
    def AddDataUser(self):
        self.__Nama : input ("masukan nama  : " )
        self.__TanggaLahir =input ("masukan Tanggal Lahir : " )  
        self.__Gender=input ("masukan Gender : " ) 
        self.__Tinggi =input ("masukan Tinggi : " )
        self.__BeratBadan =input ("masukan Berat : " ) 
        self.__nik =input ("masukan NIK  : " ) 
        self.__NomorHP =input ("masukan NomorHP  : " ) 
        self.__NilaiUN =input ("masukan Nilai UN  : " ) 
        self.__AsalSekolah =input ("masukan Asal Sekolah : " ) 
        self.__jurusan =input ("masukan Jurusan : " )  
        self.__NamaAyah =input ("masukan Nama Ayah : " ) 
        self.__NamaIbu =input ("masukan Nama Ibu : " ) 
        self.__KerjaAyah =input ("masukan Pekerjaan Ayah : " ) 
        self.__KerjaIbu =input ("masukan Nama Ibu : " ) 
        self.__JmlhSaudara =input ("masukan Jumlah saudara : " ) 
        self.__status =input ("masukan Status  : " ) 
class panitia (user) :
    def __init__ (self) :
        self.__Nip = None
    def AddDataPanitia (self) :
        self.__Nip =  None 