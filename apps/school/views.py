from django.views.generic import CreateView, ListView

from .forms import SearchForm, StudentForm
from .models import Student


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = SearchForm(self.request.GET)

        if self.form.is_valid():
            search = self.form.cleaned_data.get('search')
            if search:
                queryset = queryset.filter(name__icontains=search)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
