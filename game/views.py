from django.shortcuts import render
from django.views.generic import TemplateView
from game.forms import GameForm
from game.game_manager import GameManager
from game.models import GameHistory


class GameView(TemplateView):
    """View to interact with user"""
    template_name = 'index.html'
    model = GameHistory

    def get(self, request, *args, **kwargs):
        """Send form at first visit"""
        form = GameForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        """Check form data, and send the result if form is valid"""
        form = GameForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            # Initialize instance of game
            game = GameManager(number_of_players=form.cleaned_data.get('number_of_players', 0),
                               sequence=form.cleaned_data.get('board', ''),
                               deck=form.cleaned_data.get('deck', ''))
            game_result = game.result()

            # Save game data at database
            self.model.objects.create(players=form.cleaned_data.get('number_of_players', None),
                                      squares=form.cleaned_data.get('number_of_squares', None),
                                      cards=form.cleaned_data.get('number_of_cards', None),
                                      sequence=form.cleaned_data.get('board', None),
                                      deck=form.cleaned_data.get('deck', None),
                                      result=game_result
                                      )

            # Send result of game to client side
            context['result'] = game_result
        else:
            context['error'] = 'Form is not valid!'
        return render(request, self.template_name, context)
