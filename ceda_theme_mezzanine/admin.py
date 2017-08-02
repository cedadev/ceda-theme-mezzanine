from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.utils.admin import SingletonAdmin
from mezzanine.pages.admin import PageAdmin

from models import (SiteSectionPage,
                    Portfolio, PortfolioItem, PortfolioItemImage,
                    PortfolioItemCategory, IconBox, HomePage, Slide)


admin.site.register(SiteSectionPage, PageAdmin)

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class PortfolioItemImageInline(TabularDynamicInlineAdmin):
    model = PortfolioItemImage
    max_num = 3

class PortfolioItemAdmin(PageAdmin):
    inlines = (PortfolioItemImageInline,)

admin.site.register(Portfolio, PageAdmin)
admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory)


class IconInline(TabularDynamicInlineAdmin):
    model = IconBox

class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, IconInline)

admin.site.register(HomePage, HomePageAdmin)
