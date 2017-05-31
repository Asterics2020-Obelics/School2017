# If you have choosen a different path than your home directory for
# your anaconda install, change the following line
ANACONDA=$HOME

if command -v export >/dev/null; then
    export PATH=$ANACONDA/anaconda3/bin:$PATH
    export PYTHONPATH=$ANACONDA/anaconda3/lib
else
    setenv PATH $ANACONDA/anaconda3/bin:$PATH
    setenv PYTHONPATH $ANACONDA/anaconda3/lib
fi

