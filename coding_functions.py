# -*- coding:Utf-8 -*-
# Author : Jacques Hoschtettler
# may 2023

# ---------------------------------------------------------------------------------- #
## Constants
    # Constants for Polybe's square method. The used square sizes 6x6. It contains 
    # the whole alphabetical characters, without ambiguity, and the whole figures.
PolybesSquare = {"a":"11", "b":"12", "c":"13", "d":"14", "e":"15", "f":"16",
                "g":"21", "h":"22", "i":"23", "j":"24", "k":"25", "l":"26",
                "m":"31", "n":"32", "o":"33", "p":"34", "q":"35", "r":"36",
                "s":"41", "t":"42", "u":"43", "v":"44", "w":"45", "x":"46",
                "y":"51", "z":"52", "0":"53", "1":"54", "2":"55", "3":"56",
                "4":"61", "5":"62", "6":"63", "7":"64", "8":"65", "9":"66",}

reversePolybesSquare = \
               [["a", "b", "c", "d", "e", "f"], 
                ["g", "h", "i", "j", "k", "l"],
                ["m", "n", "o", "p", "q", "r"], 
                ["s", "t", "u", "v", "w", "x"],
                ["y", "z", "0", "1", "2", "3"], 
                ["4", "5", "6", "7", "8", "9"]]

# ---------------------------------------------------------------------------------- #
## Functions level 0
# Shaping of sentences and keys

def shaping_sentence(sentence):
    """ This function shapes the sentence to be coding. It puts the sentence in lower-case, 
        removes accents on vowels, and cedilla. 
        "sentence" is the sentence to let in shape. It is a string.
        It returns a string, the treated sentence.
    """
    # "minusSentence" is the sentence all in lower-case
    # "character" is one element of the minusSentence
    # "finalSentence" is the final sentence which is return
    minusSentence = sentence.lower()
    finalSentence = ""
    for character in minusSentence:
        if character in ["é", "è", "ë", "ê"]:
            finalSentence += "e"
        elif character in ["à", "â"]:
            finalSentence += "a"
        elif character in ["î", "ï"]:
            finalSentence += "i"
        elif character == "ô":
            finalSentence += "o"
        elif character in ["ù", "û"]:
            finalSentence += "u"
        elif character == "ç":
            finalSentence += "c"
        else:
            finalSentence += character
    return finalSentence

def shaping_key(rawKey):
    """ This function puts a characters string in low-case and removes 
        the acccents on vowels and the cedilla (call of the shaping_sentence 
        function), then it takes away non alphabetical characters (spaces, 
        punctuation marks, figures).
        "rawKey" is the key given by the user. It is a string.
        It returns a string, the treated sentence.
    """
    # "intermediateKey" is the lower-case string, without accents nor cedilla.
    # "pureKey" is the original key wihitout punctuation, spaces, accents, cedilla,
    #           all in lower-case.
    # "character" is one element of the intermediateKey
    pureKey =""
    intermediateKey = shaping_sentence(rawKey)
    for character in intermediateKey:
        if character.isalpha():
            pureKey += character
    return pureKey

def cutting_long_sentence(longSentence, maximalLength):
    """ This function is cutting a one line sentence too long to going in a limited 
        length window.
        "longSentence" is the initial sentence, without cut.
        "maximaLength" is the maximal number of character per line.
        It return a string, the sentence cut in lines. Cuts replace some spaces.
    """
    # "pointer" is the position of the actual read character of the sentence.
    # "lastSpaceRead" is the position of the last read space character. It can
    #       a postion for the cut.
    # "lastCuttingPosition" is the position of the last cut of the sentence.
    # "sentenceLength" is the length of the initial sentence.
    # "cutSentence" is the returned cut sentence.
    # "cutNumber" is the number of the cuts ("\n")
    pointer = 0
    lastSpaceRead = 0
    lastCuttingPosition = 0
    cutSentence = ""
    sentenceLength = len(longSentence)
    cutNumber = 0
    while pointer < sentenceLength and (pointer - lastSpaceRead) <= maximalLength :
        if longSentence[pointer] == " ":
            lastSpaceRead = pointer
        if (pointer - lastCuttingPosition) >= maximalLength:
                cutSentence += longSentence[lastCuttingPosition:lastSpaceRead]
                cutNumber += 1
                if (sentenceLength - lastSpaceRead) >= maximalLength :
                    cutSentence += "\n"
                lastCuttingPosition = lastSpaceRead +1  # +1 to remove the space
        pointer += 1
    if (sentenceLength - lastCuttingPosition) >0:
        if cutNumber > 0:
            cutSentence += "\n"
        cutSentence += longSentence[lastCuttingPosition:sentenceLength]
        cutNumber += 1
    return cutSentence, cutNumber

