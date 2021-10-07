import codecs
import sys

from collections import Counter
from typing import List

from tqdm import tqdm
from janome.analyzer import Analyzer
from janome.tokenfilter import ExtractAttributeFilter, POSKeepFilter


token_filters = [
    POSKeepFilter(['名詞', '動詞']),
    ExtractAttributeFilter('base_form')
]
analyzer = Analyzer(token_filters=token_filters)


def main():
    file_path = sys.argv[1]
    print(f'{sys.argv[1]} を解析')
    tokens: List[str] = analyze(read_file(file_path))
    sorted_tokens: List[str] = count(tokens)
    write_file(sorted_tokens)


def read_file(path: str) -> List[str]:
    with codecs.open(path, 'r', 'utf-8') as f:
        return [row.strip() for row in f]


def write_file(tokens: List[str]):
    with codecs.open('word_count.csv', 'w', 'utf-8') as f:
        for token in tokens:
            f.write(f'{token[0]},{token[1]}')
            f.write('\n')


def analyze(texts: List[str]) -> List[str]:
    tokens = []
    for text in tqdm(texts, desc='解析中'):
        for token in analyzer.analyze(text):
            tokens.append(token)
    return tokens


def count(tokens: List[str]) -> List[str]:
    counter = Counter(tokens)
    items = counter.items()
    return sorted(list(items), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    main()
