from setuptools import setup

setup(
    name='augmix',
    version='0.0.0',
    packages=['augmix'],
    package_dir={'augmix': '.'},
    install_requires=['numpy', 'pillow'],
    extras_require={
        "develop": ['torch']
    },
)
