
import sys

abjad = set("ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyz")
abjadplus = set("ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyz ")
kapital = set("ABCDEFGHIJKLMNOPRSTUVWXYZ")
hurufkecil = set("abcdefghijklmnoprstuvwxyz")
angka = set("1234567890")
spesial = set("&^%$#!@ ")

useridbaru = str()
passwordbaru = str()
namabaru = str()
emailbaru = str()
umurbaru = str()
genderbaru = str()
pekerjaanbaru = str()
hobibaru = str()
namakotabaru = str()
rtbaru = str()
rwbaru = str()
kodeposbaru = str()
latbaru = str()
longbaru = str()
hpbaru = str()

datauserfinal = dict()
databarang = dict()
stokbarang = dict()



def userid(inputuserid):
    global spesial
    


    if (any((c in angka) for c in inputuserid)) and (any((c in spesial) for c in inputuserid) == False) and len(inputuserid) >= 6 and len(inputuserid) <= 20 and (any((c in abjad) for c in inputuserid)):
        return('format benar\n')

    return "USER id tidak sesuai format"

def password(inputuserid):
    global spesial
    


    if (any((c in kapital) for c in inputuserid)) and (any((c in spesial) for c in inputuserid)) and (any((c in hurufkecil) for c in inputuserid)) and (any((c in angka) for c in inputuserid)) and len(inputuserid) >= 8 :
        return('format benar\n')

    return "Password tidak sesuai format"

def emailseluruh(inputuser):

    try: 
        # Pemisahan email untuk di verifikasi (apakah format awal benar atau tidak)

        pemisah1 = inputuser.split("@")

        namauser = pemisah1[0]


        hostingexs = pemisah1[1]

        pemisah2 = hostingexs.split(".")

        hosting = pemisah2[0]

        extensi = pemisah2[1]

        extensi2 = ""

        

        if len(pemisah2) > 2:

            extensi2 = pemisah2[2]

            
            

        def verificationemail(Input1, NamaUser, Hosting, Pemisah2,  Extensi1, Extensi2):
            import re 
            


            if NamaUser == "":
                return("Format email anda salah tidak terdapat nama user didalam nya\n")

            inital = re.search(" ", Input1)

            if inital: 
                return("Format email anda salah terdapat spasi di dalam nya\n")

            
            if len(Pemisah2) > 3:

                return("Format extensi yang anda gunakan tidak valid\n")

            userdepan = NamaUser[0].isalpha()
            userdepan1 = NamaUser[0].isnumeric()

            if userdepan == False and userdepan1 == False :
                return("Format tidak valid karena nama user name hanya dapat di awali huruf atau angka\n")

            testhosting = Hosting.isnumeric()

            if testhosting == True:
                return("Format email invalid karena hosting tidak boleh hanya berisikan nomor\n")

            extensicek1 = Extensi1.isalpha()
            extensicek2 = Extensi2.isalpha()

            
            if extensi2 == "":

                if (len(Extensi1) > 5 or extensicek1 == False) :

                    return("Format tidak valid karena extensi anda salah\n")

            else:
                if (len(Extensi1) > 5 or extensicek1 == False) or (len(Extensi2) > 5 or extensicek2 == False):

                    return("Format tidak valid karena extensi anda salah\n")



            chars = set(''')(<>,;:\/"][}{''')

            if any((c in chars) for c in Input1):
                return('Format email anda salah terdapat special character di dalam nya\n')

            if any((c in chars) for c in NamaUser):
                return('Format email anda salah terdapat special character di dalam nya\n')

                
            else: 
                return("Alamat email anda valid\n")


        hasilakhir = verificationemail(inputuser, namauser, hosting, pemisah2, extensi, extensi2)

        return hasilakhir


    except:

        return("Format dalam email anda salah karena '@' atau extensi anda tidak valid\n")

def print_menu():       
    print ("\n---------------MENU APPLIKASI DIFA -----------------" )
    print ("1. Registration")
    print ("2. Log In")
    print ("3. Exit")
    print (67 * "-")

def print_menulogin():       
    print ("\n---------------MENU APPLIKASI DIFA -----------------" )
    print ("1. User Profile")
    print ("2. Menu Transaksi")
    print ("3. Log out")
    print (67 * "-")

def print_menutransaksi():       
    print ("\n---------------MENU TRANSAKSI -----------------" )
    print ("1. Create Data")
    print ("2. Read Data")
    print ("3. Update Data")
    print ("4. Delete Data")
    print ("5. Kembali ke Menu Awal")
    print (67 * "-")

def regnama(inputuserid):
    global spesial
    


    if (any((c in abjadplus) for c in inputuserid)):
        return('format benar\n')

    return "Nama tidak sesuai format"

