

1. count_vowels(s) — conta as vogais (a, e, i, o, u, sem distinguir maiúsculas).
count_vowels('Python') → 1, count_vowels('AEIOU') → 5
def count_vowels(s):
     num_vowels=0             #criei uma variável de contagem de vogais
     string_to_compare="aeiou"#criei uma variável para comparar
     lower_string_transformation=s.lower()#criei uma variável que mete as palavras em minusculas
     for char in lower_string_transformation:#para cada letra do input em minusculas
         if char in string_to_compare:       #se essa letra estiver no string de comparação
             num_vowels+=1                   #adiciona mais 1 à variável que conta vogais
     return num_vowels                       #retorna a variável de contagem de vogais

2. reverse_words(s) — inverte a ordem das palavras.
reverse_words('olá mundo bonito') → 'bonito mundo olá'
Dica: .split() e .join().

def reverse_words(s):
    list_of_word=s.split()#criei uma lista com as palavras separadas
    reverse_list=list_of_word.reverse()#reverti a lista_of_word
    final_result=" ".join(list_of_word)#juntei a lista das palavras revertidas com espaço entre elas
    return final_result

reverse_words("Olá eu gosto de pizza")


3. common_elements(a, b) — devolve os elementos presentes nas duas listas, sem repetidos e ordenados.
common_elements([1, 2, 2, 3, 5], [2, 3, 3, 4]) → [2, 3]
Dica: pesquisa o que é um set.

def common_elements(a, b):
    result_list=[]
    for ele in a:
        if ele in b and ele not in result_list:
            result_list.append(ele)
    return sorted(result_list)

common_elements([1, 2, 2, 3, 5], [2, 3, 3, 4])  

4. second_largest(nums) — devolve o segundo maior valor distinto.
second_largest([4, 9, 9, 2, 7]) → 7

def second_largest(nums):
    with_out_repetitions=set(nums)
    sort=sorted(with_out_repetitions)
    return sort[-2]

second_largest([4, 9, 9, 2, 7])

Nível 2: coisas novas (dicionários e comprehensions)

5. count_letters(s) — devolve um dicionário com a contagem de cada letra.
count_letters('banana') → {'b': 1, 'a': 3, 'n': 2}

def count_letters(s):
    count_dictionary={}   #criei um dicionário
    for char in s:        #para cada letra das palavras
        if char in count_dictionary:#se a letra estiver no dicionário
            count_dictionary[char]+=1#adiciona +1 no valor dessa palavra
        else:                        #caso contrário
            count_dictionary[char]=1 #da a essa palavra o valor de 1
    return count_dictionary          #retorna o dicionário

count_letters('banana')

6. most_common_word(text) — devolve a palavra que mais se repete (ignora maiúsculas).
most_common_word('o gato e o rato e o cão') → 'o'

def most_common_word(text):
    list_text=text.lower().split()#como é texto vou dar split pra criar uma lista de palavras
    count_d={}#criei um dicionário para contyar o nº de letras
    for word in list_text: #para cada palavra na lista de palavras
        if word in count_d:#se a palavra ta no dicionário ent adiciona +1
            count_d[word]+=1 
        else:#caso contrário
            count_d[word]=1#atribui o valor 1 a palavra pra começar a contagem
    return max(count_d, key=count_d.get)#compara as palavras pelas suas contagens, e devolve a palavra com a contagem maior.
        
most_common_word('o gato e o rato e o cão')

7. squares_of_evens(nums) — devolve os quadrados dos números pares, numa só linha com list comprehension.
squares_of_evens([1, 2, 3, 4, 6]) → [4, 16, 36]

def squares_of_evens(nums):
    even_list=[]
    for num in nums:
        if num%2==0:
            even_list.append(num**2)
    return even_list

squares_of_evens([1,2,3,4,5,6])

            

Nível 3: bioinformática

8. gc_content(dna) — percentagem de G+C, arredondada a 2 casas.
gc_content('ATGC') → 50.0, gc_content('GGGCA') → 80.0

def gc_content(dna):
    percentagem_de_cada_letra=100/len(dna)
    identificador_de_GC="GC"
    percentagem=0
    for nucle in dna:
        if nucle in identificador_de_GC:
            percentagem+=percentagem_de_cada_letra
    return round(percentagem, 2)
gc_content('ATGC')

            



9. reverse_complement(dna) — faz o reverso complementar sem Biopython, usando um dicionário {'A': 'T', ...}. Depois confirma com Seq(dna).reverse_complement().
reverse_complement('ATGC') → 'GCAT'

def reverse_complement(dna):
    d={"A":"T","C":"G","T":"A","G":"C"}#i crated a dictionary
    reverse_list=""#created a variable with empty string
    for nucl in dna[::-1]:#i did a loop with the dna reverse already
        d[nucl]           #with that code it gives the value of nucl
        reverse_list+=d[nucl]#i added to the variable the value of nucl
    return reverse_list#return the reverse list

reverse_complement('ATGC')
        



10. count_codons(dna) — divide a sequência em codões e devolve um dicionário com a contagem de cada um.
count_codons('ATGGCTATGGCT') → {'ATG': 2, 'GCT': 2}
Dica: range(0, len(dna), 3).

11. hamming_distance(a, b) — número de posições onde duas sequências do mesmo tamanho diferem.
hamming_distance('GATTACA', 'GACTATA') → 2
Dica: zip(a, b).

def hamming_distance(a, b):
    num_difer_position=0   #criei uma variável de contagem
    for x, y in zip(a, b): #para cada elemento do par, no zip(a,b)-junta os valores lado a lado com o seu correspondente
        if x!=y:           #se um elemento for != do outro
            num_difer_position+=1 #if the condition is true then add 1 on variavel 
    return num_difer_position     #retorna a variavel de contagem
            
hamming_distance('GATTACA', 'GACTATA')   

12. find_sites(dna, site) — devolve a lista de todas as posições (índice inicial) onde site aparece, incluindo sobreposições.
find_sites('GAATTCAAGAATTC', 'GAATTC') → [0, 8]
Dica: str.find(site, início) num while.

def find_sites(dna, site):
    result_list=[]#created a list
    inicio=dna.find(site, 0)#created a variable that say to start searching the site from the loc 0
    while inicio!=-1:#made a loop with the condition to counter empty dna
        result_list.append(inicio)#added into list
        inicio=dna.find(site, inicio+1)#after the adding i tell where the search begin(inicio+1)
    return result_list#return the list


find_sites('GAATTCAAGAATTC', 'GAATTC')    



13. parse_fasta(text) — recebe o texto de um FASTA (pode ter sequências em várias linhas) e devolve um dicionário {id: sequência}.

>gene1
ATGC
GGA
>gene2
TTTT

→ {'gene1': 'ATGCGGA', 'gene2': 'TTTT'}
Este é o mais difícil. Usa .splitlines() e startswith('>').

Nível 3: pandas e matplotlib

14. mean_by_strain(df) — o DataFrame tem as colunas 'strain' e 'od'. Devolve um dicionário com a média de od por estirpe.
Dica: df.groupby('strain')['od'].mean().to_dict().

15. strong_changes(df) — colunas 'gene', 'control', 'treated'. Calcula log2(treated / control) numa nova coluna 'log2fc' e devolve a lista de genes com abs(log2fc) > 1.
Dica: import numpy as np e np.log2.

16. expression_bar(genes, values) — faz um gráfico de barras com ax.bar(), título 'Expression', eixo y 'TPM', e devolve ax (sem plt.show() dentro da função).