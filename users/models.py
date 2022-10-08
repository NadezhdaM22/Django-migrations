from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')
    #/www.iconfinder.com/

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'

    def save(self, *arg, **kwargs):
        super().save()

        image=Image.open(self.img.path)

        if image.width > 256 or image.height > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'