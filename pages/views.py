from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def pagesIndex(request):
    return HttpResponse ("Hello from pages index")

def pagesAbout(request):
    return HttpResponse ("Hello from pages about")

def renderHtml(request):
    # dic ={"user":"marwa","name":"ahmed @@@@ ali","salary":100000}
    newdic =[{"user":"ahmed","salary":100000},{"user":"omar","salary":200000}]
    dic = {"users" : newdic}
    return render(request,'pages/index.html',dic)

def renderHtml2(request):
    dic = {"user" :"hello"}
    return render(request,'pages/about.html',dic)

def showAllProjects(request):
    return render(request,'pages/showAllProjects.html',{"projects":Project.objects.all().order_by('id')}) #=> return all elements
    #  return render(request,'pages/cars.html', {"car":Car.objects.get(name ="bmw")})  #=> get return only one element
    # return render(request,'pages/cars.html', {"cars":Car.objects.filter(name = "car2")})  #filterlazm andeha bloop 
    # cars = Car.objects.all().filter(price__exact='99')
    #  cars = Car.objects.all().filter(price__contains='99')
    #  cars = Car.objects.all().order_by('model').exclude(name="lancer")
    #  dic = {"cars":cars}
    #  return render(request,'pages/cars.html', dic)
 


from .forms import ProjectForm
def createProject(request):
    project = ProjectForm(request.POST, request.FILES)
    if project.is_valid():
        project.save()
    else :
        print("not valid")
    return render(request,'pages/createProject.html',{"form" :  ProjectForm})



def showProjectWithid (request,id):
    project= Project.objects.get(pk = id)
    return render(request,'pages/projectDetails.html',{"project" : project})
    # return HttpResponse(project)

def deleteProjectWithid  (request,id):
    project= Project.objects.get(pk = id)
    project.delete()
    projects = Project.objects.all().order_by('id')
    return render(request,'pages/showAllProjects.html',{"projects" : projects})
    # return HttpResponse(project)