from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    request.session['counter'] = 0
    return redirect('/random_word')

def random_word(request):

    request.session['counter'] += 1
    context = {
        "palabra" : get_random_string(length=14)
    }
    return render(request, 'randomword.html', context)