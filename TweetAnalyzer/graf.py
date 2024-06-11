from HashTable import *
from Kullanici_Liste import *
class Node:
    def __init__(self, veri, sonraki=None):
        self.veri = veri
        self.komsular = BagliListe()
        self.sonraki= sonraki

    def ekle_komsu(self, node):
        self.komsular.ekle(node)

    def sil_komsu(self, node):
        self.komsular.sil(node)

    def get_veri(self):
        return self.veri


    def get_name(self):
        return self.veri.name





class BagliListe:
    def __init__(self):
        self.bas = None

    def ekle(self, veri):
        yeni_node = Node(veri)
        if not self.bas:
            self.bas = yeni_node
        else:
            aktif = self.bas
            while aktif.sonraki:
                aktif = aktif.sonraki
            aktif.sonraki = yeni_node

    def sil(self, veri):
        aktif = self.bas
        onceki = None
        while aktif:
            if aktif.veri == veri:
                if onceki:
                    onceki.sonraki = aktif.sonraki
                else:
                    self.bas = aktif.sonraki
                return True
            onceki = aktif
            aktif = aktif.sonraki
        return False

    def getir(self, index):
        aktif = self.bas
        count = 0
        while aktif:
            if count == index:
                return aktif.veri
            count += 1
            aktif = aktif.sonraki
        raise IndexError("Index bulunamadı.")

    def __iter__(self):
        aktif = self.bas
        while aktif:
            yield aktif.veri
            aktif = aktif.sonraki

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.getir(index)
        else:
            raise TypeError("Index türü desteklenmiyor.")

    def __setitem__(self, index, veri):
        yeni_node = Node(veri)
        if index == 0:
            yeni_node.sonraki = self.bas
            self.bas = yeni_node
        else:
            aktif = self.bas
            count = 0
            while aktif:
                if count == index - 1:
                    yeni_node.sonraki = aktif.sonraki
                    aktif.sonraki = yeni_node
                    return
                count += 1
                aktif = aktif.sonraki
            raise IndexError("Index bulunamadı.")

    def __delitem__(self, index):
        self.sil(self.getir(index))

    def goster(self):
        aktif = self.bas
        while aktif:
            print(aktif.veri)
            aktif = aktif.sonraki


class Graph:
    def __init__(self):
        self.nodes = BagliListe()

    def node_ekle(self, veri):
        yeni_node = Node(veri)
        self.nodes.ekle(yeni_node)
        return yeni_node

    def node_getir(self, veri):
        aktif = self.nodes.bas
        while aktif:
            if aktif.veri.veri == veri:
                return aktif.veri
            aktif = aktif.sonraki
        return None

    def edge_ekle(self, veri1, veri2):
        node1 = self.node_getir(veri1)
        node2 = self.node_getir(veri2)
        if node1 and node2:
            node1.ekle_komsu(node2)

    def edge_sil(self, veri1, veri2):
        node1 = self.node_getir(veri1)
        node2 = self.node_getir(veri2)
        if node1 and node2:
            node1.sil_komsu(node2)





    def kontrol(self, veri1, veri2):
        node1 = self.node_getir(veri1)
        node2 = self.node_getir(veri2)
        if node1 and node2:
            return node2 in node1.komsular
        return False







'''
# Örnek Kullanım
graf = Graph()



graf.node_ekle('A')
graf.node_ekle('B')
graf.node_ekle('C')
graf.node_ekle('D')


graf.edge_ekle('A', 'B')
graf.edge_ekle('B', 'C')
graf.edge_ekle('C', 'D')
graf.edge_ekle('D', 'A')


print(graf.kontrol('A', 'B'))  # True
print(graf.kontrol('B', 'D'))  # False


graf.edge_sil('A', 'B')
print(graf.kontrol('D', 'A')) 
'''


def kullanicilariiliskilendir(graf,nodelist):
    for node in nodelist:
        kullanici = node.get_veri()


        for takip_edilen_kullanici_adi in kullanici.following:
            j = 0
            for diger_node in nodelist:
                diger_kullanici = diger_node.get_veri()
                if diger_kullanici.username == takip_edilen_kullanici_adi and node != diger_node:

                    graf.edge_ekle(node.get_veri(), diger_node.get_veri())




        for takipci_kullanici_adi in kullanici.followers:
            for diger_node in nodelist:
                diger_kullanici = diger_node.get_veri()
                if diger_kullanici.username == takipci_kullanici_adi and node != diger_node:

                    graf.edge_ekle(diger_node.get_veri(), node.get_veri())