def reggender(inputgender):
    global spesial
    
    inputgender = inputgender.lower()

    if inputgender == "male" or inputgender == "female":
        return('format benar\n')

    return "Password tidak sesuai format"

def regumur(inputuserid):
    global spesial

    if inputuserid.isnumeric():
        
        inputuseridnama = int(inputuserid)
        
        if inputuseridnama >= 17 and inputuseridnama <= 80 :
            return('format benar\n')

        else:
            return "Nama tidak sesuai format"
    
    else:   

     return "Nama tidak sesuai format"
 
def regpekerjaan(inputuserid):
    global spesial
    


    if (any((c in abjadplus) for c in inputuserid)):
        return('format benar\n')

    return "Nama tidak sesuai format"      
 
def regrt(inputuserid):
    global spesial

    if inputuserid.isnumeric():
        
        return("a")

    return "Nama tidak sesuai format"

def regkodepos(inputuserid):
    global spesial

    if inputuserid.isnumeric():
        
        
        
        
        if len(inputuserid) == 5 :
            return("a")

        else:
            return "kode tidak sesuai format"
        
        
        
        
    else:
        return "kode tidak sesuai format"

def reglat(inputuserid):


    cek = isinstance(inputuserid, float)
    if cek == True:
        return"a"

    return"kode tidak sesuai format"

def reghp(inputuserid):
    global spesial

    if inputuserid.isnumeric():
        
        
        
        if len(inputuserid) >= 11 and len(inputuserid) <= 13 :

            
            return"a"

        else:
            return "Nama tidak sesuai format"
    
    else:   

     return "Nama tidak sesuai format"



