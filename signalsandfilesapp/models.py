from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    '''The files uploaded to FileField or ImageField are not stored in the database but in the filesystem.
        FileField and ImageField are created as a string field in the database (usually VARCHAR), containing the reference to the actual file.
        If you delete a model instance containing FileField or ImageField,
        Django will not delete the physical file, but only the reference to the file.'''

    image = models.ImageField(upload_to='pictures/', default='profilepicture.png')
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
