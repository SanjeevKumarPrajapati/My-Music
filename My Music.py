from playsound import playsound
from gtts import gTTS
def speak(text):
    import playsound
    tts=gTTS(text=text,lang="en")
    filename="abcd.mp3"
    tts.save(filename)
    playsound.playsound(filename)
def super_main():
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
    print("\t\t\t\t1.) Play List .............")
    print("\t\t\t\t2.) Instruction  .............")
    print("\t\t\t\t3.) Play Song ..............")
    print("\t\t\t\t4. ) Exit .............")
    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
    aaa=int(input("\t\t\t\tEnter Your Choice : "))
    if(aaa==1):
        song_name()
        super_main()
    elif(aaa==2):
        speak("My Music Player provides a powerful music play functionality and essential features for you with beautifully crafted with Material Design in mind It is one of the Best Music Players which can fulfill all your Musical needs My Music Player is not only based on artists or albums, but also based on genres and folder structure. My Music Player will guide you find all the music files in seconds Play all your music with My Music Player now Key features 1.) Supports various music file formats 2.) Not Supports playing music by categories such as Song, Artist, Album, Genre and Folder")
        super_main()
    elif(aaa==3):
        main()
        super_main()
    else:
        speak("Thankyou  So much for using My Music Player Created By Black Panther")
        exit
def song_name():
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
    print("Your Playlist is ...........\n\n")
    print(" 1.) Apna Time Aayega ")
    print(" 2.) Blue Eyes Yo Yo Honey Singh")
    print(" 3.) Bandook Chlegi Haryanvi Song " )
    print(" 4.) Bapu Zimidar")
    print(" 5.) Busy Busy Rahe raat bhar phone tera")
    print(" 6.) Chale Aana")
    print(" 7.) Cham Cham Cham ke Bandhe Haath ki ghadi Tanhai haryanvi")
    print(" 8.) Daru Badnaam kr di")
    print(" 9.) Dekhoon Tujhe To Pyaar Aaye")
    print("10.) Dil Mang Raha Hai Mohlat")
    print("11.) Ed Sheeran Shape of you")
    print("12.) EMIWAY GULLY KA KUTTA ")
    print("13.) EMIWAY HARD ")
    print("14.) EMIWAY MAALIK")
    print("15.) EMIWAY ROUND ONE")
    print("16.) Emiway bantai coronavirus")
    print("17.) EMIWAY BANTAI KHATAM")
    print("18.) EMIWAY MACHAYENGE")
    print("19.)  EMIWAY JUMP KAR")
    print("20.) EMIWAY SAMAJH MEIN AAYA KYA")
    print("21.)  Kuch Yesha Kr Kamaal Ki tera ho jau")
    print("22.) Gucci Payi Mayne Nai Rakhde Jassi_Gill ")
    print("23.) Guitar Sikhda Jassi_Gill")
    print("24.) Gulzaar Chhaniwala")
    print("25.) HapPy birthday to u shyam")
    print("26.) Har Dhaga Yahan Par Kacha hai")
    print("27.) Ikka")
    print("28.) Jab Bhi Teri Yaad")
    print("29.) Kalesh")
    print("30.) Yaar Naa Mile")
    print("31. ) Kisi Se Tum Pyar Karo")
    print("32.) Koi puche mere dil se keshe ye zahar piya ha")
    print("33.) Laung Be me Laachi")
    print("34.) Despacito")
    print("35.) Lungi Dance")
    print("36.) Mahiya Tu Vada kr kabbhi door na javega")
    print("37.) Main Barish Ka mausam hu mera itbaar na krna")
    print("38.) Geet Gau")
    print("39.) Mera tu hi ha bas yara")
    print("40.) Mere Mehboob Qayamat hogi")
    print("41.) Mera wala sardar")
    print("42.) Moto")
    print("43.) Naino ki jo baat naina jane ha")
    print("44.) Pachtaoge")
    print("45.) Prichay (Amit Badana")
    print("46.) Party With You Bhootnath")
    print("47.) Tum jaise Chutiyo ka sahara ha dosto")
    print("48.) Saturday saturday")
    print("49.) Taaron ke sahar")
    print("50.) Tera Fitoor jab se chad gya re")
    print("51.) Tum se jyada me na janu")
    print("52.) Ve mahi ve")
    print("53.) Mera tu hi ha bs yara")
    print("54.) Yaara teri yari ko mene to khuda mana")
    print("55.) Woh ladki nhi zindgi ha meri")
    print("56.) Dil kre chu che chu che cheeeeeee")
    print("57.) Chor Dinge")
    print("58.) Chacha Rap Part 2")
    print("59.) Baarish ki jaye")
    print("60.) Dil Tod ke hste ho mera")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
