from setuptools import setup, find_packages

setup(
    name='gini-sdk',
    version='0.1.0',
    author='Roba Olana',
    author_email='support@gini.works',
    description='SDK to interact with Gini',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Works-By-Gini/gini-sdk', 
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: Apache Software License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)