from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import loader
import datetime
from django.contrib import messages
from application.models import *
from application.forms import *
from django.contrib.auth.models import User
from users.models import *


def index_view(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            if request.user.profile.is_whole:
                return HttpResponseRedirect('/w/')
            elif request.user.profile.is_retail:
                return HttpResponseRedirect('/r/')
        else:
            return render(request,'index.html',{})
    else:
        return render(request, "home.html",{})

def admin_dashboard(request):
    return render(request,'admin_dashboard.html',{})

def Product_index(request):
    context = {}
    context['pl1'] = ProductListings.objects.all()
    if request.user.profile.is_whole:
        return render(request, "w_product_index.html", context)
    else:
        return render(request, "product_index.html", context)

def productListings_index(request):
    context = {}
    pId = request.GET.get('pId')
    pl = ProductListings.objects.filter(pId = pId)
    context['pl1'] = pl
    if request.user.profile.is_whole:
        return render(request, 'w_productListings_index.html', context)
    else:
        return render(request, 'productListings_index.html', context)

@login_required
def stock_index(request):
    context={}
    context['stock'] = Stock.objects.all()
    return render(request, 'stock_index.html', context)

def stock_detail_index(request):
    context = {}
    sd = StockDetail.objects.all()
    context['sd'] = sd
    return render(request, 'stock_detail_index.html', context)

def transaction(request):
    context = {}
    t = Transaction.objects.all()
    context['t'] = t
    return render(request, 'transaction.html', context)

def transaction_detail(request):
    context = {}
    t = Transaction.objects.all()
    td = TransactionDetail.objects.all()
    context['td'] = td
    context['t'] = t
    return render(request, 'transaction_detail.html', context)



# def stockDetail_index(request):
#     context={}
#     context['stockd'] = StockDetail.objects.all()
#     u1 = Users.objects.get(uName='Nisarg')
#
#     s1 = Stock.objects.filter(uId=u1.uId).first()
#
#     context['x'] = s1.sQty
#     context['stId'] = s1.stId
#     sd1 = StockDetail(stId = Stock.objects.filter(uId=u1.uId).first(), pNo = 3.1)
#     sd1.save()
#     for a in range(1,s1.sQty):
#         s = StockDetail.objects.last()
#         sd1 = StockDetail(stId = Stock.objects.filter(uId=u1.uId).first(), pNo = Decimal(s.pNo)+Decimal(0.1))
#         sd1.save()
#
#     context['stId'] = sd1.stId
#     context['pNo'] = sd1.pNo
#     return render(request, 'stockDetail_index.html', context)
