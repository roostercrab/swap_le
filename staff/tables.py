import django_tables2 as tables
from .models import Staff
import itertools
from django.utils.html import format_html
from students.models import Student
from django_tables2 import A


class StaffTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name="Row")
    edit_staff = tables.TemplateColumn('<a href=" {% url "institutions:edit_institution_staff" username=record.staffuser  %} ">Edit</a>')
    delete_staff = tables.TemplateColumn('<a href=" {% url "institutions:delete_institution_staff" username=record.staffuser  %} ">Delete</a>')
    email_student = tables.Column(accessor='staffuser.email',
                          verbose_name='Email')
    first_name = tables.Column(accessor='staffuser.first_name',
                          verbose_name='First Name')
    last_name = tables.Column(accessor='staffuser.last_name',
                          verbose_name='Last Name')
    
    def __init__(self, *args, **kwargs):
        super(StaffTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_row_number(self):
        return '%d' % (int(next(self.counter))+1)

    

    class Meta:
        model = Staff
        # add class="paleblue" to <table> tag
        exclude = ('id', 'deleted', 'user_type', 'institute', 'created', 'updated', 'allowregistration', )
        attrs = {'class': 'paleblue'}
        # fields = ('row_number', 'institute',)
        sequence = ('row_number', 'staffuser', 'first_name', 'last_name', 'email_student', 'user_type', 'deleted')



class StudentTable(tables.Table):
    row_number = tables.Column(empty_values=())
    first_name = tables.Column(accessor='studentuser.first_name',
                               verbose_name='First Name')
    last_name = tables.Column(accessor='studentuser.last_name',
                              verbose_name='Last Name')
    email = tables.Column(accessor='studentuser.email',
                          verbose_name='Mail Address')
    
    edit_student = tables.TemplateColumn('<a href=" {% url "staff:student_edit_by_staff" upk=record.pk  %} ">Edit</a>')
    delete_student = tables.TemplateColumn('<a href=" {% url "staff:delete_institution_staff_student" username=record.studentuser  %} ">Delete</a>')
    student_fees = tables.TemplateColumn('<a href=" {% url "staff:fees:manage_fees_installment" pk=record.id  %} ">Installment</a>')
    
    def __init__(self, *args, **kwargs):
        super(StudentTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_row_number(self):
        return ' %d' % next(self.counter)

    def render_first_name(self,value):
        return value
    
    def render_last_name(self,value):
        return value
    
    def render_email(self,value):
        return value
    class Meta:
        model = Student
        sequence = ('row_number', 'studentuser','first_name','last_name','email', 'staffuser', 'created', 'updated', 'user_type', )
        # add class="paleblue" to <table> tag 
        attrs = {'class': 'paleblue'}
        # fields = ('row_number', 'institute',)
        exclude = ('id', 'deleted', 'last_login')