# ---------------------------------------------------------------------------------- #
## Functions level 1

def coding_Cesar(characterToBeCoded, shiftValue):
    """ This function allows the coding of a checked character (in lower-case,
        without accent, which is not punctuation nor space). It uses the Cesar's  
        coding method, shifting the letters of shift value. 
        "characterToBeCoded" is the character to be treated. It is a string.
        "shiftValue" is the  size of the shift. The character is coded if the shift 
        is positive, and undecoded if the shift is negative. It is an integer.
        It returns a string of length 1, the treated character.
    """
    # "rank" is the number of the letter in alphabet
    # "coding" is the computed rank of the coded letter.
    # "result" is the codes character.
    # In the ASCII code for characters, 97 matches to "a", 98 to "b", … , 122 to "z".
    rank = ord(characterToBeCoded) - 96      # rank is in the range [1;26] of alphabet
    coding = rank + shiftValue
    # If the variable "coding" goes out of the range [1;26] of letters of alphabet, 
    # it is put back in the range.
    if coding <1:
        coding += 26
    elif coding > 26:
        coding -= 26
    coding += 96                 # Back to the ASCII code of the character
    result = chr(coding)
    return result

def coding_Polybe(character):
    """ This function codes a character using the Polybe's square 
        "character" is the alphanumeric character to be coded. It is a string.
        It returns a string of length 1, the treated character.
    """
    # "coordinates" is a string of two figures corresponding to the position of the
    # character in the Polybe's square
    coordinates = PolybesSquare[character]
    return coordinates

def uncoding_Polybe(row, column):
    """ This function returns the character that corresponds to the two figures :
        the first is the row of the Polybe's table, and the second is 
        the column.
        "row" is the number of the row. It is an integer.
        "column" is the number of the column. It is an integer.
        It returns a string of length 1, the treated character.
    """
    # "character" is the character in the cell with coordinates (row, column).
    # The coordinates are minus 1 because the coordinates of the table are in the
    # range [0; 5].
    character = reversePolybesSquare[row-1][column-1]
    return character


# ---------------------------------------------------------------------------------- #
## Functions level 2

def management_coding_Cesar(sentence, shiftValue):
    """ This function manages the coding and the uncoding of a whole sentence by
        regular shift of letters, also called the method Cesar. It uses the
        coding_Cesar function. The parameter "sentence" is beforehand shaped.
        "sentence" is the sentence to be treated.  It is a string.
        "shiftValue" is the size of the shift. The sentence is coded if the shift 
        value is positive, and undecoded if the shift value is negative.  It is a 
        integer.
        It returns a string, the treated sentence.
    """
    # "finalSentence" is the treated sentence gradualy build
    # "character" is one element of the original sentence. If is a letter, it will be 
    # coded, if it is not a letter (punctuation, space, etc.), it be copied as it is.
    finalSentence =""
    for character in sentence:
        if character.isalpha():
            finalSentence += coding_Cesar(character, shiftValue)
        else:
            finalSentence += character
    return finalSentence

def management_coding_Vigenere(sentence, rawKey, sens):
    """ This function manages the coding and the uncoding of a whole sentence using 
        the Vigenere's code. It uses a alphabetical key in which each letter 
        indicates the shift of the alphabetical character corresponding in the 
        sentence. Normaly the key is smaller as the sentence, so it is repeated as 
        many times as necessary in a bid to make corresponding each alphabetical 
        character of the sentence to be coded (or uncoded) with a letter of the key.
        The Vigenere's code uses the Cesar's coding method. This function do that
        calling the coding_Cesar function.
        Only the alphabetical characters of the sentence are treated.
        "sentence" is the sentence to be treated.  It is a string.
        "rawKey" is the key given by the user. It is a string.
        If "sens" is even, the sentence is coded (positive shift). If sens is odd,
            the sentence is uncoded (negative shift). It is an integer.
        It returns a string, the treated sentence.
    """
    
    finalSentence = ""                        # "finalSentence" is the coded sentence
    characterPointer = 0                        # Pointer on the treated character
    alphaCharacterCount = 0                     # Count of alphabetical characters 
    key = shaping_key(rawKey)                   # shaped key used for the treatment
    sentenceLength= len(sentence)               # length of the treated sentence 
    keyLength = len(key)                        # length of the used key

    while characterPointer < sentenceLength:
        character = sentence[characterPointer]  # character to be treated
        if character.isalpha():
            # The following line computes the rank of the character ("characterKeyRank")
            # of the key that corresponds to the treated character, when the key is 
            # repeated along the alphabetical characters of the treated sentence.
            characterKeyRank = alphaCharacterCount % keyLength 
            characterKey = key[characterKeyRank]
            shiftValue = (-1)**(sens) * (ord(characterKey) - 97)
            finalSentence += coding_Cesar(character, shiftValue)
            characterPointer += 1
            alphaCharacterCount += 1
        else:
            finalSentence += character
            characterPointer += 1
    return finalSentence

