from django.shortcuts import render
import datetime
# Create your views here.
def filters(request):
    dt=datetime.datetime.now()
    d={'data':'Performing Filters Methods','dt':dt,'c':2}
    return render(request,'filters.html',d)