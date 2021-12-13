from django.db import models


# Create your models here.
class User(models.Model):
    """
    This model is created for user login creation with django form.
    """

    class Meta:
        db_table = "user_record"

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    username = models.EmailField(max_length=25)
    password = models.CharField(max_length=15)

    def __str__(self):
        ret = self.username
        return ret


class MessageData(models.Model):
    """
    This model is created for user login creation with django form.
    """

    class Meta:
        db_table = "message_record"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_message"
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    message = models.CharField(max_length=255)

    def __str__(self):
        ret = self.message
        return ret
