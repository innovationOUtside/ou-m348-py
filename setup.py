from setuptools import setup
from setuptools.command.install import install

import subprocess
from os import path



def enable_extensions():
    """Enable extensions."""
    print("Installing extensions...")
    cmds = ["jupyter nbclassic-serverextension enable --py --user nbzip",
        "jupyter nbclassic-extension install --py --user nbzip",
        "jupyter nbclassic-extension enable --py --user nbzip",
        "jupyter nbclassic-extension install --py --user jupyter_nbextensions_configurator",
        "jupyter nbclassic-extension enable --py --user jupyter_nbextensions_configurator",
        "jupyter nbclassic-serverextension enable --py --user jupyter_nbextensions_configurator",
        "jupyter nbclassic-extension install --py --user jupyter_contrib_nbextensions",
        "jupyter nbclassic-extension enable --user spellchecker/main",
        "jupyter nbclassic-extension enable --user rubberband/main",
        "jupyter nbclassic-extension enable --user exercise2/main",
        #"pip install https://github.com/uclixnjupyternbaccessibility/accessibility_toolbar/archive/refs/heads/master.zip",
        #"jupyter nbclassic-extension install accessibility_toolbar",
        "R -e \"install.packages(c('nlme', 'tseries', 'urca', 'plm', 'formatR'), repos='https://www.stats.bris.ac.uk/R/')\" ",
        "Rscript -e \"install.packages('IRkernel', repos='https://www.stats.bris.ac.uk/R')\" ",
        "Rscript -e \"IRkernel::installspec()\" ",
        "R -e \"install.packages('./M348_1.3.4.tar.gz')\" "
        ]
    for cmd in cmds:
        try:
            subprocess.check_output(cmd, shell=True)
        except Exception as e:
            print(f"Failed to run command: {cmd}\nError: {e}")


class CustomInstall(install):
    def run(self):
        # Call custom installation routines
        enable_extensions()
        install.run(self)


def get_requirements(fn='requirements.txt', nogit=True):
   """Get requirements."""
   if path.exists(fn):
      with open(fn, 'r') as f:
        requirements = [r.split()[0].strip() for r in f.read().splitlines() if r and not r.startswith('#')]
   else:
     requirements = []

   if nogit:
       requirements = [r for r in requirements if not 'git+' in r]
   return requirements
   
requirements = get_requirements(nogit=False)

print(f'Requirements: {requirements}')

extras = {

    }
    
setup(
    # Meta
    author='Tony Hirst',
    author_email='tony.hirst@open.ac.uk',
    description='Python package installation for OU module M348',
    name='ou-m348-py',
    license='MIT',
    url='https://github.com/innovationOUtside/innovationOUtside/ou-tm351-py',
    version='0.0.1',
    packages=['ou_m348_py'],

    # Dependencies
    install_requires=requirements,
    #setup_requires=[],

    # Packaging
    #entry_points="",
    include_package_data=True,
    zip_safe=False,
    cmdclass={"install": CustomInstall},
    # Classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Education',
        'License :: Free For Educational Use',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
)

