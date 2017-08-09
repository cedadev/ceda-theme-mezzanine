from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.utils.admin import SingletonAdmin
from mezzanine.pages.admin import PageAdmin

from models import (SiteSectionPage,
                    Portfolio, PortfolioItem, PortfolioItemImage,
                    PortfolioItemPerson,
                    PortfolioItemCategory, IconBox, HomePage, Slide)


admin.site.register(SiteSectionPage, PageAdmin)

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class PortfolioItemImageInline(TabularDynamicInlineAdmin):
    model = PortfolioItemImage
    max_num = 3

class PortfolioItemPersonInline(TabularDynamicInlineAdmin):
    model = PortfolioItemPerson
    max_num = 40

class PortfolioItemAdmin(PageAdmin):
    inlines = (PortfolioItemImageInline,PortfolioItemPersonInline)

admin.site.register(Portfolio, PageAdmin)
admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory)


class IconInline(TabularDynamicInlineAdmin):
    model = IconBox

class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, IconInline)

admin.site.register(HomePage, HomePageAdmin)
