""" Solution for http://www.checkio.org/mission/monkey-typing/ in Python 2.7 """

def count_words(text, words):
    
    text = text.lower()
    result = 0
    for word in words:
        if text.find(word) >= 0:
            result += 1
    return result


if __name__ == '__main__':
    #These uu"1sserts" using only for self-checking and not necessary for auto-testing
    assert count_words(u"How aresjfhdskfhskd you?", {u"how", u"are", u"you", u"hello"}) == 3, "Example"
    assert count_words(u"Bananas, give me bananas!!!", {u"banana", u"bananas"}) == 2, "BANANAS!"
    assert count_words(u"Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {u"sum", u"hamlet", u"infinity", u"anything"}) == 1, "Weird text"
