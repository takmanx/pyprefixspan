# -*- coding: utf-8 -*-
import re

class pyprefixspan:
    # init
    def __init__(self, pattern, minsup=2, len=1):
        self.minsup = minsup
        self.seq = pattern
        self.len = len
        self.out = {}

    def setlen(self, len=1):
        self.len = len
        print(self)

    def setminsup(self, minsup=2):
        self.minsup = minsup
        print(self)

    def extract(self, minsup, seq):
        h = dict()
        for i, item in enumerate(seq):
            dist = re.split(' +', item)
            for j in dist:
                if j in h:
                    h[j] += 1
                else:
                    h[j] = 1
        for k in list(h):
            # minsup
            if h[k] < minsup:
                del h[k]
        return h

    def projection(self, seq, b):
        h = []
        for i, item in enumerate(seq):
            list = re.split(' +', item)
            if b in list:
                dist = list[list.index(b)+1:]
                if len(dist) > 0:
                    h.append(" ".join(dist))
        return h

    def _prefixspan(self, prefix, seq):
        minsup = self.minsup;

        pattern = self.extract(minsup, seq)
        for key, value in pattern.items():
            p = prefix + " " + key

            count = len(re.findall(' +', p))
            # length
            if count >= self.len:
                p = p.strip()
                self.out.update({p:value})
#                print('  ==out ', p, value)
            j = self.projection(seq, key)
            self._prefixspan(p, j);
        return

    def run(self):
        self._prefixspan("", self.seq)
        return

    def out(self, str):
        print(str)        


 
