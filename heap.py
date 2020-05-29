#!/usr/bin/env python

from typing import Any, Union
# https://docs.python.org/3/library/typing.html#the-any-type
# https://docs.python.org/3/library/typing.html#typing.Union

class HeapNode:
  def __init__(self, data: Any, value: int) -> None:
    self.data = data
    self.value = value
  def __str__(self) -> str:  return "<HeapNode <%s> %d>" % (str(self.data), self.value)
  def __repr__(self) -> str: return "<%d>" % self.value

class Heap:
  """This is a max-heap."""
  def __init__(self) -> None:
    self.heap = []

  def __str__(self) -> str:  return "<Heap%s>" % str(self.heap)
  def __repr__(self) -> str: return str(self)

  # len(<Heap>)
  def __len__(self) -> int: return len(self.heap)
  # <Heap>[<index>]
  def __getitem__(self, index: int) -> HeapNode: return self.heap[index]
  # <Heap>[<index>] = <HeapNode>
  def __setitem__(self, index: int, value: HeapNode) -> None: self.heap[index] = value
  # del <Heap>[<index>]
  def __delitem__(self, index: int) -> None: del self.heap[index]

  # these get the **index** of the node
  def get_parent(self, i: int) -> int:  return (i - 1) // 2
  def get_left(self, i: int) -> int:    return 2 * i + 1
  def get_right(self, i: int) -> int:   return 2 * i + 2

  def has_parent(self, i: int) -> bool: return self.get_parent(i) >= 0
  def has_left(self, i: int) -> bool:   return self.get_left(i)  < len(self)
  def has_right(self, i: int) -> bool:  return self.get_right(i) < len(self)

  def swap(self, i: int, j: int) -> None:
    self[i], self[j] = self[j], self[i]

  def push(self, node: HeapNode) -> None:
    self.heap.append(node)
    self.bubble_up(len(self) - 1)

  def pop(self) -> Union[HeapNode, None]:
    if len(self) == 0: return None
    out = self.heap[0]
    self.swap(0, len(self) - 1)
    del self[len(self) - 1]
    self.bubble_down(0)
    return out

  def bubble_up(self, i: int) -> None:
    if self.has_parent(i):
      parent = self.get_parent(i)
      if self[parent].value < self[i].value:
        self.swap(i, parent)
        self.bubble_up(parent)

  def bubble_down(self, i: int) -> None:
    largest = i

    if self.has_left(i):
      left = self.get_left(i)
      if self.heap[left].value > self.heap[largest].value:
        largest = left

    if self.has_right(i):
      right = self.get_right(i)
      if self.heap[right].value > self.heap[largest].value:
        largest = right

    if largest != i:
      self.swap(i, largest)
      self.bubble_down(largest)

# Tests

# heap = Heap()
# heap.push( HeapNode("Aardvark", 20)   )
# heap.push( HeapNode("Albatross", 10)  )
# heap.push( HeapNode("Alligator", 30)  )
# heap.push( HeapNode("Alpaca", 25)     )
# heap.push( HeapNode("Ant", 45)        )
# heap.push( HeapNode("Anteater", 40)   )
# heap.push( HeapNode("Antelope", 40)   )
# heap.push( HeapNode("Ape", 10)        )
# heap.push( HeapNode("Armadillo", 5)   )
# heap.push( HeapNode("Ass/donkey", 28) )

# print(heap.heap, end = "\n\n")

# while len(heap) != 0:
#   print("{:<25} {}".format(str(heap.pop()), heap.heap))
