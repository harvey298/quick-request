from setuptools import setup

project_name = 'QuickRequest'

setup(
    name= project_name,
    version='0.1.1',    
    description='A library for quick and dirty requests',
    url='https://github.com/harvey298/Quick-Request',
    author='harvey298',
    author_email="n/a",
    license='GNU GPL 3',
    packages=[project_name],
    install_requires=['requests','colour_lib',                     
                      ],

)