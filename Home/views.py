from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/index.html'


class ReView(TemplateView):
    template_name = 'home/recaptcha.html'
