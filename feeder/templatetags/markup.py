from django import template
from django.conf import settings
from django.utils.encoding import force_bytes, force_text
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
def restructuredtext(value):
    import warnings
    warnings.warn('The restructuredtext filter has been deprecated',
                  category=DeprecationWarning)
    from docutils.core import publish_parts
    docutils_settings = getattr(
        settings, "RESTRUCTUREDTEXT_FILTER_SETTINGS", {})
    parts = publish_parts(
        source=force_bytes(value),
        writer_name="html4css1",
        settings_overrides=docutils_settings)
    return mark_safe(force_text(parts["html_body"]))
