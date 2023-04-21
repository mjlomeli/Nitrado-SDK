# Updates all packages which are in the requirements.txt file

pip3 install -r test_requirements_pypi.txt --upgrade
pip3 install -r test_requirements_test_pypi.txt --upgrade --extra-index-url https://test.pypi.org/simple/
