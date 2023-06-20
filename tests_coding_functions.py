# -*- coding:Utf-8 -*-
# Author : Jacques Hoschtettler
# may 2023

from coding_functions import *


# ---------------------------------------------------------------------------------- #
## Constants
typeSentence = "Portez ce vieux whisky au juge blond qui fume."

# ---------------------------------------------------------------------------------- #
## Functions tests of functions level 0

def test_shaping_sentence():
    print("Test of the sentence shaping")
    assert shaping_sentence("àâèèêëîïôùûç") == "aaeeeeiiouuc"
    print(".", end="")
    print("\n\tAll is right.\n")

def test_shaping_key():
    print("Test of the key shaping (Vigenere coding)")
    assert shaping_key("Bonjour, l'élève est français !") == "bonjourleleveestfrancais"
    print(".", end="")
    print("\n\tAll is right.\n")

def test_cutting_long_sentence():
    print("Test of the sentence cutting")
    assert cutting_long_sentence(typeSentence, 25) == ("Portez ce vieux whisky au\njuge blond qui fume.", 2)
    print(".", end="")
    assert cutting_long_sentence(typeSentence, 46) == (typeSentence, 1)
    print(".", end="")
    print("\n\tAll is right.\n")

# ---------------------------------------------------------------------------------- #
## Functions tests of functions level 1

def test_coding_Cesar():
    print("Test of function Cesar coding method")
    assert coding_Cesar("a", 3) == "d" 
    print(".", end="")
    assert coding_Cesar("x", 3) == "a" 
    print(".", end="")
    assert coding_Cesar("z", 3) == "c" 
    print(".", end="")
    assert coding_Cesar("d", -3) == "a" 
    print(".", end="")
    assert coding_Cesar("a", -3) =="x" 
    print(".", end="")
    assert coding_Cesar("c", -3) =="z" 
    print(".", end="")   
    assert coding_Cesar("a", 13) =="n"
    print(".", end="")
    assert coding_Cesar("m", 13) =="z"
    print(".", end="")
    assert coding_Cesar("n", 13) == "a"
    print(".", end="")
    assert coding_Cesar("z", 13) =="m"
    print(".", end="")   
    assert coding_Cesar("a", 26) == "a"
    print(".", end="")
    assert coding_Cesar("z", 26) == "z"
    print(".", end="")
    assert coding_Cesar("a", -26) == "a"
    print(".", end="")
    assert coding_Cesar("z", -26) == "z"
    print(".", end="")    
    print("\n\tAll is right.\n")

def test_coding_Polybe():
    print("Test of Polybe's square coding method")
    assert coding_Polybe("a") == "11"
    print(".", end="")
    assert coding_Polybe("z") == "52"
    print(".", end="")
    assert coding_Polybe("9") == "66"
    print(".", end="")
    print("\n\tAll is right.\n")

def test_uncoding_Polybe():
    print("Test of Polybe's square uncoding method")
    assert uncoding_Polybe(1, 1) == "a"
    print(".", end="")
    assert uncoding_Polybe(5, 2) == "z"
    print(".", end="")
    assert uncoding_Polybe(6, 6) == "9"    
    print(".", end="")
    print("\n\tAll is right.\n")


# ---------------------------------------------------------------------------------- #
## Functions tests of functions level 2

def test_management_coding_Cesar():
    print("Test de la management du chiffrement César")
    assert management_coding_Cesar("abcde fghij.klmnop1qrstuv!wxyz?", 10) == "klmno pqrst.uvwxyz1abcdef!ghij?"
    print(".", end="")
    assert management_coding_Cesar("klmno pqrst.uvwxyz1abcdef!ghij?",-10) == "abcde fghij.klmnop1qrstuv!wxyz?"
    print(".", end="")
    print("\n\tAll is right.\n")

