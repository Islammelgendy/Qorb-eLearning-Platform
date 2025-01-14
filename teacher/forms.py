from attr import field
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm

# local imports goes here 
from accounts.models import Profile, Teacher
from src.current_user import get_current_user
from .models import ( 
    Course,Student, Subject, Report,Report_student)


User = get_user_model()
# <-------------------------- Teacher Profile Form ------------------------------------------> 

class UpdateUserForm(forms.ModelForm):
	username = forms.CharField(max_length=100, required=True,
	                           widget=forms.TextInput(attrs={'class': 'input-i'}))
	email = forms.EmailField(required=True, widget=forms.TextInput(
	    attrs={'class': 'input-i'}))

	class Meta:
		model = User
		fields = ['username', 'email']
        


class UpdateTeacherProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        "hidden":"hidden","name":"posti" ,"accept":"image/*","id":"id_posti",'class':'img-i-1',"onchange":"loadFile(event)" 
    }))
    age = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'class': 'input-i'}))
    full_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'class': 'input-i'}))

    
    class Meta:
        model = Teacher 
        fields = ['avatar', 'age', 'full_name']

    


class FormPasswordChange(PasswordChangeForm):
    
    old_password = forms.CharField(label='كلمة المرور القديمة',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='كلمة المرور الجديدة',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='تأكيد كلمة المرور الجديدة',widget=forms.PasswordInput(attrs={'class': 'form-control'})) 



# <---------------------------------- Teacher Course form --------------------------------------------> 


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name','description','image',]

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'اسم الكورس','id': 'course_name_id'}))
    description = forms.CharField(widget=forms.Textarea(attrs={ 'row':5,'id': 'description_id'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"hidden":"hidden","name":"posti" ,"accept":"image/*","id":"id_posti",'class':'img-i-1',"onchange":"loadFile(event)" }))


class AddMatrialForm(forms.ModelForm):
    document = forms.FileField(widget=forms.FileInput(attrs={"hidden":"hidden","name":"posti" ,"id":"id_posti",'class':'img-i-1','onchange':"loadFile()"}))
    class Meta:
        model = Subject
        fields = ('description', 'document', )

class AddReportForm(forms.ModelForm):
    document = forms.FileField(widget=forms.FileInput(attrs={"hidden":"hidden","name":"posti2" ,"id":"id_posti2",'class':'img-i-1','onchange':"loadFile2()"}))
    class Meta:
        model = Report
        fields = ('description_report', 'document', )





class UpdateReportGradeForm(forms.ModelForm):
    class Meta:
        model = Report_student
        fields = ['teacher_notes', 'grade','deadline']
    deadline = forms.DateField(input_formats = ['%Y-%m-%dT%H:%M'],widget=forms.widgets.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
    )

class UpdateReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['deadline']
    deadline = forms.DateField(input_formats = ['%Y-%m-%dT%H:%M'],widget=forms.widgets.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
    )
    