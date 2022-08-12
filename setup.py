from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='ceasar_cipher',
    version='1.0.1',
    url='https://github.com/yuritorresf/ceasar_cipher',
    license='MIT License',
    author='Yuri F. Torres',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='feereira@gmail.com',
    keywords='Pacote',
    description=u'Ceasar Cipher - Cifra de César',
    packages=['ceasar_cipher'],
    python_requires='>=3.5',
    install_requires=['os', 'sys'],)