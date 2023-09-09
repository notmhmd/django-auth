from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password=None, user_type=1, **extra_fields):
        from .models import USER, ADMIN, STAFF
        if not email:
            raise ValueError('Email is Required')

        extra_fields.setdefault('is_active', True)

        if user_type == USER:
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)

        if user_type == ADMIN:
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', True)

        if user_type == STAFF:
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', False)

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
