import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name='edc-base',
    version='0.1.0',
    author=u'MoffatMore',
    author_email='mofenyimoffat@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/Pixel-5/edc-base',
    license='MIT licence, see LICENCE',
    description='Base mixins and utilities for pixel-5/edc projects.',
    long_description=README,
    zip_safe=False,
    keywords='django base models fields forms admin',
    install_requires=[
        'django',
        'django[argon2]',
        'django-simple-history',
        'django-js-reverse',
        'django-logentry-admin',
        'django-debug-toolbar',
        'django-extensions',
        'django-revision',
        'python-dateutil',
        'docutils',
        'model_mommy',
        'Faker',
        'pytz',
        'arrow',
        'python-memcached',
        'pymysql',
        'tqdm',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
