from django.shortcuts import render,  redirect, get_object_or_404
from .models import (slider_news, small_slider, FeaturedNews, NewsletterSubscription, News,
                     PopularNews, CategoryNews, SingleNews, BreakingNews)
from core.forms import ContactForm, NewsletterForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator
from news_backend.settings import EMAIL_HOST_USER, BASE_DIR
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags


def home_view(request):
    BigSlider = slider_news.objects.filter(is_activate=True).order_by('-created_date')[:3]
    SmallSlider = small_slider.objects.all().order_by('-created_date')[:4]
    featured_news = FeaturedNews.objects.all().order_by('-created_date')[:5]
    news = News.objects.all().order_by('-created_at')[:6]
    news_list = PopularNews.objects.all().order_by('-published_date')[:5]
    breaking_news = BreakingNews.objects.all().order_by('-created_at')[:5]
    return render(request,'home.html',{'BigSlider':BigSlider, 'SmallSlider':SmallSlider, 'featured_news':featured_news , 'news': news,
                                       'news_list': news_list,'breaking_news':breaking_news})


def read_more_featured(request, id):
    news = get_object_or_404(FeaturedNews, id=id)
    return render(request, 'read_more_featured.html', {'news': news})


def slider_detail_view(request, id):
    slider = slider_news.objects.get(id=id)
    return render(request, 'slider_detail.html', {'slider': slider})


def read_more(request, id):
    slider = small_slider.objects.get(id=id)
    return render(request, 'read_more_page.html', {'slider': slider})

def read_more_news(request):
    news_list = News.objects.all().order_by('-created_at')
    paginator = Paginator(news_list, 6)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    return render(request, 'read_more_news.html', {'news': news})

def news_detail(request, pk):
    article = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'article': article})

def PopularNews_detail(request, news_id):
    news = get_object_or_404(PopularNews, id=news_id)
    return render(request, 'PopularNews_detail.html', {'news': news})


def category_view(request):
    news_list = PopularNews.objects.all().order_by('-published_date')[:5]
    news = CategoryNews.objects.all().order_by('-created_at')[:6]
    return render(request,'category.html',{'news_list': news_list, 'news':news})

def read_more_category_news(request):
    category_news_list = CategoryNews.objects.all().order_by('-created_at')
    paginator = Paginator(category_news_list, 6)
    page_number = request.GET.get('page')
    category_news = paginator.get_page(page_number)
    return render(request, 'read_more_category_news.html', {'category_news': category_news})

def category_news_detail(request, pk):
    category_news = get_object_or_404(CategoryNews, id=pk)
    return render(request, 'category_news_detail.html', {'article': category_news})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            "receiver_name": "Behbud Behbudov",
            "age": 18,
            "profession": "Backend Developer",
            "marital_status": "Divorced",
            "address": "Planet Earth",
            "year": 2025
        }
        template_name = f"{BASE_DIR}/templates/mail.html"
        convert_to_html_content = render_to_string(
            template_name=template_name,
            context=context
        )
        plain_message = strip_tags(convert_to_html_content)
        send_mail("Test Subject",
                  plain_message,
                  EMAIL_HOST_USER,
                  ["shohretaga@gmail.com"],
                  html_message=convert_to_html_content,
                  fail_silently=True
                  )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("core:contact")
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form':form})


def single_view(request):
    news_list = PopularNews.objects.all().order_by('-published_date')[:5]
    latest_news = SingleNews.objects.order_by('-created_at').first()
    breaking_news = BreakingNews.objects.all().order_by('-created_at')[:5]
    comments = latest_news.comments.order_by('-created_at')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = latest_news
            comment.save()
            return render(request, 'single.html', {
                'news_list': news_list,
                'latest_news': latest_news,
                'breaking_news': breaking_news,
                'comments': comments,
                'form': form
            })
    else:
        form = CommentForm()

    return render(request, 'single.html', {
        'news_list': news_list,
        'latest_news': latest_news,
        'breaking_news': breaking_news,
        'comments': comments,
        'form': form
    })



def newsletter_signup(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            if not NewsletterSubscription.objects.filter(email=email).exists():
                form.save()
                messages.success(request, "Abunə oldunuz!")
            else:
                messages.warning(request, "Bu e-poçt artıq qeydiyyatdan keçib.")
        else:
            messages.error(request, "Düzgün e-poçt daxil edin.")
    return redirect(request.META.get("HTTP_REFERER", "home.html"))



