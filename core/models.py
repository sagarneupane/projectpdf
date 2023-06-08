from django.db import models

# Create your models here.
class PDFFile(models.Model):
    file = models.FileField(upload_to='pdf_files/')