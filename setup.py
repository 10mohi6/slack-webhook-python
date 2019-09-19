from setuptools import setup, find_packages

with open('README.md') as f:
   long_description = f.read()

setup(
    name  = 'slack-webhook',
    version = '0.1.0',
    description = 'slack-webhook is a python client library for slack api Incoming Webhooks',
    long_description = long_description,
    license = 'MIT',
    author = '10mohi6',
    author_email = '10.mohi.6.y@gmail.com',
    url='https://github.com/10mohi6/slack-webhook-python',
    keywords = 'slack webhook',
    packages = find_packages(),
    install_requires = [],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License'
    ]
)