def management_coding_Polybe(sentence):
    """ This function receives a sentence, read it, and pour each character, it
        verifies that the read character is available for coding before calling 
        the coding function (coding_Polybe) is necessary.
        "sentence" is the sentence to be treated. It is a string.
        It returns a string, the treated sentence.
    """
    # "finalSentence" is the coded sentence
    # "character" is the read and treated character
    finalSentence = ""
    for character in sentence:
        if character.isalnum():
            finalSentence += coding_Polybe(character)
        else:
            finalSentence += character
    return finalSentence

def management_uncoding_Polybe(sentence):
    """ This function uncodes a sentence coded with the Polybe's square. The problem
        is to well extract the two figures of each code, avoiding the spaces and the
        non alphanumeric characters (punctuation, etc.)
        "sentence" is the sentence to be treated. It is a string.
        It returns a string, the treated sentence.
    """
    # "finalSentence" is the uncoded sentence.
    finalSentence = ""
    pointer = 0                            # pointer on the treated character
    while pointer < (len(sentence)-1):
        if not(sentence[pointer].isnumeric()):
            finalSentence += sentence[pointer]
            pointer += 1
        else:
            character = uncoding_Polybe(int(sentence[pointer]), int(sentence[pointer+1]))
            finalSentence += character
            pointer += 2
    # If the number of characters is even, taking the last character in account.
    if pointer == (len(sentence)-1):
        finalSentence += sentence[pointer]           
    return finalSentence


# ---------------------------------------------------------------------------------- #
## Functions level 3
 
def coding_manager(choice, shiftValue, key, sens, initialSentence):
    """ This function carry out the coding or the uncoding of sentencest under, 
        optional, Cesar coding, ROT13, Vigenere coding or Polybe's square methods.
        The result is a sentence in lower-case, spaces and puntuation are unchanged.
        It uses the functions management_coding_Cesar; management_coding_Vigenere;
        management_coding_Polybe and management_uncoding_Polybe.
        "choice" is the number of the selected method. It is an integer. 
            1 is for Cesar coding method; 
            2 is for ROT13 method;
            3 is for Vigenere coding method;
            4 is for Polybe's square method.
        "shiftValue" is the value of the shift for the Cesar coding method.
            It is an integer in the range [1; 25] (0 and 26 mean no changes).
        "key" is the key used by the Vigenere coding method. It is a string. It
            can be a simple word or a sentence. It must contain a least one 
            alphabetical character, if the Vigenere coding methode is selected.
        "sens" is the sens of the treatment. It is an integer, If it is an even
            number, the treatment is coding. If it is an odd number, the treatment
            is uncoding.
        "initialSentence" is the sentence to be treated. It is a string.
        It returns a string, the treated sentence.
    """
    # "sentenceToBeCoded" is the sentence shaped for the treatment
    # "finalSentence" is the treated sentence
    # Shaping the sentence to let available the treatment
    sentenceToBeCoded = shaping_sentence(initialSentence)

    # Selon le choix de méthode fait, traimenent de la sentence
    if choice == 1:
        finalSentence = management_coding_Cesar(sentenceToBeCoded, (-1)**sens*shiftValue)
    elif choice == 2:
        finalSentence = management_coding_Cesar(sentenceToBeCoded, 13)
    elif choice == 3:
        finalSentence = management_coding_Vigenere(sentenceToBeCoded, key, sens)
    elif choice == 4:
        if sens == 0:
            finalSentence = management_coding_Polybe(sentenceToBeCoded)
        else:
            finalSentence = management_uncoding_Polybe(sentenceToBeCoded)

    return finalSentence