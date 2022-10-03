from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    news = [{
        'title':'первая статья',
        'text':'полный текс',
        'author': 'Люба',
        'date': '1.09.2007'
    },
    {
        'title': 'первая статья',
        'text': 'полный текс',
        'date': ' 1.09.2007'

    }]
    data = {
        'news': news,
        'title': 'Главная страница'
    }
    return render(request, 'home/home.html', data)

def contacts(request):
    return render(request, 'home/allcontacts.html', {'title': 'Страница контакты!'})

