from setuptools import setup, find_packages

setup(
    name='supabase-management',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'httpx',
    ],
    author='YoGoUrT',
    author_email='work@minefloat.com',
    description='A Python client for the Supabase Management API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yogourt20/supabase-management-py',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
