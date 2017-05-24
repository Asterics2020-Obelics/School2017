[![School banner](https://indico.in2p3.fr/event/14227/logo)](https://indico.in2p3.fr/event/14227/logo)

# Overview

This repository contains all the material needed for the [1st
ASTERICS-OBELICS International
School](https://indico.in2p3.fr/event/14227) on "Advanced software
programming for astrophysics and astroparticle physics".

# Software install

## Recommendation for Python install

- python 3.x
- Anaconda [link](https://www.continuum.io/downloads)

### Linux

[Download](https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh)
the linux `Anaconda` installer for Python 3.6 (see install instruction
[here](https://www.continuum.io/downloads#linux). Run the following
command line:

	bash Anaconda3-4.3.1-Linux-x86_64.sh

Answer `no` to the following question if you do not want to mess up your previous installs of python:
	

	Do you wish the installer to prepend the Anaconda3 install location
	to PATH in your /home/chotard/.bashrc ? [yes|no]
	[no] >>> no

Run the following script (located in the current directory) to set up
the correct PATH and PYTHONPATH anabling the use of your install of
`Anaconda`.

	source anaconda_setup.sh

You can either run this command each time you need to use anaconda, or
add these lines to your .bashrc (or equivalent) so set it up
permanently when opening a new terminal.

### Mac

### Windows

## Python library requirements

- ipython
- jupyter
- numpy
- scipy
- pandas
- sympy
- numexpr
- astropy
- numba
- matplotlib
- cython
- h5py
- pytables
- (scikit-learn?)

## Other requirements

- pycharm

# Tutors

Here is the list of tutors for the hands-on sessions. Four are needed for each session.

| Hands-on               | Main tutor(s)              | Other tutors                              |
| ---------------------- |----------------------------|-------------------------------------------|
| Numpy                  | Tamas Gal                  | Axel Donath, Johannes King                |
| Pandas                 | Tamas Gal                  |                                           |
| Astropy                | Axel Donath, Johannes King |                                           |
| Profiling & Debugging  | Karl Kosack                | Axel Donath                               |
| Parallel Programming   | Damian Podareanu           | Tamas Gal                                 |
| GPU Programming        | Valeriu Codreanu           |                                           |

 
# Help

Please create a [new
issue](https://github.com/Asterics2020-Obelics/School2017/issues) for
each questions you may have before or during the school about software
install and/or about one of the classes. Of course, you might want to
first check the existing list of issues to see if your question has
already been asked and answered before creating a new one.
