import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mindpowered-englishauction',
    version='0.0.64',
    author="Mind Powered Corporation",
    author_email="support@mindpowered.dev",
    license="MIT",
    url="https://mindpowered.dev/",
    description="Online auctions with ascending price and time limit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['englishauction'],
    packages=['mindpowered_englishauction'],
    package_dir={'mindpowered_englishauction': 'wrappers'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'mindpowered-maglev',
    ],
)
