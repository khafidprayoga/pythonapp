from setuptools import setup, find_packages

setup(
    name = 'calculator',
    version = '0.1',
    author = 'Khafid Prayoga',
    author_email = 'khafid.dev@gmail.com',
    description = ('Simple calculator for CS students.'),
    package = find_packages(),
    include_package_data = True,
    install_requires = [
        'Click',
    ],
    entry_points = '''
        [console_scripts]
        calculate=main:calculate
    '''
)
