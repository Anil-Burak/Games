hangman = [" ",
           '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']


def check_letter(character):
    if len(character) == 1:
        return True
    else:
        print("Doğru şekilde harf girmediniz. ")
        return False


while True:
    word = input("Kelimeyi girin: ").lower()
    wordList = list(word)
    lettersInWord = []
    for letter in wordList:
        if letter != " " and letter not in lettersInWord:
            lettersInWord.append(letter)
    lettersInWord.sort()
    correctLetters = []
    usedLetters = []
    count = 0
    while True:
        for element in word:
            if element in usedLetters:
                print(element, end=" ")
            elif element == " ":
                print("/ ", end="")
            else:
                print("_ ", end="")
        newLetter = input(" ").lower()
        if check_letter(newLetter):
            if newLetter in usedLetters:
                print("Harf önceden girilmiş")
                continue
            elif newLetter in lettersInWord:
                correctLetters.append(newLetter)
                correctLetters.sort()
                if correctLetters == lettersInWord:
                    print(word)
                    print("Kazandınız \n")
                    break
                usedLetters.append(newLetter)
            else:
                usedLetters.append(newLetter)
                count += 1
                print(hangman[count])
                if count == 7:
                    print("Kaybettiniz. \n")
                    break
                else:
                    print("Yanlış harfler: ", end="")
                    for x in usedLetters:
                        if x in correctLetters:
                            continue
                        else:
                            print(x, end=" ")
                    print("")