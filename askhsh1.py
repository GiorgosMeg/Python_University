def vowel_remover(text):
    vowels = ('a', 'e', 'i', 'o', 'y',  'A', 'E', 'I', 'O', 'Y', 'U') #I  consider y as a vowel
    for char in text:
        if char in vowels:
            text = text.replace(char, '')
    return text          






with open('aaa.txt', 'r') as myfile:
    words = myfile.read().split()
    
long1 = max(words, key=len)#Search for  longest word

words.remove(long1)#Remove the  longest from list of words

long1 = vowel_remover(long1)#Call function to remove the vowels

print("The first longest word is  : ",long1[::-1])#Print the  longest word backwords



long2 = max(words, key=len)#Search for the  longest word

words.remove(long2)#Remove the longest from list of words

long2 = vowel_remover(long2)#Call function to remove the vowels 

print("The second longest word is  : ",long2[::-1])#Print the longest word backwords



long3 = max(words, key=len)#Search for the longest word

words.remove(long3)#Remove the longest word from list of words

long3 = vowel_remover(long3)#Call function to remove the vowels

print("The third longest word is  : ",long3[::-1])#Print the longest word backwords



long4 = max(words, key=len)#Search for the longest word

words.remove(long4)#Remove the longest word from list of words

long2 = vowel_remover(long4)#Call function to remove the vowels

print("The fourth longest word is  : ",long4[::-1])#Print the longest word backwords



long5 = max(words, key=len)#Search for the longest word

words.remove(long5)#Remove the longest word from list of words

long5 = vowel_remover(long5)#Call function to remove the vowels

print("The fifth longest word is  : ",long5[::-1])#Print the longest word backwords



    
