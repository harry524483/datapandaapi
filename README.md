How to use this project

1) Create a virtualenv as normal. Do not activate it yet.

2) Now you need to install the required packages. If you do not readily remember it, ask pip:

	pip freeze > requirements.txt

3) Now edit requirements.txt so that only the packages you know you installed are included. Note that the list will include all dependencies for all installed packages. Remove them, unless you want to explicitly pin their versions, and know what you're doing.

4) Now activate the virtualenv (the normal source path/to/virtualenv/bin/activate).

5) Install the dependencies you've collected:

	pip install -r requirements.txt
	The dependencies will be installed into your virtualenv.

6) The same way you'll be able to re-create the same env on your deployment target.