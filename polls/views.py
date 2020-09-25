from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice

# Create your views here.
def polls_display(request):
	polls = [q for q in Question.objects.order_by('create_date')]
	context = {
	'polls':polls,
	}
	return render(request, 'polls/polls.html', context)


def polls_details(request, pk):
	poll = get_object_or_404(Question, pk=pk)
	return render(request, 'polls/polls_details.html', {'poll':poll})


def polls_results(request, pk):
	poll = get_object_or_404(Question, pk=pk)
	choices = poll.choice_set.all()
	total_votes = sum([choice.votes for choice in choices])
	results = [f'{choice}: {round(((choice.votes/total_votes) * 100), 1)}%' for choice in choices]
	context = {
		"results":results,
	}
	return render(request, 'polls/polls_results.html', context)


def polls_vote(request, pk):
	poll = get_object_or_404(Question, pk=pk)
	try:
		selected_choice = poll.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/polls_details.html', {
			'poll':poll,
			'error_message': 'You didn\'t select a choice.',
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		return redirect('polls_results', pk=poll.pk)
