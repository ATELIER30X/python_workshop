# zapis promenych
# https://naucse.python.cz/course/pyladies/beginners/variables/
# int		x = 1

# float		x = 1.5

# str		x = "text"

# list		x = [1, 2, 3]	(indexovani od 0)
#		x = [1, 2, [3, 4]]	volani - x[2][1]
#		pridani prvku - x.append(5)

# boolean	x = True		x = False

#-----------------------------------
# https://naucse.python.cz/course/pyladies/beginners/comparisons/
# porovnavaci podminky - pouzitelne v podminkach (if) nebo cyklech (while)
# == (je rovno)
# != (neni rovno) 
# >= (vetsi rovno nez)  > (vetsi nez)
# <= (mensi rovno nez)  < (mensi nez)

x = 1

if x == 2:
    print("x je 2")
elif x == 3:
    print("x je 3")
else:
    print("x neni ani 2, ani 3")


#-----------------------------------
#https://www.learnpython.org/en/Loops
#for cyklus s danym poctem iteraci - od 2 do 10, s intervalem 3
#prvni cislo urcuje kde zaciname, druhe cislo kde koncime minus 1, treti cislo po kolika skaceme

for i in range(2, 10, 3):
    print(i)


#-----------------------------------
#while cyklus - provadi se dokud je splnena podminka
#pozor na zacykleni

y = 1
while y < 5:
    print (y)
    y += 1 
    

#-----------------------------------
#continue - skoci na dalsi iteraci cyklu
#break - cyklus se rovnou prerusi

#modulo - zbytek po deleni - zapis %



