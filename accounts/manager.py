from django.contrib.auth.models import  UserManager

class CustomUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('الحقل email مطلوب')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('يجب أن تكون is_staff=True للمشرف.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('يجب أن تكون is_superuser=True للمشرف.')

        return self.create_user(email, password, **extra_fields)
