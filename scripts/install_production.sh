# This installs the package from the test.pypi
# Only run this file if you're the owner of the upload at test.pypi
# Otherwise, to test for changes made from your editor
# run the 'install_locally.sh' file instead

_package_name="nitrado"

if [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "darwin" ]]
then
  # POSIX compatibility layer and Linux environment emulation for Windows
  printf "y" | python3 -m pip uninstall "$_package_name"
  python3 -m pip install "$_package_name"
  _version=$(pip freeze | grep "$_package_name.*")
  printf "\n\033[32m$_version\033[0m\n"
elif [[ "$OSTYPE" == "msys" ]]
then
  # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
  printf "y" | python -m pip uninstall "$_package_name"
  python -m pip install "$_package_name"
  _version=$(pip freeze | grep "$_package_name.*")
  printf "\n\033[32m$_version\033[0m\n"
else
  printf "Haven't created a command for $OSTYPE"
fi