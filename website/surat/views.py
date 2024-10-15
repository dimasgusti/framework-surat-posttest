from django.shortcuts import render, redirect, get_object_or_404
from .forms import LetterForm
from .models import Letter
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    return render(request, "base.html")


def about(request):
    return render(request, "pages/about.html")


def letter_index(request):
    query = request.GET.get("q")
    letters = Letter.objects.all()
    if query:
        letters = Letter.objects.filter(
            Q(judul_icontains=query) | Q(pesan_icontains=query)
        )
    else:
        letters = Letter.objects.all()
    return render(request, "letter/index.html", {"letters": letters})


@login_required
def letter_create(request):
    if request.method == "POST":
        form = LetterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("letter_index")
    else:
        form = LetterForm()
    return render(request, "letter/create.html", {"form": form})


def letter_update(request, letter_id):
    letter = get_object_or_404(Letter, id=letter_id)
    if request.method == "POST":
        form = LetterForm(request.POST, instance=letter)
        if form.is_valid():
            form.save()
            return redirect("letter_index")
    else:
        form = LetterForm(instance=letter)
    return render(request, "letter/update.html", {"form": form, "letter": letter})


def letter_delete(request, letter_id):
    letter = get_object_or_404(Letter, id=letter_id)
    if request.method == "POST": 
        letter.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False, "error": "Invalid request"})
