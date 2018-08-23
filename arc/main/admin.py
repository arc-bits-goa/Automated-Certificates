from django.contrib import admin
from main.models import *
from django.contrib.auth.models import Group,User
from django.shortcuts import render
from django.utils.html import format_html


admin.site.unregister(Group)

def graduating(modeladmin, request, queryset):
    for student in queryset:
    	if(Graduating.objects.filter(student=student).exists()==False):
    		cert=Graduating.objects.create(student=student)    	

def thesis(modeladmin, request, queryset):
    for student in queryset:
    	if(Thesis.objects.filter(student=student).exists()==False):
    		cert=Thesis.objects.create(student=student)   

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'bitsId','username']
    actions = [graduating,thesis,]

@admin.register(Graduating)
class GraduatingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'graduating_actions',
    )
    def get_url(self, pk):
        url = '/printg/' + str(Graduating.objects.get(pk=pk).id)
        return url

    def graduating_actions(self, obj):
        return format_html  (
            '<a class="button" href="{}" target="blank_">Print</a>&nbsp;',
            self.get_url(obj.pk),
        )
    graduating_actions.short_description = 'Certificate Actions'
    graduating_actions.allow_tags = True

@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'thesis_actions',
    )
    def get_url(self, pk):
        url = '/printt/' + str(Thesis.objects.get(pk=pk).id)
        return url

    def thesis_actions(self, obj):
        return format_html  (
            '<a class="button" href="{}" target="blank_">Print</a>&nbsp;',
            self.get_url(obj.pk),
        )
    thesis_actions.short_description = 'Certificate Actions'
    thesis_actions.allow_tags = True