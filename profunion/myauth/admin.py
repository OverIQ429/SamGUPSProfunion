from django.contrib import admin
from .models import Appends, Description, AllGroups, Decision, Profile
# Register your models here.

@admin.register(Appends)
class AppendsAdmin(admin.ModelAdmin):
    list_display = ("user", "description", "file", "commentary", "decision")

@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ("text", )

@admin.register(AllGroups)
class AllGroupsAdmin(admin.ModelAdmin):
    list_display = ("groupname", "course", "faculty",)

@admin.register(Decision)
class DecisionAdmin(admin.ModelAdmin):
    list_display = ("text", )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "group", "email", "phone_number", "agreement_accepted", "avatar", "is_union_member",)