import json
from Kullanici_Liste import *
from HashTable import *
from User import *
import networkx as nx
import matplotlib.pyplot as plt
def dosya_oku_ve_yazdir(dosya_yolu):

    bagli_liste = BagliListe()
    json_veri=BagliListe()
    try:
        with open(dosya_yolu, 'r', encoding='utf-8') as dosya:

            json_veri = json.load(dosya)



            for eleman in json_veri:
                bagli_liste.ekle(eleman)


        return bagli_liste






    except FileNotFoundError:
        print("Dosya bulunamadı. Lütfen dosya yolunu kontrol edin.")

    except json.JSONDecodeError:
        print("JSON formatında bir hata var. Dosya geçerli bir JSON dosyası olmayabilir.")





def liste_olustur(veri_listesi):

    kullanicilistesi=BagliListe()
    hashtable=HashTable()


    i=0


    for hashtable in veri_listesi:







        kullanici = User(
            hashtable.get('username'),
            hashtable.get('name'),
            hashtable.get('followers_count'),
            hashtable.get('following_count'),
            hashtable.get('language'),
            hashtable.get('region'),
            hashtable.get('tweets'),
            hashtable.get('following'),


            hashtable.get('followers')
        )

        tweet_list = hashtable.get('tweets')
        tweet_linked_list = BagliListe()


        for tweet in tweet_list:
            tweet_linked_list.ekle(tweet)


        kullanici.tweets = tweet_linked_list








        following_list = hashtable.get('following')
        following_linked_list = BagliListe()


        for following in following_list:
            following_linked_list.ekle(following)


        kullanici.following = following_linked_list





        followers_list = hashtable.get('followers')
        followers_linked_list = BagliListe()
        for followers in followers_list:
            followers_linked_list.ekle(followers)

        kullanici.followers = followers_linked_list




        kullanicilistesi.ekle(kullanici)

        i+=1

        if i==10000:
            break














    return kullanicilistesi






def kullanicihasholustur(b_liste):

    hashtb=HashTable()

    for z in b_liste:
        hashtb.set(z.username,z)

    return hashtb


import networkx as nx
import matplotlib.pyplot as plt

def takipci_graf_ciz(kullanici_hash, username):
    graf = nx.DiGraph()


    takipciler = kullanici_hash.get(username).followers
    for takipci in takipciler:
        graf.add_edge(takipci, username)



    node_sizes = {node: 20000 if node == username  else 300 for node in graf.nodes()}



    plt.figure(figsize=(15, 10))
    pos = nx.spring_layout(graf)
    nx.draw(
        graf,
        pos,
        with_labels=True,
        node_size=[node_sizes[node] for node in graf.nodes()],
        node_color='skyblue',
        font_size=8,
        font_weight='bold',
        arrows=True
    )
    plt.title(f'{username} Kullanıcısının Takipçi-Takip Grafiği')
    plt.show()


def takip_edilen_graf_ciz(kullanici_hash, username):
    graf = nx.DiGraph()



    takip_edilenler = kullanici_hash.get(username).following
    for takip_edilen in takip_edilenler:
        graf.add_edge(username, takip_edilen)


    node_sizes = {node: 20000 if node == username else 300 for node in graf.nodes()}

    plt.figure(figsize=(15, 10))
    pos = nx.spring_layout(graf)
    nx.draw(
        graf,
        pos,
        with_labels=True,
        node_size=[node_sizes[node] for node in graf.nodes()],
        node_color='skyblue',
        font_size=8,
        font_weight='bold',
        arrows=True
    )
    plt.title(f'{username} Kullanıcısının Takipçi-Takip Grafiği')
    plt.show()
