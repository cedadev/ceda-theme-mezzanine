from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.utils.admin import SingletonAdmin
from mezzanine.pages.admin import PageAdmin

from copy import deepcopy

from models import (SiteSectionPage,
                    Portfolio, PortfolioItem, PortfolioItemImage,
                    Person,PortfolioItemPerson,
                    PortfolioItemCategory, IconBox, HomePage, Slide)
from django.forms import TextInput, Textarea
from django.db import models

admin.site.register(SiteSectionPage, PageAdmin)

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class PortfolioItemPersonInline(TabularDynamicInlineAdmin):
    model = PortfolioItemPerson

class PortfolioItemImageInline(TabularDynamicInlineAdmin):
    model = PortfolioItemImage
    max_num = 3

# Specify order for fields from custom model
portfolioitem_fieldsets = deepcopy(PageAdmin.fieldsets)
for field in ("icon", "leader", "intro", "content", "href", "button_text", "categories"):
    portfolioitem_fieldsets[0][1]["fields"].insert(-2, field)

class PortfolioItemAdmin(PageAdmin):
    inlines = (PortfolioItemImageInline,PortfolioItemPersonInline)
    fieldsets = portfolioitem_fieldsets

admin.site.register(Portfolio, PageAdmin)
admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory)
admin.site.register(Person)


class IconInline(TabularDynamicInlineAdmin):
    model = IconBox

class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, IconInline)

admin.site.register(HomePage, HomePageAdmin)
