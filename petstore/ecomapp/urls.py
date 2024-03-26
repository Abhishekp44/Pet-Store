from django.urls import path
from ecomapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('product',views.product),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sortbyprice),
    path('pricefilter',views.pricefilter),
    path('search',views.search),
    path('productdetail/<pid>',views.productdetail),
    path('addtocart/<pid>',views.addtocart),
    path('viewcart',views.viewcart),
    path('updateqty/<x>/<cid>',views.updateqty),
    path('remove/<cid>',views.remove),
    path('placeorder',views.placeorder),
    path('fetchorder',views.fetchorder),
    path('makepayment',views.makepayment),
    path('paymentsuccess',views.paymentsuccess),
    path('landing',views.landing),
    path('orderhistory',views.orderhistory),
]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
