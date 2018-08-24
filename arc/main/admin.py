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

def cgpaConversion(modeladmin, request, queryset):
    for student in queryset:
        if(CGPAConversion.objects.filter(student=student).exists()==False):
            cert=CGPAConversion.objects.create(student=student) 

def courseCompletion(modeladmin, request, queryset):
    for student in queryset:
        if(CourseCompletion.objects.filter(student=student).exists()==False):
            cert=CourseCompletion.objects.create(student=student) 

def englishMedium(modeladmin, request, queryset):
    for student in queryset:
        if(English.objects.filter(student=student).exists()==False):
            cert=English.objects.create(student=student)   

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'bitsId','username']
    actions = [graduating,thesis,cgpaConversion,courseCompletion,englishMedium]

@admin.register(Graduating)
class GraduatingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'certificate_actions',
    )
    def get_url(self, pk):
        url = '/printg/' + str(Graduating.objects.get(pk=pk).id)
        return url

    def certificate_actions(self, obj):
        return format_html  (
            '<a class="button" href="{}" target="blank_">Print</a>&nbsp;',
            self.get_url(obj.pk),
        )
    certificate_actions.short_description = 'Certificate Actions'
    certificate_actions.allow_tags = True

@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'certificate_actions',
    )
    def get_url(self, pk):
        url = '/printt/' + str(Thesis.objects.get(pk=pk).id)
        return url

    def certificate_actions(self, obj):
        return format_html  (
            '<a class="button" href="{}" target="blank_">Print</a>&nbsp;',
            self.get_url(obj.pk),
        )
    certificate_actions.short_description = 'Certificate Actions'
    certificate_actions.allow_tags = True

@admin.register(CGPAConversion)
class CGPAConversionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'certificate_actions',
    )
    def get_url(self, pk):
        url = '/printc/' + str(CGPAConversion.objects.get(pk=pk).id)
        return url

    def certificate_actions(self, obj):
        return format_html  (
            '<a class="button" href="{}" target="blank_">Print</a>&nbsp;',
            self.get_url(obj.pk),
        )
    certificate_actions.short_description = 'Certificate Actions'
    certificate_actions.allow_tags = True


@admin.register(CourseCompletion)
class CourseCompletionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'certificate_actions',
    )
    def get_url(self, pk):
        url = '/printcc/' + str(CourseCompletion.objects.get(pk=pk).id)
        return url

    def certificate_actions(self, obj):
        return format_html  (
            '<a class="button" href="{}" target="blank_">Print</a>&nbsp;',
            self.get_url(obj.pk),
        )
    certificate_actions.short_description = 'Certificate Actions'
    certificate_actions.allow_tags = True

@admin.register(English)
class EnglishAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'certificate_actions',
    )
    def get_url(self, pk):
        url = '/printe/' + str(English.objects.get(pk=pk).id)
        return url

    def certificate_actions(self, obj):
        return format_html  (
            '<a class="button" href="{}" target="blank_">Print</a>&nbsp;',
            self.get_url(obj.pk),
        )
    certificate_actions.short_description = 'Certificate Actions'
    certificate_actions.allow_tags = True