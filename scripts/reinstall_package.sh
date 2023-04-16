# This installs the package from the test.pypi
# Only run this file if you're the owner of the upload at test.pypi
# Otherwise, to test for changes made from your editor
# run the 'install_locally.sh' file instead


_file="./setup.cfg"


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


function install_package () {
  # Installs from PyPi
  # :param $1: The package name.
  # Example:
  #     install_package "package_name"

  if [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "darwin" ]]
  then
    # POSIX compatibility layer and Linux environment emulation for Windows
    printf "y" | python3 -m pip uninstall "$1"
    python3 -m pip install "$1"
    _version=$(pip freeze | grep "$1.*")
    printf "\n\033[32m$_version\033[0m\n"
  elif [[ "$OSTYPE" == "msys" ]]
  then
    # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
    printf "y" | python -m pip uninstall "$1"
    python -m pip install "$1"
    _version=$(pip freeze | grep "$1.*")
    printf "\n\033[32m$_version\033[0m\n"
  else
    printf "Haven't created a command for $OSTYPE"
  fi
}



if ! get_package_name $_file &>/dev/null
then
  echo $(get_package_name $_file)
  return 1
fi

_package_name="$(get_package_name $_file)"

install_package $_package_name
