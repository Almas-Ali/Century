import setuptools

with open('README.md', 'r') as README:
    long_description = README.read()

classifiers = [
    'Development Status :: 1 - Planning',
    'Operating System :: OS Independent',
    'Intended Audience :: Developers',
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    'Natural Language :: English',
]

setuptools.setup(
    name="Century",
    version="0.0.1",
    description="Century - A flask based web application manager.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/Almas-Ali/Century",
    author="Md. Almas Ali",
    author_email="almaspr3@gmail.com",
    keyword="Century, Flask, ORM, Web Application Manager, CLI",
    license="MIT",
    classifiers=classifiers,
    packages=setuptools.find_packages(),
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask_migrate',
        'typer',
        'rich',
        
    ],  # external packages as dependencies
    entry_points={
        'console_scripts': [
            'century = century.cli:app',
        ],
    },
)