def test_management_coding_Vigenere():
    print("Test of management of Vigenere coding method")
    assert management_coding_Vigenere("j'adore ecouter la radio toute la journee !", \
                                        "Musique", 0) == "v'uvwhy ioimbul pm lslyi xaolm bu naojvuy !"
    print(".", end="")
    assert management_coding_Vigenere("comment allez vous aujourd'hui ?", "Le vent souffle !", 0) \
                                        == "nshqrgl ofqjk zzyn ehcgili'mfm ?"
    print(".", end="")
    assert management_coding_Vigenere("v'uvwhy ioimbul pm lslyi xaolm bu naojvuy !", "musique", 1) \
                                         == "j'adore ecouter la radio toute la journee !"
    print(".", end="")    
    assert management_coding_Vigenere("nshqrgl ofqjk zzyn ehcgili'mfm ?", "Le vent souffle !", 1) \
                                        == "comment allez vous aujourd'hui ?"
    print(".", end="")  
    print("\n\tAll is right.\n")

def test_management_coding_Polybe():
    print("Test of management of Polybe's square coding method")
    assert management_coding_Polybe("voici une phrase-test ! 2003") \
            == "4433231323 433215 342236114115-42154142 ! 55535356"
    print(".", end="")
    print("\n\tAll is right.\n")

def test_management_uncoding_Polybe():
    print("Test of management of Polybe's square uncoding method")
    assert management_uncoding_Polybe("4433231323 433215 342236114115-42154142 ! 55535356") \
                == "voici une phrase-test ! 2003"
    print(".", end="")
    print("\n\tAll is right.\n")


# ---------------------------------------------------------------------------------- #
## Functions tests of functions level 3

def test_coding_manager():
    print("Test of management of (un)coding methods")
    assert coding_manager(1, 3, "", 0, typeSentence) =="sruwhc fh ylhxa zklvnb dx mxjh eorqg txl ixph."
    print(".", end="")
    assert coding_manager(1, 3, "", 1, "sruwhc fh ylhxa zklvnb dx mxjh eorqg txl ixph.") == \
    "portez ce vieux whisky au juge blond qui fume."
    print(".", end="")
    assert coding_manager(2, 1, "", 0, typeSentence) =="cbegrm pr ivrhk juvfxl nh whtr oybaq dhv shzr."
    print(".", end="")
    assert coding_manager(2, 1, "", 1, "cbegrm pr ivrhk juvfxl nh whtr oybaq dhv shzr.") == \
    "portez ce vieux whisky au juge blond qui fume."
    print(".", end="")
    assert coding_manager(3, 1, "La vie est belle !", 0, typeSentence) =="aombid ux wmpfb hhdaoc sn kyrp fwoil uya yvqp."
    print(".", end="")
    assert coding_manager(3, 1, "La vie est belle !", 1, "aombid ux wmpfb hhdaoc sn kyrp fwoil uya yvqp.") == \
    "portez ce vieux whisky au juge blond qui fume."
    print(".", end="")
    assert coding_manager(4, 1, "", 0, typeSentence) == \
        "343336421552 1315 4423154346 452223412551 1143 24432115 1226333214 354323 16433115."
    print(".", end="")
    assert coding_manager(4, 1, "", 1, 
        "343336421552 1315 4423154346 452223412551 1143 24432115 1226333214 354323 16433115.") == \
    "portez ce vieux whisky au juge blond qui fume."
    print(".", end="")

    print("\n\tAll is right.\n")


# ---------------------------------------------------------------------------------- #
## Tests

# Shapings tests
test_shaping_sentence()
test_shaping_key()
test_cutting_long_sentence()

# Cesar coding tests
test_coding_Cesar()
test_management_coding_Cesar()

# Vigenere coding tests
test_management_coding_Vigenere()

# Polybe's square coding tests
test_coding_Polybe()
test_management_coding_Polybe()
test_uncoding_Polybe()
test_management_uncoding_Polybe()

# Coding management tests
test_coding_manager()

