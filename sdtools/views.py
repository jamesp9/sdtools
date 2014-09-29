from django.shortcuts import render_to_response

def menupage(request):
    return render_to_response('index.html')
