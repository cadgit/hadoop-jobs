from __future__ import print_function
import sys

for line in sys.stdin:
    article_id, content = line.split("\t", 1)
    words = content.split("\W+", content)
    for word in words:
        if word:
            print(word, 1, sep="\t")