def main():          
    print_menu()    ## Displays menu
    global useridbaru
    

    choice = input("Enter your choice [1-3]: ")
    
    if choice == "1":     #registration
        print ("\nREGISTRATION SELECTED")

        for i in range(5): #registrasi user id
    
            print("\n-------------REGISTRASI----------")
            print("\nBatas maksimal percobaan adalah 5 kali bila berhasil akan lanjut ke perintah selanjutnya")  
            print("\nKetentuan membuat User ID\n1. Kombinasi angka dan huruf\n2. Tidak boleh ada spesial karakter\n3. Minimal 6 dan maksimal 20\n") 
            inputuseridluar = input("masukan user id yang anda inginkan: ")
            


            batas = userid(inputuseridluar)

            if (any((c in inputuseridluar) for c in datauserfinal)):
                print("\nUser ID yang anda masukan sudah terpakai")

            elif batas == 'format benar\n':
                useridbaru = inputuseridluar
                break

            if i == 4 :
                print("Anda telah memasukan lebih dari 5 kali")
                sys.exit() 
        
        for i in range(5): #membuat pasword
    

            print("\nKetentuan membuat pasword\n1. Terdapat huruf kapital dan kecil\n2. Terdapat spesial karakter dan angka\n3. Minimal 8 karakter")

            inputpass = input("Masukan password yang anda inginkan sesuai ketentuan: ")

            

            batas = password(inputpass)

            if batas == 'format benar\n':
                passwordbaru = inputpass
                break
                

            if i == 4 :
                print("Anda telah memasukan lebih dari 5 kali")
                sys.exit() 
        
        for i in range(5):  #registrasi email
            input1 = input("\nmasukan email anda untuk registrasi: ")
            batas = (emailseluruh(input1))
        
            if batas == 'Alamat email anda valid\n':
                emailbaru = input1
                break

            if i == 4 :
                print("Anda telah memasukan lebih dari 5 kali")
                sys.exit() 

        for i in range(5):  #registrasi nama

            print("\nKetentuan nama diri\n1. Hanya boleh huruf dan spasi\n")
            namabaru1 = input("Masukan nama anda:")

            hasilnama = regnama(namabaru1)

            

            if hasilnama == "format benar\n":
                namabaru = namabaru1
                

                break



            if i == 4 :
                print("Anda telah memasukan lebih dari 5 kali")
                sys.exit() 

        for i in range(5):  #registrasi gender

            
            genderbaru1 = input("\nMasukan gender anda (Male/Female):")

            hasilgender = reggender(genderbaru1)

            

            if hasilgender == "format benar\n":
                genderbaru = genderbaru1
                print("sesi selanjutnya") 

                break



            if i == 4 :
                print("Anda telah memasukan lebih dari 5 kali")
                sys.exit() 

        for i in range(5):  #registrasi umur

            print("\nKetentuan Umur\n1. Minimal 17 Tahun dan Maksimal 80 Tahun\n")
            umurbaru1 = input("Masukan umur anda:")

            hasilumur = regumur(umurbaru1)

            

            if hasilumur == "format benar\n":
                umurbaru1 = int(umurbaru1)
                umurbaru = umurbaru1
                

                break



            if i == 4 :
                print("Anda telah memasukan lebih dari 5 kali")
                sys.exit() 

        for i in range(5):  #registrasi pekerjaan

            print("\nKetentuan pekerjaan\n1. Hanya boleh huruf dan spasi\n")
            pekerjaanbaru1 = input("Masukan pekerjaan anda:")

            hasilpekerjaan = regpekerjaan(pekerjaanbaru1)

            

            if hasilpekerjaan == "format benar\n":
                pekerjaanbaru = pekerjaanbaru1
                

                break



            if i == 4 :
                print("Anda telah memasukan lebih dari 5 kali")
                sys.exit() 

        for i in range(5):  #registrasi hobi

            print("\nKetentuan hobi\n1. Hanya boleh huruf dan spasi\n")
            hobibaru1 = input("Masukan hobi anda:")

            hasilhobi = regpekerjaan(hobibaru1)

            

            if hasilhobi == "format benar\n":
                hobibaru = hobibaru1
                

                break



            if i == 4 :
                print("Anda telah memasukan lebih dari 5 kali")
                sys.exit() 

        for i in range(5):  #registrasi nama kota

            print("\n-------------Registrasi Alamat-----------")
            print("\nKetentuan nama kota\n1. Hanya boleh huruf dan spasi\n")
            namakotabaru1 = input("Masukan nama kota anda:")

            hasilnamakota = regpekerjaan(namakotabaru1)

            

            if hasilnamakota == "format benar\n":
                namakotabaru = namakotabaru1
                

                break



            if i == 4 :
                print("Anda telah memasukan lebih dari 5 kali")
                sys.exit() 

        for i in range(5):  #registrasi rt

            
            rtbaru1 = input("\nMasukan RT anda:")

            hasilrt = regrt(rtbaru1)

        
            

            if hasilrt == "a":
                rtbaru1 = int(rtbaru1)
                rtbaru = rtbaru1
                
                break



            if i == 4 :
                print("Anda telah memasukan lebih dari 5 kali")
                sys.exit() 

        for i in range(5):  #registrasi rw

            
            rwbaru1 = input("\nMasukan RW anda:")

            hasilrw = regrt(rwbaru1)

            

            if hasilrw == "a":
                rwbaru1 = int(rwbaru1)
                rwbaru = rwbaru1
                break



            if i == 4 :
                print("Anda telah memasukan lebih dari 5 kali")
                sys.exit() 

        for i in range(5):  #registrasi kodepos

            
            kodeposbaru1 = input("\nMasukan kodepos anda:")

            hasilkodepos = regkodepos(kodeposbaru1)

            

            if hasilkodepos == "a":
                kodeposbaru1 = int(kodeposbaru1)
                kodeposbaru = kodeposbaru1
                break



            if i == 4 :
                print("Anda telah memasukan lebih dari 5 kali")
                sys.exit() 

        for i in range(5):  #registrasi lat

            
            try:
                print("\n----------Registrasi Geographical----------")
                print("\nAnda hanya memiliki 5 kali percobaan")
                latbaru1 = float(input("masukan latitude: "))

                hasillat = reglat(latbaru1)

                if hasillat == "a":
                    latbaru = latbaru1
                    break



                if i == 4 :
                    print("Anda telah memasukan lebih dari 5 kali")
                    sys.exit() 

            except:   
                    print("latitude salah")

        for i in range(5):  #registrasi long

            
            try:
                print("\nAnda hanya memiliki 5 kali percobaan")
                longbaru1 = float(input("\nmasukan longitude: "))

                hasillong = reglat(longbaru1)

                if hasillong == "a":
                    longbaru = longbaru1
                    break



                if i == 4 :
                    print("Anda telah memasukan lebih dari 5 kali")
                    sys.exit() 

            except:   
                    print("latitude salah")

        for i in range(5):  #registrasi HP

            
            hpbaru1 = input("\nMasukan Nomor HP anda (antara 11 - 13):")

            hasilhp = reghp(hpbaru1)


            if hasilhp == "a":
                hpbaru1 = int(hpbaru1)
                hpbaru = hpbaru1
                break



            if i == 4 :
                print("Anda telah memasukan lebih dari 5 kali")
                sys.exit() 

        datauser = {useridbaru : { 
            "password" : passwordbaru,
            "email" : emailbaru,
            "nama" : namabaru, 
            "gender" : genderbaru,
            "usia" : umurbaru,
            "pekerjaan" : pekerjaanbaru,
            "hobi" : hobibaru,
            "alamat" : { 
                "nama kota" : namakotabaru,
                "rt" : rtbaru,
                "rw" : rwbaru,
                "kodepos" : kodeposbaru,
                "geo" : {
                    "lat" : latbaru,
                    "long" : longbaru,}
            },
            "hp" : hpbaru}}
   
        # akhir dari registrasi untuk menyimpan file 
        print("\n -----------------------------------------")
        save = input("\napakah anda mau menyimpan file (Y/N): ")
        save1 = save.lower()
        if save1 == "y":
            datauserfinal.update(datauser)
            print("\nData anda sudah tersimpan, anda sudah bisa untuk log in")
            main()
        
        elif save1 == "n":
            print("\nAnda tidak jadi menyimpan data anda")
            main()

        else:
            print("\nAnda salah melakukan input data yang sudah anda masukan tidak tersimpan")
            main()
       
    elif choice == "2": #log in 
        stokbarang = dict()
        global inputuserdaf

        for i in range(5): #user id 

            print ("\n---------Please Log In----------")
            inputuserdaf = input("\nMasukan user id: ")
            if (any((c in inputuserdaf) for c in datauserfinal)):
                break
            
            print("User ID anda salah, maksimal percobaan hanya 5 kali")

            if i == 4:
                print("anda sudah mencoba selama 5 kali ")
                main()

        for i in range(5): #password 

            inputuserpass = input("Masukan password anda: ")
            if (any((c in inputuserpass) for c in datauserfinal[inputuserdaf]["password"])):
                break
            
            print("Password anda salah, maksimal percobaan hanya 5 kali")

            if i == 4:
                print("anda sudah mencoba selama 5 kali ")
                

        print("Anda berhasil log in\n")

        
        submain()
   
    elif choice == "3":
        print ("EXIT")
        sys.exit() 
       
    else:
        
        print("Wrong option selection. Enter any key to try again..")

