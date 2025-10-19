#from django.conf import settings
from django.db import models
from django.urls import reverse

class Order(models.Model):
    name:models.CharField = models.CharField(
        max_length=128,
        unique=True
    )
    slug:models.SlugField = models.SlugField(max_length=128)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def get_absolute_url(self):
        return reverse(
            'birds:family-list',
            args=[
                self.slug,
            ]
        )

    def __str__(self):
        return self.name


class Family(models.Model):
    name:models.CharField = models.CharField(
        max_length=128,
        unique=True
    )
    slug:models.SlugField = models.SlugField(max_length=128)
    order:models.ForeignKey = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='families'
    )

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def get_absolute_url(self):
        return reverse(
            'birds:genus-list',
            args=[
                self.slug,
            ]
        )

    def __str__(self):
        return self.name


class Genus(models.Model):
    name:models.CharField = models.CharField(
        max_length=128,
        unique=True
    )
    slug:models.SlugField = models.SlugField(max_length=128)
    family:models.ForeignKey = models.ForeignKey(
        Family,
        on_delete=models.CASCADE,
        related_name='genuses'
    )
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def get_absolute_url(self):
        return reverse(
            'birds:species-list',
            args=[
                self.slug,
            ]
        )

    def __str__(self):
        return self.name


class Species(models.Model):
    common_name:models.CharField = models.CharField(
        max_length=256,
        unique=True
    )
    slug:models.SlugField = models.SlugField(max_length=256)
    species:models.CharField = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        unique=True
    )
    genus:models.ForeignKey = models.ForeignKey(
        Genus,
        on_delete=models.CASCADE,
        related_name='species',
        null=True,
        blank=True
    )
    link:models.CharField = models.CharField(
        max_length=512,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse(
            'birds:species-detail',
            args=[
                self.id,
            ]
        )

    class Meta:
        ordering = ['common_name']
        indexes = [
            models.Index(fields=['common_name'])
        ]

    def __str__(self):
        return self.common_name


class Location(models.Model):
    name:models.CharField = models.CharField(
        max_length=256,
        unique=True
    )
    slug:models.SlugField = models.SlugField(max_length=256)
    description:models.TextField = models.TextField(
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        return reverse(
            'birds:location-detail',
            args=[
                self.slug
            ]
        )

    class Meta:
        ordering=['name']
        indexes=[
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name


class Event(models.Model):
    date:models.DateField = models.DateField()
    slug:models.SlugField = models.SlugField(max_length=48)
    location:models.ForeignKey = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='events'
    )
    birds:models.ManyToManyField = models.ManyToManyField(
        Species,
        related_name='events'
    )
    comment:models.TextField = models.TextField(
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        return reverse(
            'birds:event-detail',
            args=[
                self.id,
            ]
        )

    class Meta:
        ordering =['-date']
        indexes = [
            models.Index(fields=['-date']),
            models.Index(fields=['location']),
        ]

    def __str__(self):
        return f"{self.location} on {self.date}, {self.birds.count()} birds detected"