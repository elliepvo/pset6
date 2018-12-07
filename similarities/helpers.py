from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # TODO

    lines_a = set(a.split("\n"))
    lines_b = set(b.split("\n"))

    return lines_a & lines_b


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO

    sentences_a = set(sent_tokenize(a))
    sentences_b = set(sent_tokenize(b))

    return sentences_a & sentences_b


def get_substring(a, n):
    substrings = []

    for i in range(len(a) - n + 1):
        substrings.append(a[i:n + i])

    return substrings
    

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO

    substrings_a = set(get_substring(a, n))
    substrings_b = set(get_substring(b, n))

    return substrings_a & substrings_b