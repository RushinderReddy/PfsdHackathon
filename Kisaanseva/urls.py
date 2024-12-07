

from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Add more paths as needed
]

urlpatterns=[
             path('index/',views.index),
path('',views.index,name='index'),
             path('login/',views.login),


             path('registers/',views.registers),
             path('userinfo/',views.userinfo),
             path('loginuser/',views.loginuser),
             path('menu/',views.menu),
path('add/',views.add),
path('add_contact/',views.add_contact),
path('feedback_add/',views.feedback_add),
path('additem/',views.additem),
path('add_table/',views.add_table),
path('pay_page/',views.pay_page),
path('deleteitem/<str:name>',views.deleteitem,name='deleteitem'),
path('delete/',views.delete),
path('update/',views.update),
path('updateitem/', views.updateitem,name='updateitem'),
path('update_form/<str:name> <int:price>', views.update_form,name='update_form'),
path('productinfo/',views.productinfo,name='productinfo'),
path('fsd/',views.fsd,name='fsd'),
path('wsd/',views.wsd,name='wsd'),
path('search_add/',views.search_add,name='search_add'),
path('sfcd/',views.sfcd,name='sfcd'),
path('about/',views.about),
path('contact/',views.contact),
path('addpayment/',views.addpayment),
path('end/',views.end),
path('amount/<int:total> <str:cart_items>/',views.amount,name='amount'),
path('order/',views.order),
path('sp/',views.sp),
path('dd/',views.dd),
path('ss/',views.ss),
path('std/',views.std,name='std'),
path('ws/',views.ws),
path('thankyou/',views.thankyou),
path('pre_order/',views.pre_order),
path('goback/',views.goback),
path('logout/',views.logout),
path('forget_pwd/',views.forget_pwd),
path('fp/',views.fp),
path('cart_add/<str:name>/', views.cart_add, name='cart_add'),
path('cart_add_search/<str:name>/', views.cart_add_search, name='cart_add_search'),
path('morning/<str:name>/', views.cart_add, name='cart'),
path('get_cart_items/',views.get_cart_items),
#path('quantity/<str:name> <int:total>/',views.quantity,name='quantity'),
path('cart_add_fertilizers/<str:name>/', views.cart_add_fertilizers, name='cart_add_fertilizers'),
path('pay/',views.pay),
path('get_cater_items/',views.get_cater_items),
path('feedback/',views.feedback),
path('dummy/',views.dummy),
path('rec/',views.rec),
path('rec/',views.add_rec),
    path('cart/',views.cart_add_fertilizers),
    path('table/', views.add_table, name=' table'),
    path('delights/', views.delights, name='delights'),
    path('wsd/',views.wsd,name='wsd'),
    path('cart/', views.cart_add),
    path('add-rec/', views.add_rec, name='add_rec'),
path('products/', views.product_list, name='product_list'),
    path('cart/', views.cart_detail, name='cart_detail'),

]
