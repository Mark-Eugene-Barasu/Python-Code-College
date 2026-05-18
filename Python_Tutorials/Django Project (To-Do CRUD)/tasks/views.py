from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import TaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_list"))
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form, "mode": "create"})


def task_update(request, pk: int):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_detail", kwargs={"pk": task.pk}))
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task_form.html", {"form": form, "mode": "update", "task": task})


def task_detail(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})


def task_delete(request, pk: int):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect(reverse("tasks:task_list"))

    return render(request, "tasks/task_confirm_delete.html", {"task": task})

