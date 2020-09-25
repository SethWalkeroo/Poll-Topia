from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from .forms import PollForm, ChoiceForm
from django.utils import timezone



def polls_new(request):
	if request.method == "POST":
		form1 = PollForm(request.POST)
		form2 = ChoiceForm(request.POST)
		if form1.is_valid() and form2.is_valid():
			poll = form1.save(commit=False)
			choices = form2.save(commit=False)
			choices.question = poll.pk
			poll.author = request.user
			poll.pub_date = timezone.now()
			poll.save()
			return redirect('polls_details', pk=poll.pk)
	else:
		form1 = PollForm()
		form2 = ChoiceForm()
	return render(request, 'polls/polls_edit.html', {'form1':form1, 'form2':form2})


def polls_edit(request, pk):
	poll = get_object_or_404(Question, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			poll = form.save(commit=False)
			poll.author = request.user
			poll.published_date = timezone.now()
			poll.save()
			return redirect('polls_details', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/polls_edit.html', {'form': form})


def polls_display(request):
	polls = [q for q in Question.objects.order_by('create_date')]
	total_counts = []
	for q in polls:
		choices = q.choice_set.all()
		total_votes = sum([choice.votes for choice in choices])
		total_counts.append(total_votes)
	polls_counts = zip(polls, total_counts)
	context = {
		'polls_counts':polls_counts
	}
	return render(request, 'polls/polls.html', context)


def polls_details(request, pk):
	poll = get_object_or_404(Question, pk=pk)
	return render(request, 'polls/polls_details.html', {'poll':poll})


def polls_results(request, pk):
	poll = get_object_or_404(Question, pk=pk)
	choices = poll.choice_set.all().order_by('-votes')
	total_votes = sum([choice.votes for choice in choices])
	percentages = [f'{round(((choice.votes/total_votes) * 100), 1)}%' for choice in choices]
	vote_results = zip(choices, percentages)
	context = {
		"total_votes":total_votes,
		"vote_results":vote_results,
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
