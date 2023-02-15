from django.contrib import admin
from .models import Movies_Info, Publisher, Contributor, MovieContributor, Review


# class Movies_InfoAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'date')
#
#     def get_author(self, obj):
#         return obj.Movies_Info.author
#     get_author.short_description = 'Movie'
#     get_author.admin_order_field = 'date'


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'website', 'email')


class MoviesAdmin(admin.ModelAdmin):
    list_filter = ('publisher',)


admin.site.register(Contributor)
admin.site.register(MovieContributor)
admin.site.register(Movies_Info, MoviesAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Review)