# Python-Autotools

The purpose of the python-autools it to automatically import subfolders (modules). Create classes based on filenames, and generate the `__init__.py` file.

## Direct Use

	cd 'your-project'
	pauto

This copies your entire project and transforms it.

After transforming, it runs the Main file.

## Use

	transform 'your-python-containing-project'

This COPIES the project into a new directory 'transform'.
Your original project will not be edited.

## Classify

Imagine a python source file called "File.py"

	def myMethod(self, a, b):
		return a + b

The Classifier will change it to

	class File:
		def myMethod(self, a, b):
			return a + b

It indents using tabs. So make sure your code is in tabs.

## Autoimport

For each subdirectory for a file residing in that directory, it prepends imports.
Here is the file MyFile.py:

	def test():
		print("test")

Is located in

	a/
		MyFile.py
		b/
		c/
			d/
		e/

Where b/, c/, and e/ are direct subdirectories of a/. This will prepend

	import b
	import c
	import e

To all python files in a/.

## Importify

Creates an `__init__.py` file and imports each file in that directory using the format:

	from .File import File

## Transform

Combines the effect of all three scripts and runs them in parallel.
