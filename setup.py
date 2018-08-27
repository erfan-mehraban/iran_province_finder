from setuptools import setup, find_packages

setup(name='iran province founder',
    version='0.1',
    description='found province of iran correspond to latitude and longtitude',
    author='Erfan Mehraban',
    author_email='erfan.mehraban@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'Shapely>=1.6.4.post2',
    ],
    include_package_data=True,
    zip_safe=False)