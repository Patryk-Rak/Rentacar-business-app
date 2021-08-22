from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from django.http import HttpResponse

from .forms import AccountRegistrationForm, ClientProfileForm
from .models import Account


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
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect("http://127.0.0.1:8000/")
        else:
            context['registration_form'] = form


    return render(request, 'user_account/register.html', context)

# def logout_view(request, *args, **kwargs):
#     logout(request)
#     return redirect("http://127.0.0.1:8000/")
#
# def login_view(request, *args, **kwargs):






















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
# class UserListView(ListView):
#     template_name = "user_account/user_list.html"
#     model = Account
#     context_object_name = 'users'
#     paginate_by = 5
#
#
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