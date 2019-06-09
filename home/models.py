from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core import blocks
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['menuitems'] = self.get_children().filter(live=True, show_in_menus=True)

        return context

    home_title = models.CharField(
        "Название сайта",
        max_length=255,
        blank=True,
        null=True
    )
    home_description = models.TextField(
        "Описание",
        blank=True,
        null=True
    )
    home_telephone = models.IntegerField(
        "Телефон",
        blank=True,
        null=True
    )
    home_address = models.CharField(
        "Адрес",
        max_length=255,
        blank=True,
        null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('home_title'),
        FieldPanel('home_description'),
        FieldPanel('home_telephone'),
        FieldPanel('home_address')
    ]

