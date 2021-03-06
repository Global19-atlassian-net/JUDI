import setuptools, re

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSIONFILE = "judi/version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE))

setuptools.setup(
     name = 'judi',  
     version = verstr,
     author = "Soumitra Pal",
     author_email = "soumitrakp@gmail.com",
     description = "A Software Workflow Management System Based on DoIt",
     long_description = long_description,
     long_description_content_type = "text/markdown",
     url = "https://github.com/ncbi/JUDI",
     packages = setuptools.find_packages(),
     classifiers = [
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
