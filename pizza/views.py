from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    view to redirect the user to their specific dashboard
    '''

    return render(request,'index.html')