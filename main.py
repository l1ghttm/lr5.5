stroka=input("Введите строку:") #ввод строки 
letter = "и" #создание переменной, в которой содержится буква "и" для дальнейшего подсчета

index = [] #индекс
skolko = 0 #для дальнейшего  кол-во совпадений с буквой "и"

for i in range(len(stroka)): #условия функции for 
    char = stroka[i].lower() #переменная для хранения буквы по индексу
    if char in letter: #условие if 
        index.append(i) #добавление элемента 
        skolko+=1 #счесткик увеличивается 

print("Кол-во букв <<и>>", skolko) #вывод
