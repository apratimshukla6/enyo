from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='enyo',
    version='0.0.4',
    description='Enyo is a lightweight multistage partition based encryption algorithm.',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Apratim Shukla, Mayank Tolani, Dipan Polley, Abhishek TK',
    author_email='apratimshukla6@gmail.com',
    keywords=['Enyo', 'EnyoCipher', 'EnyoEncryption'],
    url='https://github.com/apratimshukla6/enyo',
    download_url='https://pypi.org/project/enyo/'
)

install_requires = []

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)