from django.db import models
from django.forms import ModelForm

# Create your models here.
class Wallpaper(models.Model):
    photo = models.FileField(upload_to='wallpaper/')
    
    @property
    def imageURL(self):
        if self.photo:
            return self.photo.url
        else:
            return  None
        

class WallpaperForm(ModelForm):
    class Meta:
        model = Wallpaper
        fields = '__all__'
