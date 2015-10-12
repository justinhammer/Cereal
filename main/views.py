from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Cereal, Manufacturer
from main.forms import CerealForm, CerealForm2, CerealUpdateForm
from django.template import RequestContext
# Create your views here.


def cereal_list(request):

    context = {}

    cereals = Cereal.objects.all()

    context['cereals'] = cereals

    return render_to_response('cereal_list.html', context, context_instance=RequestContext(request))


def cereal_detail(request, pk):

    context = {}

    cereal = Cereal.objects.get(pk=pk)

    context['cereal'] = cereal

    return render_to_response('cereal_detail.html', context, context_instance=RequestContext(request))


def cereal_search(request):

    context = {}

    context['request'] = request

    cereal = request.GET.get('cereal', None)

    if cereal != None:
        cereals = Cereal.objects.filter(name__icontains=cereal)
    else:
        cereals = Cereal.objects.all()

    context['cereals'] = cereals

    return render_to_response('cereal_search.html', context, context_instance=RequestContext(request))


def manufacturer_detail(request, pk):

    context = {}

    manufacturer = Manufacturer.objects.get(pk=pk)

    context['manufacturer'] = manufacturer

    return render_to_response('manufacturer_detail.html', context, context_instance=RequestContext(request))


def create_view1(request):

    context = {}

    form = CerealForm()

    context['form'] = form

    if request.method == 'POST':
        form = CerealForm(request.POST, request.FILES)

        if form.is_valid():

            print form.is_valid

            form.save()

            return HttpResponseRedirect('/list_view/')
        else:
            context['errors'] = form.errors

    return render_to_response('create_view2.html', context, context_instance=RequestContext(request))


def create_view2(request):

    context = {}

    form = CerealForm2()
    context['form'] = form

    if request.method == 'POST':
        form = SpeedModelForm2(request.POST, request.FILES)

        if form.is_valid():

            print form.cleaned_data

            name = form.cleaned_data['title']
            hctype = form.cleaned_data['hctype']
            calories = form.cleaned_data['calories']

            new_object = Cereal()

            new_object.name = name
            new_object.hctype = hctype
            new_object.calories = calories

            new_object.save()

            return HttpResponseRedirect('/list_view/')
        else:
            context['errors'] = form.errors
    return render_to_response('create_view2.html', context, context_instance=RequestContext(request))


def update_view(request, pk):

    context = {}

    cereal_object = Cereal.objects.get(pk=pk)

    context['cereal_object'] = cereal_object

    form = CerealUpdateForm()

    context['form'] = form

    if request.method == 'POST':
        form = CerealUpdateForm(request.POST, request.FILES)

        if form.is_valid():
            cereal_object.name = form.cleaned_data['name']
            cereal_object.hctype = form.cleaned_data['hctype']
            cereal_object.calories = form.cleaned_data['calories']

            cereal_object.save()

            return HttpResponseRedirect('/update_view/%s/' % pk)

        else:
            context['errors'] = form.errors

    return render_to_response('update_view.html', context, context_instance=RequestContext(request))
