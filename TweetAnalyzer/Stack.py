
from Kullanici_Liste import *
class Stack:
    def __init__(self):
        self.bas = None

    def push(self, veri):
        yeni_node = Node(veri)
        yeni_node.sonraki = self.bas
        self.bas = yeni_node

    def pop(self):
        if not self.bas:
            raise IndexError("Stack boş.")
        cikarilan = self.bas
        self.bas = self.bas.sonraki
        return cikarilan.veri

    def peek(self):
        if not self.bas:
            raise IndexError("Stack boş.")
        return self.bas.veri

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
