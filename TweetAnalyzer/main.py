from HashTable import *
from Kullanici_Liste import *
from User import *
from okujson import *
import networkx as nx
import matplotlib.pyplot as plt
from graf import *
from Kuyruk import Queue
from Stack import Stack
from AnalyzeTweets import *


dosya_yolu = r'C:\Users\Sait Omer\Desktop\twitter_data.json'

kullaniciL=BagliListe()
kullaniciL=dosya_oku_ve_yazdir(dosya_yolu)
kullaniciListesi=BagliListe()
kullaniciListesi=liste_olustur(kullaniciL)
kullaniciHash=HashTable()
kullaniciHash=kullanicihasholustur(kullaniciListesi)

graf = Graph()
nodelist=BagliListe()

for kullanici in kullaniciListesi:
    node=graf.node_ekle(kullanici)
    nodelist.ekle(node)


kullanicilariiliskilendir(graf, nodelist)

def takip_takipci_iliskilerini_txtye_yaz(graf, dosya_yolu):
    with open(dosya_yolu, 'w') as dosya:
        for node in graf.nodes:
            kullanici = node.get_veri()
            dosya.write(f"Kullanıcı: {kullanici.username}\n")

            dosya.write("Takip Ettikleri:\n")
            for takip_edilen_node in kullanici.following:

                dosya.write(f"- {takip_edilen_node}\n")
            dosya.write("--------------------------------------\n")
            dosya.write("Takipçileri:\n")
            for takipci_node in kullanici.followers:

                dosya.write(f"- {takipci_node}\n")

            dosya.write("\n")
            dosya.write("**************************************\n")
            dosya.write("\n")
    print(f"İlişkiler {dosya_yolu} dosyasına yazıldı.")

takip_takipci_iliskilerini_txtye_yaz(graf,r'C:\Users\Sait Omer\Desktop\takip_takipci.txt')

#son 2 ister
y=ortak_takipci_sayisi_bfs(graf,graf.node_getir(nodelist.getir(0).get_veri()))
#***************
all_tweets = []

for kullanici in kullaniciListesi:

    user_tweets = kullanici.tweets

    for tweet in user_tweets:
        all_tweets.append(tweet)

for kullanici in kullaniciListesi:
    ilgi_alanlari = analyze_tweets(kullanici.tweets)
    for ilgi_alani in ilgi_alanlari:
        kullanici.add_interest(ilgi_alani)
        kullanici.ilgialan.ekle(ilgi_alani)
for kullanici in kullaniciListesi:
    print(f"{kullanici.name} (@{kullanici.username}) - İlgi Alanları: {list(kullanici.interests)}")


ortak_ilgi_alanlari = ortak_ilgi_alanlari_bul(kullaniciListesi, "TR")

for kullanici, ortak_ilgi_alanlari_listesi in ortak_ilgi_alanlari.items():
    print(f"{kullanici}'nin ortak ilgi alanları:")
    for ilgi in ortak_ilgi_alanlari_listesi:
        print(f"- {ilgi}")

    print()

op = verilen_ilgi_alanini_bul(kullaniciListesi, "Asker")
print(op.getir(1).username)

takipci_graf_ciz(kullaniciHash, kullaniciListesi.getir(0).username)
takip_edilen_graf_ciz(kullaniciHash, kullaniciListesi.getir(0).username)





takip_takipci_iliskilerini_txtye_yaz(graf,r'C:\Users\Sait Omer\Desktop\takip_takipci.txt')






#son 2 ister
y=ortak_takipci_sayisi_bfs(graf,graf.node_getir(nodelist.getir(0).get_veri()))





#nodelist.getir(1).get_veri().language="ho"
#nodelist.getir(2).get_veri().language="ho"
xx = ortak_dil_dfs(graf,graf.node_getir(nodelist.getir(0).get_veri()))

verilen_ilgi_alanini_bul(kullaniciListesi,"Asker")
ilgi_alani_txt(kullaniciListesi)


ortak_ilgi_alan(kullaniciListesi)



#print(nodelist.getir(0).get_veri().ilgialan.getir(0))


dfs_tweet_ilgialani(graf,graf.node_getir(nodelist.getir(0).get_veri()))










"""

keywords_to_search = ["python", "coding"]
hashtags_to_search = ["datascience", "machinelearning"]

result_dfs_keywords_hashtags = []
for user in kullaniciListesi:
    dfs_keywords_hashtags(user, keywords_to_search, hashtags_to_search, set(), result_dfs_keywords_hashtags)


for user, tweet in result_dfs_keywords_hashtags:
    print(f"{user.name} ({user.username}): {tweet}")


user1 = kullaniciListesi[0]
user2 = kullaniciListesi[1]

common_interest_users = []
for user in kullaniciListesi:
    if user != user1 and user != user2:
        similarity = bfs_interests_similarity(user1, user)
        if similarity != -1:
            common_interest_users.append((user, similarity))


for user, similarity in common_interest_users:
    print(f"{user1.name} ve {user.name} arasında benzer ilgi alanına sahip. Benzerlik derecesi: {similarity}")


mst_edges = minimum_spanning_tree(kullaniciListesi)
for user1, user2, weight in mst_edges:
    print(f"{user1.name} - {user2.name}: Benzerlik derecesi: {weight}")
    
"""
