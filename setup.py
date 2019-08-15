import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='graphqt',  
     version='0.2',
     scripts=['graphqt/graphqt.py'] ,
     author="Amit Singh Sansoya",
     author_email="tusharamit@yahoo.com",
     description="Create Graph DataStructure",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/ToughX-devs/graphqt-python",
     packages=setuptools.find_packages(),
     license="MIT",
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
