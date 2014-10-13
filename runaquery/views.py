from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import EnterDataForm


# Create your views here.
def enterdata(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EnterDataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/runaquery/showdata/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EnterDataForm()

    return render(request, 'runaquery/enterdata.html', {'form': form})


def showdata(request):
    return render(request, 'runaquery/showdata.html')

