from django.shortcuts import render, redirect  
from Trainers.forms import TrainerForm  
from Trainers.models import Trainer  
# Create your views here.  
def trn(request):  
    if request.method == "POST":  
        form = TrainerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = TrainerForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    trainers = Trainer.objects.all()  
    return render(request,"show.html",{'trainers':trainers})  
def edit(request, id):  
    trainer = Trainer.objects.get(id=id)  
    return render(request,'edit.html', {'trainer':trainer})  
def update(request, id):  
    trainer = Trainer.objects.get(id=id)  
    form = TrainerForm(request.POST, instance = trainer)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'trainer': trainer})  
def delete(request, id):  
    trainer = Trainer.objects.get(id=id)  
    trainer.delete()  
    return redirect("/show")