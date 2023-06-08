from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import PDFFile
from .forms import PDFFileForm

def pdf_view(request, pdf_id):
    pdf_file = PDFFile.objects.get(id=pdf_id)
    domain = request.META["HTTP_HOST"]
    return render(request, 'pdf_view.html', {'pdf_file': pdf_file,"domain":domain})




def upload_pdf(request):
    if request.method == 'POST':
        form = PDFFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_view')
    else:
        form = PDFFileForm()
    return render(request, 'upload_pdf.html', {'form': form})