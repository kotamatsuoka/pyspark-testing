# /bin/bash

python setup.py bdist_wheel
twine upload --repository pypitest dist/*
