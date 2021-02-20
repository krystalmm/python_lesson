# coding: UTF-8

def hangman(word):
    wrong = 0
    stages = ["",
              "_________        ",
              "|                ",
              "|        |       ",
              "|        O       ",
              "|       /|\      ",
              "|       / \      ",
              "|                "
            ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:  # len(stages) - 1 としているのは、wrongが１から始まるのに対し、len(stages)は０から始まるため！！
      # 見栄えを良くするための空行！！
      print("\n")
      msg = "１文字を予想してね"
      char = input(msg)
      if char in rletters:
        # indexメソッドで、最初に見つかった要素に対応するインデックスを取得する！（存在しなければvalueerrorが発生する！）
        cind = rletters.index(char)
        board[cind] = char
        # 正解の文字が重複している場合、最初の文字だけをindexメソッドでは取得するので、正解した文字を$にし、ループさせることでそれに対応する！！（次のループでは、indexメソッドで２つ目の場所を返してくれる！）
        rletters[cind] = '$'
      else:
        wrong += 1
      print(" ".join(board))
      # 1を足しているのは、足さずにそのまま使った場合、終了インデックスに指定した値の手前までしかスライスされず、stagesの最後の要素が出力されないから！！
      e = wrong + 1
      print("\n".join(stages[0:e]))
      if "_" not in board:
        print("あなたの勝ち！")
        print(" ".join(board))
        win = True
        break

    if not win:
      print("\n".join(stages[0:wrong+1]))
      print("あなたの負け！正解は {}.".format(word))

hangman("cat")
