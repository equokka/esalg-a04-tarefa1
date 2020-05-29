#!/usr/bin/env python

from queue  import Queue
from person import Person, PersonHeap, generate_person
from utils  import get_severity, is_int, get_option

sev = ["Azul", "Verde", "Amarelo", "Laranja", "Vermelho"]

queue = Queue()
heap = PersonHeap()

def show_stats():
  print("\nFila de espera:  %d pessoa%s" % (len(queue), ("" if len(queue) == 1 else "s")))
  print(  "Fila de triagem: %d pessoa%s" % (len(heap),  ("" if len(heap)  == 1 else "s")))
  print(  "  Vermelho : %d" % len(list(filter(lambda x: x.value == 4, heap))))
  print(  "  Laranja  : %d" % len(list(filter(lambda x: x.value == 3, heap))))
  print(  "  Amarelo  : %d" % len(list(filter(lambda x: x.value == 2, heap))))
  print(  "  Verde    : %d" % len(list(filter(lambda x: x.value == 1, heap))))
  print(  "  Azul     : %d" % len(list(filter(lambda x: x.value == 0, heap))))
  print("-" * 80)

while True:
  show_stats()
  print(" 1 – Gerar pessoas para fila de espera")
  print(" 2 - Adicionar uma pessoa à fila de espera manualmente")
  print(" 3 - Passar pessoas da fila de espera para a fila de triagem")
  print(" 4 - Simular o atendimento da fila de triagem")
  print(" 5 - Saír")
  option = get_option("> ", 5)
  if option == 1:
    while True:
      show_stats()
      print(" Gerar quantas pessoas?")
      print(" 1 - 10 pessoas")
      print(" 2 - 30 pessoas")
      print(" 3 - 100 pessoas")
      print(" 4 - Número específico")
      print(" 5 - Voltar a tráz")
      option = get_option("> ", 5)
      if option == 1:
        [queue.push(generate_person()) for _ in range(10)]
        break
      elif option == 2:
        [queue.push(generate_person()) for _ in range(30)]
        break
      elif option == 3:
        [queue.push(generate_person()) for _ in range(100)]
        break
      elif option == 4:
        print("Quantas pessoas?")
        while True:
          i = input("> ").strip()
          if is_int(i):
            [queue.push(generate_person()) for _ in range(int(i))]
            break
          print("Números inteiros, por favor.")
        break
      elif option == 5:
        break
  elif option == 2:
    person = Person(input("Nome: ").strip())
    severity = get_severity(True)
    heap.person_push(person, severity)
    print(" {:<8} {}".format(sev[severity], person))
  elif option == 3:
    if len(queue) != 0:
      while True:
        show_stats()
        print(" 1 – Processar a fila inteira automáticamente")
        print(" 2 - Processar parte da fila automáticamente")
        print(" 3 - Processar uma pessoa manualmente")
        print(" 4 - Voltar a tráz")
        option = get_option("> ", 4)
        if option == 1:
          while len(queue) != 0:
            person = queue.pop()
            severity = get_severity()
            heap.person_push(person, severity)
            print(" {:<8} {}".format(sev[severity], person))
          break
        elif option == 2:
          print("Quantas pessoas?")
          while True:
            i = input("> ").strip()
            if is_int(i):
              for _ in range(int(i)):
                person = queue.pop()
                severity = get_severity()
                heap.person_push(person, severity)
                print(" {:<8} {}".format(sev[severity], person))
              break
            print("Números inteiros, por favor.")
          break
        elif option == 3:
          person = queue.pop()
          print(" Nome:             %s" % person.name)
          print(" Número de utente: %d" % person._id)
          severity = get_severity(True)
          print("Nível de urgência %s" % sev[severity])
          heap.person_push(person, severity)
          break
        elif option == 4:
          break
    else:
      print("A lista de espera está vazia.")
      print("Adicione à lista de espera com as opções 1 ou 2 primeiro.")
  elif option == 4:
    if len(heap) != 0:
      while True:
        show_stats()
        print(" 1 – Atender a fila de triagem inteira automáticamente")
        print(" 2 - Atender parte da fila de triagem automáticamente")
        print(" 3 - Voltar a tráz")
        option = get_option("> ", 3)
        if option == 1:
          while len(heap) != 0:
            node = heap.pop()
            person = node.data
            severity = node.value
            print(" {:<8} {}".format(sev[severity], person))
          break
        elif option == 2:
          print("Quantas pessoas?")
          while True:
            i = input("> ").strip()
            if is_int(i):
              for _ in range(int(i)):
                node = heap.pop()
                person = node.data
                severity = node.value
                print(" {:<8} {}".format(sev[severity], person))
              break
            print("Números inteiros, por favor.")
          break
        elif option == 3:
          break
    else:
      print("A fila de triagem está vazia.")
      print("Passe algumas pessoas para a fila de triagem primeiro com a opção 3.")
  elif option == 5:
    break
