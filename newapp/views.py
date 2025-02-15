from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from .models import Member


def Board(request):
    mem=Member.objects.all()
    return render(request,'Board_list.html',{"mem":mem})

def Write(request):
    return render(request,"Board_write.html")


def Saverec(request):
    if request.method == "POST":
        x = request.POST.get('title')  
        y = request.POST.get('name')
        z = request.POST.get('details')

        if x and y and z:  
            mem = Member(title=x, name=y, details=z)
            mem.save()
            return redirect("/")  
        else:
            return HttpResponse("All fields are required!", status=400)  

    return HttpResponse("Invalid request", status=405)  




def Delete(request, id):
    if not Member.objects.filter(id=id).exists():
        return HttpResponse("Error: Member not found", status=404) 

    mem = get_object_or_404(Member, id=id)  
    mem.delete()
    return redirect("/") 



def View(request, id):
    mem = get_object_or_404(Member, id=id)  
    return render(request, 'Board_view.html', {'mem': mem})  


def Edit(request, id):
    mem = get_object_or_404(Member, id=id) 

    if request.method == "POST":
        mem.title = request.POST.get("title")
        mem.name = request.POST.get("name")
        mem.details = request.POST.get("details")
        mem.save()

        return redirect("/") 

    return render(request, "Board_edit.html", {"mem": mem})  