from django.contrib import auth
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the Publisher.")
    website = models.URLField(help_text="The Publisher's website.")
    email = models.EmailField(help_text="The Publisher's email address.")

    def __str__(self):
        return self.name

class Movies_Info(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the Movie.")
    data = models.DateField(verbose_name="Data the movie was released")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through="MovieContributor")

    def __str__(self):
        return self.name

class Contributor(models.Model):
    first_name = models.CharField(max_length=50, help_text="The Contributor's first name")
    last_name = models.CharField(max_length=50, help_text="The contributor's last name or name")
    email = models.EmailField(help_text="The contact email for the contributor.")

    def __str__(self):
        return self.first_name

class MovieContributor(models.Model):
    class ContributionRole(models.TextChoices):
        ACTOR = 'ACTOR', 'Actor'
        DIRECTOR = "DIRECTOR", "Director"
    movie = models.ForeignKey(Movies_Info, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the movie.",
                            choices=ContributionRole.choices, max_length=20)

class Review(models.Model):
    contact = models.TextField(help_text="The Review text.")
    rating = models.IntegerField(help_text="The rating the reviewer has given")
    date_created = models.DateTimeField(auto_created=True,
                                        help_text="The date and time the review was created.")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)

    movie = models.ForeignKey(Movies_Info, on_delete=models.CASCADE,
                              help_text="The Movie that this review is for.")