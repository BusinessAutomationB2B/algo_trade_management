20/12/2019

https://docs.anaconda.com/anaconda/user-guide/getting-started/

> conda install pip    // for installing things like backtesting



# install zipline in conda
https://towardsdatascience.com/introduction-to-backtesting-trading-strategies-7afae611a35e

# create new virtual environment
conda create -n env_zipline python=3.7   # activate it
conda activate env_zipline     # install zipline
conda install -c Quantopian zipline

# install zipline in windows
https://www.marketcalls.in/python/install-quantopian-zipline-windows.html


# install backtesting
https://pypi.org/project/Backtesting/

 pip install backtesting






# python path
C:\Python27;C:\Python27\Lib\site-packages\;C:\Python27\Scripts\;
C:\Program Files\Python37;C:\Program Files\Python37\Lib\site-packages\;C:\Program Files\Python37\Scripts\;


# final solution
custom install pyton 3.7.X and specify the location as C:\python37 and select add it to path variable.// did not work


# final solution:
manual install pip - worked
Installing Pip

Once you’ve confirmed that Python is correctly installed, you can proceed with installing Pip.

    Download get-pip.py to a folder on your computer.
    Open a command prompt and navigate to the folder containing get-pip.py.
    Run the following command:
    python get-pip.py
    Pip is now installed!

You can verify that Pip was installed correctly by opening a command prompt and entering the following command:

pip -V

You should see output similar to the following:

pip 18.0 from c:\users\administrator\appdata\local\programs\python\python37\lib\site-packages\pip (python 3.7)

Now that Pip is installed and configured, you can begin using it to manage your Python packages. For a brief overview of the available commands and syntax for Pip, open a command prompt and enter:

pip help

All of Liquid Web’s Windows core-managed servers can run Python and our support team can assist with installation and verification if needed. ActiveState Python 2.6.5 can be installed on Plesk Fully Managed servers if desired.



# location of window binary wheels for TA-Lab required for zipline installation
https://www.lfd.uci.edu/~gohlke/pythonlibs/