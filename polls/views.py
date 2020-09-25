from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

# Create your views here.
def polls_display(request):
	polls = [q for q in Question.objects.order_by('pub_date')]

	context = {
	'polls':polls,
	}
	
	return render(request, 'polls/polls.html', context)


def polls_details(request, pk):
	poll = get_object_or_404(Question, pk=pk)
	return render(request, 'polls/polls_details.html', {'poll':poll})