from django.db import models
from datetime import datetime

BRANCH = {
    'A1': 'B.E.(Hons) Chemical Engineering',
    'A3': 'B.E.(Hons) Electrical and Electronics Engineering',
    'A4': 'B.E.(Hons) Mechanical Engineering',
    'A7': 'B.E.(Hons) Computer Science',
    'A8': 'B.E.(Hons) Electronics and Instrumentation Engineering',
    'B1': 'MSc. (Hons) Biology',
    'B2': 'MSc. (Hons) Chemistry',
    'B3': 'MSc. (Hons) Economics',
    'B4': 'MSc. (Hons) Mathematics',
    'B5': 'MSc. (Hons) Physics',
    'AA': 'B.E.(Hons) Electronics and Communication Engineering',
    'PH': 'PhD.',
    'H1': 'M.E. (Hons) Computer Science',

}

YEARNAMES = {
     1: 'first',
     2: 'second',
     3: 'third',
     4: 'forth',
     5: 'fifth',
}

STUDENT_STATUS = (
    ('Student', 'Student'),
    ('Thesis', 'Thesis'),
    ('PS2', 'PS2'),
    ('Graduate', 'Graduate'))

class Student(models.Model):    
    name = models.CharField(max_length=50,null=True)
    bitsId = models.CharField(max_length=15,null=True)
    username = models.CharField(max_length=10,null=True)
    gender = models.CharField(max_length=1, blank=True)
    cgpa = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.bitsId + ' (' + self.name + ')'
class Graduating(models.Model):
    student = models.ForeignKey('Student', on_delete = models.CASCADE)
    text = models.TextField(default='', blank=True)

    def createText(self):
        gender = "Mr. " if self.student.gender.lower() == 'm' else "Ms. "
        pronoun = "He " if gender=="Mr. " else "She "
        firstDeg=self.student.bitsId[4:6]
        secondDeg=self.student.bitsId[6:8]
        branch = BRANCH[firstDeg]
        if secondDeg != 'PS' and firstDeg != 'H1' and firstDeg != 'PH':
            branch = branch +' and '+ BRANCH[secondDeg]
        return "This is to certify that "+self.student.name+", ID No. "+self.student.bitsId + " is a student of "+branch +" of the institute. "+pronoun+" is likely to be graduated in July 2018 from our institute after completing all the course requirements at the end of second semester 2017-2018."

    def save(self, *args, **kwargs):
        if self.text == '':
            self.text = self.createText()
        super(Graduating, self).save(*args, **kwargs)

    def __str__(self):
        return self.student.bitsId + ' (' + self.student.name + ')'
    class Meta:
        verbose_name_plural = "Graduating Certificates"
class Thesis(models.Model):
    student = models.ForeignKey('Student', on_delete = models.CASCADE)
    text = models.TextField(default='', blank=True)

    def createText(self):
        gender = "Mr. " if self.student.gender.lower() == 'm' else "Ms. "
        pronoun = "He " if gender=="Mr. " else "She "
        firstDeg=self.student.bitsId[4:6]
        secondDeg=self.student.bitsId[6:8]
        branch = BRANCH[firstDeg]
        if secondDeg != 'PS' and firstDeg != 'H1' and firstDeg != 'PH':
            branch = branch +' and '+ BRANCH[secondDeg]
        return "This is to certify that this institute permits students to do thesis for a year as part of their course curriculum. The following bonafide student of BITS, Pilani K.K Birla Goa Campus student will be doing an off campus thesis for the academic year 2013-2014";

    def save(self, *args, **kwargs):
        if self.text == '':
            self.text = self.createText()
        super(Thesis, self).save(*args, **kwargs)

    def __str__(self):
        return self.student.bitsId + ' (' + self.student.name + ')'
    class Meta:
        verbose_name_plural = "Thesis Certificates"

class CGPAConversion(models.Model):
    student = models.ForeignKey('Student', on_delete = models.CASCADE)
    text = models.TextField(default='', blank=True)

    def createText(self):
        gender = "Mr. " if self.student.gender.lower() == 'm' else "Ms. "
        pronoun = "He " if gender=="Mr. " else "She "
        firstDeg=self.student.bitsId[4:6]
        secondDeg=self.student.bitsId[6:8]
        branch = BRANCH[firstDeg]
        if secondDeg != 'PS' and firstDeg != 'H1' and firstDeg != 'PH':
            branch = branch +' and '+ BRANCH[secondDeg]
        return "This is to certify that "+self.student.name+", ID No. "+self.student.bitsId + " has obtained a CGPA "+self.student.cgpa +" at the end of second semester 2016-2017. This is equivalent to "+pronoun+" based on the formula used by the institution for the conversion of CGPA of a candidate into equivalent percentage.<br><br>Equivalent percentage = (CGPA obtained/10*) x 100<br>*Maximum CGPA"

    def save(self, *args, **kwargs):
        if self.text == '':
            self.text = self.createText()
        super(CGPAConversion, self).save(*args, **kwargs)

    def __str__(self):
        return self.student.bitsId + ' (' + self.student.name + ')'
    class Meta:
        verbose_name_plural = "CGPA Conversion Certificates"

