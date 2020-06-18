from django.http import JsonResponse
from django.shortcuts import render
import operator as op


def home(request):
    return render(request, 'home.html')


def get_count(request):
    word_count = dict()
    word_count2 = dict()
    word_count3 = dict()
    for line in open('D:/PY/Spark/file/tags_count.txt', 'r', errors='ignore',encoding='utf-8'):
        data = line.strip('\n').strip('(').strip(')')
        one_data = data.split(',')
        word = one_data[0].strip('\'')
        count = one_data[1]
        word_count[word] = int(count)
    for k in sorted(word_count, key=word_count.__getitem__, reverse=True):
        word_count2[k] = word_count[k]
    for i, (k, v) in enumerate(word_count2.items()):
        word_count3[k] = v
        if i == 19:
            break
    return JsonResponse(word_count3)

def get_count2(request):
    word_count = dict()
    word_count2 = dict()
    word_count3 = dict()
    for line in open('D:/PY/Spark/file/tags_count.txt', 'r', errors='ignore',encoding='utf-8'):
        data = line.strip('\n').strip('(').strip(')')
        one_data = data.split(',')
        word = one_data[0].strip('\'')
        count = one_data[1]
        word_count[word] = int(count)
    for k in sorted(word_count, key=word_count.__getitem__, reverse=True):
        word_count2[k] = word_count[k]
    for i, (k, v) in enumerate(word_count2.items()):
        if i >= 20:
            word_count3[k] = v
        if i==39:
            break
    return JsonResponse(word_count3)
