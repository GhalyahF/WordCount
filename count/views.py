import operator
from django.shortcuts import render

def home(request):
    return render (request, 'home.html')

def count(request):
    fulltext= request.GET['fulltext']
    wordlist= fulltext.split()
    count= len(wordlist)
    worddict= {}

    for word in wordlist:
        if word in worddict:
            worddict[word]+= 1
        else:
            worddict[word]= 1

    sortedwords= sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    context={
    'fulltext':fulltext,
    'wordlist': wordlist,
    'sortedwords':sortedwords,
    'count':count,
    }
    return render (request, 'count.html', context)
