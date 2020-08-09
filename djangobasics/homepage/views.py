from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = 'index.html'

    """
    Using context data to add variables in our Template.
    Context data is used to evaluate variables.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_statement'] = 'This is Ayush!'
        return context

    """
    Using view method to add functions in our Template.
    View Methods are used to evaluate function calls.
    """
    def my_job(self):
        return "I'm an iOS Developer"