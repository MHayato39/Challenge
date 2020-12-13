#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import shuffle


# In[2]:


class Card:
    # カードのマークを表す
    marks = {0:"spades", 1:"hearts", 2:"diamonds", 3:"clubs"}
    # カードの値を表す
    # 値とインデックスが一致するように頭2つにNoneを格納（有効なインデックス：2~14）
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
    


# In[3]:


class Deck:
    # 52枚のカードのデッキを作成
    def __init__(self):
        self.cards = []
        for i in range(2, 15): # Cardのvaluesに対応
            for j in range(4): # Cardのmarksに対応
                self.cards.append((Card.values[i], Card.marks[j]))
        shuffle(self.cards) # デッキをシャッフルする
        
    # 手札を出す
    def rm_card(self):
        if len(self.cards) == 0:  # 手札が０の場合はNoneを返す
            return 
        return self.cards.pop()  # 手札を1枚出す
        


# In[4]:


# プレイヤーを表すクラス
class Player:
    def __init__(self, name):
        self.wins = 0 # ゲームで何回勝ったか
        self.card = None # プレイヤーが持っているカード
        self.name = name # プレイヤーの名前


# In[11]:


# ゲーム本体のクラス
class Game:
    def __init__(self):
        name1 = input("プレイヤー１の名前")
        name2 = input("プレイヤー２の名前")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        
    def wins(self, winner):
        w = "このラウンドは {} が勝ちました"
        w = w.format(winner)
        print(w)
        print()
        
    def draw(self, p1n, p1c, p2n, p2c):
        # p1n, p2n : プレイヤー1, 2の名前
        # p1c, p2c : プレイヤー1, 2のカード
        d = "{} は {}, {} は {} を引きました"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)
        
    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます")
        while len(cards) >= 2:
            m = "q で終了, それ以外のキーでPlay"
            response = input(m)
                             
            if self.p1.wins==0 and self.p2.wins==0 and response == 'q': # ゲームを1回も実行しないで終了
                print("終了しました")
                return 
            if response == 'q': # ゲームを途中で終了
                break;
                
            p1c = self.deck.rm_card() # カードを出す
            p2c = self.deck.rm_card() # カードを出す
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
                
        print()
        win = self.winner(self.p1, self.p2)
        print(p1n, self.p1.wins, " : ", p2n, self.p2.wins)
    
        if self.p1.wins == 0 and self.p2.wins == 0:
            print("ゲーム終了")
        elif self.p1.wins == self.p2.wins:
            print("ゲーム終了, {} です".format(win))
        else:
            print("ゲーム終了, {} の勝利です".format(win))
        
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p1.wins < p2.wins:
            return p2.name
        return "引き分け"


# In[15]:


game = Game()


# In[16]:


game.play_game()

