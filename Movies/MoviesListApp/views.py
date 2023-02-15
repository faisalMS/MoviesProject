from django.shortcuts import render, get_object_or_404, redirect
from .models import Movies_Info, Publisher
from .utils import average_rating
from .forms import PublisherForm
from django.contrib import messages


def Movies_list(request):
    Movies = Movies_Info.objects.all()
    Movies_list = []
    for Movie in Movies:
        reviews = Movie.review_set.all()
        if reviews:
            Movie_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            Movie_rating = None
            number_of_reviews = 0

        Movies_list.append({'Movie': Movie, 'Movie_rating': Movie_rating, 'number_of_reviews': number_of_reviews})

    context = {'Movies_list': Movies_list}
    return render(request, 'MoviesListApp/Movies_list.html', context)


def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None

    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            update_publisher = form.save()
            if publisher is None:
                messages.success(request, "Publisher \"{}\" was created.".format(update_publisher))
            else:
                messages.success(request, "Publisher \"{}\" was update.".format(update_publisher))
            return redirect("publisher_edit", update_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)
    return render(request, "forms.html", {"method": request.method, "form": form})