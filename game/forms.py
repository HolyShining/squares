from django import forms


class GameForm(forms.Form):
    """Implements basic input form for game"""

    number_of_players = forms.IntegerField()
    number_of_squares = forms.IntegerField()
    number_of_cards = forms.IntegerField()
    board = forms.CharField()
    deck = forms.CharField()

