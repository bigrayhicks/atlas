from setuptools import setup, find_packages

setup(
    name='atlas',
    version='0.1',
    description="Browse international public records",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Friedrich Lindenberg',
    author_email='pudo@occrp.org',
    url='https://occrp.org',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=['flask'],
    test_suite='nose.collector',
    entry_points={},
    tests_require=['coverage', 'nose']
)
