from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Bills
from .forms import BillForm


def index(request):

    success_save_form = 0
    if request.method == 'POST':
        form = BillForm(request.POST)
        id_select_user = form.data.get('user_id')
        count_bills = len(Bills.objects.filter(user_id=id_select_user,
                                               state=False))
        if form.is_valid() and count_bills < 1:
            form.save()
            success_save_form = 1
        else:
            success_save_form = 2

    template = 'index.html'
    context = {
        'bills': Bills.objects.all(),
        'form': BillForm(),
        'save_form': success_save_form,
    }
    return render(request, template, context)


def bill_payment(request, pk):
    template = 'pay.html'
    context = {
        'pay': get_object_or_404(Bills, pk=pk),
    }
    return render(request, template, context)


def bill_success(request, pk):
    if get_object_or_404(Bills, pk=pk).state:
        message = f'The bill №{pk} has already been paid.'
    else:
        Bills.objects.filter(pk=pk).update(state=True)
        message = f'The bill №{pk} is paid.'
    template = 'pay-success.html'
    context = {
        'message': message
    }
    return render(request, template, context)


def bill_deletion(request, pk):
    Bills.objects.get(pk=pk).delete()
    return redirect(reverse('index'))
