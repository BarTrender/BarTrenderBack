from django.urls import path,include
from .views import *

urlpatterns = [
    # Get QR
    path('<int:establishment_id>/discounts/<int:discount_id>/getQR', DiscountsQR.as_view()),
    # Get Establishments By Filters
    path('get', Establishments.as_view()),
    # Scan Code
    path('<int:establishment_id>/discounts/<int:discount_id>/client/<int:client_id>/scan', ScanDiscount.as_view()),
    # Get Discount from establishment
    path('<int:establishment_id>/discounts/get', Discounts.as_view()),
    #Create Discount
    path('<int:establishment_id>/discounts/create', Discounts.as_view()),
    # Update Discount
    path('<int:establishment_id>/discounts/<int:discount_id>/update', Discounts.as_view()),
    # Delete Discount
    path('<int:establishment_id>/discounts/<int:discount_id>/delete', Discounts.as_view()),
    #Get Establishment By Establishment Id
    path('<int:establishment_id>/get', Establishment_By_EstablishmentId.as_view()),
    # Get Establishments by logged owner since owner is fetched from token
    path('get_by_owner', EstablishmentsByOwner.as_view())
]
