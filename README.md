[![School banner](https://indico.in2p3.fr/event/14227/logo)](https://indico.in2p3.fr/event/14227/logo)

This repository contains all the material needed for the [1st
ASTERICS-OBELICS International
School](https://indico.in2p3.fr/event/14227) on "Advanced software
programming for astrophysics and astroparticle physics". The time
table is available at the following
[location](https://indico.in2p3.fr/event/14227/timetable/#20170606).

# Table on content

- [Important links](#links)
- [Get a copy of this repository with `git`](#repo)
- [Recommendation for Python install](#python)
    - [Linux](#linux)
    - [Mac](#mac)
    - [Windows](#windows)
    - [Library requirements](#python-req)
- [Jupyter](#jupyter)    
- [IDE: PyCharm](#pycharm)
- [Cartesius machines](#cartesius)
- [Chat rooms](#chat)
- [Tutors](#tutors)
- [Help](#help)

# Important links <a name="links"></a>

- [Local copies](https://lapp-owncloud.in2p3.fr/index.php/s/HtYGL5G7TAe0nok) of needed software, like Anaconda and PyCharm
- [Gitter chat rooms](https://gitter.im/Asterics2020-Obelics-School2017)
- [Cartesius access form](https://docs.google.com/forms/d/e/1FAIpQLSc9MMnpX6NYkK0CZuYMmd_O8YssO18mK9rEcfQwz-8-7Xy5Fw/alreadyresponded?c=0&w=1)

# Get a copy of this repository with `git` <a name="repo"></a>

Clone this repository on your personal computer.

      git clone https://github.com/Asterics2020-Obelics/School2017.git

You will need it before the school to install the different tools, and
during the school while attending the hands-on. For Windows, see [below](#windows).

# Recommendation for Python install <a name="python"></a>

You must install Python 3.6 and a few Python libraries. The
recommended way to do so is to use
[Anaconda](https://www.continuum.io/downloads). The procedures described bellow will help you install what is needed for the school.

## Linux <a name="linux"></a>

1. Install required distribution packages :
    - Ubuntu: `sudo apt-get install -y git bzip2 wget`
    - Fedora 25: `sudo dnf install -y git wget bzip2`
    - CERN Scientific Linux 6: `sudo yum install -y git tar bzip2 wget`
    - CERN CentOS 7: `sudo yum install -y git bzip2 wget`

1. [Download](https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh) ([local copy](https://lapp-owncloud.in2p3.fr/index.php/s/HtYGL5G7TAe0nok))
the Linux `Anaconda` installer for Python 3.6.

1. Run the following command line:

		bash Anaconda3-4.3.1-Linux-x86_64.sh

1. Answer `no` to the following question if you do not want to mess up
  your previous installs of python.
	
		Do you wish the installer to prepend the Anaconda3 install location
		to PATH in your /home/chotard/.bashrc ? [yes|no]
		[no] >>> no

1. If you haven't cloned this repository, download one of the
`anaconda_setup` script (`sh` or `csh` depending on your shell):

		wget https://raw.githubusercontent.com/Asterics2020-Obelics/School2017/master/anaconda_setup.sh
		or
		wget https://raw.githubusercontent.com/Asterics2020-Obelics/School2017/master/anaconda_setup.csh

1. If you have installed `anaconda` in a different directory than the default one suggested by the `anaconda` installer (your home directory), edit the first line of the `anaconda_setup` script with your selected path.

		ANACONDA=YOURSELECTEDPATH
		or
		setenv ANACONDA YOURSELECTEDPATH

1. Run the `anaconda_setup` script to set up the correct PATH and
PYTHONPATH enabling the use of your `Anaconda` install.

		source anaconda_setup.sh
		or
		source anaconda_setup.csh

    You can either run this command each time you need to use `Anaconda`,
    or add its content to your `.bashrc` (or equivalent) to set it up at
    the opening of a new terminal.

1. See next section for extra Python libraries requirements (if any).

## Mac <a name="mac"></a>

1. [Download](https://repo.continuum.io/archive/Anaconda3-4.3.1-MacOSX-x86_64.sh) ([local copy](https://lapp-owncloud.in2p3.fr/index.php/s/HtYGL5G7TAe0nok))
the Mac `Anaconda` installer for Python 3.6.

1. Run the following command line:

		bash Anaconda3-4.3.1-MacOSX-x86_64.sh

1. Answer `no` to the following question if you do not want to mess up
  your previous installs of python.
	
		Do you wish the installer to prepend the Anaconda3 install location
		to PATH in your /home/chotard/.bashrc ? [yes|no]
		[no] >>> no

1. If you haven't cloned this repository, first get the `anaconda_setup.sh` script:

		wget https://raw.githubusercontent.com/Asterics2020-Obelics/School2017/master/anaconda_setup.sh

1. If you have installed `anaconda` in a different directory than the default one suggested by the `anaconda` installer (your home directory), edit the first line of the `anaconda_setup` script with your selected path.

		ANACONDA=YOURSELECTEDPATH

1. Run the `anaconda_setup.sh` script to set up the correct PATH and
PYTHONPATH enabling the use of your `Anaconda` install.

		source anaconda_setup.sh

    You can either run this command each time you need to use `Anaconda`,
    or add its content to your `.bashrc` (or equivalent) to set it up at
    the opening of a new terminal.

1. See next section for extra Python libraries requirements (if any).

## Windows <a name="windows"></a>

Instruction for Windows can be found
[here](https://www.continuum.io/downloads#windows) for the installation of Anaconda ([local copy](https://lapp-owncloud.in2p3.fr/index.php/s/HtYGL5G7TAe0nok)). Once installed, you can run `Anaconda navigator`. To run Jupyter, on the main page of the Anaconda navigator, click on `Launch` on the Jupyter notebook box. This will open your favorite browser. From there, you can either load a notebook (e.g. from the Git folder) or create a new notebook by clicking `new -> Python 3`. 

You can also install a Git tool for Windows: [Git for Windows](https://git-for-windows.github.io/). Launch `Git GUI` or `Git bash` to get started. 

## Library requirements <a name="python-req"></a>

All the required libraries come with the `Anaconda` install described
above. If you have followed the previous steps to install Python, you
can skip this section.

If you choose an other way to install Python 3.6 than the one
recommended above, you must install manually the Python libraries
listed in the [requirements.txt](requirements.txt) file. To do so, we
recommend using `pip`.

	  pip install -r requirements.txt

# Jupyter <a name="jupyter"></a>

To launch a Jupyter notebook, simply run the following command:

`jupyter notebook`

On Windows, see in the [above](#windows).

# IDE: PyCharm <a name="pycharm"></a>

We strongly recommend to use pycharm, especially for the "Debugging & profiling" course. Free Community Edition: [Download PyCharm](https://www.jetbrains.com/pycharm/download) ([local copy](https://lapp-owncloud.in2p3.fr/index.php/s/HtYGL5G7TAe0nok)) or opt for a free copy of the Professional Edition under [Student License](https://www.jetbrains.com/student/).

# Cartesius machines <a name="cartesius"></a>

For the parallel and GPU sessions, we will use the [Cartesius machines](https://userinfo.surfsara.nl/systems/cartesius) that are generously made available by SURFsara for the OBELICS school. You will need to connect to them through the ssh protocol (natively installed on Linux and Mac).

For Windows users, we recommend these tools to connect via ssh:
- [Putty](http://www.putty.org/) & [Winscp](https://winscp.net)
- Or, on Windows 10: use the [native bash environment](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)

## Connect to Cartesius

To connect to Cartesius, please open a terminal and use the following command:

    ssh accntXXX@cartesius.surfsara.nl

Where XXX is the account number you received via email. Type in the password you received together with your login name and press enter.
NOTE that, the cursor won't move while tying in the password, this is normal, so just keep typing.

The account is made available for the school and will be valid till 30th of June. If you would like to connect to Cartesius from outside of LAPP, please use the following command:

    ssh accntXXX@doornode.surfsara.nl

Type in your password and select system Cartesius.

## Preparation for Hands-on session of GPU programming

Login to Cartesius, clone the git repository and generate a key pair.

    ssh accntXXX@cartesius.surfsara.nl
    git clone https://github.com/Asterics2020-Obelics/School2017.git
    
    ssh-keygen -t rsa

Press Enter three times. A key pair will be generated for you in directory .ssh. Copy the contents of the public key to file authorized_keys:

    cat .ssh/id_rsa.pub >> .ssh/authorized_keys

## Submit a job to Cartesius
When the hands-on session starts, submit the following job to Cartesius:

    cd School2017/gpu_programming
    sbatch job.jupyter.gpu

Open a new terminal and do the following:

    ssh -L5XXX:localhost:5XXX vis.cartesius.surfsara.nl

Note that, you need to replace XXX with the three digits of your login account.
Now you can open a new tab in your browser and go to localhost:5XXX (replace XXX with the three digits of your own account).
   
# Chat rooms <a name="chat"></a>

[Gitter chat rooms](https://gitter.im/Asterics2020-Obelics-School2017) have been created for each hands-on session and group. If you need to talk to each other during the session, share information, ask questions and get fast answer in case all the tutors are busy, you can use the corresponding chat rooms to do so. These chat rooms can also be used by the different tutors to give information or advices before or during the hands-on sessions.

Be aware that you will need to be connected to use these chat rooms, preferentially using your github account. You can also start one-to-one chat rooms.

# Tutors <a name="tutors"></a>

Here is the list of tutors for the hands-on sessions. Four (or more) are needed for each session (except for GPU and parallel which are parallel sessions).

| Hands-on               | Main tutor(s)              | Other tutors                                                         |
| ---------------------- |----------------------------|----------------------------------------------------------------------|
| Numpy                  | Tamas Gal                  | Axel Donath, Johannes King, Pierre Aubert, Tristan Carel, N. Chotard |
| Pandas                 | Tamas Gal                  | Damian Podareanu, Karl Kosack, Johannes King, N. Chotard             |
| Astropy                | Axel Donath, Johannes King | Karl Kosack, Hendrik Heinl, Tim Jeness, N. Chotard                   |
| Profiling & Debugging  | Karl Kosack                | Axel Donath, Zheng Meyer-Zhao, Pierre Aubert, Tristan Carel          |
| Parallel Programming   | Damian Podareanu           | Tamas Gal, Pierre Aubert, Jean Jacquemier, Tristan Carel             |
| GPU Programming        | Valeriu Codreanu           | Pierre Aubert, Zheng Meyer-Zhao, Tristan Carel (?)                   |

The full list of tutors is available [here](https://indico.in2p3.fr/event/14227/page/10).

 
# Help

Please create a [new
issue](https://github.com/Asterics2020-Obelics/School2017/issues) (you
will need a github account) for each question you may have before or
during the school about software install and/or about one of the
classes. Of course, you should first check the existing list of issues
to see if your question has already been asked and answered before
creating a new one.
