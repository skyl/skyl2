from django.contrib import admin

from feeder.models import Member


class MemberAdmin(admin.ModelAdmin):
    change_form_template = add_form_template = "member_change_form.html"

    class Media:
        css = {
            "all": ["css/native.css"],
        }

admin.site.register(Member, MemberAdmin)
