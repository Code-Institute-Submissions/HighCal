"""highcal_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index
from accounts import urls as accounts_urls
from products import urls as urls_products
from products.views import all_products
from portfolio.views import all_portfolio
from portfolio import urls as urls_portfolio
from cart import urls as urls_cart
from search_product import urls as urls_search_product
from search_blog import urls as urls_search_blog
from reviews import urls as urls_reviews
from reviews.views import all_reviews
from contact.views import contact
from contact import urls as urls_contact
from checkout import urls as urls_checkout
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^products/', include(urls_products)),
    url(r'^contact/', include(urls_contact)),
    url(r'^portfolio/', include(urls_portfolio)),
    url(r'^reviews/', include('reviews.urls')),
    url(r'^reviews/', include(urls_reviews)),
    url(r"^reviews$", all_reviews, name="all_reviews"),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search_product/', include(urls_search_product)),
    url(r'^search_blog/', include(urls_search_blog)),
    url(r'^$', RedirectView.as_view(url='posts/')),
    url(r'^posts/', include('posts.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
