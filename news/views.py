from django.shortcuts import render

def publications_list(request):
    return render(request, 'news/publications_list.html', {})