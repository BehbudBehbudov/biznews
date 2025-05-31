from django.urls import path
from core.views import (home_view, contact_view, category_view, single_view, slider_detail_view, read_more,
                                read_more_featured, newsletter_signup, read_more_news, news_detail, PopularNews_detail, read_more_category_news
                        , category_news_detail)

app_name = 'core'

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('category/', category_view, name='category'),
    path('single/', single_view, name='single'),
    path('slider/<int:id>/', slider_detail_view, name='slider_detail'),
    path('slider/read-more/<int:id>/', read_more, name='read_more_page'),
    path('featured/<int:id>/', read_more_featured, name='read_more_featured'),
    path("newsletter-signup/", newsletter_signup, name="newsletter_signup"),
    path('read-more/', read_more_news, name='read_more_news'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('PopularNews/<int:news_id>/', PopularNews_detail, name='PopularNews_detail'),
    path('read-more-category/', read_more_category_news, name='read_more_category_news'),
    path('category_news/<int:pk>/', category_news_detail, name='category_news_detail'),
    path('news/latest/', single_view, name='latest_news'),
]

