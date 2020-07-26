from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictinary = {}

    for word in words:
        if word in word_dictinary:
            word_dictinary[word]+=1
        else:
            word_dictinary[word]=1
    
    return render(request, 'result.html',{'full': text, 'total':len(words), 'dictinary' :word_dictinary.items()})