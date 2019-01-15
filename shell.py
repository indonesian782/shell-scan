y# ! / usr / bin / python3
# Kode oleh:X-PL0Y

dari permintaan impor urllib.request, urlopen
dari urllib.error, impor URLError, HTTPError
impor argparse
impor sys
waktu impor

global yang starttime

kelas  ZeroScann ():

    def  __init__ ( mandiri ):
        diri .scan ()
        
     pemindaian def ( mandiri ):
        # argumen parser seperti kotoran
        parser = argparse.ArgumentParser ( prog = " PosiX.py " , description = " Simple Find Shell in Website " )
        parser.add_argument ( " -u " , dest = " domain " , help = " your url " )
        parser.add_argument ( " -w " , dest = " wordlist " , help = " your wordlsit " )
        args = parser.parse_args ()
        jika  tidak args.domain:
            sys.exit ( " \ 033 [36musage: shell.py -u example.com -w wordlist.txt " )
        jika  tidak args.wordlist:
            sys.exit ( " \ 033 [36musage: shell.py -u example.com -w wordlist.txt " )
            
        # menangani format situs web url
        situs = args.domain
        cetak ( " \ 033 [96m [?] \ 033 [0m Mulai Merangkak ... " )
        cetak ( " \ 033 [96m [!] \ 033 [0mTunggu sebentar! " , " \ n " )
        time.sleep ( 3 )
        jika  tidak site.startswith ( " http: // " ):
            site =  " http: // " + situs
        jika  tidak site.endswith ( " / " ):
            situs = situs + " / "
        # memuat daftar kata
        coba :
            pathlist = args.wordlist
            wlist =  terbuka (pathlist, " r " )
            wordlist = wlist.readlines ()
        kecuali FileNotFound sebagai e:
            print ( " \ 033 [91mUpss, Wordlist Tidak Ditemukan! \ 033 [0m " )
            keluar ()
        akhirnya :
            coba :
                wlist.close ()
            kecuali :
                print ( " \ 033 [91mWordlist Bisa \' t Tutup! \ 033 [0m " )
        # agen pengguna
        user_agent =  " Mozilla / 5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit / 537.36 (KHTML, seperti Gecko) Chrome / 35.0.1916.47 Safari / 537.36 "
        # Daftar untuk memegang hasil kita menemukan
        ditemukan = []
        # kode tanggapan
        resp_codes = { 403 : " 403 forbidden " , 401 : " 401 tidak sah " }
        # loop dengan gabung pathlist
        starttime = time.time ()
        untuk psx di daftar kata:
            coba :
                psx = psx.replace ( " \ n " , " " )
                url = situs + psx
                req = Permintaan (url, header = { " User-Agent " : user_agent})
                time.sleep ( 0.1 )
                coba :
                    koneksi = urlopen (req)
                    cetak ( " \ 033 [96m [ \ 033 [90m {0} \ 033 [96m] " .format (time.strftime ( " % H:% M:% S " )), " \ 033 [92mfound: " , " \ 033 [0m / " + psx)
                    found.append (url)
                    
                kecuali HTTPError sebagai e:
                    jika e.code ==  404 :
                        cetak ( " \ 033 [96m [ \ 033 [90m {0} \ 033 [96m] " .format (time.strftime ( " % H:% M:% S " )), " \ 033 [91merror: " , " \ 033 [0m / " + psx)
                    lain :
                        cetak ( " \ 033 [96m [ \ 033 [90m {0} \ 033 [96m] " .format (time.strftime ( " % H:% M:% S " )), " \ 033 [92minfo: " , " \ 033 [33m / " + psx, " \ 033 [92mstatus: \ 033 [33m " , resp_codes [e.code])
                        
                kecuali URLError sebagai e:
                    sys.exit ( " \ 033 [31m [!] Upss, Tanpa Koneksi Internet " )
                kecuali  Pengecualian  sebagai er:
                    cetak ( " \ n \ 033 [93m [?] \ 033 [0m Sambungan Anda Buruk " )
                    cetak ( " \ 033 [93m [!] \ 033 [Program 0mExit " )
                    time.sleep ( 3 )
                    keluar ()
            kecuali  KeyboardInterrupt  sebagai e:
                cetak ( " \ n \ 033 [96m [?] \ 033 [0mCTRL + C Terdeteksi " )
                cetak ( " \ 033 [96m [!] \ 033 [Program 0mExit " )
                time.sleep ( 2 )
                keluar ()
        
        jika ditemukan:
            cetak ( " \ n \ 033 [96m [+] \ 033 [0mHasil Ditemukan \ 033 [92m " )
            print ( " \ n " .join (ditemukan))
            cetak ( " \ 033 [96m [?] \ 033 [0mWaktu Dihapus: \ 033 [35m % .2f \ 033 [0m Detik "  %  float (time.time () - waktu mulai ))
        lain :
            cetak ( " \ n \ 033 [96m [!] \ 033 [0m Tidak Dapat Menemukan Shell Backdoor " )
            cetak ( " \ 033 [96m [?] \ 033 [0mWaktu Dihapus: \ 033 [33m % .2f \ 033 [0m Detik "  %  float (time.time () - waktu mulai ))
                
     spanduk def ():
        # hanya tampilan layar seperti ini
        info = .o oOOOOOOOo OOOo
             Ob.OOOOOOOo OOOo. oooo .adOOOOOOO
             OboO "" "" "" "" "" "" ". OOo. .oOOOOOo. OOOo.oOOOOOo .. "" "" "" "" "" OO
             OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.` "OOOOOOOOOOP, OOOOOOOOOOOB '
             `OOOOO '` OOOOo "OOOOOOOOOOO`. AdOOOOOOOOO" oOOO' `OOOOo
             .OOOO '`OOOOOOOOOOOOOOOOOOOOOOOOOO'` OO
             OOOOO '"OOOOOOOOOOOOOOOO" `oOO
            oOOOOOba. .adOOOOOOOOOOba .adOOOOo.
           oOOOOOOOOOOOOOba. .adOOOOOOOOOO @ ^ OOOOOOOba. .adOOOOOOOOOOOO
          OOOOOOOOOOOOOOO.OOOOOOOOOOOOOO "` '"OOOOOOOOOOOOO.OOOOOOOOOOOOOOOO
          "OOOO" "YOoOOOOMOIONODOO" `. '"OOROAOPOEOOOoY" "OOO"
             Y 'OOOOOOOOOOOOOO: .oOOo. : OOOOOOOOOOO? ' : `
             : .oO% OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?          
                          oOOP "% OOOOOOOOoOOOOOOO? oOOOOO? OOOO" OOo
                          '% o OOOO "% OOOO%"% OOOOO "OOOOOO" OOO':
                               `$" `OOOO '` O "Y'` OOOO 'o              
                                      OP ": o      
 # ================================= #
 # Shell Scanner #
# Kode oleh:X-PL0Y # 
 # 2019 #
 # Indonesian Security Team #
 # ================================= #
              "" "
        kembalikan info
    cetak (spanduk ())
                
if  __name__  ==  ' __main__ ' :
    ZeroScann ()
