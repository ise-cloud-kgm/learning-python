def delete_odd_indexes(text):
    """Удаляет нечётные индексы в тексте.

    :param text: принимаемый текст
    :type text: str

    :rtype: str
    :return: строка, в которой символы выводятся "через один" (0, 2, 4, ...)
    """
    if len(text) == 0:
        return text
    return text[0] + delete_odd_indexes(text[2:])


print(delete_odd_indexes('Mike Tyson'))
