from django import forms

from wagtail.wagtailcore import blocks


class FormFieldBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=True)
    help_text = blocks.CharBlock(required=False)

    def get_form_field(self, options={}):
        raise Exception('You must implement get_form_field')

    def get_options_for_field(self, options):
        return options


class SingleLineFieldBlock(FormFieldBlock):
    def get_form_field(self, options={}):
        return forms.CharField(**options)

    class Meta:
        icon = 'italic'


class MultiLineFieldBlock(FormFieldBlock):
    def get_form_field(self, options={}):
        return forms.CharField(widget=forms.Textarea, **options)

    class Meta:
        icon = 'italic'


class RadioFieldBlock(FormFieldBlock):
    choices = blocks.ListBlock(blocks.CharBlock(required=True), required=True)

    def get_form_field(self, options={}):
        return forms.ChoiceField(widget=forms.RadioSelect, **options)

    def get_options_for_field(self, options):
        options['choices'] = [(x, x) for x in options.popitem('choices')[1]]
        return options

    class Meta:
        icon = 'radio-empty'


class CheckboxFieldBlock(FormFieldBlock):
    def get_form_field(self, options={}):
        return forms.BooleanField(**options)

    class Meta:
        icon = 'tick'


class CheckboxesFieldBlock(FormFieldBlock):
    choices = blocks.ListBlock(blocks.CharBlock(required=True), required=True)

    def get_form_field(self, options={}):
        return forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, **options)

    def get_options_for_field(self, options):
        options['choices'] = [(x, x) for x in options.popitem('choices')[1]]
        return options

    class Meta:
        icon = 'tick'


class DateFieldBlock(FormFieldBlock):
    def get_form_field(self, options={}):
        return forms.DateField(**options)

    class Meta:
        icon = 'date'


class DateTimeFieldBlock(FormFieldBlock):
    def get_form_field(self, options={}):
        return forms.DateTimeField(**options)

    class Meta:
        icon = 'time'


class NumberFieldBlock(FormFieldBlock):
    def get_form_field(self, options={}):
        return forms.DecimalField(**options)

    class Meta:
        icon = 'order'


class EmailFieldBlock(FormFieldBlock):
    def get_form_field(self, options={}):
        return forms.EmailField(**options)

    class Meta:
        icon = 'mail'


FIELD_BLOCKS = [
    ('singleline', SingleLineFieldBlock()),
    ('multiline', MultiLineFieldBlock()),
    ('radio', RadioFieldBlock()),
    ('checkbox', CheckboxFieldBlock()),
    ('checkboxes', CheckboxesFieldBlock()),
    ('date', DateFieldBlock()),
    ('datetime', DateTimeFieldBlock()),
    ('number', NumberFieldBlock()),
    ('email', EmailFieldBlock()),
]
