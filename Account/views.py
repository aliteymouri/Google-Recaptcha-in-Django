from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm


class LoginView(View):
    template_name = 'account/login.html'
    form_class = LoginForm

    def get(self, req):
        form = self.form_class()
        return render(req, self.template_name, {'form': form})

    def post(self, req):
        form = self.form_class(req.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(req, user)
                return redirect('home:home')
            else:
                form.add_error('email', 'User Not Found')
        return render(req, self.template_name, {'form': form})
