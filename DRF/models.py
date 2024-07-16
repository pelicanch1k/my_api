from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class Json(models.Model):
    title = models.CharField(max_length=64, help_text='Your Website Title', default='Your Website Title')

    class Meta:
        verbose_name_plural = 'json'

    def __str__(self):
        return f'Id: {self.id} | Title: {self.title}'



class Metadata(models.Model):
    title = models.ForeignKey(Json, on_delete=models.CASCADE)

    description = models.CharField(max_length=128,
                                   default="This is the meta description for your website. It should summarize your site's content.",
                                   blank=True,
                                   help_text='Описание'
                                   )

    keywords = models.CharField(max_length=255, default='{"data": "text"}', blank=True)

    canonical = models.URLField(blank=True, default='https://www.yourwebsite.com/', help_text='URL')

    language = models.CharField(max_length=5,
                                help_text='Язык',
                                verbose_name='language',
                                blank=True,
                                default='en')

    def __str__(self):
        return self.title.title

    class Meta:
        verbose_name_plural = 'metadata'



class Microdata(models.Model):
    title = models.ForeignKey(Json, on_delete=models.CASCADE)

    schemaType = models.CharField(max_length=50, blank=True, default='Organization')
    name = models.CharField(max_length=100, blank=True, default='Your Company')
    url = models.URLField(blank=True, default='https://www.yourwebsite.com/')
    logo = models.ImageField(upload_to='image', null=True, blank=True)

    # contact
    telephone = PhoneNumberField(blank=True, verbose_name='contact/telephone', default='+375296335566')
    email = models.EmailField(verbose_name='contact/email', blank=True, default='info@yourwebsite.com')

    def __str__(self):
        return self.title.title

    class Meta:
        verbose_name_plural = 'MicroData'

class SocialMedia(models.Model):
    title = models.ForeignKey(Json, on_delete=models.CASCADE)
    ogTitle = models.CharField(max_length=100, default='Your Website Title for Social Media', blank=True)
    ogType = models.CharField(max_length=50, default='website', blank=True)
    ogImage = models.ImageField(upload_to='image', null=True, blank=True)
    ogDescription = models.TextField(default='Description for social media sharing', blank=True)
    twitterCard = models.CharField(max_length=20, default='summary', blank=True)
    twitterSite = models.CharField(max_length=50, default='@YourTwitterHandle', blank=True)
    twitterTitle = models.CharField(max_length=100, default='Your Website Title for Twitter', blank=True)
    twitterDescription = models.TextField(default='Description for Twitter', blank=True)
    twitterImage = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return self.ogTitle

    class Meta:
        verbose_name_plural = 'socialMedia'



class GoogleRichSnippets(models.Model):
    title = models.ForeignKey(Json, on_delete=models.CASCADE)

    type = models.CharField(max_length=50, default='Article', blank=True)
    headline = models.CharField(max_length=100, default='Introduction to Instagram', blank=True)
    author = models.CharField(max_length=100, default='Author Name', blank=True)
    datePublished = models.DateField(default=timezone.now, blank=True)
    dateModified = models.DateField(default=timezone.now, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)

    # publisher
    publisher_type = models.CharField(max_length=50, default='Organization', blank=True, verbose_name='publisher/type')
    name = models.CharField(max_length=100, default='Your Company', blank=True, verbose_name='publisher/name')
    logo = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name_plural = 'GoogleRichSnippets'

class AdditionalSEO(models.Model):
    title = models.ForeignKey(Json, on_delete=models.CASCADE)

    robots = models.CharField(max_length=100, default='index, follow', blank=True)
    viewport = models.CharField(max_length=100, default='width=device-width, initial-scale=1.0', blank=True)

    def __str__(self):
        return self.robots

    class Meta:
        verbose_name_plural = 'additionalSEO'

class ColorBody(models.Model):
    title = models.ForeignKey(Json, on_delete=models.CASCADE)

    active_color = models.CharField(max_length=20, default='#FD021A', blank=True)
    focused_color = models.CharField(max_length=20, default='#FE6776', blank=True)
    def_color = models.CharField(max_length=20, default='#FD3548', blank=True)

    def __str__(self):
        return "Color Body"

    class Meta:
        verbose_name_plural = 'Color-Body'

###

class HeroBlock(models.Model):
    json = models.ForeignKey(Json, on_delete=models.CASCADE)

    pre_title = models.CharField(max_length=100, blank=True, default='Welcome to Instagram story')
    title = models.CharField(max_length=100, blank=True, default='Introduction to Instagram')
    description = models.TextField(blank=True, default='Before Instagram became the social media giant it is today, it started as a humble photo-sharing platform.')
    icons_hero = models.ImageField(upload_to='image', null=True, blank=True)
    download = models.FileField(upload_to='uploads', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Hero-Block'

class BlockHistory(models.Model):
    json = models.ForeignKey(Json, on_delete=models.CASCADE)

    date = models.CharField(max_length=4, default='2010', blank=True)
    title_history = models.TextField(default="The history of the Instagram logo", blank=True)
    description_history = models.TextField(default="The first iteration of the Instagram logo was simply an image of a Polaroid OneStep camera. It worked as a concept, but Systrom realized that as the brand grew, it would need a new, more creative and distinctive logo that wasn’t dependent on the Polaroid design",blank=True)
    icons_history = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return self.title_history

    class Meta:
        verbose_name_plural = 'Block-History'


class AlternativeBlock(models.Model):
    json = models.ForeignKey(Json, on_delete=models.CASCADE)

    title_Alternative = models.CharField(max_length=100, default='Instagram logo', blank=True)
    icons_Alternative = models.ImageField(upload_to='image', null=True, blank=True)
    download_Alternative = models.FileField(upload_to='uploads', null=True, blank=True)

    def __str__(self):
        return self.title_Alternative

    class Meta:
        verbose_name_plural = 'Alternative-Block'

class Article(models.Model):
    json = models.ForeignKey(Json, on_delete=models.CASCADE)

    headline = models.CharField(max_length=128, default='Why Logos Matter: The Significance Behind Changes', blank=True)
    content = models.CharField(max_length=128, default='Article content here...', blank=True)

    class Meta:
        verbose_name_plural = 'Article'

class FAQ(models.Model):
    json = models.ForeignKey(Json, on_delete=models.CASCADE)

    title_FAQ = models.CharField(max_length=100, default="Why did Instagram change its logo?")
    an_FAQ = models.TextField(default="o reflect its growth and evolution as more than just a photo-sharing platform")

    def __str__(self):
        return self.title_FAQ

    class Meta:
        verbose_name_plural = 'FAQ'


class Footer(models.Model):
    json = models.ForeignKey(Json, on_delete=models.CASCADE)

    title_text_footer = models.CharField(max_length=128, blank=True, default="Download full pack of icons")
    text_footer = models.TextField(blank=True, default="In May 2022, Instagram rolled out a visual refresh of its logo.se to our colors, typeface, logo and other brand elements,\" the company announced on its website. \"The gradient is reimagined with vibr")

    # links
    text = models.CharField(max_length=255, default='Privacy Policy', blank=True, verbose_name='links/text')
    url = models.CharField(max_length=128,default='/privacy-policy', blank=True, verbose_name='links/url')

    class Meta:
        verbose_name_plural = 'Footer'