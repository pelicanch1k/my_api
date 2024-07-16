from django.contrib import admin

from .models import Metadata, Json, Microdata, SocialMedia, GoogleRichSnippets,\
    AdditionalSEO, \
    ColorBody, HeroBlock, BlockHistory, AlternativeBlock, FAQ, Footer, Article


class MetaDataAdmin(admin.TabularInline):
    model = Metadata
    fields = ('description', 'keywords', 'canonical', 'language')
    extra = 0

class MicrodataAdmin(admin.TabularInline):
    model = Microdata
    fields = ('schemaType', 'name', 'url', 'logo', 'telephone', 'email')
    extra = 0

class SocialMediaAdmin(admin.TabularInline):
    model = SocialMedia
    fields = ('ogTitle',
              'ogType',
              'ogImage',
              'ogDescription',
              'twitterCard',
              'twitterSite',
              'twitterTitle',
              'twitterDescription',
              'twitterImage'
              )
    extra = 0

class GoogleRichSnippetsAdmin(admin.TabularInline):
    model = GoogleRichSnippets
    fields = ('type',
              'headline',
              'author',
              'datePublished',
              'dateModified',
              'image',
              'publisher_type',
              'name',
              'logo'
              )
    extra = 0

class AdditionalSEOAdmin(admin.TabularInline):
    model = AdditionalSEO
    fields = ('robots',
              'viewport'
              )
    extra = 0

class ColorBodyAdmin(admin.TabularInline):
    model = ColorBody
    fields = ('active_color',
              'focused_color',
              'def_color'
              )
    extra = 0

class HeroBlockAdmin(admin.TabularInline):
    model = HeroBlock
    fields = ('pre_title',
              'title',
              'description',
              'icons_hero',
              'download'
              )
    extra = 0

class BlockHistoryAdmin(admin.TabularInline):
    model = BlockHistory
    fields = ('date',
              'title_history',
              'description_history',
              'icons_history',
              )
    extra = 0

class AlternativeBlockAdmin(admin.TabularInline):
    model = AlternativeBlock
    fields = ('title_Alternative',
              'icons_Alternative',
              'download_Alternative',
              )
    extra = 0

class ArticleAdmin(admin.TabularInline):
    model = Article
    fields = ('headline',
              'content'
              )
    extra = 0

class FAQAdmin(admin.TabularInline):
    model = FAQ
    fields = ('title_FAQ',
              'an_FAQ'
              )
    extra = 0

class FooterAdmin(admin.TabularInline):
    model = Footer
    fields = ('title_text_footer',
              'text_footer',
              'text',
              'url'
              )
    extra = 0

@admin.register(Json)
class JsonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    inlines = (
        MetaDataAdmin,
       MicrodataAdmin,
       SocialMediaAdmin,
       GoogleRichSnippetsAdmin,
       AdditionalSEOAdmin,
       ColorBodyAdmin,
       HeroBlockAdmin,
       BlockHistoryAdmin,
       AlternativeBlockAdmin,
        ArticleAdmin,
       FAQAdmin,
       FooterAdmin,
           )
