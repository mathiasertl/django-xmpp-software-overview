# -*- coding: utf-8 -*-
#
# This file is part of django-xmpp-software-overview
# (https://github.com/mathiasertl/django-xmpp-software-overview)
#
# This project is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with django-xmpp-account.
# If not, see <http://www.gnu.org/licenses/>.

from django import template
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from core.templatetags.icons import icon_success
from core.templatetags.icons import icon_question
from core.templatetags.icons import icon_error

register = template.Library()


@register.simple_tag
def yes(tooltip=None, plugin=None):
    attrs = {}
    if plugin is not None:
        attrs['data-toggle'] = 'tooltip'
        attrs['title'] = mark_safe(_('With <a href=\'%(url)s\'>plugin</a>') % {'url': plugin})
    elif tooltip is not None:
        attrs['data-toggle'] = 'tooltip'
        attrs['title'] = mark_safe(tooltip)

    return icon_success(**attrs)


@register.simple_tag
def no():
    return icon_error()


@register.simple_tag
def unknown():
    return icon_question()


@register.simple_tag(takes_context=True)
def os_attrs(context, *os, **kwargs):
    """Add os-specific attributes to HTML elements."""

    detected = context['os']
    cls = 'os-specific %s' % ' '.join(['os-%s' % o for o in os])
    if 'cls' in kwargs:
        cls += ' %s' % kwargs['cls']
    if detected in os or ('mobile' in os and detected in ['android', 'ios']) or detected == 'any':
        cls += ' os-shown'

    attrs = {
        'class': cls.strip(),
    }
    return flatatt(attrs)
