from django.db import models

class Story(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Page(models.Model):
    story = models.ForeignKey(Story)
    page_number = models.IntegerField()

    image = models.ImageField()
    music = models.FileField()

    def __str__(self):
        return "Page %d of %s" % (self.page_number, self.story)
