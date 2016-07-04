#!/usr/bin/env python
from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

install_reqs = parse_requirements("requirements.txt", session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]
version = '0.1'

print("""-----------------------------------
 Installing TargQC version {}
-----------------------------------
""".format(version))

name = 'targqc'

setup(
    name=name,
    version=version,
    author='Vlad Saveliev and Alla Mikheenko',
    author_email='vladislav.sav@gmail.com',
    description='Target coverage evaluation tool',
    long_description=(open('README.md').read()),
    keywords='bioinformatics',
    url='https://github.com/vladsaveliev/TargQC',
    download_url='https://github.com/vladsaveliev/TargQC/releases',
    license='GPLv3',
    packages=find_packages(),
    package_data={
        'GeneAnnotation': [
            'RefSeq/*.bed'
        ],
        'Utils': [
            'reference_data/fai/*.fai',
            '*.txt',
            '*.js',
            '*.css',
            '*.png',
            '*.pxm',
            '*.json',
            '*.html',
            'sambamba_*',
            '*.sh',
        ],
        'targqc': [
            'bedops_*',
            '*.jar',
            '*.bed',
            'qualimap'
            '*.r'
        ],
    },
    include_package_data=True,
    zip_safe=False,
    scripts=['scripts/' + name],
    install_requires=reqs,
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)

print("""
--------------------------------
 TargQC installation complete!
--------------------------------
Usage: {name} *.bam -o targqc_stats [--bed target.bed ...]'

For help in running TargQC, please see the documentation available at https://github.com/vladsaveliev/TargQC
or run: targqc --help
""".format(name=name))
