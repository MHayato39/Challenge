#!/usr/bin/env python
# coding: utf-8

# In[1]:


# プレイヤーを表すクラス
class Player:
    def __init__(self, name):
        self.wins = 0 # ゲームで何回勝ったか
        self.card = None # プレイヤーが持っているカード
        self.name = name # プレイヤーの名前
        
if __name__ == '__main__':
    Player

