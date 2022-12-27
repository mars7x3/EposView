from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


# class ContactsPhoneAdmin(admin.TabularInline):
#     model = ContactsPhone
#     fields = ('priem', 'faqs')
#     max_num = 100
#     extra = 0

# @admin.register(Contacts)
# class ContactsAdminList(TranslationAdmin):
#     inlines = [ContactsPhoneAdmin]

admin.site.register(Contacts)
admin.site.register(ContactsPhone)
admin.site.register(Logo)
admin.site.register(HomeBanner)
admin.site.register(HomeBook)
admin.site.register(HomeAbout)
admin.site.register(HomeAfisha)
admin.site.register(HomeComment)
admin.site.register(HomeAcademy)
admin.site.register(Partner)
admin.site.register(HomeStatistic)
admin.site.register(News)
admin.site.register(Issues)
admin.site.register(IssuesCategory)





