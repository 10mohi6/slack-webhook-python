import os
import pypandoc

with open('README.txt','w+') as f:
   f.write(pypandoc.convert('README.md', 'rst'))

os.system("python setup.py sdist bdist_wheel")
os.system("twine upload dist/*")
os.remove('README.txt')