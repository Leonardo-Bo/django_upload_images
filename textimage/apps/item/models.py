from django.db import models


def image_upload_to(instance, filename):
    return "{}/{}".format(instance.textmodel.pk, filename)


class TextModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title", unique=True)
    content = models.TextField(verbose_name="Content")

    def __str__(self):
        return self.title


class ImageModel(models.Model):
    reftext = models.ForeignKey(TextModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_to)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
