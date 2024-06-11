class Node:
    def __init__(self, veri):
        self.veri = veri
        self.sonraki = None


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

    def __len__(self):
        count = 0
        aktif = self.bas
        while aktif:
            count += 1
            aktif = aktif.sonraki
        return count


    def goster(self):
        aktif = self.bas
        while aktif:
            print(aktif.veri)
            aktif = aktif.sonraki





