list1=[1,2,3,4,5]
list2=['banana','apple','mango','orange']
list3=[4,5,1,6,3,2]

list1.extend(list2)         # 2 listeyi birlestirmek icin kullanilir
list2.append('cherry')      # listenin sonuna eleman eklemek icin 
list2.insert(1, 'kiwi')     # listenin 2. elemenina elenir ve diger elemenlari 1 e kaydirir
list2.remove('banana')      # listedeki banana elemanini siler
list1.clear()               # listenin icini temizler ve bos liste olur
list3.sort()                # listeyi kucukten buyuge siralamak icin
list2.reverse()             # listeyi tersken siralamak
list4 = list2.copy()        # list i copyalar
list2.pop()                 # listedin sonundali elemani siler
del list4[1]                # list 4 deki 1 index deki elemeni siler


print(list2.index('mango')) # mango nun listediki index numarasini gosterir
print(list2.count('mango')) # listediki mangolari sayar

print(list1)
print(list2)
print(list3)
print(list4)