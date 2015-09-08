""" Solution for http://www.checkio.org/mission/morse-clock/ in Python 2.7 """

def char_to_bin(a, length=4):
    result = ""
    for bit in bin(int(a))[2:]:
        result += {"0": ".", "1": "-"}[bit]
        
    return result.rjust(length, ".") + " "

def number_to_bin_morse(number, first_length):
    if len(number) == 1:
        return ("." * first_length) + " " + char_to_bin(number)
    else:
        return char_to_bin(number[0], first_length) + char_to_bin(number[1])
    
def checkio(time_string):
    parts = time_string.split(":")
    return number_to_bin_morse(parts[0], 2) + ": " + number_to_bin_morse(parts[1], 3) + ": " + number_to_bin_morse(parts[2], 3).strip()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio(u"21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio(u"00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio(u"23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

