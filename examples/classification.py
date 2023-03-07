# -*- coding: utf-8 -*-

import os
from pprint import pprint

from lanno.config import Tasks, Languages, OpenAIModels, ClassificationFormatter
from lanno import GPTModel, GPTAnnotator

print('All Supported Tasks:', Tasks.list_attributes())
print('All Supported Languages:', Languages.list_attributes())
print('All Supported NERFormatter:', ClassificationFormatter.list_attributes())
print('All Supported OpenAIModels:', OpenAIModels.list_attributes())

api_key = os.getenv('OPENAI_KEY')
model = GPTModel(api_key, model=OpenAIModels.ChatGPT)

# 1. english example
annotator = GPTAnnotator(model,
                         task=Tasks.Classification,
                         language=Languages.EN,
                         label_mapping={
                            "positive": 'POS',
                            'negative': 'NEG'})
doc = '''The food is very awful, I don't like it'''
# w/o hint, w/o formatted result
# ret = annotator(doc)
# w/o hint, w/ formatted result
# ret = annotator(doc, formatter=NERFormatter.BIO)
# w/ hint, w/ formatted result
hint = 'This domain is sentiment classification. The label positive means positive sentiment, negative stands negative sentiment'
ret = annotator(doc, hint=hint, formatter=ClassificationFormatter.JSONL)
print('english output:')
pprint(ret)

# 2. chinese example
annotator = GPTAnnotator(model,
                         task=Tasks.Classification,
                         language=Languages.ZH_CN,
                         label_mapping={
                            "正向": 'POS',
                            '负向': 'NEG'})
hint = '这是一个情感分类任务，正向代表正面情感，负向代表负面情感'
doc = '这家店的太太难吃了，下次再也不来了'
ret = annotator(doc, hint=hint, formatter=ClassificationFormatter.JSONL)
print('chinese output:')
pprint(ret)