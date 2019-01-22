from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text=request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    # <단어 : 몇번 단어 : 몇번>

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1

    # 총 단어수 = len(word)
    return render(request, 'result.html', {'full':text, 'total' : len(words), 'dictionary' : word_dictionary.items()})