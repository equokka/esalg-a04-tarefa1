#!/usr/bin/env python

from typing import Any
# https://docs.python.org/3/library/typing.html#the-any-type

from collections import deque
# https://docs.python.org/3/library/collections.html#collections.deque

class Queue:
  def __init__(self) -> None:
    self.queue = deque([])

  def __str__(self) -> str:
    return "Queue%s" % str(list(self.queue))

  def __repr__(self) -> str:
    return str(self)

  def push(self, item) -> None:
    self.queue.appendleft(item)

  def pop(self) -> Any:
    return self.queue.pop()

  def peek(self) -> Any:
    return self.queue[-1]

  def __len__(self) -> int:
    return len(self.queue)

  def empty(self) -> None:
    self.queue = deque([])

  def __iter__(self) -> None:
    yield from reversed(self.queue)
