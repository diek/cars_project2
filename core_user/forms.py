from django.forms import forms, DateField, DateInput, ModelForm, ValidationError
from django.forms.formsets import BaseFormSet
from .models import Profile, User, SecondaryEmailSMS


class Html5DateInput(DateInput):
    input_type = 'date'


class UserForm(ModelForm):
    date_joined = DateField(
        required=False,
        widget=Html5DateInput,
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'date_joined')

    def clean_date_joined(self):
        cd = self.cleaned_data
        date = cd['date_joined']
        if date:
            return date
        else:
            raise ValidationError("Enter a date.")

    def save(self, commit=True):
        date = self.cleaned_data["date_joined"]
        user = super(UserForm, self).save(commit=False)
        user.date_joined = date
        if commit:
            user.save()
        return user


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location')


class EmailSMSForm(ModelForm):
    class Meta:
        model = SecondaryEmailSMS
        fields = ('alternate_email', 'alternate_sms_telephone')


# ---- Formset
class BaseLinkFormSet(BaseFormSet):
    def clean(self):
        """
        Adds validation to check that no two links have the same anchor or URL
        and that all links have both an anchor and URL.
        """
        if any(self.errors):
            return

        anchors = []
        urls = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                anchor = form.cleaned_data['anchor']
                url = form.cleaned_data['url']

                # Check that no two links have the same anchor or URL
                if anchor and url:
                    if anchor in anchors:
                        duplicates = True
                    anchors.append(anchor)

                    if url in urls:
                        duplicates = True
                    urls.append(url)

                if duplicates:
                    raise forms.ValidationError(
                        'Links must have unique anchors and URLs.',
                        code='duplicate_links'
                    )

                # Check that all links have both an anchor and URL
                if url and not anchor:
                    raise forms.ValidationError(
                        'All links must have an anchor.',
                        code='missing_anchor'
                    )
                elif anchor and not url:
                    raise forms.ValidationError(
                        'All links must have a URL.',
                        code='missing_URL'
                    )
