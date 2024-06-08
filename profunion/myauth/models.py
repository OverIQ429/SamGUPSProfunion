from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

def user_avatar_directory_path(instance: "User", filename: str) -> str:
    return "users/users_{pk}/avatars/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )

phone_regex = RegexValidator(regex=r'^\+7\d{10}$', message="Phone number must be entered in the format: '+79999999999'. Up to 10 digits allowed.")

class AllGroups(models.Model):
    groupname = models.CharField(max_length=10)
    course = models.IntegerField()
    faculty = models.CharField(max_length=100)

    def __str__(self):
        return self.groupname


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=14)
    lastname = models.CharField(null=True, max_length=14)
    secondname = models.CharField(null=True, max_length=14)
    group = models.ForeignKey(AllGroups,null=True, on_delete=models.CASCADE )
    email = models.EmailField(null=True, max_length=254)
    phone_number = models.CharField(validators=[phone_regex],null=True, max_length=12)
    agreement_accepted = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True, upload_to=user_avatar_directory_path)
    is_union_member = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
class Description(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Decision(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
class Appends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.ForeignKey(Description,null=True, on_delete=models.CASCADE)
    file = models.FileField(null=True ,upload_to='appends/receipts/')
    decision = models.ForeignKey(Decision,null=True, on_delete=models.CASCADE)
    commentary = models.TextField(null=True, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

class News_Type(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Photo(models.Model):
    image = models.ImageField(upload_to="photo")
class News(models.Model):
    type = models.ForeignKey(News_Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    article = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='images')
    images = models.ManyToManyField(Photo)
    document = models.FileField(upload_to='document', null=True)