def submain():
            import sys
            print_menulogin()    ## Displays menu
            
            choice2 = input("Enter your choice [1-3]: ")

            if choice2 == "1":
                namakeluar = datauserfinal[inputuserdaf]["nama"]
                emailkelaur = datauserfinal[inputuserdaf]["email"]
                genderkelaur = datauserfinal[inputuserdaf]["gender"]
                usiakeluar = datauserfinal[inputuserdaf]["usia"]
                pekerjaankeluar = datauserfinal[inputuserdaf]["pekerjaan"]
                hobikeluar = datauserfinal[inputuserdaf]["hobi"]
                namakotakeluar = datauserfinal[inputuserdaf]["alamat"]["nama kota"]
                rtkeluar = datauserfinal[inputuserdaf]["alamat"]["rt"]
                rwkeluar = datauserfinal[inputuserdaf]["alamat"]["rw"]
                kodeposkeluar = datauserfinal[inputuserdaf]["alamat"]["kodepos"]
                latkeluar = datauserfinal[inputuserdaf]["alamat"]["geo"]["lat"]
                longkeluar = datauserfinal[inputuserdaf]["alamat"]["geo"]["long"]
                hpkeluar = datauserfinal[inputuserdaf]["hp"]

                print("\n-----------User Profile----------")
                print(f"Nama      : {namakeluar} ")
                print(f"Email     : {emailkelaur} ")
                print(f"Gender    : {genderkelaur} ")
                print(f"Usia      : {usiakeluar} ")
                print(f"Pekerjaan : {pekerjaankeluar} ")
                print(f"Hobi      : {hobikeluar} ")
                print(f"Alamat    :")
                print(f"    Nama Kota   : {namakotakeluar} ")
                print(f"    RT          : {rtkeluar:02d} ")
                print(f"    RW          : {rwkeluar:02d} ")
                print(f"    Kode Pos    : {kodeposkeluar} ")
                print(f"    Lat         : {latkeluar:6f} ")
                print(f"    Long        : {longkeluar:6f} ")
                print(f"HP        : {hpkeluar:012d} ")
                
                pilihan = input("\nDo you want go to main menu (Y/N(logout)): ")
                pilihan1 = pilihan.lower()

                if pilihan1 == "y":
                    submain()
                
                if pilihan1 == "n":
                    main()

            elif choice2 == "2":
                
                transaksi()

            elif choice2 == "3":
                main()

            else:
                print("Wrong option selection. Enter any key to try again..")
                submain()

