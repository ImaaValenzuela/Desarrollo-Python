def palindromo(sentence: str) -> bool:
    """ Permite conocer si un string, es o no, un palindromo.

    Args:
        sentence : string

    Return:
        bool
    """

    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence [::-1]