from django import forms

RADIO_CHOICES = (
    ("Value One", "Value One Display"),
    ("Value Two", "Text for value Two"),
    ("Value Three", "Value Three's Display Text")
)


MOVIE_CHOICES = (
    ("Non-fiction", (("1", "Movie X",), ("2", "Movie Z"))),
    ("Fiction", (("3", "Movie A"), ("4", "Movie B")))
)


class ExampleForm(forms.Form):
    text_input = forms.CharField(max_length=3)
    password_input = forms.CharField(min_length=8, widget=forms.PasswordInput)
    checkbox_on = forms.BooleanField()
    radio_input = forms.ChoiceField(choices=RADIO_CHOICES, widget=forms.RadioSelect)
    favorite_movie = forms.ChoiceField(choices=MOVIE_CHOICES)
    movies_you_own = forms.MultipleChoiceField(required=False, choices=MOVIE_CHOICES)
    text_area = forms.ChoiceField(widget=forms.Textarea)
    integer_input = forms.IntegerField(min_value=1, max_value=10)
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField(max_digits=5, decimal_places=3)
    email_input = forms.EmailField()
    date_input = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")