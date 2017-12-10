from collections import OrderedDict
from django.utils.six import text_type
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from unidecode import unidecode
from wagtail.wagtailforms import models

from wagtailstreamfieldforms.forms import BaseForm


def clean_name(name):
    # unidecode will return an ascii string while slugify wants a
    # unicode string on the other hand, slugify returns a safe-string
    # which will be converted to a normal str
    return str(slugify(text_type(unidecode(name))))


class StreamFieldFormMixin:
    def get_form_fields_field_name(self):
        return 'form_fields'

    def get_form_fields(self):
        fields = getattr(self, self.get_form_fields_field_name())
        formfields = OrderedDict()

        for field in fields:
            options = field.block.get_options_for_field(field.value)
            formfields[clean_name(field.value[
                'label'])] = field.block.get_form_field(options=options)

        return formfields

    def get_data_fields(self):
        data_fields = [
            ('submit_time', _('Submission Date')),
        ]
        data_fields += [
            (clean_name(field.value['label']), field.value['label'])
            for field in getattr(self, self.get_form_fields_field_name())
        ]

        return data_fields

    def get_form_class(self):
        return type(
            str('WagtailSurveysForm'), (BaseForm, ), self.get_form_fields())


class AbstractForm(StreamFieldFormMixin, models.AbstractForm):
    class Meta:
        abstract = True


class AbstractEmailForm(models.AbstractEmailForm, StreamFieldFormMixin):
    class Meta:
        abstract = True
