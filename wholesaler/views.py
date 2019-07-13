from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from application.models import *
from users.models import *
from django.contrib.auth.models import User
from .forms import *
from django.db.models import Q


@login_required
def w_index(request):
    context={}
    p = Profile.objects.get(id = request.user.profile.id)
    if p.is_whole:
        catList = []
        subcatList = []
        c = Category.objects.all()
        for i in c:
            if(len(catList)<4):
                x=0
                sc1 = SubCategory.objects.filter(catId = i)
                for b in sc1[:2]:
                    if Product.objects.filter(catId = i, subCatId = b):
                        subcatList.append(b)
                        x = 1
                if x==1:
                    catList.append(i)
            else:
                break
        context['pro'] = ProductListings.objects.order_by('-date')[:4]
        # assert False
        context['sc'] = subcatList
        context['c'] = catList

        return render(request, 'w_index.html',context)
    else:
        error = "You must be Wholesaler to access this Page"
        context['error'] = error
        return render(request, 'error.html', context)


@login_required
def w_add_product(request):
    if request.method == 'POST':
        u = request.user.username
        form1 = w_AddProductForm(request.POST,request.FILES)
        form2 = w_ProductListForm(request.POST, request.FILES)
        form3 = ManufacturerForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            f1 = form1.save(commit = False)
            f2 = form2.save(commit = False)
            f3 = form3.save(commit = False)
            f1.save()
            f3.save()
            f2.pId = f1
            f2.uName = request.user
            f2.manuName = f3
            f2.save()

            #p.user = u
            #p.save()
            pl = ProductListings.objects.get(id = f2.id)
            quant = pl.qty
            #pl1 = ProductListings.objects.filter(uName__username = u).get(pId = Product.objects.get(id = f1.id))
            #Creating Stock
            s1 = Stock(uName = request.user, pListId = pl, sQty = quant)
            s1.save()
            #Creating Transaction
            m = Manufacturer.objects.last()
            t1 = Transaction(pListId = pl,
                s_uId = m.manuName ,
                b_uId = request.user.username,
                price = pl.b_price,
                tQty = quant,
                stock_left = 0)
            t1.save()
            #Creating pNo
            product_id = pl.pId.id
            product_no = str(product_id) + '.001'
            pNo = float(product_no)
            #Creating StockDetail and Transaction Detail

            l1 = []
            l2 = []
            sd1 = StockDetail(stId = s1, pNo = pNo)
            td1 = TransactionDetail(tId = t1, pNo = pNo)
            l1.append(sd1)
            l2.append(td1)
            for a in range(1, quant):
                pNo = pNo + 0.001
                sd1 = StockDetail(stId = s1, pNo = pNo)
                td1 = TransactionDetail(tId = t1, pNo = pNo)
                l1.append(sd1)
                l2.append(td1)

            StockDetail.objects.bulk_create(l1)
            TransactionDetail.objects.bulk_create(l2)
            # sd1 = StockDetail(stId = s1, pNo = pNo)
            # sd1.save()
            # td1 = TransactionDetail(tId = t1,
            #     pNo = sd1.pNo)
            # td1.save()
            # for a in range(1, s1.sQty):
            #     pNo = pNo + 0.001
            #     sd2 = StockDetail(stId = s1, pNo = pNo)
            #     sd2.save()
            #     td1 = TransactionDetail(tId = t1,
            #         pNo = pNo)
            #     td1.save()

            return HttpResponseRedirect('/w/')
    elif request.method == 'GET':

        form1 = w_AddProductForm()
        form2 = w_ProductListForm()
        form3 = ManufacturerForm()

    context = {
        'form1':form1,
        'form2':form2,
        'form3':form3
    }
    return render(request, 'w_addProduct.html', context)

@login_required
def w_inventory(request):
    context = {}
    if request.user.profile.is_whole:
        s = Stock.objects.filter(uName__username = request.user.username)
        context['s'] = s
        return render(request, 'w_inventory.html', context)
    else:
        error = "You must be Wholesaler to access this Page"
        context['error'] = error
        return render(request, 'error.html', context)

@login_required
def w_stockDetail(request):
    context = {}
    stId = request.GET.get('stId')
    sd = StockDetail.objects.filter(stId = stId)
    context['sd'] = sd
    return render(request, 'w_stockDetail.html', context)

