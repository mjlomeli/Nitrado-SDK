# This installs the package from the test.pypi
# Only run this file if you're the owner of the upload at test.pypi
# Otherwise, to test for changes made from your editor
# run the 'install_locally.sh' file instead

if [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "darwin" ]]
then
  # POSIX compatibility layer and Linux environment emulation for Windows
  echo y | python3 -m pip uninstall arkdriver
  python3 -m pip install -i https://test.pypi.org/simple/ nitrado
elif [[ "$OSTYPE" == "msys" ]]
then
  # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
  echo y | python -m pip uninstall arkdriver
  python -m pip install -i https://test.pypi.org/simple/ nitrado
else
  printf "Haven't created a command for $OSTYPE"
fi