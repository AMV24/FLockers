from django.shortcuts import render
from django.views import generic

# Create your views here.
class Index(generic.View):
    template = 'home/index.html'
    context = {}

    def get(self, request):
        self.context = {
            'name': 'Abraham'
        }

        return render(request, self.template, self.context)