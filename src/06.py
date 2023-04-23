import re
from os.path import dirname, join
from typing import List

from gensim import corpora, models
from nltk.corpus import stopwords
from nltk.text import TextCollection

STOPWORDS = stopwords.words("chinese")

CORPUS_DIR = join(dirname(__file__), "in")

CHINESE_BIG_NUMBERS = [
    "零",
    "壹",
    "贰",
    "叁",
    "肆",
    "伍",
    "陆",
    "柒",
    "捌",
    "玖",
    "拾",
]
WORD_PATTERN = re.compile(r"([^\s]+?)/[a-vz]+?\b")

CORPUS: List[List[str]] = []
for filename in (join(CORPUS_DIR, f"明朝那些事儿·{i}.txt") for i in CHINESE_BIG_NUMBERS[1:8]):
    with open(filename, "r", encoding="gbk") as f:
        CORPUS.append([w for w in WORD_PATTERN.findall(f.read()) if w not in STOPWORDS])

dic = corpora.Dictionary(CORPUS)

# train the model
# corpus = [dic.doc2bow(text) for text in CORPUS]
# tfidf = models.TfidfModel(corpus)
# tfidf.save("tfidf.model")

tfidf = models.TfidfModel.load(join(dirname(__file__), "tfidf.model"))

for i, book in enumerate(CORPUS, 1):
    print(f"第 {i} 部书的关键词：")
    string_bow = dic.doc2bow(book)
    string_tfidf = tfidf[string_bow]
    string_tfidf.sort(key=lambda x: x[1], reverse=True)
    for word_id, score in string_tfidf[:5]:
        print(f"{dic[word_id]}：{score:.3f}")
