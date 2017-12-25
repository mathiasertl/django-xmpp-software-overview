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

from ua_parser import user_agent_parser

from django.views.generic.base import TemplateView


class ClientsView(TemplateView):
    template_name = 'xmpp_software_overview/clients.html'

    def get_context_data(self, **kwargs):
        context = super(ClientsView, self).get_context_data(**kwargs)
        if 'os' in self.request.GET:
            context['os'] = self.request.GET['os']
        else:
            ua_string = self.request.META['HTTP_USER_AGENT']
            ua_parsed = user_agent_parser.ParseOS(ua_string)
            os = ua_parsed['family'].lower().strip()
            if os == 'mac os x':
                context['os'] = 'osx'
            elif os == 'ios':
                context['os'] = 'ios'
            elif os == 'android':
                context['os'] = 'android'
            elif os == 'linux':
                context['os'] = 'linux'
            elif os.startswith('windows'):
                context['os'] = 'win'
            else:
                context['os'] = 'any'
        context['os_mobile'] = context['os'] in ['android', 'ios']

        return context
