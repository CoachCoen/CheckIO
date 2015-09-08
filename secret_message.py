""" Solution for http://www.checkio.org/mission/secret-message/ in Python 2.7 """

def find_message(text):
    """Find a secret message"""
    
    result = ""
    for a in text:
        if a.isupper():
            result += a
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message(u"How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message(u"hello world!") == "", "Nothing"
    assert find_message(u"HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
