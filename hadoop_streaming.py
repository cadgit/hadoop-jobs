#!/usr/bin/env python

import sys
import re

# Wikipedia dataset location in HDFS: /data/wiki/en_articles_part
# "Stop words" dataset is located in '/datasets/stop_words_en.txt’ file in local filesystem.
# Format: article_id <tab> article_text

reload(sys)
sys.setdefaultencoding('utf-8')

for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        continue
    text = re.sub("^\W+|\W+$", "", text, flags=re.UNICODE)
    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)

    # your code goes here