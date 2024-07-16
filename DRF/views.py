from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from .models import Metadata, Json, Microdata, SocialMedia, GoogleRichSnippets, \
    AdditionalSEO,ColorBody, HeroBlock, BlockHistory, AlternativeBlock, Article ,FAQ, Footer

import json
from .serializers import WebsiteSerializer

class JsonList(APIView):
    def get(self, request, pk):
        return self.jsonObject(pk)
    
    def post(self, request, pk):
        return self.jsonObject(pk)
    
    def jsonObject(self, pk):
        self.pk = pk
        
        return Response({'metadata': self.metadata_handler(),
                         'microdata': self.microdata_handler(),
                         'socialMedia': self.socialMedia_handler(),
                         'googleRichSnippets': self.GoogleRichSnippets_handler(),
                         'additionalSEO': self.additionalSEO_handler(),
                         "Color-body": self.ColorBody_handler(),
                         "Hero-block": self.HeroBlock_handler(),
                         "BlockHistory": self.BlockHistory_handler(),
                         "AlternativeBlock": self.AlternativeBlock_handler(),
                         "article": self.Article_handler(),
                         "FAQ": self.FAQ_handler(),
                         "footer": self.Footer_handler()
                         })


    def metadata_handler(self):
        metadata_list = list(Metadata.objects.filter(title_id=self.pk).values("title__title", "description", "canonical", "language"))
        keywords = list(Metadata.objects.filter(title_id=self.pk).values("keywords"))

        keywords = keywords[0]['keywords']
        metadata_list[0].update({'keywords': json.loads(keywords)})

        return metadata_list[0]

    def microdata_handler(self):
        microdata_list = list(Microdata.objects.filter(title_id=self.pk).values("schemaType", "name", "url", "logo"))
        contact = list(Microdata.objects.filter(title_id=self.pk).values("telephone", 'email'))

        contact = contact[0]

        microdata_list[0].update({'contact':
                                    {
                                        'telephone': contact['telephone'],
                                        'email': contact['email']
                                    }
        })

        return microdata_list[0]

    def socialMedia_handler(self):
        _list = list(SocialMedia.objects.filter(title_id=self.pk).values())
        return _list[0]

    def GoogleRichSnippets_handler(self):
        googleRich_list = list(GoogleRichSnippets.objects.
                            filter(title_id=self.pk).values("type",
                                                        "headline",
                                                        "author",
                                                        "datePublished",
                                                        "dateModified",
                                                        "image"
                                                        ))
        publisher = list(GoogleRichSnippets.objects.filter(title_id=self.pk).values("publisher_type",
                                                                            'name',
                                                                            'logo'))
        publisher = publisher[0]

        googleRich_list[0].update({'publisher':
            {
                'type': publisher['publisher_type'],
                'name': publisher['name'],
                'logo': publisher['logo']
            }
        })

        return googleRich_list[0]


    def additionalSEO_handler(self):
        _list = list(AdditionalSEO.objects.filter(title_id=self.pk).values('robots', 'viewport'))
        return _list[0]

    def ColorBody_handler(self):
        _list = list(ColorBody.objects.filter(title_id=self.pk).values('active_color',
                                                                'focused_color',
                                                                'def_color'))
        return _list[0]

    def HeroBlock_handler(self):
        _list = HeroBlock.objects.filter(json_id=self.pk).values('pre_title',
                                                            'title',
                                                            'description', 'icons_hero', 'download')
        return _list[0]

    def BlockHistory_handler(self):
        _list = BlockHistory.objects.filter(json_id=self.pk).values('date', 'title_history', 'description_history', 'icons_history')
        return list(_list)

    def AlternativeBlock_handler(self):
        _list = list(AlternativeBlock.objects.filter(json_id=self.pk).values('title_Alternative',
                                                                        'icons_Alternative',
                                                                        'download_Alternative'))
        return _list

    def Article_handler(self):
        _list = list(Article.objects.filter(json_id=self.pk).values('headline', 'content'))
        return _list

    def FAQ_handler(self):
        _list = list(FAQ.objects.filter(json_id=self.pk).values('title_FAQ', 'an_FAQ'))
        return _list[0]

    def Footer_handler(self):
        footer_list = list(Footer.objects.
                            filter(json_id=self.pk).values("title_text_footer",
                                                        "text_footer",
                                                        ))

        links = list(Footer.objects.filter(json_id=self.pk).values("text",
                                                                'url'))
        links = links[0]

        footer_list[0].update({'links':
            {
                'text': links['text'],
                'url': links['url'],
            }
        })
        return footer_list[0]
