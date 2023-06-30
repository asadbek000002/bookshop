from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.views import View

# asosiy oyna class

def indexView(request):
    return render(request, 'blog/index.html')




# kitoblar oynasiga yonaltrilgan class

def booksView(request):
    if 'q' in request.GET:
        q = request.GET['q']
        kitoblar = Kitob.objects.filter(Q(sarlavha__icontains=q) | Q(muallif__icontains=q) | Q(tarif__icontains=q))
    else:
        kitoblar = Kitob.objects.all().order_by('-id')
        q = None
    context = {
        'kitoblar': kitoblar,
        'q' : q
    }
    return render(request, 'blog/books.html', context)





# kitob xarid qilishni taminlovchi class

@login_required
def single(request, pk=None):
    kitob = Kitob.objects.get(pk=pk)
    form = ChoiceForm()
    if request.method == 'POST':
        form = ChoiceForm(request.POST, request.FILES)
        if form.is_valid():
            buy = form.save(commit=False)
            buy.kitob = kitob
            buy.user_id = request.user.id
            if kitob.mavjud_miqdor > 0:
                kitob.mavjud_miqdor -= 1
                kitob.save()
                buy.save()
                messages.success(request, 'muvaffaqiyatli sotib olindi!')
            else:
                messages.error(request, 'hozircha sotuvda mavjud emas!')
        else:
            print(form.errors)
    context = {
        'kitob': kitob,
        'form': form
    }
    return render(request, 'blog/book_detail.html', context)



# sotib olingan kitoblarni saqlovchi class

@login_required
def my_books(request):
    buys = Buy.objects.filter(user=request.user).order_by('-id')
    kitob_xarid = Kitob.objects.exclude(buy__user=request.user)
    context = {
        'buys': buys,
        'kitob_xarid': kitob_xarid
    }
    if not buys:
        messages.warning(request, 'Xaridlar mavjud emas.')
        return redirect('home')
    return render(request, 'blog/book_history.html', context)









# saqlanganlarga saqlash va saqlanganlardan kitoblarni chiqaruvchi class


class AddRemoveSavedView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request, pk):
        book = get_object_or_404(Kitob, id=pk)
        saved_book = Saved.objects.filter(user=request.user, book=book)
        if saved_book:
            saved_book.delete()
            messages.info(request, 'Saqlanganlardan chiqarildi')
        else:
            Saved.objects.create(user=request.user, book=book)
            messages.info(request, 'Saqlandi')
        return redirect(request.META.get("HTTP_REFERER"))





# saqlanganlarni korish uchun class

class SavedView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        saveds = Saved.objects.filter(user=request.user.id ).order_by('-id')
        return render(request, 'blog/saved.html', {'saveds': saveds})





