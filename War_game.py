# カードを表すクラス

class Card:
  suits = ["spades", "hearts", "diamonds", "clubs"]

  # 最初の２つをNoneにしてるのは、インデックス番号を2の時に２と合わせるため！！
  values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

  def __init__(self, v, s):
    """スート（マーク）も値も整数値です"""
    self.value = v
    self.suit = s

  # __lt__はLessThan（未満）の特殊メソッド！
  def __lt__(self, c2):
    if self.value < c2.value:
      return True
    if self.value == c2.value:
      if self.suit < c2.suit:
        return True
      else:
        return False
    return False

  # __gt__はGreaterThan（より大きい）の特殊メソッド！
  def __gt__(self, c2):
    if self.value > c2.value:
      return True
    if self.value == c2.value:
      if self.suit > c2.suit:
        return True
      else:
        return False
    return False

  def __repr__(self):
    v = self.values[self.value] + " of "\
      + self.suits[self.suit]
    return v


# デッキを表すクラス

from random import shuffle

class Deck:
  def __init__(self):
    self.cards = []
    # 2から15なのは、カードが２からAce（インデックス番号14）まであるから！
    for i in range(2, 15):
      # suit（マーク）が４種類（インデックス番号0,1,2,3）だから０から４まで！
      for j in range(4):
        # for文で繰り返し、それをself.cardsに代入することで、52枚のカードが用意できる！
        self.cards.append(Card(i, j))
    # カードをシャッフルする！
    shuffle(self.cards)

  def rm_card(self):
    if len(self.cards) == 0:
      return
    # popメソッドは、リストの要素を削除する！（カードの数が０以外の時は１枚削除する！）
    return self.cards.pop()


# プレイヤーを表すクラス

class Player:
  def __init__(self, name):
    self.wins = 0
    self.card = None
    self.name = name


# ゲームを表すクラス

class Game:
  def __init__(self):
    name1 = input("プレーヤー1の名前 ")
    name2 = input("プレーヤー2の名前 ")
    self.deck = Deck()
    self.p1 = Player(name1)
    self.p2 = Player(name2)

  def wins(self, winner):
    w = "このラウンドは {} が勝ちました"
    w = w.format(winner)
    print(w)

  def draw(self, p1n, p1c, p2n, p2c):
    d = "{} は {}、{} は {} を引きました"
    d = d.format(p1n, p1c, p2n, p2c)
    print(d)

  def play_game(self):
    cards = self.deck.cards
    print("戦争を始めます！")
    # デッキのカードが２枚未満になるかqを入力したら終了！
    while len(cards) >= 2:
      m = "q で終了、それ以外のキーでPlay:"
      response = input(m)
      if response == 'q':
        break
      p1c = self.deck.rm_card()
      p2c = self.deck.rm_card()
      p1n = self.p1.name
      p2n = self.p2.name
      self.draw(p1n, p1c, p2n, p2c)
      if p1c > p2c:
        self.p1.wins += 1
        self.wins(self.p1.name)
      else:
        self.p2.wins += 1
        self.wins(self.p2.name)

    win = self.winner(self.p1, self.p2)
    print("ゲーム終了、{} の勝利です！".format(win))

  def winner(self, p1, p2):
    if p1.wins > p2.wins:
      return p1.name
    if p1.wins < p2.wins:
      return p2.name
    return "引き分け！"


game = Game()
game.play_game()
