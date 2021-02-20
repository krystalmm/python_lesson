# coding: UTF-8

# スタックを理解する！
# スタックは、リストのようなデータ構造（LIFO: Last In First Out）（最後に入れた要素だけを取り出せる！）

class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return not self.items

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    last = len(self.items) - 1
    return self.items[last]

  def size(self):
    return len(self.items)


# stack = Stack()
# stack.push(1)
# item = stack.pop()
# print(item)
# print(stack.is_empty())

stack = Stack()
for c in "Hello":
  stack.push(c)

reverse = ""

while stack.size():
  reverse += stack.pop()

print(reverse)



