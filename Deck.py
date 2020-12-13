#!/usr/bin/env python
# coding: utf-8

# In[2]:


from random import shuffle # リストをシャッフルする


# In[80]:


class Deck:
    # 52枚のカードのデッキを作成
    def __init__(self):
        self.cards = []
        for i in range(2, 15): # Cardのvaluesに対応
            for j in range(4): # Cardのmarksに対応
                self.cards.append((i, j))
        shuffle(self.cards) # デッキをシャッフルする
        
    # 手札を出す
    def rm_card(self):
        if len(self.cards) == 0:  # 手札が０の場合はNoneを返す
            return 
        print(self.cards.pop())  # 手札を1枚出す
        
if __name__ == '__main__':
    Deck


# In[78]:


# deck = Deck()
# deck.cards


# In[79]:


deck.rm_card

