_major_version=0
_minor_version=0
_revision=0

_package_name="nitrado"

# Install build if not already installed
if ! (pip freeze | grep build) &>/dev/null;
then
  if [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "darwin" ]];
  then
    # POSIX compatibility layer and Linux environment emulation for Windows
    python3 -m pip install build;
  elif [[ "$OSTYPE" == "msys" ]];
  then
    # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
    python -m pip install build;
  else
    printf "Haven't created a command for $OSTYPE";
    exit 1;
  fi
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
fi



_setup="./setup.cfg"
_found=$(cat "$_setup" | grep "version = .*")
IFS='.' read -ra VERSION <<< "$_found"
_revision="${VERSION[2]}"
_revision="$((_revision + 1))"
_search="^version = [0-9]*\.[0-9]*\.[0-9]*$"
_replace="version = $_major_version.$_minor_version.$_revision"
if [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "darwin" ]]
then
  if ! sudo sed -i "s/$_search/$_replace/" "$_setup" &>/dev/null
  then
    printf "\r\033[31mFailed to increment version\033[0m       \n\n";
    exit 1;
  fi
elif [[ "$OSTYPE" == "msys" ]]
then
  if ! sed -i "s/$_search/$_replace/" "$_setup" &>/dev/null
  then
    printf "\r\033[31mFailed to increment version\033[0m       \n\n";
    exit 1;
  fi
else
  printf "Haven't created a command for $OSTYPE"
fi


# Upload to PyPi
if [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "darwin" ]]
then
  sudo rm -r dist &>/dev/null
  sudo rm -r "src/$_package_name.egg-info" &>/dev/null
  python3 -m build
  python3 -m twine upload --repository pypi dist/* -u"__token__" -p"$PYPI"
  git add .
  git commit -m "uploaded to pypi version $_major_version.$_minor_version.$_revision"
  git push
  sudo rm -r dist &>/dev/null
elif [[ "$OSTYPE" == "msys" ]]
then
  # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
  rm -r dist &>/dev/null
  rm -r "src/$_package_name.egg-info" &>/dev/null
  python -m build
  python -m twine upload --repository pypi dist/* -u"__token__" -p"$PYPI"
  git add .
  git commit -m "uploaded to pypi version $_major_version.$_minor_version.$_revision"
  git push
  rm -r dist &>/dev/null
else
  printf "Haven't created a command for $OSTYPE"
  exit 1
fi