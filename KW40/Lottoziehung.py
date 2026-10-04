import random


def genNumbers():
    numbers = []
    for i in range(1,46,1):
        numbers.append(i)
    
    return numbers
        
def pullNumbers(pulls,numbers = [],pulledNumbers=[]):
    
    
    
  
         if len(pulledNumbers) == pulls:
             return pulledNumbers       # schöner wäre es so: newSize = len(numbers) -1 - len(pulledNumbers)
                                        #,aber ich mag des nit
         wonNumber = random.randint(0,len(numbers) -1 - len(pulledNumbers))
         numbers = switchIndices(wonNumber,len(numbers) -1 - len(pulledNumbers),numbers)

         pulledNumbers.append(numbers[len(numbers) -1 - len(pulledNumbers)])
         return  pullNumbers(pulls, numbers,pulledNumbers)

            
    
        

        
def sortStatistics(times,pulls):
    pulledNumbers = []
    sorted ={}
    for i in genNumbers() :
        sorted[i] = 0
    for i in range(times):                              
                                                            #[13, 3, 17, 25, 22, 33]
                                                            #[13, 3, 17, 25, 22, 33]
                                                            #[13, 3, 17, 25, 22, 33]
                                                            #[13, 3, 17, 25, 22, 33]
                                                            #[13, 3, 17, 25, 22, 33]
                                                            #[13, 3, 17, 25, 22, 33]
                                                            #[13, 3, 17, 25, 22, 33]
                                                            #Hab den dritten Argumente (liste entleeren) nicht berücksichtig 
                                                            #die Ausgabe war dann wie folgt (oben) 
        pulledNumbers= (pullNumbers(pulls,genNumbers(),pulledNumbers=[]))
        for i in pulledNumbers:
            sorted[i] += 1
    return sorted
        
        
        
            
        



def switchIndices(wonNumber,switchIndex, numbers = []):
    #Habs online gesehen
    numbers[switchIndex], numbers[wonNumber] = numbers[wonNumber], numbers[switchIndex]
    return numbers




#Ich habe die Methode gelassen, 
# weil ich nicht genau verstanden habe,
# warum das "append" unbedingt in eine eigene Zeile geschrieben werden muss.

#Abgesehen davon,
# dass Methodenkopf und die rekursiv-Logik nicht stimmen 
# und ohnehin zum Abstürz des Programmes führen!
#KI-Zitat :In Python führt .append() eine In-Place-Operation aus und gibt None zurück

def pullNumberFehlerhaft(pulls,newSize,list = [], pulledNumbers =[]):

    endRecursive = False
    if endRecursive == False:
        wonNumber = random.randint(0,len(list) -1 - len(pulledNumbers))
        switchIndices(wonNumber,len(list) -1 - len(pulledNumbers),list)
        if len(list) -1 - len(pulledNumbers) < (len(list) - pulls):

            newSize = len(list)

            endRecursive = True
    pullNumberFehlerhaft(pulls,len(list) -1 - len(pulledNumbers),list,pulledNumbers.append(list[len(list) -1 - len(pulledNumbers)]))

    return pulledNumbers

       



print(sortStatistics(12633712,6))
#Die Zahlen sind ziemlich Gleichverteilt! 
#Merklich ist es vor allem bei größeren Iterationen


