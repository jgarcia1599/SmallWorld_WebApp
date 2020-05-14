
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about.html'

class GetInvolvedView(TemplateView):
    template_name = 'getinvolved.html'

class TeamView(TemplateView):
    template_name = 'team.html'

class WorkView(TemplateView):
     template_name = 'work.html'

class GAAView(TemplateView):
    template_name = 'gaa.html'

