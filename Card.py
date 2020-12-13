#!/usr/bin/env python
# coding: utf-8

# カードゲーム「戦争」のサンプルコード
# 
# （ルール）
# 1. カードの強さは左から順に「1, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2」で強い
# 2. マークの強さは左から順に「スペード, ハート, ダイヤ, クローバー」で強い
# 3. カードを1枚出し合い、数の大きいカードを出した方が勝ち
# 4. 勝った方が場に出たカードをもらえる
# 5. 手札がなくなるまで3~4を行い、取ったカードの枚数が多いほうを勝者とする

# コード概要
# 
# marks : カードのマーク（スペード、ハート、ダイヤ、クローバー）を表す<br>
# values : カードの数字を表す
# 
# （例）<br>
# ハートの２→Card(2, 1)  <br>
# クローバーのJack →Card(11,3)
# 
# 
# 特殊メソッド ＿＿lt＿＿, ＿＿gt＿＿<br>
# Cardオブジェクトの大小比較を可能にするメソッド<br>
# 数字が同じ場合は、マークで大小比較を行う
# 
# 
# 特殊メソッドは以下を参照<br>
# https://docs.python.org/ja/3/library/operator.html
# 

# In[3]:


class Card:
    # カードのマークを表す
    marks = ["spades", "hearts", "diamonds", "clubs"]
    # カードの値を表す
    # 値とインデックスが一致するように頭2つにNoneを格納
    values =[None, None,
             "2", "3", "4", "5", "6", "7", "8", "9",
             "10", "Jack", "Queen", "King", "Ace"]
    
    def __init__(self, v, m):
        self.value = v
        self.mark = m
        
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.mark < c2.mark:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.mark > c2.mark:
                return True
            else :
                return False
        return False
    
    # __reprをオーバーライド
    # これによってprint()関数でオブジェクトを渡したとき、returnの値が表示される
    # 記述がない場
    def __repr__(self):
        v = self.values[self.value] + " of " + self.marks[self.mark]
        return v
    
if __name__ == '__main__':
    Card


# In[1]:


# # ダイヤの10 と クローバーのJack
# card1 = Card(10, 2)
# card2 = Card(11, 3)
# print(card1 < card2)
# print(card1 > card2)

# print()

# # スペートの4 と スペードのJack
# card1 = Card(4, 0)
# card2 = Card(11, 0)
# print(card1 < card2)
# print(card1 > card2)

# print()

# # カード情報を出力
# print(card1)
# print(str(card1))
# print(repr(card1))

