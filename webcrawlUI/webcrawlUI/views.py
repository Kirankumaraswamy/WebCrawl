from django.shortcuts import render, redirect
from webCrawl.sample import hello

import sys
sys.path.append("..")


# Create your views here.

def home(request):
    print(sys.path)
    return render(request, 'webcrawlUI/home.html')


def runWebCrawlTask(request):
    print("Helloooooooooooooo")
    hello()

    return redirect('/webCrawl')
