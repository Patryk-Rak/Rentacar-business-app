from django.conf import settings  # TODO: ADD THIS LINE.

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import AccountRegistrationForm, AccountAuthenticationForm
from .models import Account


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
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect("http://127.0.0.1:8000/")
        else:
            context['registration_form'] = form

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
    except:
        return HttpResponse("Something went wrong.")
    if account:
        context['id'] = account.id
        context['email'] = account.email
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
        return render(request, "user_account/profile_info.html", context)

# class SignUpView(CreateView):
#     form_class = AccountRegistrationForm
#     success_url = reverse_lazy('login')
#     template_name = 'user_account/signup.html'
#
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(data=request.POST)
#         profile_form = ClientProfileForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             profile_form.save()
#             return render(request, 'user_account/change_password.html', {'change_password_form': form})
#         else:
#             messages.error(request, "źle wprowadzone dane.")
#     else:
#         form = PasswordChangeForm(request.user)
#         profile_form = ClientProfileForm(request.user)
#         context = {'form' : form, 'profile_form' : profile_form}
#     return render(request, 'user_account/change_password.html', {'change_password_form': form})
#
#
# def password_change_view(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(user=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request, 'Twoje hasło zostało zmienione :)!')
#             return render(request, 'user_account/change_password.html', {'change_password_form': form})
#         else:
#             messages.error(request, "źle wprowadzone dane.")
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'user_account/change_password.html', {'change_password_form': form})
#
#