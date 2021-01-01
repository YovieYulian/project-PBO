import sqlite3

cn = sqlite3.connect('E:/Kuliah/Python/PBO/dbbaru.db')

query = [
    'CREATE TABLE IF NOT EXISTS "StatusSiswa" ("idStatus" INTEGER NOT NULL, "Status" TEXT NOT NULL, PRIMARY KEY("idStatus"))', 
    'CREATE TABLE IF NOT EXISTS "Pekerjaan" ("idPekerjaan" INTEGER NOT NULL, "Pekerjaan" TEXT NOT NULL, PRIMARY KEY("idPekerjaan"))',
    'CREATE TABLE IF NOT EXISTS "Jurusan" ("idJurusan" INTEGER NOT NULL, "JurusanPilihan" TEXT NOT NULL, PRIMARY KEY("IdJurusan"))',
    'CREATE TABLE IF NOT EXISTS "AsalSekolah" (	"idSekolah"	INTEGER NOT NULL, "SekolahAsal" TEXT NOT NULL, PRIMARY KEY("idSekolah"))',
    'CREATE TABLE IF NOT EXISTS "Genders" ("idGender" INTEGER NOT NULL, "GenderDetail" TEXT NOT NULL, PRIMARY KEY("idGender"))',
    'CREATE TABLE IF NOT EXISTS "Panitia" ("idPanitia" INTEGER NOT NULL, "Username"	TEXT NOT NULL, "Password" TEXT NOT NULL, "Nama" TEXT NOT NULL, "NIP" TEXT NOT NULL, PRIMARY KEY("idPanitia"))',
    'CREATE TABLE IF NOT EXISTS "User" ("idUser" INTEGER NOT NULL, "Username" TEXT NOT NULL, "Password" TEXT NOT NULL, "Nama" TEXT NOT NULL, "tglLahir"	DATE NOT NULL, "Gender"	INTEGER, "tinggiBadan"	TEXT NOT NULL, "beratBadan"	TEXT NOT NULL, "NIK" TEXT NOT NULL,	"noHp" TEXT NOT NULL, "Alamat" TEXT NOT NULL, "nilaiUN"	INTEGER NOT NULL, "asalSekolah"	INTEGER, "jurusanPilihan" INTEGER, "namaAyah" TEXT NOT NULL, "namaIbu" TEXT NOT NULL,	"pekerjaanAyah"	INTEGER, "pekerjaanIbu" INTEGER, "jmlSaudara"	TEXT NOT NULL,"status" INTEGER, "panitiaPenerima" INTEGER,	PRIMARY KEY("idUser"), FOREIGN KEY("status") REFERENCES "StatusSiswa"("idStatus"), FOREIGN KEY("panitiaPenerima") REFERENCES "Panitia"("idPanitia"), FOREIGN KEY("Gender") REFERENCES "Genders"("idGender"),	FOREIGN KEY("asalSekolah") REFERENCES "AsalSekolah"("idSekolah"), FOREIGN KEY("jurusanPilihan") REFERENCES "Jurusan"("idJurusan"), FOREIGN KEY("pekerjaanIbu") REFERENCES "Pekerjaan"("idPekerjaan"),	FOREIGN KEY("pekerjaanAyah") REFERENCES "Pekerjaan"("idPekerjaan"))',
]

def generate():
    for p in range(len(query)):
        cn.execute(query[p])
        cn.commit

generate()
