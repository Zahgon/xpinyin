import re
from pathlib import Path
from typing import List, Optional

from xpinyin.combs import get_combs

PinyinToneMark = {
    0: "aoeiuv\u00fc",
    1: "\u0101\u014d\u0113\u012b\u016b\u01d6\u01d6",
    2: "\u00e1\u00f3\u00e9\u00ed\u00fa\u01d8\u01d8",
    3: "\u01ce\u01d2\u011b\u01d0\u01d4\u01da\u01da",
    4: "\u00e0\u00f2\u00e8\u00ec\u00f9\u01dc\u01dc",
}


class Pinyin:
    """Translate Chinese hanzi to pinyin (æ‹¼éŸ³) by Python, æ±‰å­—è½¬æ‹¼éŸ³

    Usage
    -----
    ::

        >>> from xpinyin import Pinyin
        >>> p = Pinyin()
        >>> # default splitter is `-`
        >>> p.get_pinyin("ä¸Šæµ·")
        'shang-hai'
        >>> # show tone marks
        >>> p.get_pinyin("ä¸Šæµ·", tone_marks='marks')
        'shÃ ng-hÇŽi'
        >>> p.get_pinyin("ä¸Šæµ·", tone_marks='numbers')
        >>> 'shang4-hai3'
        >>> # remove splitter
        >>> p.get_pinyin("ä¸Šæµ·", '')
        'shanghai'
        >>> # set splitter as whitespace
        >>> p.get_pinyin("ä¸Šæµ·", ' ')
        'shang hai'
        >>> p.get_initial("ä¸Š")
        'S'
        >>> p.get_initials("ä¸Šæµ·")
        'S-H'
        >>> p.get_initials("ä¸Šæµ·", '')
        'SH'
        >>> p.get_initials("ä¸Šæµ·", ' ')
        'S H'
        >>> # get_initials with retroflex, #39
        >>> p.get_initials("ä¸Šæµ·", splitter='-', with_retroflex=True)
        'SH-H'
        >>> # get combinations of the multiple readings of the characters
        >>> p.get_pinyins('æ¨¡åž‹', splitter=' ', tone_marks='marks')
        ['mÃ³ xÃ­ng', 'mÃº xÃ­ng']
        >>> p.get_pinyins('æ¨¡æ ·', splitter=' ', tone_marks='marks')
        ['mÃ³ yÃ¡ng', 'mÃ³ yÃ ng', 'mÃ³ xiÃ ng', 'mÃº yÃ¡ng', 'mÃº yÃ ng', 'mÃº xiÃ ng']
    """

    data_path = Path(__file__).resolve().with_name('Mandarin.dat')

    def __init__(self, data_path: str = str(data_path)) -> None:
        lines = Path(data_path).read_text().splitlines()
        self.pinyins = dict(tuple(line.split('\t', maxsplit=1)) for line in lines)

    @staticmethod
    def decode_pinyin(s: str) -> str:
        pass

    @staticmethod
    def convert_pinyin(word: str, convert: str) -> str:
        pass

    def get_pinyins(self, chars: str, splitter: str = '-',
                    tone_marks: Optional[str] = None, convert: str = 'lower', n: int = 10) -> List[str]:
        """
        Get All pinyin combinations given all possible readings of each character.
        The number of combinations is limited par default to 10 to avoid exponential explosion on long texts.
        """
        pass

    def get_pinyin(self, chars: str, splitter: str = '-',
                   tone_marks=None, convert: str = 'lower') -> str:

        pass

    def get_initial(self, char: str, with_retroflex: bool = False) -> str:
        pass

    def get_initials(self, chars: str, splitter: str = '-', with_retroflex: bool = False):
        pass
