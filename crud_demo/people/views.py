from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm

def person_list(request):
    people = Person.objects.all()
    return render(request, 'person_list.html', {'people': people})

def person_create(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})

def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})

def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_confirm_delete.html', {'person': person})
