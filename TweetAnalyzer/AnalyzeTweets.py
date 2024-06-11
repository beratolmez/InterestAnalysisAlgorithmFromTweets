import nltk
from collections import Counter
from nltk.corpus import stopwords
from Kullanici_Liste import *
from HashTable import  *

def analyze_tweets(tweet_list):

    stop_words = set(stopwords.words('turkish'))

    new_stopwords = ["oldu", "ayrıca", "sonra", "bir", "iki", "tarafından", "yer", "büyük", "olarak", "vardır", "olan",
                     "birçok", "aynı", "ilk", "ancak"]

    stop_words.update(new_stopwords)


    all_tweets = " ".join(tweet_list)

    words = nltk.word_tokenize(all_tweets)


    filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word.isalpha()]



    sports_keywords = ["spor", "futbol", "basketbol", "tenis", "voleybol", "yüzme","dağcılık",
                       "koşu", "bisiklet", "macera sporları"]
    art_keywords = ["sanat", "resim", "heykel", "müze", "grafik tasarım", "sinema","tiyatro"]
    music_keywords = ["müzik", "konser", "şarkı", "albüm", "rock", "jazz","şarkı"]
    tech_keywords = ["teknoloji", "programlama", "yazılım", "donanım", "yapay zeka", "veri bilimi"]
    travel_keywords = ["seyahat", "gezi", "tatil", "doğa", "şehir turu", "kamp"]
    film_keywords= ["film", "dizi", "sinema", "televizyon", "vizyon", "senaryo"]
    yemek_keywords=["yemek", "mutfak", "lezzet", "gastronomi", "şef", "restoran"]
    tarih_keywords=["tarih", "arkeoloji", "antik", "savaş tarihi", "medeniyetler", "tarihi eserler","roma"]
    saglikli_yasam_keywords=["sağlık", "fitness", "beslenme", "sağlıklı yaşam", "egzersiz", "ruh sağlığı"]
    evcil_hayvanlar_keywords=["evcil hayvanlar", "köpek", "kedi", "papağan", "hayvan davranışları"]
    doga_koruma_keywords=["geri dönüşüm", "çevre bilinci", "iklim değişikliği", "biyoçeşitlilik", "doğa koruma",
                          "ekoloji", "ozon tabakası", "ormanlar", "su kaynakları", "biyolojik denge", "çevre kirliliği","buzullar","çevre"]
    user_interests = set()


    for word in filtered_words:
        if word in sports_keywords:
            user_interests.add("Spor")
        elif word in art_keywords:
            user_interests.add("Sanat")
        elif word in music_keywords:
            user_interests.add("Müzik")
        elif word in tech_keywords:
            user_interests.add("Teknoloji")
        elif word in travel_keywords:
            user_interests.add("Seyahat")
        elif word in film_keywords:
            user_interests.add("Film")
        elif word in yemek_keywords:
            user_interests.add("Yemek")
        elif word in tarih_keywords:
            user_interests.add("Tarih")
        elif word in saglikli_yasam_keywords:
            user_interests.add("Saglikli Yasam")
        elif word in evcil_hayvanlar_keywords:
            user_interests.add("Evcil Hayvanlar")
        elif word in doga_koruma_keywords:
            user_interests.add("Doğa Koruma")
    return user_interests


def find_common_interests(users):
    common_interest_list = []

    for i, user1 in enumerate(users):
        for j, user2 in enumerate(users):
            if i != j:
                 for interest in user1.interests.keys():
                    users1 = user1.interests.get(interest, BagliListe())
                    users2 = user2.interests.get(interest, BagliListe())
                    if users1 and users2:
                        common_interest_list.append((user1, user2, interest, users1, users2))

    return common_interest_list





