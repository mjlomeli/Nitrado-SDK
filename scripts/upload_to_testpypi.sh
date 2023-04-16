# Need to have the Test PyPi token as an environment variable named 'TEST_PYPI'
# Ex.
# TEST_PYPI="1232abcd!@#$%^"



_file="./setup.cfg"


# Install build if not already installed
function install_build () {
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
}

# Install twine if not already installed
function install_twine () {
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
}

# Gets the package name in the 'setup.cfg' file
function get_package_name () {
  # Gets the package name from a 'setup.cfg' file.
  # :param $1: The path to the file. If empty, default is local "./setup.cfg"

  _path="$1";
  if [[ -z "$1" ]] # if param $1 is NULL
  then
    if [[ ! -f "./setup.cfg" ]] # if default file path doesn't exist
    then
      echo "[ERROR]: File setup.cfg does not exist locally"
      return 1
    fi
    _path="./setup.cfg";  # use default file path
  elif [[ ! -f "$1" ]] # if param $1 file path does not exists
  then
    echo "[ERROR]: File $1 does not exist";
    return 1
  fi

  _found=$(cat "$_path" | grep "name = .*")
  IFS=' ' read -ra LINE <<< "$_found"
  echo "${LINE[2]}"
}

# Gets the test version incremented by 1 revision number
function get_new_test_version () {
  # Gets the test version from a 'setup.cfg' file and increments the revision number.
  # :param $1: The path to the file. If empty, default is local "./setup.cfg"

  _path="$1";
  if [[ -z "$1" ]] # if param $1 is NULL
  then
    if [[ ! -f "./setup.cfg" ]] # if default file path doesn't exist
    then
      echo "[ERROR]: File setup.cfg does not exist locally"
      return 1
    fi
    _path="./setup.cfg";  # use default file path
  elif [[ ! -f "$1" ]] # if param $1 file path does not exists
  then
    echo "[ERROR]: File $1 does not exist";
    return 1
  fi

  _found=$(cat "$_path" | grep "test_version = .*")
  IFS='.' read -ra VERSION <<< "$_found"
  _major_text="${VERSION[0]}"
  _minor_version="${VERSION[1]}"
  _revision_version="$((VERSION[2] + 1))"

  IFS=' ' read -ra _parsed_text <<< $_major_text
  _major_version="${_parsed_text[2]}"

  echo "$_major_version.$_minor_version.$_revision_version"
}

# Updates the cfg file version
function update_cfg_version () {
  # Updates the cfg file's version number.
  # :param $1: The path to the local cfg file, else 'setup.cfg' is the default.
  # :param $2: The version number.
  # Example:
  #     update_cfg_version "setup.cfg" "1.2.3"

  _search="^version = [0-9]*\.[0-9]*\.[0-9]*$"
  _replace="version = $2"
  if [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "darwin" ]]
  then
    if ! sudo sed -i "s/$_search/$_replace/" "$1" &>/dev/null
    then
      printf "\r\033[31mFailed to increment version\033[0m       \n\n";
      exit 1;
    fi
  elif [[ "$OSTYPE" == "msys" ]]
  then
    if ! sed -i "s/$_search/$_replace/" "$1" &>/dev/null
    then
      printf "\r\033[31mFailed to increment version\033[0m       \n\n";
      exit 1;
    fi
  else
    printf "Haven't created a command for $OSTYPE"
  fi
}

# Updates the cfg file test_version
function update_cfg_test_version () {
  # Updates the cfg file's test_version number.
  # :param $1: The path to the local cfg file, else 'setup.cfg' is the default.
  # :param $2: The version number.
  # Example:
  #     update_cfg_version "setup.cfg" "1.2.3"

  _search="^test_version = [0-9]*\.[0-9]*\.[0-9]*$"
  _replace="test_version = $2"
  if [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "darwin" ]]
  then
    if ! sudo sed -i "s/$_search/$_replace/" "$1" &>/dev/null
    then
      printf "\r\033[31mFailed to increment version\033[0m       \n\n";
      exit 1;
    fi
  elif [[ "$OSTYPE" == "msys" ]]
  then
    if ! sed -i "s/$_search/$_replace/" "$1" &>/dev/null
    then
      printf "\r\033[31mFailed to increment version\033[0m       \n\n";
      exit 1;
    fi
  else
    printf "Haven't created a command for $OSTYPE"
  fi
}

# Upload to Test PyPi
function upload_to_test_pypi () {
  # Uploads to Test PyPi
  # :param $1: The path to the local cfg file, else 'setup.cfg' is the default.
  # :param $2: The version number.
  # :param $3: The package name.
  # Example:
  #     update_cfg_version "setup.cfg" "1.2.3"

  if [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "darwin" ]]
  then
    # POSIX compatibility layer and Linux environment emulation for Windows
    sudo rm -r dist &>/dev/null
    sudo rm -r "src/$3.egg-info" &>/dev/null
    python3 -m build
    python3 -m twine upload --repository testpypi dist/* -u"__token__" -p"$TEST_PYPI"
    sudo rm -r dist &>/dev/null
    sudo rm -r "src/$3.egg-info" &>/dev/null
  elif [[ "$OSTYPE" == "msys" ]]
  then
    # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
    rm -r dist &>/dev/null
    rm -r "src/$3.egg-info" &>/dev/null
    python -m build
    python -m twine upload --repository testpypi dist/* -u"__token__" -p"$TEST_PYPI"
    rm -r dist &>/dev/null
    rm -r "src/$3.egg-info" &>/dev/null
  else
    printf "Haven't created a command for $OSTYPE"
    return 1
  fi

  git add .
  git commit -m "Uploaded $3@$2 to Test PyPi"
  git push
}



# If any functions get_package_nane or get_new_test_version fails, exit the program

if ! get_package_name $_file &>/dev/null
then
  echo $(get_package_name $_file)
  return 1
elif ! get_new_test_version $_file &>/dev/null
then
  echo $(get_new_test_version $_file)
  return 1
fi


_version="$(get_new_test_version $_file)"
_package_name="$(get_package_name $_file)"

install_build
install_twine
update_cfg_test_version $_file $_version
update_cfg_version $_file $_version
upload_to_test_pypi $_file $_version $_package_name


exit 0