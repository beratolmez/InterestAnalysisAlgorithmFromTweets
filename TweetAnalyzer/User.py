from Kullanici_Liste import *
from HashTable import *
from Kuyruk import Queue
from Stack import Stack
class User:



    def __init__(self, username, name, followers_count, following_count, language, region,tweets,following,followers):
        self.username = username
        self.name = name
        self.followers_count = followers_count
        self.following_count = following_count
        self.language = language
        self.region = region
        self.tweets = tweets
        self.following = following
        self.followers = followers

        self.interests = HashTable()

        self.ilgialan=BagliListe()
        self.takip_edenler = BagliListe()
        self.takip_edilenler = BagliListe()



    def add_interest(self, interest):
        if interest not in self.interests:
            self.interests.set(interest, BagliListe())
        self.interests.get(interest).ekle(self)

    def get_interests(self):
        return self.interests

    def kelime_ayir(self,cumle):
        kelime = ""
        kelimeler = BagliListe()
        for karakter in cumle:

            if karakter != " ":
                kelime += karakter
            else:
                kelimeler.ekle(kelime)
                kelime = ""
        if kelime:
            kelimeler.ekle(kelime)
        return kelimeler

    def frekansHesapla(self,cumleListesi):
        frekanslar =HashTable()
        for cumle in cumleListesi:
            kelimeler = self.kelime_ayir(cumle)
            for kelime in kelimeler:
                if kelime in frekanslar:
                    frekanslar[kelime] += 1
                else:
                    frekanslar[kelime] = 1
        return frekanslar




def ortak_takipci_sayisi_bfs(graf, baslangic_dugumu):
    ortak_takipci_sayisi=BagliListe()
    ziyaret_edildi = BagliListe()
    kuyruk = Queue()
    kuyruk.enqueue(baslangic_dugumu)
    ziyaret_edildi.ekle(baslangic_dugumu)
    ortak_takipci_sayisi.ekle(baslangic_dugumu.get_veri())
    takipcisayisi=int(baslangic_dugumu.get_veri().followers_count)

    while not kuyruk.is_empty():
        aktif_dugum = kuyruk.dequeue()
        #print(aktif_dugum.get_veri().username)
        print(aktif_dugum.get_veri().username)

        for komsu in graf.node_getir(aktif_dugum.get_veri()).komsular:
            if komsu not in ziyaret_edildi:
                kuyruk.enqueue(komsu)

                ziyaret_edildi.ekle(komsu)

                if takipcisayisi==int(komsu.get_veri().followers_count):
                    ortak_takipci_sayisi.ekle(komsu.get_veri())



    dosyayolu=r"C:\Users\Sait Omer\Desktop\ortaktakipcisayilari.txt"

    with open(dosyayolu, 'w') as dosya:

        for kullanicilar in ortak_takipci_sayisi:
            dosya.write(kullanicilar.username)
            dosya.write("\n")

    return ortak_takipci_sayisi





def ortak_dil_dfs(graf,baslangic_dugumu):
    ziyaret_edilen = BagliListe()
    stack = Stack()
    stack.push(baslangic_dugumu)
    ortak_dil=BagliListe()
    ortak_dil.ekle(baslangic_dugumu.get_veri())
    while len(stack) > 0:
        current_node = stack.pop()
        if current_node not in ziyaret_edilen:

            ziyaret_edilen.ekle(current_node)





            for komsu in graf.node_getir(current_node.get_veri()).komsular:


                if komsu not in ziyaret_edilen:
                    stack.push(komsu)

                    if komsu.get_veri().language == baslangic_dugumu.get_veri().language and komsu.get_veri() not in ortak_dil:
                        ortak_dil.ekle(komsu.get_veri())

    dosyayolu = r"C:\Users\Sait Omer\Desktop\ortakdil.txt"

    with open(dosyayolu, 'w') as dosya:

        for kullanicilar in ortak_dil:
            dosya.write(kullanicilar.username)
            dosya.write("\n")



    return ortak_dil


def ilgi_alani_txt(kullanicilist):
    i=0
    dosyayolu = r"C:\Users\Sait Omer\Desktop\kullaniciilgialani.txt"

    with open(dosyayolu, 'w') as dosya:

        for kullanici in kullanicilist:

            dosya.write(f"\n{kullanici.username} isimli kullanicinin ilgi alanları=\n")

            for ilgi in kullanici.ilgialan:

                dosya.write(f"-{ilgi}\n")



def dfs_tweet_ilgialani(graf,baslangic_dugumu):

    keywords = {
        "Spor": ["spor", "futbol", "basketbol", "tenis", "voleybol", "yüzme", "dağcılık",
                   "koşu", "bisiklet", "macera sporları"],
        "Sanat": ["sanat", "resim", "heykel", "müze", "grafik tasarım", "sinema", "tiyatro"],
        "Müzik": ["müzik", "konser", "şarkı", "albüm", "rock", "jazz", "şarkı"],
        "Teknoloji": ["teknoloji", "programlama", "yazılım", "donanım", "yapay zeka", "veri bilimi"],
        "Seyahat": ["seyahat", "gezi", "tatil", "doğa", "şehir turu", "kamp"],
        "Film": ["film", "dizi", "sinema", "televizyon", "vizyon", "senaryo"],
        "Yemek": ["yemek", "mutfak", "lezzet", "gastronomi", "şef", "restoran"],
        "Tarih": ["tarih", "arkeoloji", "antik", "savaş tarihi", "medeniyetler", "tarihi eserler", "roma"],
        "Sağlıklı Yaşam": ["sağlık", "fitness", "beslenme", "sağlıklı yaşam", "egzersiz", "ruh sağlığı"],
        "Evcil Hayvanlar": ["evcil hayvanlar", "köpek", "kedi", "papağan", "hayvan davranışları"],
        "Çevre": ["geri dönüşüm", "çevre bilinci", "iklim değişikliği", "biyoçeşitlilik", "doğa koruma",
                        "ekoloji", "ozon tabakası", "ormanlar", "su kaynakları", "biyolojik denge", "çevre kirliliği",
                        "buzullar", "çevre"],
        "Astronomi": ["astronomi", "yıldız", "gök cismi", "gök bilimi", "uzay", "meteor", "galaksi", "astronot"],
        "Biyoloji": ["biyoloji", "hücre", "genetik", "DNA", "canlılar", "biyoteknoloji"]
    }

    dosyayolu = r"C:\Users\Sait Omer\Desktop\ilgialanisecilentweetler.txt"

    with open(dosyayolu, 'w') as dosya:
        ziyaret_edilen = set()
        stack = Stack()
        stack.push(baslangic_dugumu)

        while len(stack) > 0:
            current_node = stack.pop()
            if current_node not in ziyaret_edilen:
                ziyaret_edilen.add(current_node)


                for category, words in keywords.items():
                    tweet_yazildi = False
                    for word in words:
                        for tw in current_node.get_veri().tweets:
                            if word in tw:
                                if not tweet_yazildi:
                                    dosya.write(f"\n{current_node.get_veri().username}  {category}    {tw}")
                                    tweet_yazildi = True
                                    break


                for komsu in graf.node_getir(current_node.get_veri()).komsular:
                    if komsu not in ziyaret_edilen:
                        stack.push(komsu)








    