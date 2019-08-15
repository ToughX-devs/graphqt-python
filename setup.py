import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='graphq',  
     version='0.1',
     scripts=['graphq/graphq.py'] ,
     author="Amit Singh Sansoya",
     author_email="tusharamit@yahoo.com",
     description="Create Graph DataStructure",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/ToughX-devs/graphq-python",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
