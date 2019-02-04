from django.contrib import admin
from main.models import *
from django.contrib.auth.models import Group,User
from django.shortcuts import render
from django.utils.html import format_html
from import_export.admin import ImportExportActionModelAdmin

admin.site.unregister(Group)
# admin.site.register(Text)

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

def fwdContinuing(modeladmin, request, queryset):
    for student in queryset:
        if(Continuing.objects.filter(student=student).exists()==False):
            cert=Continuing.objects.create(student=student) 

def fwdGraduated(modeladmin, request, queryset):
    for student in queryset:
        if(Graduated.objects.filter(student=student).exists()==False):
            cert=Graduated.objects.create(student=student) 

def oneSemesterThesis(modeladmin, request, queryset):
    for student in queryset:
        if(ThesisSem.objects.filter(student=student).exists()==False):
            cert=ThesisSem.objects.create(student=student)  

@admin.register(Student)
class StudentAdmin(ImportExportActionModelAdmin):
    search_fields = ['name', 'bitsId',]
    actions = [graduating,thesis,cgpaConversion,courseCompletion,englishMedium,fwdContinuing,fwdGraduated,oneSemesterThesis]

@admin.register(Graduated_Students)
class GraduatedAdmin(ImportExportActionModelAdmin):
    search_fields = ['name', 'campusid',]

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

@admin.register(Continuing)
class ContinuingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'certificate_actions',
    )
    def get_url(self, pk):
        url = '/printfc/' + str(Continuing.objects.get(pk=pk).id)
        return url

    def certificate_actions(self, obj):
        return format_html  (
            '<a class="button" href="{}" target="blank_">Print</a>&nbsp;',
            self.get_url(obj.pk),
        )
    certificate_actions.short_description = 'Certificate Actions'
    certificate_actions.allow_tags = True

@admin.register(Graduated)
class GraduatedAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'certificate_actions',
    )
    def get_url(self, pk):
        url = '/printfg/' + str(Graduated.objects.get(pk=pk).id)
        return url

    def certificate_actions(self, obj):
        return format_html  (
            '<a class="button" href="{}" target="blank_">Print</a>&nbsp;',
            self.get_url(obj.pk),
        )
    certificate_actions.short_description = 'Certificate Actions'
    certificate_actions.allow_tags = True


@admin.register(ThesisSem)
class ThesisSemdAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'certificate_actions',
    )
    def get_url(self, pk):
        url = '/printts/' + str(ThesisSem.objects.get(pk=pk).id)
        return url

    def certificate_actions(self, obj):
        return format_html  (
            '<a class="button" href="{}" target="blank_">Print</a>&nbsp;',
            self.get_url(obj.pk),
        )
    certificate_actions.short_description = 'Certificate Actions'
    certificate_actions.allow_tags = True