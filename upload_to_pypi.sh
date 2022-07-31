# Install build if not already installed
if ! (pip freeze | grep build) &>/dev/null
then
  if [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "darwin" ]]
then
  # POSIX compatibility layer and Linux environment emulation for Windows
  python3 -m pip install build
elif [[ "$OSTYPE" == "msys" ]]
then
  # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
  python -m pip install build
else
  printf "Haven't created a command for $OSTYPE"
  exit 1
fi


# Install twine if not already installed
if ! (pip freeze | grep twine) &>/dev/null
then
  if [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "darwin" ]]
then
  # POSIX compatibility layer and Linux environment emulation for Windows
  python3 -m pip install twine
elif [[ "$OSTYPE" == "msys" ]]
then
  # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
  python -m pip install twine
else
  printf "Haven't created a command for $OSTYPE"
  exit 1
fi


# Upload to PyPi
if [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "darwin" ]]
then
  # POSIX compatibility layer and Linux environment emulation for Windows
  sudo rm -r dist
  sudo rm -r src/arkdriver.egg-info
  python3 -m build
  printf '__token__' | python3 -m twine upload --repository pypi dist/*
elif [[ "$OSTYPE" == "msys" ]]
then
  # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
  rm -r dist
  rm -r src/arkdriver.egg-info
  python -m build
  printf '__token__' | python -m twine upload --repository pypi dist/*
else
  printf "Haven't created a command for $OSTYPE"
  exit 1
fi