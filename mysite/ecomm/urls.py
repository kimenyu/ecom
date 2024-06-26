from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, CartItemListView, CartItemCreateView, CartItemDeleteView, CartItemUpdateView, OrderCreateView, OrderListView, OrderDetailView, OrderUpdateView, OrderDeleteView, ContactInfoCreateView, ContactInfoListView, ContactInfoDetailView, ContactInfoUpdateView, ContactInfoDeleteView, ProfileListView, ProfileCreateView, ProfileDetailView, ProfileUpdateView, ProfileDeleteView, CategoryCreateView, CategoryListView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView, RegisterView, AdminRegisterView, LoginView

app_name = 'products'

urlpatterns = [
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    
    path('accounts/admin/register/', AdminRegisterView.as_view(), name='register'),
    path('accounts/admin/login/', LoginView.as_view(), name='login'),

    
    
    path('product/create/', ProductCreateView.as_view(), name='create-product'),
    path('product/list/', ProductListView.as_view(), name='list-product'),
    path('product/detail/<int:pk>/', ProductDetailView.as_view(), name='detail-product'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='update-product'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete-product'),

    path('category/create/', CategoryCreateView.as_view(), name='create-category'),
    path('category/list/', CategoryListView.as_view(), name='list-category'),
    path('category/detail/<int:pk>/', CategoryDetailView.as_view(), name='detail-category'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='update-category'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete-category'),

    path('cart/', CartItemListView.as_view(), name='cart'),
    path('cart-item/create/', CartItemCreateView.as_view(), name='create-cart-item'),
    path('cart-item/delete/<int:pk>/', CartItemDeleteView.as_view(), name='delete-cart-item'),
    path('cart-item/update/<int:pk>/', CartItemUpdateView.as_view(), name='update-cart-item'),

    path('profile/', ProfileListView.as_view(), name='profile'),
    path('profile/create/', ProfileCreateView.as_view(), name='create-profile'),
    path('profile/detail/<int:pk>/', ProfileDetailView.as_view(), name='detail-profile'),
    path('profile/update/<int:pk>/', ProfileUpdateView.as_view(), name='update-profile'),
    path('profile/delete/<int:pk>/', ProfileDeleteView.as_view(), name='delete-profile'),

    path('order/create/', OrderCreateView.as_view(), name='create-order'),
    path('order/list/', OrderListView.as_view(), name='list-order'),
    path('order/detail/<int:pk>/', OrderDetailView.as_view(), name='detail-order'),
    path('order/update/<int:pk>/', OrderUpdateView.as_view(), name='update-order'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='delete-order'),

    path('contact-info/create/', ContactInfoCreateView.as_view(), name='create-contact-info'),
    path('contact-info/list/', ContactInfoListView.as_view(), name='list-contact-info'),
    path('contact-info/detail/<int:pk>/', ContactInfoDetailView.as_view(), name='detail-contact-info'),
    path('contact-info/update/<int:pk>/', ContactInfoUpdateView.as_view(), name='update-contact-info'),
    path('contact-info/delete/<int:pk>/', ContactInfoDeleteView.as_view(), name='delete-contact-info'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)