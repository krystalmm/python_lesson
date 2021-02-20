# coding: UTF-8

# キューを使って映画のチケットを買う待ち行列をプログラミングしてみる！

import time
import random

class Queue:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return not self.items

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)


def simulate_line(till_show, max_time):
  pg = Queue()
  tix_sold = []

  for i in range(100):
    pg.enqueue("person" + str(i))

  t_end = time.time() + till_show
  now = time.time()
  while now < t_end and not pg.is_empty():
    now = time.time()
    r = random.randint(0, max_time)
    time.sleep(r)
    person = pg.dequeue()
    print(person)
    tix_sold.append(person)

  return tix_sold

sold = simulate_line(5,1)
print(sold)
