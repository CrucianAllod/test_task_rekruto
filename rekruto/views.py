from django.shortcuts import render
from django.http import HttpResponse

def home(request):
        if request.method == "GET":
            name = request.GET.get('name', None)
            message = request.GET.get('message', None)

            content = {
                'name': name,
                'message': message
            }

            return render(request, 'rekruto/home.html', content)


