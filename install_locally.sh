# Run this to simulate installing the package.
# Once ran, restart the python environment and import arkdriver
if [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "linux-gnu" ]] | [[ "$OSTYPE" == "darwin" ]]
  # POSIX compatibility layer and Linux environment emulation for Windows
  pip3 install -e .
elif [[ "$OSTYPE" == "msys" ]]
then
  # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
  pip install -e .
else
  printf "Haven't created a command for $OSTYPE"
fi