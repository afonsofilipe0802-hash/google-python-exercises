#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    if len(s)<3:         #se o comprimento da string for menor que 3
        return s         #retorna o string
    if s.endswith("ing"):#se acabar com (ing)
        return s+"ly"    #retorna a palavra e adiciona (ly)
    return s+"ing"       #vai retorna a palavra e adicionar (ing) se as condições de cima forem Falsas


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    loc_de_not=s.find("not")                                       #criei uma variável em que identifica numa frase a palavra (not).esta função(find) se ñ encontrar a palavra devolve um (-1)
    loc_de_bad=s.find("bad")                                       #criei uma variável em que identifica numa frase a palavra (bad)
    if loc_de_not!=-1 and loc_de_bad!=-1 and loc_de_not<loc_de_bad:#se identificar not na frase e se identificar bad na frase e not vem primeiro que bad
        return s[:loc_de_not]+"good"+s[loc_de_bad+3:]              #retorna a frase antes do not adiciona (good) e a frase depois de bad(+3 pois bad tem 3 letras)
    return s                                                       #retorna a frase normal caso a condição de cima seja falsa
  


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    meio_a=(len(a)+1)//2                        #criei uma variável em que diz como a palavra fica dividida(2-2 ou 3-2) para o a
    meio_b=(len(b)+1)//2                        #criei uma variável em que diz como a palavra fica dividida(2-2 ou 3-2) para o b
    a_front=a[:meio_a]                          #criei uma variável em vai ter as primeiras palavras de a até o meio da palavra
    a_back=a[meio_a:]                           #criei uma variável em vai ter as ultimas palavras de a partir do meio da palavra
    b_front=b[:meio_b]                          #criei uma variável em vai ter as primeiras palavras de b até o meio da palavra
    b_back=b[meio_b:]                           #criei uma variável em vai ter as ultimas palavras de b partir do meio da palavra
    return a_front + b_front + a_back + b_back  #retorna a palavra com inicio de a + inicio de b + fim de a + fim de b


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
