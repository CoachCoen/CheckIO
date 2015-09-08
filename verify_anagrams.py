"""Solution for http://www.checkio.org/mission/verify-anagrams/, in Python 2.7"""

def verify_anagrams(first_word, second_word):
    first_word = first_word.replace(" ", "").lower()
    second_word = second_word.replace(" ", "").lower()
    if len(first_word) != len(second_word):
        return False
        
    first_word = list(first_word)
    second_word = list(second_word)
        
    first_word.sort()
    second_word.sort()
    for i in range(len(first_word)):
        if first_word[i] != second_word[i]:
            return False
    return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams(u"a", u"z"), bool), "Boolean!"
    assert verify_anagrams(u"Programming", u"Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams(u"Hello", u"Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams(u"Kyoto", u"Tokyo") == True, "The global warming crisis of 3002"
