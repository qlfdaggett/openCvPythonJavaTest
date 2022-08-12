# openCvPythonJavaTest

Demonstration for possible opencv solutions for nautilus JRNY. 

Requires an installation of openCV for python. Pip is probably your best option for acquisition. 


I decied to run openCV through python because running it through java required a different JDK from the one we're using for the project.

Essentially, it's a python script that takes 2 command line arguments; the screenshot from the app and an image of what we are trying to match. The output will be two integers representing the center coordinates of the matching area in the image.

The demonstration accomplishes this by running the python script from the command line, with java methods, and reading back its output in the java project.
