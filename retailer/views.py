from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from application.models import *
from users.models import *
from django.contrib.auth.models import User
from retailer.forms import *
from django.db.models import Q,F
from django.db import transaction

@login_required
def r_index(request):
    context = {}
    p = Profile.objects.get(id = request.user.profile.id)
    if p.is_retail:
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
        return render(request, 'r_index.html',context)
    else:
        error = "You must be Retailer to access this Page"
        context['error'] = error
        return render(request, 'error.html', context)

def r_product_index(request):
    context = {}
    context['pl1'] = ProductListings.objects.order_by('-date')
    return render(request, "r_product_index.html", context)

def r_productListings(request):
    context = {}
    pId = request.GET.get('pId')
    pl = ProductListings.objects.filter(pId = pId)
    context['pl1'] = pl
    return render(request, 'r_productListings.html', context)

@transaction.atomic
def r_buy_product(request):
    context = {}
    pl = request.GET.get('pl')
    pl1 = ProductListings.objects.get(id = pl)
    if request.method == 'GET':
        context['pl1'] = pl1

    elif request.method == 'POST':
        #Fetching Seller Stock
        qty = request.POST.get('tQty')
        tQty = int(qty)
        s_seller = Stock.objects.filter(uName__username = pl1.uName, pListId = pl1).first()
        seller_stock_id = s_seller.id

        #Validate that the entered qnty is less than available
        if (s_seller.sQty-tQty) < 0:
            messages.error(request, f'You must Enter Quantity less than {s_seller.sQty}')
            return HttpResponseRedirect('/r/r_buy_product/?pl='+str(pl))

        else:
            #Check if the Product already exists in the inventory
            st = Stock.objects.filter(uName = request.user, pListId = pl1).first()
            if st:
                stock_left = st.sQty
                #Transaction
                t = Transaction(pListId = pl1, s_uId = pl1.uName ,
                    b_uId = request.user, price = pl1.s_price, tQty = tQty, stock_left = stock_left)
                t.save()
                #Stock
                st.sQty = st.sQty + tQty
                st.save()
                #StockDetail and TransactionDetail
                sd = s_seller.stockdetail_set.all()[:tQty]
                StockDetail.objects.filter(id__in = sd).update(stId = st)
                sd1 = st.stockdetail_set.all()[:tQty]
                l2 = []
                for s_obj in sd1:
                    # s_obj.stId = s
                    # s_obj.save()
                    td = TransactionDetail(tId = t, pNo = s_obj.pNo)
                    l2.append(td)
                TransactionDetail.objects.bulk_create(l2)

            else:
                stock_left = 0
                #Transaction
                t = Transaction(pListId = pl1, s_uId = pl1.uName ,
                    b_uId = request.user, price = pl1.s_price, tQty = tQty, stock_left = stock_left)
                t.save()
                #Stock
                s = Stock(uName = request.user, pListId = pl1, sQty = tQty)
                s.save()

                #StockDetail and TransactionDetail
                sd = s_seller.stockdetail_set.all()[:tQty]
                StockDetail.objects.filter(id__in = sd).update(stId = s)
                sd1 = s.stockdetail_set.all()[:tQty]
                l2 = []
                for s_obj in sd1:
                    # s_obj.stId = s
                    # s_obj.save()
                    td = TransactionDetail(tId = t, pNo = s_obj.pNo)
                    l2.append(td)
                TransactionDetail.objects.bulk_create(l2)

                # for a in range(1,tQty):
                #     #c = a + sd.id
                #     sd2 = sd[a]
                #     #sd2 = StockDetail.objects.filter(stId = seller_stock_id).get(id = c)
                #     sd2.stId = s
                #     sd2.save()
                #     td = TransactionDetail(tId = t, stdId = sd2)
                #     td.save()

            #Removing the stock from seller
            pl1.qty = pl1.qty - tQty
            pl1.save()
            s_seller.sQty = s_seller.sQty - tQty
            s_seller.save()

            #Delete the Stock of Wholesaler if its 0
            if s_seller.sQty == 0:
                s_seller.delete()
            return HttpResponseRedirect('/r/')

    return render(request, 'r_buy_product.html', context)


@login_required
def r_inventory(request):
    context = {}
    if request.user.profile.is_retail:
        s = Stock.objects.filter(uName__username = request.user.username)
        context['s'] = s
        return render(request, 'r_inventory.html', context)
    else:
        error = "You must be Retailer to access this Page"
        context['error'] = error
        return render(request, 'error.html', context)

@login_required
def r_stockDetail(request):
    context = {}
    stId = request.GET.get('stId')
    sd = StockDetail.objects.filter(stId = stId)
    context['sd'] = sd
    return render(request, 'r_stockDetail.html', context)

@login_required
def r_transaction(request):
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
    return render(request, 'r_transaction.html', context)

@login_required
def r_transactionDetail(request):
    context = {}
    tId = request.GET.get('tId')
    td = TransactionDetail.objects.filter(tId = tId)
    context['td'] = td
    return render(request, 'r_transactionDetail.html', context)

@login_required
def r_sell_product_index(request):
    context = {}
    sId = request.GET.get('stId')
    #stId = int(sId)
    s = Stock.objects.get(id = sId)
    pl = ProductListings.objects.get(id = s.pListId.id)
    if request.method == 'GET':

        context['pl'] = pl
        context['s'] = s

    elif request.method == 'POST':
        pr = request.POST.get('price')
        qt = request.POST.get('tQty')
        price = int(pr)
        tQty = int(qt)
        st = Stock.objects.filter(uName__username = request.user.username, pListId = pl).first()
        #Validate that the entered qnty is less than available
        if (st.sQty-tQty) < 0:
            messages.error(request, f'You must Enter Quantity less than {st.sQty}')
            return HttpResponseRedirect('/r/r_sell_product_index/?stId='+str(sId))

        stock_left = st.sQty
        #Transaction
        t = Transaction(pListId = pl,
            s_uId = request.user.username, b_uId = 'Customer', tQty = tQty, price = price, stock_left = stock_left)
        t.save()
        #TransactionDetail
        sd = StockDetail.objects.filter(stId = s.id).first()
        td = TransactionDetail(tId = t, pNo = sd.pNo)
        td.save()
        for b in range(1, tQty):
            c = 0
            c = b + sd.id
            sd2 = StockDetail.objects.get(id = c)
            td1 = TransactionDetail(tId = t, pNo = sd2.pNo)
            td1.save()

        #stock quantity update
        st.sQty = st.sQty - tQty
        st.save()
        #stockDetail update
        for a in range(1,tQty+1):
            std = StockDetail.objects.filter(stId = st.id).first()
            std.delete()

        #Delete the Stock of Wholesaler if its 0
        if st.sQty == 0:
            st.delete()

        return HttpResponseRedirect('/r/')

    return render(request, 'r_sell_product_index.html', context)


def r_subcat(request):
    context={}
    sid = request.GET.get('sid')
    p = Product.objects.filter(subCatId = sid)
    pl1 = []
    for x in p:
        pl = ProductListings.objects.get(pId = x)
        pl1.append(pl)
    context['pl1']=pl1

    return render(request,'r_subcat.html', context)

@login_required
def r_invoice(request):
    context = {}
    tId = request.GET.get('tId')
    t = Transaction.objects.get(id = tId)
    context['total'] = float(t.price*t.tQty)
    td = TransactionDetail.objects.filter(tId = tId)
    context['td'] = td
    context['t'] = t
    return render(request,'r_invoice.html',context)
