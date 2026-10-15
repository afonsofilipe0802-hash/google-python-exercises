#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    result_list=[]          #criei uma lista
    for num in nums:        #para cada nº na lista
        if len(result_list)==0 or num!=result_list[-1]:#se a qt de nºs da lista for igual a 0 ou se o nº for diferente do ultimo nºda lista
            result_list.append(num)      #se o que ta em cima for verdade ent adiciona a lista
    return result_list # depois de percorrer todos os números, devolve a lista final
  
  


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    result = []                          # cria a lista de resultado, vazia
    i = 0                                # índice da posição atual em list1
    j = 0                                # índice da posição atual em list2
    while i < len(list1) and j < len(list2):   # enquanto nenhuma das listas tiver acabado
        if list1[i] <= list2[j]:         # se o elemento atual de list1 é menor ou igual ao de list2
            result.append(list1[i])      # guarda o de list1 no resultado
            i = i + 1                    # avança para o próximo elemento de list1
        else:                            # caso contrário, o de list2 é o menor
            result.append(list2[j])      # guarda o de list2 no resultado
            j = j + 1                    # avança para o próximo elemento de list2
    result = result + list1[i:]          # junta o que sobrou de list1 (vazio se já acabou)
    result = result + list2[j:]          # junta o que sobrou de list2 (vazio se já acabou)
    return result                        # devolve a lista final já ordenada
                                   

                                     #ou
                                
def linear_merge(list1, list2):
    result = []                              # lista de resultado, vazia (vai ficar ao contrário)
    while len(list1) > 0 and len(list2) > 0: # enquanto as duas listas tiverem elementos
        if list1[-1] >= list2[-1]:           # se o último (maior) de list1 é maior ou igual ao de list2
            result.append(list1.pop())       # tira-o de list1 e guarda no resultado
        else:                                # caso contrário, o maior é o de list2
            result.append(list2.pop())       # tira-o de list2 e guarda no resultado
    while len(list1) > 0:                    # se sobrou algo em list1
        result.append(list1.pop())           # tira o último e guarda
    while len(list2) > 0:                    # se sobrou algo em list2
        result.append(list2.pop())           # tira o último e guarda
    result.reverse()                         # inverte o resultado para ficar por ordem crescente
    return result                            # devolve a lista final                                

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print()
  print('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
