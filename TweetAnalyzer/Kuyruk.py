from Kullanici_Liste import *

class Queue:
    def __init__(self):
        self.bagli_liste = BagliListe()

    def enqueue(self, veri):
        self.bagli_liste.ekle(veri)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Kuyruk boş.")
        else:
            veri = self.bagli_liste.getir(0)
            del self.bagli_liste[0]
            return veri

    def peek(self):
        if self.is_empty():
            raise IndexError("Kuyruk boş.")
        else:
            return self.bagli_liste.getir(0)



    def is_empty(self):
        return len(self.bagli_liste) == 0

    def size(self):
        return len(self.bagli_liste)




