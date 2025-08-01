from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import pdfDataForm
from .models import pdfData


# Create your views here.
def index(request):

    item_list = pdfData.objects.order_by("-date")
    if request.method == "POST":
        form = pdfDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pdfs')
    form = pdfDataForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "PDFS",
    }
    return render(request, 'pdfs/index.html', item_list)

def get(request, item_id):
    item = pdfData.objects.get(id=item_id)
    return render(request, 'pdfs/index.html', item)

def remove(request, item_id):
    item = pdfData.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('pdfs')
