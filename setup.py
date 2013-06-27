from distutils.core import setup

setup(
    name='SpriteGenerator',
    version='0.1dev',
    packages=['spritegenerator',],
    license='MIT',
    long_description=open('README.md').read(),
    scripts=['learningtest/learningTest.py'],
    install_requires=[
    	'Pillow==1.7.8'
    ]
)