[![School banner](https://indico.in2p3.fr/event/14227/logo)](https://indico.in2p3.fr/event/14227/logo)

# Overview

This repository contains all the material needed for the [1st
ASTERICS-OBELICS International
School](https://indico.in2p3.fr/event/14227) on "Advanced software
programming for astrophysics and astroparticle physics".

# Software install

## Recommendation for Python install

- Python 3.6
- Anaconda [link](https://www.continuum.io/downloads)

### Linux

- [Download](https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh)
the linux `Anaconda` installer for Python 3.6 (see install instruction
[here](https://www.continuum.io/downloads#linux)).

- Run the following command line:

	bash Anaconda3-4.3.1-Linux-x86_64.sh

Answer `no` to the following question if you do not want to mess up your previous installs of python.
	
	Do you wish the installer to prepend the Anaconda3 install location
	to PATH in your /home/chotard/.bashrc ? [yes|no]
	[no] >>> no

- Run the following script (located in the current directory) to set up
the correct PATH and PYTHONPATH enabling the use of your `Anaconda` install.

	source anaconda_setup.sh

You can either run this command each time you need to use `Anaconda`,
or add these lines to your `.bashrc` (or equivalent) to set it up at
the opening of a new terminal.

- Install the extra python libraries (see next section).

### Mac

Instruction for Mac can be found
[here](https://www.continuum.io/downloads#macos). To set up the PATH
and PYTHON, you can do as explained in the previous section for Linux
install. (Not tested yet).

### Windows

Instruction for Windows can be found [here](https://www.continuum.io/downloads#windows). (Not tested yet).

## Python library requirements

If you choose an other way to install Python 3.6 than the one
recommended above, you might want to install manually the Python
libraries listed in the [requirements.txt](requirements.txt) file. To
do so, we recommand using `pip`.

	  pip install -r requirements.txt

All these libraries come with the `Anaconda` install described above.

## Other requirements

Some other Python related tools that you might consider installing:

- pycharm (Free Community Edition: [Download PyCharm](https://www.jetbrains.com/pycharm/download) or opt for a free copy of the Professional Edition under [Student License](https://www.jetbrains.com/student/))

# Tutors

Here is the list of tutors for the hands-on sessions. Four are needed for each session.

| Hands-on               | Main tutor(s)              | Other tutors                              |
| ---------------------- |----------------------------|-------------------------------------------|
| Numpy                  | Tamas Gal                  | Axel Donath, Johannes King, Pierre Aubert |
| Pandas                 | Tamas Gal                  | Damian Podareanu, Karl Kosack             |
| Astropy                | Axel Donath, Johannes King | Karl Kosack                               |
| Profiling & Debugging  | Karl Kosack                | Axel Donath, Zheng Meyer-Zhao, Pierre Aubert|
| Parallel Programming   | Damian Podareanu           | Tamas Gal, Pierre Aubert, Jean Jacquemier |
| GPU Programming        | Valeriu Codreanu           | Pierre Aubert                             |

 
# Help

Please create a [new
issue](https://github.com/Asterics2020-Obelics/School2017/issues) for
each questions you may have before or during the school about software
install and/or about one of the classes. Of course, you might want to
first check the existing list of issues to see if your question has
already been asked and answered before creating a new one.
