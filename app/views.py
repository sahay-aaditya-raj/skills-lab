from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class HomezView(View):
    context = {}
    def get(self, request, *args, **kwargs):
        return render(request,'home.html',)

    
    
class Knowledge(View):
    def get(self, request):
        return render(request,'knowledge.html')
    
class Research(View):
    def get(self, request):
        return render(request,'research.html')
    
    
class Publications(View):
    def get(self, request):
        return render(request, 'publications.html')
    
    
class Events(View):
    def get(self, request):
        return render(request, 'events.html')