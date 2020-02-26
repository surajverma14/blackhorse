from django.urls import path
# from .views import (
#     ItemDetailView,
#     CheckoutView,
#     HomeView,
#     OrderSummaryView,
#     add_to_cart,
#     remove_from_cart,
#     remove_single_item_from_cart,
#     PaymentView,
#     AddCouponView,
#     RequestRefundView
# )

from .views import home ,contact , leadership , contact_form_submission

app_name = 'core'

urlpatterns = [
    path('',home, name='home'),
    path('contact', contact, name='contact'),
    path('leadership', leadership, name='leadership'),
    # path('career/',views.career,name='career'),
    path('contact_form_submission/',contact_form_submission, name='contact_form_submission'),
    # path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    # path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    # path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    # path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    # path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    # path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
    #      name='remove-single-item-from-cart'),
    # path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    # path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
