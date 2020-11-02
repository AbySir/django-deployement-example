from django.shortcuts import render

# Create your views here.
def index(request):

    dict = {"key":"value"}
    myc = Circle()
    print("print = " ,myc.area())

    return render(request, 'app/index.html' , context = dict)


class Circle():
    pi = 3.14
    
    def __init__ (self,radius=2):
        self.radius = radius

    def area(self):
        area = self.radius* self.radius * Circle.pi 
        return area

        
