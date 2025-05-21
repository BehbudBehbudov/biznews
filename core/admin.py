from django.contrib import admin
from .models import (ContactUs, slider_news, small_slider, FeaturedNews, NewsletterSubscription, News, PopularNews,
                     CategoryNews, SiteSettings, SingleNews, BreakingNews,Comment, all_news)

admin.site.register(ContactUs)
admin.site.register(slider_news)
admin.site.register(small_slider)
admin.site.register(FeaturedNews)
admin.site.register(NewsletterSubscription)
admin.site.register(News)
admin.site.register(PopularNews)
admin.site.register(CategoryNews)
admin.site.register(SiteSettings)
admin.site.register(SingleNews)
admin.site.register(BreakingNews)
admin.site.register(Comment)
admin.site.register(all_news)




