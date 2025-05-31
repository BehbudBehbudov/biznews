from django.db import models

class slider_news(models.Model):
    slider_image = models.ImageField(upload_to = 'slider_news/')
    slider_title = models.CharField(max_length=100)
    slider_content = models.TextField(default="Default content")
    slider_category = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    is_activate = models.BooleanField(default=True)
    is_big = models.BooleanField(default=True)
    is_small = models.BooleanField()
    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField()

    def __str__(self):
        return self.slider_title

class small_slider(models.Model):
    image = models.ImageField(upload_to = 'small_slider_news/')
    title = models.CharField(max_length=100)
    content = models.TextField(default="Default content")
    category = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class FeaturedNews(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='featured_news/')
    category = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default="Default content")
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class PopularNews(models.Model):
    CATEGORY_CHOICES = (
        ('biznes', 'Biznes'),
        ('idman', 'Idman'),
        ('texnologiya', 'Texnologiya'),
        ('əyləncə', 'Əyləncə'),
        ('həyat tərzi', 'Həyat tərzi'),
        ('qida', 'Qida'),
        ('elmlər', 'Elmlər'),
        ('təhsil', 'Təhsil'),
        ('sağlamlıq', 'Sağlamlıq'),
        ('korporativ', 'Korporativ'),
        ('siyasət', 'Siyasət'),
        ('din', 'Din'),
        ('cəmiyyət', 'Cəmiyyət')
    )

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_images/')
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class News(models.Model):
    CATEGORY_CHOICES = (
        ('biznes', 'Biznes'),
        ('idman', 'Idman'),
        ('texnologiya', 'Texnologiya'),
        ('əyləncə', 'Əyləncə'),
        ('həyat tərzi','Həyat tərzi'),
        ('qida','Qida'),
        ('elmlər','Elmlər'),
        ('təhsil','Təhsil'),
        ('sağlamlıq','Sağlamlıq'),
        ('korporativ','Korporativ'),
        ('siyasət','Siyasət'),
        ('din','Din'),
        ('cəmiyyət','Cəmiyyət')
    )

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='news_images/')
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CategoryNews(models.Model):
    CATEGORY_CHOICES = (
        ('biznes', 'Biznes'),
        ('idman', 'Idman'),
        ('texnologiya', 'Texnologiya'),
        ('əyləncə', 'Əyləncə'),
        ('həyat tərzi','Həyat tərzi'),
        ('qida','Qida'),
        ('elmlər','Elmlər'),
        ('təhsil','Təhsil'),
        ('sağlamlıq','Sağlamlıq'),
        ('korporativ','Korporativ'),
        ('siyasət','Siyasət'),
        ('din','Din'),
        ('cəmiyyət','Cəmiyyət')
    )

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='CategoryNews_images/')
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class SiteSettings(models.Model):
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "Site Settings"


class SingleNews(models.Model):
    CATEGORY_CHOICES = (
        ('biznes', 'Biznes'),
        ('idman', 'Idman'),
        ('texnologiya', 'Texnologiya'),
        ('əyləncə', 'Əyləncə'),
        ('həyat tərzi', 'Həyat tərzi'),
        ('qida', 'Qida'),
        ('elmlər', 'Elmlər'),
        ('təhsil', 'Təhsil'),
        ('sağlamlıq', 'Sağlamlıq'),
        ('korporativ', 'Korporativ'),
        ('siyasət', 'Siyasət'),
        ('din', 'Din'),
        ('cəmiyyət', 'Cəmiyyət')
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='null')
    image = models.ImageField(upload_to='news_images/')
    author = models.CharField(max_length=100, default='BizNews')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"{self.title} - {self.get_category_display()}"

class Comment(models.Model):
    news = models.ForeignKey(SingleNews, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.news.title}"


class BreakingNews(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class all_news(models.Model):
    image = models.ImageField(upload_to='news_images/')
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_big_slider = models.BooleanField(default=False)
    is_small_slider = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"self.title + self.content[:50] "


