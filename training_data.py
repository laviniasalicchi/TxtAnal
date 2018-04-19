import json
import jsonlines
import io
import pickle
import numpy as np
import tokenize


def getData():
    datas = []
    target = []

    '''{
        "id": "<instance id>",
        "postTimestamp": "<weekday> <month> <day> <hour>:<minute>:<second> <time_offset> <year>",
        "postText": ["<text of the post with links removed>"],
        "postMedia": ["<path to a file in the media archive>"],
        "targetTitle": "<title of target article>",
        "targetDescription": "<description tag of target article>",
        "targetKeywords": "<keywords tag of target article>",
        "targetParagraphs": ["<text of the ith paragraph in the target article>"],
        "targetCaptions": ["<caption of the ith image in the target article>"]
    }'''

    file_inst = 'datasets/1/instances.jsonl'
    with jsonlines.open(file_inst) as reader:
        for instances in reader:
            datas.append(instances)




    '''{
        "id": "<instance id>",
        "truthJudgments": [<number in [0,1]>],
        "truthMean": <number in [0,1]>,
        "truthMedian": <number in [0,1]>,
        "truthMode": <number in [0,1]>,
        "truthClass": "clickbait | no-clickbait"
      }'''

    file_truth = 'datasets/1/truth.jsonl'
    with jsonlines.open(file_truth) as reader:
        i=0
        for truths in reader:
            target.append(truths)
            '''if target[i]['truthClass'] == 'clickbait':
                print(i)
                print(datas[i])
            '''
            i=i+1

    return datas, target

getData()
