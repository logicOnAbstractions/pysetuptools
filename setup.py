from setuptools import setup

""" a minimalist setup.py sample structure """

setup(
   name='pysetuptools',
   version='0.1.0',
   author='An Awesome demo of the basics of using pkgs',
   author_email='francisvahcon.it@gmail.com',
   packages=['pysetuptools',
             'test'],
   scripts=['pysetuptools/bin/demo_script.py',
            'pysetuptools/bin/bash_run'],
   package_data={'pysetuptools':['data/dummy.yaml']},
   license='license.txt',
   description='An awesome package that does something',
   long_description=open('readme').read(),
   install_requires=["numpy","PyYAML"],
)