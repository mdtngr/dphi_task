from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, phone, first_name, password=None):
        if not email:
            raise ValueError("Email??????")
        if not phone:
            raise ValueError("Phone??????")

        user = self.model(email=self.normalize_email(email),
                          phone=phone, first_name=first_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, first_name, password):
        user = self.create_user(email=self.normalize_email(
            email), phone=phone, first_name=first_name, password=password)
        user.save(using=self._db)

    def create_superuser(self, email, phone, first_name, password):
        user = self.create_user(email=self.normalize_email(
            email), phone=phone, first_name=first_name, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class UserData(AbstractBaseUser):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    username = models.CharField(max_length=10, default="new_user")

    is_admin = models.BooleanField(verbose_name="admin status", default=False)
    is_staff = models.BooleanField(verbose_name="staff status", default=False)
    is_superuser = models.BooleanField(
        verbose_name="superuser status", default=False)

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    phone = models.CharField(max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'first_name']
    objects = MyAccountManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.first_name+" | "+self.email + " | " + self.phone
        return self.first_name

    class Meta():
        verbose_name = "User Detail Row"
        verbose_name_plural = "User Data"


class PlantDetails(models.Model):
    plant_id = models.IntegerField(primary_key=True)
    plant_name = models.CharField(max_length=40)
    plant_price = models.FloatField(default=0)
    plant_image = models.ImageField(
        upload_to='static_cdn/img', null=True, blank=True)

    def __str__(self):
        return self.plant_name+" | "+"Rs "+str(self.plant_price) + " | "


class OrderDetails(models.Model):
    txn_id = models.IntegerField(primary_key=True)
    plant_id = models.ForeignKey(
        PlantDetails, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(
        UserData, on_delete=models.CASCADE, null=True, blank=True)
    txn_amount = models.FloatField()
    txn_date = models.DateTimeField(default=datetime.now, blank=True)
