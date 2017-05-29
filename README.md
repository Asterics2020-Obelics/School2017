[![School banner](https://indico.in2p3.fr/event/14227/logo)](https://indico.in2p3.fr/event/14227/logo)

This repository contains all the material needed for the [1st
ASTERICS-OBELICS International
School](https://indico.in2p3.fr/event/14227) on "Advanced software
programming for astrophysics and astroparticle physics". The time
table is available at the following
[location](https://indico.in2p3.fr/event/14227/timetable/#20170606).

# Table on content

- [Local copy of this repository](#repo)
- [Recommendation for Python install](#python)
    - [Linux](#linux)
    - [Mac](#mac)
    - [Windows](#windows)
    - [Library requirements](#python-req)
- [Other requirements](#other-req)
- [Cartesius machines](#cartesius)
- [Tutors](#tutors)
- [Help](#help)

# Local copy of this repository <a name="repo"></a>

Clone this repository on your personal computer.

      git clone https://github.com/Asterics2020-Obelics/School2017.git

You will need it before the school to install the different tools, and
during the school while attending the hands-on.

# Recommendation for Python install <a name="python"></a>

You must install Python 3.6 and a few python libraries. The
recommended way to do so is to use
[Anaconda](https://www.continuum.io/downloads). The procedures
described bellow will help you install what is needed for the school.

## Linux <a name="linux"></a>

- [Download](https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh)
the linux `Anaconda` installer for Python 3.6.

- Run the following command line:

		bash Anaconda3-4.3.1-Linux-x86_64.sh

- Answer `no` to the following question if you do not want to mess up
  your previous installs of python.
	
		Do you wish the installer to prepend the Anaconda3 install location
		to PATH in your /home/chotard/.bashrc ? [yes|no]
		[no] >>> no

- If you haven't cloned this repository, download the `anaconda_setup.sh` script:

		wget https://raw.githubusercontent.com/Asterics2020-Obelics/School2017/master/anaconda_setup.sh

- Run the `anaconda_setup.sh` script to set up the correct PATH and
PYTHONPATH enabling the use of your `Anaconda` install.

		source anaconda_setup.sh

You can either run this command each time you need to use `Anaconda`,
or add its content to your `.bashrc` (or equivalent) to set it up at
the opening of a new terminal.

- See next section for extra python libraries requirements (if any).

## Mac <a name="mac"></a>

- [Download](https://repo.continuum.io/archive/Anaconda3-4.3.1-MacOSX-x86_64.sh)
the Mac `Anaconda` installer for Python 3.6.

- Run the following command line:

		bash Anaconda3-4.3.1-MacOSX-x86_64.sh

- Answer `no` to the following question if you do not want to mess up
  your previous installs of python.
	
		Do you wish the installer to prepend the Anaconda3 install location
		to PATH in your /home/chotard/.bashrc ? [yes|no]
		[no] >>> no

- If you haven't cloned this repository, first get the `anaconda_setup.sh` script:

		wget https://raw.githubusercontent.com/Asterics2020-Obelics/School2017/master/anaconda_setup.sh

- Run the `anaconda_setup.sh` script to set up the correct PATH and
PYTHONPATH enabling the use of your `Anaconda` install.

		source anaconda_setup.sh

You can either run this command each time you need to use `Anaconda`,
or add its content to your `.bashrc` (or equivalent) to set it up at
the opening of a new terminal.

- See next section for extra python libraries requirements (if any).

## Windows <a name="windows"></a>

Instruction for Windows can be found
[here](https://www.continuum.io/downloads#windows). (Not tested yet).

## Library requirements <a name="python-req"></a>

All the required libraries come with the `Anaconda` install described
above. If you have followed the previous steps to install python, you
can skip this section.

If you choose an other way to install Python 3.6 than the one
recommended above, you must install manually the Python libraries
listed in the [requirements.txt](requirements.txt) file. To do so, we
recommand using `pip`.

	  pip install -r requirements.txt

# Other requirements <a name="other-req"></a>

Some other Python related tools that you might consider installing:

- pycharm (Free Community Edition: [Download
  PyCharm](https://www.jetbrains.com/pycharm/download) or opt for a
  free copy of the Professional Edition under [Student
  License](https://www.jetbrains.com/student/))

# Cartesius machines <a name="cartesius"></a>

For the parallel and GPU sessions, we will use the [Cartesius machines](https://userinfo.surfsara.nl/systems/cartesius) that are generously made available by SURFsara for the OBELICS school. You will need to connect to them through the ssh protocol (natively installed on Linux and Mac).

For Windows users, we recommend these tools to connect via ssh:
- [Putty](http://www.putty.org/) & [Winscp](https://winscp.net)
- Or, on Windows 10: use the [native bash environment](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)

# Tutors <a name="tutors"></a>

Here is the list of tutors for the hands-on sessions. Four (or more) are needed for each session (except for GPU and parallel which are parallel sessions).

| Hands-on               | Main tutor(s)              | Other tutors                                                |
| ---------------------- |----------------------------|-------------------------------------------------------------|
| Numpy                  | Tamas Gal                  | Axel Donath, Johannes King, Pierre Aubert, Tristan Carel    |
| Pandas                 | Tamas Gal                  | Damian Podareanu, Karl Kosack                               |
| Astropy                | Axel Donath, Johannes King | Karl Kosack                                                 |
| Profiling & Debugging  | Karl Kosack                | Axel Donath, Zheng Meyer-Zhao, Pierre Aubert, Tristan Carel |
| Parallel Programming   | Damian Podareanu           | Tamas Gal, Pierre Aubert, Jean Jacquemier, Tristan Carel    |
| GPU Programming        | Valeriu Codreanu           | Pierre Aubert, Zheng Meyer-Zhao, Tristan Carel(?)           |

The full list of tutors is available [here](https://indico.in2p3.fr/event/14227/page/10).

 
# Help

Please create a [new
issue](https://github.com/Asterics2020-Obelics/School2017/issues) (you
will need a github account) for each question you may have before or
during the school about software install and/or about one of the
classes. Of course, you should first check the existing list of issues
to see if your question has already been asked and answered before
creating a new one.
