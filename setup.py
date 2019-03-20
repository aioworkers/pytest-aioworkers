from pathlib import Path
from setuptools import setup


def read(fname):
    p = Path(__file__).parent / fname
    return p.read_text(encoding='utf-8')


setup(
    name='pytest-aioworkers',
    version='0.1.0',
    author='Alexander Malev',
    author_email='malev@somedev.ru',
    maintainer='Alexander Malev',
    maintainer_email='malev@somedev.ru',
    license='Apache Software License 2.0',
    url='https://github.com/aioworkers/pytest-aioworkers',
    description='A plugin to test aioworkers project with pytest',
    long_description=read('README.rst'),
    py_modules=['pytest_aioworkers'],
    python_requires='>=3.5',
    install_requires=[
        'pytest>=3.5.0',
        'pytest-aiohttp',
        'aioworkers',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'pytest11': [
            'aioworkers = pytest_aioworkers',
        ],
    },
)
