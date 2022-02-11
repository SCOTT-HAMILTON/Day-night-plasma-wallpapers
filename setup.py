from setuptools import setup, find_packages

setup(
    name='DayNightPlasmaWallpapers',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules = [ 'update' ],

    install_requires=['dbus-next'],

    entry_points='''
        [console_scripts]
        update-day-night-plasma-wallpapers=DayNightPlasmaWallpapers.update:update
    ''',

    # metadata to display on PyPI
    author='Scott Hamilton',
    author_email='sgn.hamilton+python@protonmail.com',
    description='KDE Plasma utility to automatically change to a night wallpaper when the sun is reaching sunset',
    keywords='wallpapers kde day night',
    url='https://github.com/SCOTT-HAMILTON/day-night-plasma-wallpapers',
    project_urls={
        'Source Code': 'https://github.com/SCOTT-HAMILTON/day-night-plasma-wallpapers',
    },
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ]
)
