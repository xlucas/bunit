from setuptools import setup

setup(
    name='units',
    version='0.1',
    description='Units printer',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    url='https://github.com/xlucas/units',
    author="Xavier Lucas",
    author_email="xavier_lucas@ymail.com",
    license='MIT',
    packages=['units'],
    entry_points={'console_scripts': ['units=units.shell:main']},
    zip_safe=False,
)
