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
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def yes(tooltip=None):
    attrs = {
        'class': 'glyphicon glyphicon-ok text-success',
        'aria-hidden': 'true',
    }
    if tooltip is not None:
        attrs['data-toggle'] = 'tooltip'
        attrs['title'] = mark_safe(tooltip)
    return format_html('<span {}></span>', flatatt(attrs))


@register.simple_tag
def no():
    return mark_safe('<span class="glyphicon glyphicon-remove text-danger" aria-hidden="true"></span>')


@register.simple_tag
def unknown():
    return mark_safe('<span class="glyphicon glyphicon-question-sign text-muted" aria-hidden="true"></span>')
