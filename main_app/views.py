from django.shortcuts import render

# keeping this here for reference of what we did first before using the render shortcut:
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ </h1>')

# Define some dummy/mock cat data
class Cat():
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

cats = [
    Cat('Lolo', 'tabby', 'foul little demon', 3),
    Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Cat('Raven', 'black tripod', '3 legged cat', 4),
]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    # render always takes request as its first parameter and then the view template
    # if the template was inside of a folder inside of templates it would be 'cats/about.html'

def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats})
    # Dango allows us to pass a third parameter to render called a context dictionary that we can inject inside of our template