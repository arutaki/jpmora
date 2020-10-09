from sudachipy import tokenizer
from sudachipy import dictionary

def jpmora(s: str) -> int:
    """
    Given a Japanese string 's', return the number of mora in a given string.

    :param s: Japanese string
    """
    # Characters exempted from mora counting
    excp = {"。",
            "、",
            "　",
            " ",
            "ャ",
            "ュ",
            "ョ",
            "ァ",
            "ィ",
            "ゥ",
            "ェ",
            "ォ"}

    # Tokenize the Japanese strings
    tokenizer_obj = dictionary.Dictionary().create()
    mode = tokenizer.Tokenizer.SplitMode.C
    m = tokenizer_obj.tokenize(s, mode)[0]
    
    # Count the mora
    n_mora = len([mora for mora in m.reading_form() if mora not in excp])
    return n_mora