class CourseCompletion(models.Model):
    student = models.ForeignKey('Student', on_delete = models.CASCADE)
    text = models.TextField(default='', blank=True)

    def createText(self):
        gender = "Mr. " if self.student.gender.lower() == 'm' else "Ms. "
        pronoun = "He " if gender=="Mr. " else "She "
        firstDeg=self.student.bitsId[4:6]
        secondDeg=self.student.bitsId[6:8]
        branch = BRANCH[firstDeg]
        if secondDeg != 'PS' and firstDeg != 'H1' and firstDeg != 'PH':
            branch = branch +' and '+ BRANCH[secondDeg]
        return "This is to certify that "+self.student.name+", ID No. "+self.student.bitsId + " is a final year student of this institute and has completed all the course requirements of B.E(Hons.) Computer Science Engineering at the end of first semester 2017-2018."

    def save(self, *args, **kwargs):
        if self.text == '':
            self.text = self.createText()
        super(CourseCompletion, self).save(*args, **kwargs)

    def __str__(self):
        return self.student.bitsId + ' (' + self.student.name + ')'
    class Meta:
        verbose_name_plural = "Course Completion Certificates"

class English(models.Model):
    student = models.ForeignKey('Student', on_delete = models.CASCADE)
    text = models.TextField(default='', blank=True)

    def createText(self):
        gender = "Mr. " if self.student.gender.lower() == 'm' else "Ms. "
        pronoun = "He " if gender=="Mr. " else "She "
        firstDeg=self.student.bitsId[4:6]
        secondDeg=self.student.bitsId[6:8]
        branch = BRANCH[firstDeg]
        if secondDeg != 'PS' and firstDeg != 'H1' and firstDeg != 'PH':
            branch = branch +' and '+ BRANCH[secondDeg]
        return "This is to certify that "+self.student.name+", ID No. "+self.student.bitsId + " is a student of "+branch +" of the institute.<br>English is the sole medium of instruction in the institute."

    def save(self, *args, **kwargs):
        if self.text == '':
            self.text = self.createText()
        super(English, self).save(*args, **kwargs)

    def __str__(self):
        return self.student.bitsId + ' (' + self.student.name + ')'
    class Meta:
        verbose_name_plural = "English Medium Certificates"

class Continuing(models.Model):
    student = models.ForeignKey('Student', on_delete = models.CASCADE)
    text = models.TextField(default='', blank=True)

    def createText(self):
        gender = "Mr. " if self.student.gender.lower() == 'm' else "Ms. "
        pronoun = "He " if gender=="Mr. " else "She "
        firstDeg=self.student.bitsId[4:6]
        secondDeg=self.student.bitsId[6:8]
        branch = BRANCH[firstDeg]
        if secondDeg != 'PS' and firstDeg != 'H1' and firstDeg != 'PH':
            branch = branch +' and '+ BRANCH[secondDeg]
        return "Please find attached the true copy of the transcripts of "+self.student.name +" ID No. "+self.student.bitsId+" who is a student of "+branch+ " of this institute."
    def save(self, *args, **kwargs):
        if self.text == '':
            self.text = self.createText()
        super(Continuing, self).save(*args, **kwargs)

    def __str__(self):
        return self.student.bitsId + ' (' + self.student.name + ')'
    class Meta:
        verbose_name_plural = "Forwarding(Continuing) Certificates"

class Graduated(models.Model):
    student = models.ForeignKey('Student', on_delete = models.CASCADE)
    text = models.TextField(default='', blank=True)

    def createText(self):
        gender = "Mr. " if self.student.gender.lower() == 'm' else "Ms. "
        pronoun = "He " if gender=="Mr. " else "She "
        firstDeg=self.student.bitsId[4:6]
        secondDeg=self.student.bitsId[6:8]
        branch = BRANCH[firstDeg]
        if secondDeg != 'PS' and firstDeg != 'H1' and firstDeg != 'PH':
            branch = branch +' and '+ BRANCH[secondDeg]
        return "Please find attached the true copy of the transcripts of "+self.student.name +" ID No. "+self.student.bitsId+" who is a student of "+branch+ " of this institute."

    def save(self, *args, **kwargs):
        if self.text == '':
            self.text = self.createText()
        super(Graduated, self).save(*args, **kwargs)

    def __str__(self):
        return self.student.bitsId + ' (' + self.student.name + ')'
    class Meta:
        verbose_name_plural = "Forwarding(Graduated) Certificates"

class ThesisSem(models.Model):
    student = models.ForeignKey('Student', on_delete = models.CASCADE)
    text = models.TextField(default='', blank=True)

    def createText(self):
        gender = "Mr. " if self.student.gender.lower() == 'm' else "Ms. "
        pronoun = "He " if gender=="Mr. " else "She "
        firstDeg=self.student.bitsId[4:6]
        secondDeg=self.student.bitsId[6:8]
        branch = BRANCH[firstDeg]
        if secondDeg != 'PS' and firstDeg != 'H1' and firstDeg != 'PH':
            branch = branch +' and '+ BRANCH[secondDeg]
        return "This is to certify that this institute permits students to do thesis for a semester as part of their course curriculum. The following bonafide student of BITS, Pilani K.K Birla Goa Campus student will be doing an off campus thesis for the Semester 1 2018-2019";

    def save(self, *args, **kwargs):
        if self.text == '':
            self.text = self.createText()
        super(ThesisSem, self).save(*args, **kwargs)

    def __str__(self):
        return self.student.bitsId + ' (' + self.student.name + ')'
    class Meta:
        verbose_name_plural = "One semester Thesis Certificates"
