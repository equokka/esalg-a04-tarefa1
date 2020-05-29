#!/usr/bin/env python

from faker import Faker # pip install Faker

from heap import *

# dirty UID implementation I know
person_ids = 0

class Person:
  def __init__(self, name: str):
    self.name = name
    global person_ids
    self._id = person_ids
    person_ids += 1
  def __str__(self) -> str: return "<%s:%s>" % (self.name, self._id)
  def __repr__(self) -> str: return str(self)

class PersonHeap(Heap):
  """ Extension of the Heap class with extra methods for handling Person(s) specifically.  """

  def __str__(self) -> str:  return "<PersonHeap%s>" % str(self.heap)

  def person_push(self, person: Person, value: int) -> None:
    """ Value can be 0-4 in increasing priority. """
    if value not in range(5): raise ValueError("value may only be int 0-4.")
    self.push(HeapNode(person, value))

  def person_pop(self) -> Person:
    return self.pop().data

fake = Faker()

def generate_person() -> Person:
  return Person(fake.name())