def main():
    a=input("\t\t\t\tEnter Song name ").lower()
    if "apna" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Apna Time Aayega.mp3")
        else:
            super_main()
        super_main()
    if "blue" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
                playsound("C:\\Users\\acer\\Music\\My Music\\Blue_Eyes_-_Yo_Yo_Honey_Singh_(PagalWorld.com)_.mp3")
        else:
            super_main()
        super_main()
    if "bandook" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Bandook.mp3")
        else:
            super_main()
        super_main()
    if "zimidar" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Bapu Zimidar.mp3")
        else:
            super_main()
        super_main()
    if "busy" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\BUSY_BUSY_RAHE_RAAT_BHAR_PHONE_TERA_song_in_korean_music(256k).mp3")
        else:
            super_main()
        super_main()
    if "aana" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\CHALE_AANA_FULL_SONG_WITH_LYRICS___De_De_Pyaar_De_I_Ajay_Devgn,_Tabu_l_Armaan_Malik,_Amaal_Mallik__(256k).mp3")
        else:
            super_main()
        super_main()
    if "cham" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Cham_Cham_Cham_ke_Bandhe_Haath_ki_ghadi_Tanhai(256k).mp3")
        else:
            super_main()
        super_main()
    if "daru" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\DARU_BADNAAM___One_Take___Tejas_Dhoke_Choreography___DanceFit_Live(256k).mp3")
        else:
            super_main()
        super_main()
    if "pyaar" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Dekhoon_Tujhe_To_Pyaar_Aaye___Apne(256k).mp3")
        else:
            super_main()
        super_main()
    if "mang" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Dil_Mang_Raha_Hai_Mohlat_Full_Video_Song_Yaseer_Desai,_Dil_Maang_Raha_Hai_Mohlat_Full_Song(256k).mp3")
        else:
            super_main()
        super_main()
    if "shape" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Ed_Sheeran___Shape_of_you_NEW_SONG_2017_Lyrics(256k).mp3")
        else:
            super_main()
        super_main()
    if "kutta" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\EMIWAY_-_GULLY_KA_KUTTA_(Prod_by_FLAMBOY)_(OFFICIAL_MUSIC_VIDEO)_(EXPLICIT)(256k).mp3")
        else:
            super_main()
        super_main()
    if "hard" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\EMIWAY_-_HARD_(PROD.HIPPY_JACK)_(OFFICIAL_MUSIC_VIDEO)(256k).mp3")
        else:
            super_main()
        super_main()
    if "maalik" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\EMIWAY_-_MAALIK_(PROD.FLAMBOY)_(OFFICIAL_ONE_TAKE_MUSIC_VIDEO)(256k).mp3")
        else:
            super_main()
        super_main()
    if "round" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\EMIWAY_-_ROUND_ONE_(OFFICIAL_MUSIC_VIDEO)(256k).mp3")
        else:
            super_main()
        super_main()
    if "virus" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Emiway_bantai_coronavirus_song(256k).mp3")
        else:
            super_main()
        super_main()
    if "khatam" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\EMIWAY_BANTAI-KHATAM_(OFFICIAL_MUSIC_VIDEO)(256k).mp3")
        else:
            super_main()
        super_main()
    if "machayenge" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\EMIWAY-_MACHAYENGE__(PROD_BY.TONY_JAMES)(256k).mp3")
        else:
            super_main()
        super_main()
    if "jump" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\EMIWAY-JUMP_KAR_(Prod_by.Flamboy)(256k).mp3")
        else:
            super_main()
        super_main()
    if "samajh" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\EMIWAY-SAMAJH_MEIN_AAYA_KYA__(OFFICIAL_MUSIC_VIDEO)(256k).mp3")
        else:
            super_main()
        super_main()
    if "kamaal" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Filhaal.mp3")
        else:
            super_main()
        super_main()
    if "gucci" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Gucci_Payi_Mayne_Nai_Rakhde___Jassi_Gill___Official_Video___Lastest_Punjabi_Songs___m_mazid_Khan(256k).mp3")
        else:
            super_main()
        super_main()
    if "gitar" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Guitar_Sikhda___Jassi_Gill___Jaani___B_Praak___Arvindr_Khaira___Lyrics___Latest_Punjabi_Song_2017(256k).mp3")
        else:
            super_main()
        super_main()
    if "gulzaar" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Gulzaar_Chhaniwala___Kasoote_2___Altu_Jalaltu_Bole_Na_Re_Faltu___Desi_Pubg___New_Haryanvi_Songs_2019(256k).mp3")
        else:
            super_main()
        super_main()
    if "birthday" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\HapPy_birthday_to_u_shyam_song___chota_lakhbir_singh_lakha(256k).mp3")
        else:
            super_main()
        super_main()
    if "dhaga" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Har_Dhaga_Yahan_Par_Kacha_hai(256k).mp3")
        else:
            super_main()
        super_main()
    if "ikka" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\ikka.mp3")
        else:
            super_main()
        super_main()
    if "yaad" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\I-SHOJ_-_Jab_Bhi_Teri_Yaad___Official_Music_Video_-_Jab_bhi_teri_yaad_aayegi(256k).mp3")
        else:
            super_main()
        super_main()
    if "kalesh" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Kalash_song_Milind_Gaba_and_Mika_Singh_and_Sandeep_Rathore_2018_ka_new_song(256k).mp3")
        else:
            super_main()
        super_main()
    if "mile" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Kick_-_Yaar_Naa_Miley_[SongsMp3.Com].mp3")
        else:
            super_main()
        super_main()
    if "kisi" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Kisi_Se_Tum_Pyar_Karo___Andaaz_Songs__Akshay_Kumar___Lara_Dutta__Johny_Lever__Aman_Verma__Gold_songs(256k).mp3")
        else:
            super_main()
        super_main()
    if "koi" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Koi_Puche_Mere_Dil_Se_Kaise_ye_Zahar_Piya_Hai___Very_Heart_Touching_Song_2018___Sahir_Ali_Bagga__(256k).mp3")
        else:
            super_main()
        super_main()
    if "laung" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Laung_Laachi_Title_Song__Mannat_Noor___Ammy_Virk,_Neeru_Bajwa,Amberdeep___Latest_Punjabi_Movie_2018(256k).mp3")
        else:
            super_main()
        super_main()
    if "despacito" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Luis_Fonsi_-_Despacito_ft._Daddy_Yankee(256k).mp3")
        else:
            super_main()
        super_main()
    if "lungi" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Lungi_Dance_-_Yo_Yo_Honey_Singh_[SongsMp3.Com].mp3")
        else:
            super_main()
        super_main()
    if "vada" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Mahiya_tu_Wada_Kar_Kabhi_Dur_na_javega_video(256k).mp3")
        else:
            super_main()
        super_main()
    if "mausam" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Main_Barish_ka_Mausam_Hu_Official_Song_Video___B_Praak_ft._Jaani___Kuch_bhi_ho_jaye(256k).mp3")
        else:
            super_main()
        super_main()
    if "geet" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Main_Koi_Aisa_Geet_Gaoon___Samne_Wali_Khidki_Mashup___ROOH_Unplugged___Retro.mp3")
        else:
            super_main()
        super_main()
    if "bas" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Mera_tu_hi_hai_bas_yaara__Tere_Yaar_bathere_ne__Mera_tu_hai_bas_yaara(256k).mp3")
        else:
            super_main()
        super_main()
    if "mehboob" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Mere_Mehboob_Qayamat_Hogi_-_Yo_Yo_Honey_Singh_(PagalWorld.com).mp3")
        else:
            super_main()
        super_main()
    if "sardar" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Mere_Wala_Sardar_(Full_Song)____Jugraj_Sandhu____New_Song_2018___New_Punjabi_Son.mp3")
        else:
            super_main()
        super_main()
    if "moto" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Moto___Haye_Re_Meri_Moto__Hi_Re_Meri_Motto__Ajay_Hooda_Diler_Kharkiya_Haryanvi_Song_2020_#Backoflove(256k).mp3")
        else:
            super_main()
        super_main()
    if "naino" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Naino_Ki_Jo_Baat_Naina_Jaane_hai_-_[Official_Video]__Romantic_Song_Ever__Mx_Musica(256k).mp3")
        else:
            super_main()
        super_main()
    if "pachtaoge" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Pachtaoge_Full_Video_Song___Arijit_Singh___Vicky_K_&_Nora_Fatehi___Jaani__B_Praak___Bada_Pachtaoge48(256k).mp3")
        else:
            super_main()
        super_main()
    if "prichay" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Parichay_-_Amit_Bhadana_(_Official_Music_Video_)___Ikka___Byg_Byrd__(256k).mp3")
        else:
            super_main()
        super_main()
    if "party" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Party_With_The_Bhoothnath_Song_(Official)___Bhoothnath_Returns___Amitabh_Bachchan,_Yo_Yo_Honey_Singh(256k).mp3")
        else:
            super_main()
        super_main()
    if "chutiyo" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Rajeev_Raja___Tum_Jaise_Chutiyo_Ka_Sahara_Hai_Dosto___Official___Yaro_Ne_Mere_Vaste___FRIENDS_ANTHEM(256k).mp3")
        else:
            super_main()
        super_main()
    if "saturday" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Saturday_Saturday_-_Indeep_Bakshi_feat_Badshah___Official_HD_Official_Song_Video(256k).mp3")
        else:
            super_main()
        super_main()
    if "sahar" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Taaron_cut.mp3")
        else:
            super_main()
        super_main()
    if "fitoor" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Tera_Fitoor.mp3")
        else:
            super_main()
        super_main()
    if "jyada" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\TUM_SE_JYADA_ME_NA_JANU__TUM_SE_KHUD_KO_PHCHANU_2019_new_sad_song._Viral_on_tik_Tok.https___youtu.be(256k).mp3")
        else:
            super_main()
        super_main()
    if "mahi" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Ve_Maahi___Kesari___Akshay_Kumar_&_Parineeti_Chopra___Arijit_Singh_&_Asees_Kaur___Tanishk_Bagchi(256k).mp3")
        else:
            super_main()
        super_main()
    if "mera tu hi " in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Yaar_Bathere_-_Yo_Yo_Honey_Singh_n_Alfaaz_(PagalWorld.com)_-_320Kbps.mp3")
        else:
            super_main()
        super_main()
    if "khuda" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Yaara_Teri_Yaari___Rahul_Jain___Pehchan_Music___Emotional_Friendship_Video_2018_(Lally's_Creation)(256k).mp3")
        else:
            super_main()
        super_main()
    if "ladki" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Woh_Ladki_Nahi_Zindagi_Hai_Meri_Cute_School_Love_Story(256k).mp3")
        else:
            super_main()
        super_main()
    if "chu" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Dil_Kare_Chu_Che_-_Full_Video___Singh_Is_Bliing___Akshay_Kumar_Amy_Jackson___Meet_Bros___Dance_Party(256k).mp3")
        else:
            super_main()
        super_main()
    if "chor" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Chhor_Denge_(LYRICS)_-_Nora_Fatehi___Parampara_Tandon___Sachet-Parampara___Ehan_Bhat___Arvindr_K(256k).mp3")
        else:
            super_main()
        super_main()
    if "chacha" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\CHACHA_RAP_PART_2____AMAN_KALAKAR____JHARKHAND_HINDI_RAP_SONG_2020(256k).mp3")
        else:
            super_main()
        super_main()
    if "baarish" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\Baarish_Ki_Jaaye___B_Praak_Ft_Nawazuddin_Siddiqui_&_Sunanda_Sharma___Jaani___Arvindr_Khaira___DM(256k).mp3")
        else:
            super_main()
        super_main()
    if "tod" in a:
        c=int(input("\t\t\t\tPress 1 for continue and 2 for exit : "))
        if(c==1):
            playsound("C:\\Users\\acer\\Music\\My Music\\B_Praak__Dil_Tod_Ke_Official_Song___Rochak_Kohli_,_Manoj_M__Abhishek_S,_Kaashish_V___Bhushan_Kumar(256k).mp3")
        else:
            super_main()
        super_main()
    else:
        print("\nPlease Enter Valid Option................\n")
        main()
super_main()


              