@login_required
def w_transaction(request):
    context = {}
    if request.method == 'GET':
        if request.GET.get('type') == 'b':
            t = Transaction.objects.filter(b_uId = request.user.username).order_by('-tDate')
            context['t'] = t
        elif request.GET.get('type') == 's':
            t = Transaction.objects.filter(s_uId = request.user.username).order_by('-tDate')
            context['t'] = t
        elif request.GET.get('type') == 'all':
            t = Transaction.objects.filter(Q(b_uId = request.user.username)|Q(s_uId = request.user.username)).order_by('-tDate')
            context['t'] = t

        return render(request,'w_transaction.html',context)

@login_required
def w_transactionDetail(request):
    context = {}
    tId = request.GET.get('tId')
    td = TransactionDetail.objects.filter(tId = tId)
    context['td'] = td
    return render(request, 'w_transactionDetail.html', context)

@login_required
def w_add_quantity(request):
    context = {}
    pl = request.GET.get('pl')
    pl1 = ProductListings.objects.get(id = pl)
    if request.method == 'GET':
        context['pl1'] = pl1
    elif request.method == 'POST':
        aq = request.POST.get('add_qnty')
        mName = request.POST.get('mName')
        buying_price = request.POST.get('bprice')
        bPrice = float(buying_price)
        add_qnty = int(aq)
        pl1.qty = pl1.qty + add_qnty
        pl1.save()
        s = Stock.objects.filter(uName = request.user, pListId = pl1).first()
        if s is not None:
            stock_left = s.sQty
            s.sQty = s.sQty + add_qnty
            s.save()
        else:
            stock_left = 0
            s = Stock(uName = request.user, pListId = pl1, sQty = pl1.qty)
            s.save()

        # #Check if Manu does not exist then add new
        # m, created = Manufacturer.objects.get_or_create(manuName = mName)

        #Creating pNo  StockDetail, TransactionDetail
        tr = Transaction.objects.filter(pListId = pl1, b_uId = request.user.username).last()
        trd = TransactionDetail.objects.filter(tId = tr).last()
        p_no = float(trd.pNo)
        #Creating Transaction
        t1 = Transaction(pListId = pl1,
                s_uId = mName,
                b_uId = request.user.username,
                price = bPrice,
                tQty = add_qnty,
                stock_left = stock_left
                )
        t1.save()

        #Creating StockDetail, TransactionDetail
        l1 = []
        l2 = []
        for a in range(1, add_qnty+1):
            p_no = p_no + 0.001
            sd1 = StockDetail(stId = s, pNo = p_no)
            td = TransactionDetail(tId = t1,pNo = sd1.pNo)
            l1.append(sd1)
            l2.append(td)

        StockDetail.objects.bulk_create(l1)
        TransactionDetail.objects.bulk_create(l2)

        return HttpResponseRedirect('/w/w_product_listing/')

    return render(request, 'w_add_quantity.html', context)

@login_required
def w_product_listing(request):
    context = {}
    context['pl'] = ProductListings.objects.filter(uName = request.user)
    return render(request, 'w_product_listing.html', context)

@login_required
def w_update_price(request):
    context = {}
    pl = request.GET.get('pl')
    pl1 = ProductListings.objects.get(id = pl)
    if request.method == 'GET':
        context['pl1'] = pl1

    elif request.method == 'POST':
        selling_price = request.POST.get('update_price')
        sPrice = float(selling_price)
        pl1.s_price = sPrice
        pl1.save()

        return HttpResponseRedirect('/w/w_product_listing/')
    return render(request, 'w_update_price.html', context)

@login_required
def w_invoice(request):
    context = {}
    tId = request.GET.get('tId')
    t = Transaction.objects.get(id = tId)
    context['total'] = float(t.price*t.tQty)
    td = TransactionDetail.objects.filter(tId = tId)
    context['td'] = td
    context['t'] = t
    return render(request,'w_invoice.html',context)

def w_subcat(request):
    context={}
    sid = request.GET.get('sid')
    p = Product.objects.filter(subCatId = sid)
    pl1 = []
    for x in p:
        pl = ProductListings.objects.get(pId = x)
        pl1.append(pl)
    context['pl1']=pl1

    return render(request,'w_subcat.html', context)

# @login_required
# def w_bTransaction(request):
#     context = {}
#
#     return render(request,'w_bTransaction.html',context)
#
# @login_required
# def w_sTransaction(request):
#     context = {}
#
#     return render(request,'w_sTransaction.html',context)
