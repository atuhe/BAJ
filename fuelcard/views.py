from django.views.generic import CreateView, TemplateView
from fuelcard.forms import PumpForm, ReportForm


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class PumpView(CreateView):
    form_class = PumpForm
    template_name = 'report2.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)


class ReportView(CreateView):
    form_class = ReportForm
    template_name = 'report2.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

#
# def about(request):
#     return render(request, 'report2.html', {})
#
#
# def report(request):
#     return render(request, 'report.html', {})
#
#
# def form(request):
#     return render(request, 'forms-advanced.html', {})
