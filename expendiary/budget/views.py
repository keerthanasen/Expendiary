from django.shortcuts import render, get_object_or_404
from .forms import ExpenseForm
from .models import Project, Category, Expense
from django.views.generic import CreateView
from django.utils.text import slugify
from django.http import HttpResponseRedirect

# Create your views here.

def list(request):
    return render(request, 'list.html')

def description(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    if(request.method == "GET"):
        category_list = Category.objects.filter(project=project)
        return render(request, 'description.html', {'project':project, 'expense_list': project.expenses.all(), 'category_list': category_list})
    elif(request.method == "POST"):
        form = ExpenseForm(request.POST)
        if(form.is_valid()):
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category_type = form.cleaned_data['category']
            category = get_object_or_404(Category, project=project, name=category_type)
            Expense.objects.create(
                project = project, 
                title = title, 
                amount = amount, 
                category = category
            ).save()

    return HttpResponseRedirect(project_slug)

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'new_project.html'
    fields = ('name', 'budget')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST['categoriesString'].split(',')
        for category in categories:
            Category.objects.create(
                project = Project.objects.get(id=self.object.id),name=category).save()
            return HttpResponseRedirect(self.get_success_url())

    def get_succes_url(self):
        return slugify(self.request.POST['name'])