def ortak_ilgi_alanlari_bul(kullanici_listesi, konum):
    ilgi_alanlari = HashTable()


    for kullanici in kullanici_listesi:
        if kullanici.region == konum:
            for ilgi in kullanici.ilgialan:
                if kullanici.username not in ilgi_alanlari:
                    ilgi_alanlari[kullanici.username] = BagliListe()
                ilgi_alanlari[kullanici.username].ekle(ilgi)


    ortak_ilgi_alanlari = HashTable()
    for kullanici in ilgi_alanlari:
        ortaklar = BagliListe()
        for ilgi in ilgi_alanlari[kullanici]:
            count = 0
            for diger_kullanici in ilgi_alanlari:
                if kullanici != diger_kullanici and ilgi in ilgi_alanlari[diger_kullanici]:
                    count += 1
            if count == len(ilgi_alanlari) - 1:
                ortaklar.ekle(ilgi)
        ortak_ilgi_alanlari[kullanici] = ortaklar

    dosyayolu = r"C:\Users\Sait Omer\Desktop\aynibolgeilgialani.txt"

    with open(dosyayolu, 'w') as dosya:
        dosya.write(f"Aranan Bölge={konum}\n")
        for kullanici, ortak_ilgi_alanlari_listesi in ortak_ilgi_alanlari.items():
            dosya.write(f"{kullanici}'nin ortak ilgi alanları:\n")
            for ilgi in ortak_ilgi_alanlari_listesi:
                dosya.write(f"- {ilgi}\n")

            dosya.write("\n")





    return ortak_ilgi_alanlari



def verilen_ilgi_alanini_bul(users,interest):
    dosyayolu = r"C:\Users\Sait Omer\Desktop\verilenilgialani.txt"

    with open(dosyayolu, 'w') as dosya:
        dosya.write(f"{interest} ilgi alanına sahip kullanıcıların isimleri aşağıdadır\n")

        eslesen_kullanicilar = BagliListe()
        for user in users:
            for twet in user.tweets:
                if interest in twet:
                    eslesen_kullanicilar.ekle(user)
                    dosya.write(f"{user.username}\n")



        return eslesen_kullanicilar

def dfs_keywords_hashtags(user, keywords, hashtags, visited, result):
    if user in visited:
        return
    visited.add(user)

    for tweet in user.tweets:
        tweet_lower = tweet.lower()
        if any(keyword in tweet_lower for keyword in keywords) or any(f"#{tag}" in tweet_lower for tag in hashtags):
            result.append((user, tweet))

    for follower in user.followers:
        dfs_keywords_hashtags(follower, keywords, hashtags, visited, result)


from collections import deque
import heapq

def bfs_interests_similarity(user1, user2, threshold=0.5):
    queue = deque([(user1, 0)])

    while queue:
        current_user, depth = queue.popleft()

        if current_user == user2:
            return depth

        for follower in current_user.followers:

            interests_user1 = set(user1.get_interests())
            interests_user2 = set(user2.get_interests())
            similarity = len(interests_user1.intersection(interests_user2)) / len(interests_user1.union(interests_user2))

            if similarity >= threshold:
                queue.append((follower, depth + 1))

    return -1

def minimum_spanning_tree(users):
    edges = []

    for i, user1 in enumerate(users):
        for j, user2 in enumerate(users):
            if i != j:

                interests_user1 = set(user1.get_interests())
                interests_user2 = set(user2.get_interests())
                similarity = len(interests_user1.intersection(interests_user2)) / len(interests_user1.union(interests_user2))

                edges.append((i, j, similarity))


    mst = []
    edges.sort(key=lambda x: x[2])
    parent = list(range(len(users)))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        parent[root_x] = root_y

    for edge in edges:
        u, v, weight = edge
        if find(u) != find(v):
            mst.append((users[u], users[v], weight))
            union(u, v)

    return mst




def ortak_ilgi_alan(kullanici_listesi):
    ilgi_alanlari = {}


    for kullanici in kullanici_listesi:
        for ilgi in kullanici.ilgialan:
            if ilgi not in ilgi_alanlari:
                ilgi_alanlari[ilgi] = []
            ilgi_alanlari[ilgi].append(kullanici)


    ortak_ilgi_kullanicilari = []
    for ilgi, kullanicilar in ilgi_alanlari.items():
        if len(kullanicilar) > 1:
            ortak_ilgi_kullanicilari.append([ilgi, kullanicilar])

    dosyayolu = r"C:\Users\Sait Omer\Desktop\ayniilgialani.txt"

    with open(dosyayolu, 'w') as dosya:
        for ilgi, kullanicilar in ortak_ilgi_kullanicilari:
            dosya.write(f"\nIlgi Alanı: {ilgi}\n")
            dosya.write("Kullanıcılar:\n")
            for kullanici in kullanicilar:
                dosya.write(f"{kullanici.username}\n")

    return ortak_ilgi_kullanicilari


