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

import os
import subprocess
import sys
from distutils.cmd import Command

from setuptools import setup

install_requires = [
    'Django>=2.0',
]


class QualityCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ca.test_settings")

        print('isort --check-only --diff -rc xmpp_software_overview/ setup.py')
        status = subprocess.call(['isort', '--check-only', '--diff', '-rc',
                                  'xmpp_software_overview/', 'setup.py'])
        if status != 0:
            sys.exit(status)

        print('flake8 xmpp_software_overview/ setup.py')
        status = subprocess.call(['flake8', 'xmpp_software_overview/', 'setup.py'])
        if status != 0:
            sys.exit(status)

        # TODO
        #work_dir = os.path.join(_rootdir, 'ca')
        #os.chdir(work_dir)
        #print('python -Wd manage.py check')
        #status = subprocess.call(['python', '-Wd', 'manage.py', 'check'])
        #if status != 0:
        #    sys.exit(status)


def find_package_data(dir):
    data = []
    package_root = 'xmpp_software_overview/'
    for root, dirs, files in os.walk(os.path.join(package_root, dir)):
        for file in files:
            if file.endswith('.swp'):
                continue
            data.append(os.path.join(root, file)[len(package_root):])
    return data


package_data = find_package_data('static') + find_package_data('templates')


setup(
    name='django-xmpp-software-overview',
    version='0.1.0',
    description='A Django app providing an overview of available XMPP clients and servers.',
    author='Mathias Ertl',
    author_email='mati@er.tl',
    url='https://github.com/mathiasertl/django-xmpp-software-overview',
    packages=[
        'xmpp_software_overview',
        'xmpp_software_overview.migrations',
        'xmpp_software_overview.templatetags',
    ],
    #package_dir={'': 'ca'},
    package_data={'': package_data},
    zip_safe=False,  # because of the static files
    install_requires=install_requires,
    cmdclass={
        #'coverage': CoverageCommand,
        #'test': TestCommand,
        'code_quality': QualityCommand,
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django :: 2.0',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security :: Cryptography',
        'Topic :: Security',
    ],
)
