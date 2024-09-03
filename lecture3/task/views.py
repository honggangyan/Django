from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django import forms

#session remembers who you are and store individual data

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "new task")
    priority = forms.IntegerField(label = "priority",min_value = 1, max_value= 3)

def index(request):
    if "task" not in request.session:
        request.session["task"] = []
    return render(request, "task/index.html", {
        "task":request.session["task"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            new_task = form.cleaned_data["task"]    
            request.session["task"] += [new_task]
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request, "task/add.html",{
                "form": form
            })
    return render(request, "task/add.html", {
        "form":NewTaskForm
    })
