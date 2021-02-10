import opencc

converter = opencc.OpenCC('s2t')


def s2t(content):
    return converter.convert(content)