def transaksi():
                    
                    print_menutransaksi()
                    choice4 = input("\nPilih yang menu anda mau lakukan: ")
                    choice4 = choice4.lower()

                    if choice4 == "1":

                        inputbrang = input("\nNama barang yang mau di input: ")
                        inputbrang = inputbrang.lower()
                        inputjumbar = input("Jumlah barang yang mau di input: ")

                        if inputjumbar.isnumeric() and inputbrang in stokbarang:
                            inputjumbar = int(inputjumbar)
                            print("Barang sudah tersedia di database\n")
                            updatebaranggak = input("Apakah anda ingin mengupdate jumlah barang (Y/N):")
                            updatebaranggak = updatebaranggak.lower()
                            if updatebaranggak == "y":
                                stokbarang.update({inputbrang: stokbarang[inputbrang]+ inputjumbar})
                                # if stokbarang[inputbrang] < 0:
                                #     print("stok minus")
                                #     stokbarang.update({inputbrang : 0 })
                                #     transaksi()
                                
                                transaksi()
                            
                            elif updatebaranggak == "n":
                                print("Tidak jadi melakukan update")
                                transaksi()
                                

                            else:
                                print("Anda salah melakukan input")
                                transaksi()

                        elif inputbrang[0].isalpha() and inputjumbar.isnumeric():
                            inputjumbar = int(inputjumbar)
                            stokbarang.update({inputbrang: inputjumbar})
                            print("Barang telah di input")
                            transaksi()

                        

                        elif inputbrang[0].isalpha() == False:
                            print("\nFormat barang yang anada masukan salah")
                            transaksi()

                        elif inputjumbar.isnumeric() == False:
                            print("\nFormat Jumlah barang yang anda masukan salah")
                            transaksi()
                        

                    elif choice4 == "2":
                        print("---------LIST BARANG----------")
                        for key, value in stokbarang.items():
                            print(key, ' : ', value)

                        transaksi()
                    
                    elif choice4 == "3":
                        inputbrang = input("\nNama barang yang mau di input: ")
                        inputbrang = inputbrang.lower()
                        inputjumbar = input("Jumlah barang yang mau di input: ")

                        if inputjumbar.isnumeric() and inputbrang in stokbarang:
                            inputjumbar = int(inputjumbar)
                            
                            updatebaranggak = input("Apakah anda ingin mengupdate jumlah barang (Y/N):")
                            updatebaranggak = updatebaranggak.lower()
                            if updatebaranggak == "y":
                                    
                                stokbarang.update({inputbrang: stokbarang[inputbrang]+ inputjumbar})
                                # if stokbarang[inputbrang] < 0:
                                #     print("stok minus")
                                #     stokbarang.update({inputbrang : 0 })
                                #     transaksi()
                            
                                transaksi()
                            
                            elif updatebaranggak == "n":
                                print("Tidak jadi melakukan update")
                                transaksi()

                            else:
                                print("Anda salah melakukan input")
                                transaksi()
                        
                        elif inputbrang[0].isalpha() and inputjumbar.isnumeric():
                            inputjumbar = int(inputjumbar)
                            print("Barang tidak tersedia di database\n")
                            updatebaranggak = input("Apakah anda ingin menambahkan barang (Y/N):")
                            updatebaranggak = updatebaranggak.lower()
                            

                            if updatebaranggak == "y":
                                stokbarang.update({inputbrang : inputjumbar})
                                transaksi()
                            
                            elif updatebaranggak == "n":
                                print("Tidak jadi melakukan update")
                                transaksi()

                            else:
                                print("Anda salah melakukan input")
                                transaksi()

                        elif inputbrang[0].isalpha() == False:
                            print("\nFormat barang yang anada masukan salah")
                            transaksi()

                        elif inputjumbar.isnumeric() == False:
                            print("\nFormat Jumlah barang yang anda masukan salah")
                            transaksi()
                        
                        

                    elif choice4 == "4":

                        inputbrang = input("\nNama barang yang mau di hapus: ")
                        inputbrang = inputbrang.lower()


                        
                        if inputbrang in stokbarang:
                            
                            updatebaranggak = input("Apakah anda ingin menghapus barang (Y/N):")
                            updatebaranggak = updatebaranggak.lower()

                            if updatebaranggak == "y":
                                stokbarang.pop(inputbrang)
                                transaksi()
                            
                            elif updatebaranggak == "n":
                                print("Tidak jadi melakukan update")
                                transaksi()

                            else:
                                print("Anda salah melakukan input")
                                transaksi()

                        else:
                            print("Barang yang anda masukan tidak ada dalam stok barang")
                            transaksi()

                            
                                



                        

                    elif choice4 == "5":

                        submain()
                    
                    else:
                        print("Wrong option selection. Enter any key to try again..")
                        transaksi()
 

main()