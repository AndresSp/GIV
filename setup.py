from setuptools import setup

import os

os.environ['FLASK_APP'] = 'seeThatSign'

setup(
    name='seeThatSign',
    version='1.0',
    description='Generate Datasets and Train a Signal Classifier',
    long_description='Generate image variations and its XML to create Datasets or any other purpose and Train a Signal Classifier that help a blind recognize signals',
    author='AndresSp, c4explosive, Martin Coronado',
    author_email='andrestunonsp@gmail.com, ao946391@gmail.com, undefined',
    url='https://github.com/AndresSp/SeeThatSign',
    license='MIT',
    platforms=['Browsers'],
    packages=['seeThatSign'],
    include_package_data=True,
    install_requires=[
        'flask>=1.0.2',
        'virtualenv'
    ],
)