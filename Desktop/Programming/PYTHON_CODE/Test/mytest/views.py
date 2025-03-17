from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import BirthDateForm
from dateutil.relativedelta import relativedelta
from django.views.generic.edit import FormView


class CalculateAgeView(FormView):
    template_name = 'index.html'
    form_class = BirthDateForm
    success_url = '/success/'

    def form_valid(self, form):
        # Process the form data
        return super().form_valid(form)

def calculate_age(date_of_birth):
    now = datetime.now()
    date_of_birth = datetime.combine(date_of_birth, datetime.min.time())  # Convert date_of_birth to datetime
    delta = relativedelta(now, date_of_birth)
    
    # Calculate total days between now and date_of_birth
    total_days = (now - date_of_birth).days
    
    # Calculate weeks and remaining days
    weeks = total_days // 7
    days = total_days % 7
    
    # Calculate total hours
    total_hours = (now - date_of_birth).total_seconds() // 3600
    
    # Approximate months and days
    approximate_months = delta.years * 12 + delta.months
    approximate_days = total_days % 365
    
    age_details = {
        'years': delta.years,
        'months': approximate_months,
        'weeks': weeks,
        'days': approximate_days,
        'hours': total_hours
    }
    
    return age_details





def calculate_age_view(request):
    age_details = None

    if request.method == 'POST':
        form = BirthDateForm(request.POST)
        if form.is_valid():
            date_of_birth = form.cleaned_data['date_of_birth']
            age_details = calculate_age(date_of_birth)
    else:
        form = BirthDateForm()

    return render(request, 'index.html', {'form': form, 'age_details': age_details})
def home(request):
    return HttpResponse("Home")

def about(request):
    return HttpResponse("About us")

def contact(request):
    return HttpResponse("Contact us")

def new(request):
    return render(request, 'mytest/index.html')