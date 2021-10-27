from django.conf import settings  # TODO: ADD THIS LINE.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse

from .forms import AccountRegistrationForm, AccountAuthenticationForm, AccountEditForm
from .models import Account, ClientProfile


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect


def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.email}.")
    context = {}

    if request.POST:
        account_form = AccountRegistrationForm(request.POST)
        if account_form.is_valid():
            account_form.save()
            email = account_form.cleaned_data.get('email').lower()
            raw_password = account_form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect("http://127.0.0.1:8000/")
        else:
            context['registration_form'] = account_form

    return render(request, 'user_account/register.html', context)


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect("http://127.0.0.1:8000/")


def login_view(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("http://127.0.0.1:8000/")

    destination = get_redirect_if_exists(request)
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect("http://127.0.0.1:8000/")
    return render(request, "user_account/login.html", context)


# class UserListView(ListView):
#     template_name = "user_account/user_list.html"
#     model = Account
#     context_object_name = 'users'
#     paginate_by = 5

# def user_list(request):
#     pg = Paginator(Account.objects.all().order_by('id'), 2)
#     page_number = request.GET.get('page')
#     try:
#         users = pg.page(page_number)
#     except EmptyPage:
#         users = pg.page(pg.num_pages)
#     except PageNotAnInteger:
#         users = pg.page(1)
#     return render(request, 'user_account/user_list.html', {'users': users})
#
# def delete_user_view(request, user_id):
#     user = Account.objects.get(pk=user_id)
#     user.delete()
#     return redirect('name_user_list_view')

def account_view(request, *args, **kwargs):
    """
    - Logic here is kind of tricky
        is_self (boolean)
            is_friend (boolean)
                -1: NO_REQUEST_SENT
                0: THEM_SENT_TO_YOU
                1: YOU_SENT_TO_THEM
    """
    context = {}
    user_id = kwargs.get("user_id")
    try:
        account = Account.objects.get(pk=user_id)
        client_details = ClientProfile.objects.get(pk=user_id)
    except:
        return HttpResponse("Something went wrong.")
    if account:
        context['id'] = account.id
        context['email'] = account.email
        context['first_name'] = account.first_name
        context['last_name'] = account.last_name
        context['hide_email'] = account.hide_email

        if client_details:
            context['user_id'] = client_details.user_id
            context['phone_number'] = client_details.phone_number
            context['address1'] = client_details.address1
            context['address2'] = client_details.address2
            context['postcode'] = client_details.postcode
            context['state'] = client_details.state
            context['country'] = client_details.country
            context['state_region'] = client_details.state_region

        # Define template variables
        is_self = True
        is_friend = False
        user = request.user
        if user.is_authenticated and user != account:
            is_self = False
        elif not user.is_authenticated:
            is_self = False

        # Set the template variables to the values
        context['is_self'] = is_self
        context['is_friend'] = is_friend
        context['BASE_URL'] = settings.BASE_URL
        return render(request, "user_account/profile_info.html", context)


def edit_account_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")
    user_id = kwargs.get("user_id")
    account = Account.objects.get(pk=user_id)
    if account.pk != request.user.pk:
        return HttpResponse("You cannot edit someone elses profile.")
    context = {}
    if request.POST:
        form = AccountEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("account:view", user_id=account.pk)
        else:
            form = AccountEditForm(request.POST, instance=request.user,
                                     initial={
                                         "id": account.pk,
                                         "email": account.email,
                                         "first_name": account.first_name,
                                         "last_name": account.last_name,
                                         "hide_email": account.hide_email,
                                     }
                                     )
            context['form'] = form
    else:
        form = AccountEditForm(
            initial={
                "id": account.pk,
                "email": account.email,
                "first_name": account.first_name,
                "last_name": account.last_name,
                "hide_email": account.hide_email,
            }
        )
        context['form'] = form
    context['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE
    return render(request, "user_account/profile_edit.html", context)
# def logout_view(request, *args, **kwargs):
#     logout(request)
#     return redirect("http://127.0.0.1:8000/")
#
# def login_view(request, *args, **kwargs):


# class UserListView(ListView):
#     template_name = "user_account/user_list.html"
#     model = Account
#     context_object_name = 'users'
#     paginate_by = 5

# def user_list(request):
#     pg = Paginator(Account.objects.all().order_by('id'), 2)
#     page_number = request.GET.get('page')
#     try:
#         users = pg.page(page_number)
#     except EmptyPage:
#         users = pg.page(pg.num_pages)
#     except PageNotAnInteger:
#         users = pg.page(1)
#     return render(request, 'user_account/user_list.html', {'users': users})
#
# def delete_user_view(request, user_id):
#     user = Account.objects.get(pk=user_id)
#     user.delete()
#     return redirect('name_user_list_view')

# TODO: ADD THIS METHOD.

def account_view(request, *args, **kwargs):
    """
    - Logic here is kind of tricky
        is_self (boolean)
            is_friend (boolean)
                -1: NO_REQUEST_SENT
                0: THEM_SENT_TO_YOU
                1: YOU_SENT_TO_THEM
    """
    context = {}
    user_id = kwargs.get("user_id")
    try:
        account = Account.objects.get(pk=user_id)
    except:
        return HttpResponse("Something went wrong.")
    if account:
        context['id'] = account.id
        context['username'] = account.username
        context['email'] = account.email
        context['profile_image'] = account.profile_image.url
        context['hide_email'] = account.hide_email

        # Define template variables
        is_self = True
        is_friend = False
        user = request.user
        if user.is_authenticated and user != account:
            is_self = False
        elif not user.is_authenticated:
            is_self = False

        # Set the template variables to the values
        context['is_self'] = is_self
        context['is_friend'] = is_friend
        context['BASE_URL'] = settings.BASE_URL
        return render(request, "account/account.html", context)


