from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.core.mail import send_mail
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from django.utils.translation import gettext as _



class ContactForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
    name = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': _('Your Name*'),
                                                            'class': 'form-control'})
                            )
    message = forms.CharField(max_length=2500,
                                widget=forms.Textarea(attrs={'placeholder': _('Your Message*'),
                                                                'class': 'form-control'}))
    client_email = forms.EmailField(
                                widget=forms.EmailInput(attrs={'placeholder': _('Your Email*'),
                                                                'class': 'form-control'})
                                )
    subject = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': _('Subject*'),
                                                            'class': 'form-control'})
                            )
    client_phone = PhoneNumberField(required=False,
                                    widget=forms.TextInput(attrs={'placeholder': _('Phone Number'),
                                                                    'class': 'form-control'})
                                    )

    def send_email(self, current_url):
        name = self.cleaned_data['name']
        message = self.cleaned_data['message']
        client_email = self.cleaned_data['client_email']
        client_phone = self.cleaned_data['client_phone']
        client_subject = self.cleaned_data['subject']
        recipients = ['contact@lavinomood.com', client_email]
        mail_subject = 'LaVino Group Received Your Message - {}'.format(client_subject)

        message_edited = '''Dear {},

Many thanks for contacting us.
We have successfully received your below message. Our team will contact you shortly.

___________________________________________

{} - Phone Number: {}
eMail Address: {}

{}

___________________________________________
Kind Regards,
LaVino Mood Team
https://www.lavinomood.com
'''
        message_edited = message_edited.format(name, name,client_phone, client_email, message)
        send_mail(mail_subject, message_edited, 'contact@lavinomood.com', recipients)
        pass

# Form Farsi
class ContactForm_fa(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
    name = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'نام*',
                                                            'class': 'form-control'})
                            )
    message = forms.CharField(max_length=2500,
                                widget=forms.Textarea(attrs={'placeholder': 'پیام شما*',
                                                                'class': 'form-control'}))
    client_email = forms.EmailField(
                                widget=forms.EmailInput(attrs={'placeholder': 'ایمیل*',
                                                                'class': 'form-control'})
                                )
    subject = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'عنوان*',
                                                            'class': 'form-control'})
                            )
    client_phone = PhoneNumberField(required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'شماره تماس',
                                                                    'class': 'form-control'})
                                    )

    def send_email(self, current_url):
        name = self.cleaned_data['name']
        message = self.cleaned_data['message']
        client_email = self.cleaned_data['client_email']
        client_phone = self.cleaned_data['client_phone']
        client_subject = self.cleaned_data['subject']
        recipients = ['contact@lavinomood.com', client_email]
        mail_subject = 'LaVino Group Received Your Message - {}'.format(client_subject)

        message_edited = '''{} عزیز,

از پیام شما سپاسگزاریم.
پیغام شما با موفقیت به دست تیم لاوینو رسیده است، و بزودی با شما تماس خواهیم گرفت.

___________________________________________

{} - شماره تماس: {}
آدرس ایمیل: {}

{}

___________________________________________
ارادتمند,
LaVino Mood Team
https://www.lavinomood.com
'''
        message_edited = message_edited.format(name, name,client_phone, client_email, message)
        send_mail(mail_subject, message_edited, 'contact@lavinomood.com', recipients)
        pass
