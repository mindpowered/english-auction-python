import setuptools

#with open("README.md", "r") as fh:
    #long_description = fh.read()
setuptools.setup(
     name='mindpowered-englishauction',
     version='0.0.22',
     author="Mind Powered Corporation",
     author_email="support@mindpowered.dev",
     license="CPAL-1.0",
     url="https://mindpowered.dev/",
     description="EnglishAuction",
     #long_description=long_description,
     #long_description_content_type="text/markdown",
     py_modules=['englishauction'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
