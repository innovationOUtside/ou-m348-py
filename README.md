# ou-m348-py

*Unofficial* utility package to install supporting environment packages for OU module M348.

__The recommended way of accessing the M348 computing environment is to access either the hosted virtual computing environment (VCE), or the Docker enabled local VCE.__

*If you try to configure your own environment, no official support will be available.*

Before installing this package, you will need to:

- [download and install R](https://cran.rstudio.com/)
- ensure you have a Pyhton environment available

From a termainal command line, run the command:

`pip install https://github.com/innovationOUtside/ou-m348-py/archive/refs/heads/main.zip`

If things don't appear to have installed, try the installation with degub reporting:

`pip install --verbose https://github.com/innovationOUtside/ou-m348-py/archive/refs/heads/main.zip`

(If you have several Pythibn environments available, you may need to ensure you are using the correct `pip` installer. You're on your own with this... that's why we suggest using officially supported environments...)

Launch the environment with:

`jupyter nbclassic`