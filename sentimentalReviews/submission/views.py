from django.http import HttpResponse
from django.shortcuts import render
from .forms import Review
from .models import review as mReview


def index(request):
    if request.method == "POST":

        form = Review(request.POST)

        if form.is_valid():
            #save to model
            review = mReview(response = form.cleaned_data['review'])
            review.save()
            print("Review Saved to Database!")





        return render(request, 'submission/submission.html', {'form': form})


    else:

        form = Review()
        return render(request, 'submission/submission.html', {'form':form })