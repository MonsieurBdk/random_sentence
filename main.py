from random import randint

subjects =  [
    "Tonton",
    "Marie",
    "Jean",
    "L'école",
    "L'enfant"
]

verbs = [
    "mange",
    "étudie",
    "crie",
    "bouge"
]

complements = [
    "à l'école",
    "au boulot",
    "lentement",
    "du fufu"
]

sentenceWordList = []
userSentence = ""
sentencesList = []
space = " "

def pickWordFromList(wordList:list):
    wordListLenght = len(wordList)
    randomIndex =randint(0, wordListLenght-1)
    return wordList[randomIndex]

while userSentence == "":
    userInput = input("Entrez une phrase: ")
    userInput = userInput.lstrip().rstrip()

    if not userInput.isalpha:
        print("Erreur, veillez entrer une phrase correcte")
    if userInput == "":
        print("Erreur, votre phrase ne peut être vide")
    else:
        userSentence = userInput

sentenceWordList = userSentence.split(" ")

for i in range(len(sentenceWordList)):
    sentence = ""
    match i:
        case 0:
            sentence = sentenceWordList[0].title() + space + pickWordFromList(wordList=verbs).lower() + space + pickWordFromList(wordList=complements).lower()
            
        case 1:
            sentence =  pickWordFromList(wordList=subjects).title() + space + sentenceWordList[1].lower() + space + pickWordFromList(wordList=complements).lower()
          
        case 2:
            sentence =  pickWordFromList(wordList=subjects).title()+ space + pickWordFromList(wordList=verbs).lower() + space + sentenceWordList[2].lower()
        case _:
            sentence = userSentence

    sentenceWordList.append(sentence)
    words = sentence.split(" ")
    words = [word.title() for word in words]
    words.sort()

    print(f'LA PHRASE ({i+1})')
    print(sentence)
    print("les mots par ordre alphabétique:")
    for word in words:
        print( " - " + word)
    print('\n')
    







    
