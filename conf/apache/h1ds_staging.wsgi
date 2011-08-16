import os
import sys

import site

# Find absolute path of project.
THIS_DIR = os.path.abspath(os.path.dirname(__file__))
n_subdir = 3
PROJECT_ROOT = THIS_DIR
for i in range(n_subdir):
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

# Find the python dir in the virtualenv
for dir in os.listdir(os.path.join(PROJECT_ROOT, 'lib')):
    if dir.startswith('python'):
       site.addsitedir(os.path.join(PROJECT_ROOT, 'lib', dir, 'site-packages'))
       
sys.path.insert(0, PROJECT_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'h1ds.settings_staging'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
