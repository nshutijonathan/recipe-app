from django import forms

RECIPES__CHOICES = (  # specify choices as a tuple
    # when user selects "Bar recipe", it is stored as "#1"
    ('#1', 'Banana recipe'),
    ('#2', 'Onion recipe'),
    ('#3', 'Matake recipe')
)


class RecipesSearchForm(forms.Form):
    recipe_instructions = forms.CharField(max_length=120)
    recipe_name = forms.ChoiceField(choices=RECIPES__CHOICES)
