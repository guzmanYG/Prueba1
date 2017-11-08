from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField,RichTextUploadingFormField



# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=200)
    contenido=RichTextUploadingField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class upload(models.Model):

    NombreDoc=models.CharField(max_length=50),
    documento=models.FileField(upload_to='documentos')