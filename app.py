class Mahasiswa:
 def __init__(self, nm, no_induk):
  self.nama = str(nm);
  self.nim = str(no_induk);

 def getNama(self):
  return self.nama;

 def getNim(self):
  return self.nim;

 def setNama(self, nm):
  self.nama = nm;

 def setNim(self, no_induk):
  self.nim = no_induk;

DftrMhs = {};
loop = True;

print("===================================");
print("=         Daftar Mahasiswa        =");
print("===================================");
print("= # MENU                          =");
print("= 1. Tambah Mahasiswa             =");
print("= 2. Hapus Mahasiswa              =");
print("= 3. Tampilkan Semua Mahasiswa    =");
print("= 4. Cari Mahasiswa               =");
print("= 5. Edit Nama Mahasiswa          =");
print("= 6. Edit Nim Mahasiswa           =");
print("= 7. Jumlah Total Mahasiswa       =");
print("= 0. Keluar                       =");
print("===================================");

while(loop):
 print("\n\n");
 menu = int(input("Masukan menu : "));

 if menu == 1:
  print("============= ANDA BERADA DI MENU TAMBAH MAHASISWA ============")
  print("==================== SILAHKAN MASUKAN DATA ====================")
  nama = str(input("MASUKAN NAMA : "));
  nim = str(input("MASUKAN NIM : "));
  mhs = Mahasiswa(nama, nim);
  DftrMhs[nim] = mhs;
  print("================DATA MAHASIWA BERHASIL DITAMBAH===============")
 elif menu == 2:
  print("========== ANDA BERADA DI MENU HAPUS DATA MAHASISWA ============")
  print("======= SILAHKAN MASUKAN NIM DATA YANG AKAN DIHAPUS ============")
  nim = str(input("MASUKAN NIM : "));
  if(nim in DftrMhs):
   del DftrMhs[nim];
   print("================DATA MAHASIWA BERHASIL DIHAPUS===============")
  else:
   print("======================DATA TIDAK DITEMUKAN!!!==================");
 elif menu == 3:
  print("======= ANDA BERADA DI MENU TAMPILKAN DATA MAHASISWA =============")
  for i in DftrMhs:
    print("Nama :", DftrMhs[i].getNama());
    print("Nim :", DftrMhs[i].getNim());
    print("===============================================================");
 elif menu == 4:
  print("=========== ANDA BERADA DI MENU CARI DATA MAHASISWA ==============")
  print("====================== SILAHKAN MASUKAN NIM ======================")
  nim = str(input("MASUKAN NIM : "));
  if(nim in DftrMhs):
   print("Nama : ", DftrMhs[nim].getNama());
   print("Nim : ", DftrMhs[nim].getNim());
   print("==========================DATA DITEMUKAN!!!=====================");
  else:
   print("======================DATA TIDAK DITEMUKAN!!!===================");
 elif menu == 5:
  print("=========== ANDA BERADA DI MENU EDIT NAMA MAHASISWA ==============")
  print("====================== SILAHKAN MASUKAN NIM ======================")
  nim = str(input("MASUKAN NIM : "));
  if(nim in DftrMhs):
   namaBaru = str(input("MASUKAN NAMA BARU : "));
   DftrMhs[nim].setNama(namaBaru);
   print("==============DATA NAMA MAHASIWA BERHASIL DI EDIT===============")
  else:
   print("======================DATA TIDAK DITEMUKAN!!!===================");
 elif menu == 6:
  print("=========== ANDA BERADA DI MENU EDIT NNIM MAHASISWA ==============")
  print("====================== SILAHKAN MASUKAN NIM ======================")
  nim = str(input("MASUKAN NIM : "));
  if(nim in DftrMhs):
   nimBaru = str(input("MASUKAN NIM BARU : "));
   DftrMhs[nim].setNim(nimBaru);
   mhs = DftrMhs[nim];
   DftrMhs[nimBaru] = mhs;
   del DftrMhs[nim];
   print("===================DATA NIM MAHASIWA BERHASIL DI EDIT===========")
  else:
      print("======================DATA TIDAK DITEMUKAN!!!===================");
 elif menu == 7:
  print("===============================================================");
  print("DATA JUMLAH MAHASISWA: ", len(DftrMhs));
 elif menu == 0:
  loop = False;
 else:
  print("XXXX");