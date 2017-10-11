try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.1.0'

with open('requirements/production.txt') as requirements_file:
    requires = [line for line in requirements_file]

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='powerlibs-django-contrib',
    version=version,
    description="Some contributions to facilitate construction of Django projects",
    long_description=readme,
    author='Cléber Zavadniak',
    author_email='cleberman@gmail.com',
    url='https://github.com/Dronemapp/powerlibs-django-contrib',
    license=license,
    packages=['powerlibs.django.contrib'],
    package_data={'': ['LICENSE', 'README.md']},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    keywords='generic libraries',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
