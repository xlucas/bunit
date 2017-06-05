from setuptools import setup

setup(
    name='bunit',
    version='0.1',
    description='Binary unit conversion tool',
    classifiers=[
        'Intended Audience :: System Administrators',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    url='https://github.com/xlucas/bunit',
    author="Xavier Lucas",
    author_email="xavier_lucas@ymail.com",
    license='MIT',
    packages=['unit'],
    entry_points={'console_scripts': ['bunit=unit.shell:main']},
    zip_safe=False,
)
