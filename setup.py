from setuptools import setup, find_packages
 
setup(
    name='slskd-api',
    setuptools_git_versioning={
        "template": "{tag}",
        "dev_template": "{tag}",
        "dirty_template": "{tag}"
    },
    setup_requires = ["setuptools-git-versioning"],
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests>=2.25.1',
    ],
    project_urls={
        'Documentation': 'https://slskd-api.readthedocs.io',
        'Source': 'https://github.com/bigoulours/slskd-python-api',
        'Funding': 'https://liberapay.com/bigoulours/donate'
    },
    author='bigoulours',
    description = 'API Wrapper to interact with slskd',
    python_requires='>=3.7',
    license='GNU Affero General Public License v3.0',
)