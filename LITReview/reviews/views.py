from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
#from rules.contrib.views import permission_required, objectgetter
from django.db.models import Q
from django.core.paginator import Paginator

import rules
from . import models, forms

""" @rules.predicate
def is_ticket_author(user, ticket):
    return ticket.author == user """

@login_required
def home(request):
    tickets = models.Ticket.objects.filter(
        Q(author__in=request.user.get_connections()) | Q(author=request.user)
    )
    reviews = models.Review.objects.filter(
        Q(user__in=request.user.get_connections()) | Q(user=request.user)
    )

    flux = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    paginator = Paginator(flux, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'page_obj':page_obj, 
    }
    return render(request, 'reviews/home.html', context=context)

@login_required
def personal_posts(request):
    tickets = models.Ticket.objects.filter(
        Q(author=request.user)
    )
    reviews = models.Review.objects.filter(
        Q(user=request.user)
    )
    flux = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    paginator = Paginator(flux, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'page_obj':page_obj, 
    }
    return render(request, 'reviews/posts.html', context=context)

@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.save()
            return render(request, 'reviews/ticket_details.html', {'ticket':ticket})
    return render(request, 'reviews/create_ticket.html', context={'form': form})

@login_required
def ticket_details(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'reviews/ticket_details.html', {'ticket':ticket})

@login_required
#@permission_required('ticket.edit_ticket', fn=objectgetter(models.Ticket, 'ticket_id'))
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if request.user != ticket.author:
        return redirect('ticket_details', ticket.id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'reviews/edit_ticket.html', context=context)


@login_required
def create_review(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    form = forms.ReviewForm()
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save(ticket, request.user)
            return render(request, 'reviews/review_details.html', {'review':review})
    return render(request, 'reviews/create_review.html', context={'form': form, 'ticket': ticket})

@login_required
def review_details(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, 'reviews/review_details.html', {'review':review})

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    if request.user != review.user:
        return redirect('review_details', review.id)
    edit_form = forms.ReviewForm(instance=review)
    delete_form = forms.DeleteReviewForm()
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_review' in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.ticket.has_review=False
                review.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'reviews/edit_review.html', context=context)

@login_required
def create_ticket_and_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.author = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.save(ticket, request.user)
            return redirect('home')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form
    }
    return render(request, 'reviews/create_ticket_and_review.html', context=context)

@login_required
def follow_users(request):
    form = forms.UserFollowForm(request.user)
    delete_form = forms.DeleteFollowForm()
    if request.method == 'POST':
        if 'delete_follow' in request.POST:
            delete_form = forms.DeleteFollowForm(request.POST)
            if delete_form.is_valid():
                connection = get_object_or_404(
                    models.UserFollow,
                    user=request.user,
                    followed_user=request.POST['followed_user']
                )
                connection.delete()
                print(request.POST)
                return redirect('follow_users')
        else:       
            form = forms.UserFollowForm(request.user, request.POST)
            if form.is_valid():
                form.clean_followed_user()
                form.save()
                return redirect('home')
    return render(request, 'reviews/follow_users_form.html', context={'form': form, 'delete_form': delete_form})
