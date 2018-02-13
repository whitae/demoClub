from django.shortcuts import render
from .models import Case

# Create your views here.
def case_title(request):
    cases = Case.objects.all()
    return render(request, "case/titles.html", {"cases":cases})
