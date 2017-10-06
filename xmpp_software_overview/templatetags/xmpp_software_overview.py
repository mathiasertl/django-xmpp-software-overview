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
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def yes():
    return mark_safe('<span class="glyphicon glyphicon-ok text-success" aria-hidden="true"></span>')


@register.simple_tag
def no():
    return mark_safe('<span class="glyphicon glyphicon-remove text-danger" aria-hidden="true"></span>')


@register.simple_tag
def unknown():
    return mark_safe('<span class="glyphicon glyphicon-question-sign text-muted" aria-hidden="true"></span>')
