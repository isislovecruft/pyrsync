===============================
#pyrsync
===============================
pyrsync is a Python module which implements the [rsync algorithm] [1], 
written in pure Python. It *is not* a wrapper for rsync, but a set of 
functions which apply full rsync functionality through Python.

The original rsync specification calls for the use of an MD5 hash, which
the developers of this module considers to be outdated, and thus all 
occurences of MD5 have been replaced with SHA256. Personally, I would
opt for using SHA512, but this would double the storage size for hash
table databases. SHA256 is sufficient to meet standard security 
requirements for verification processes as of this release, although,
eventually, added functionality for the user/developer to choose between
various hashes should be considered for further releases.

The majority of the code for this module is taken from [Eric Pruitt's
post at ActiveState] [1]. It was orginally licensed under an [MIT license]
[2], and this license has been kept wthout modifications.

## Installation
--------------------------------
If you have [setuptools] [3] installed, simply do:

    $ sudo python setup.py install

If you do not have setuptools, the setup.py script will detect this and 
default to using the python builtin distutils. To install using distutils,
the installation process is the same as documented above for setuptools.

## Use
--------------------------------
An example use case for this module:

    # On the system containing the file that needs to be patched
    >>> import pyrsync
    >>> unpatched = open("unpatched.file", "rb")
    >>> hashes = pyrsync.blockchecksums(unpatched)

    # On the remote system after having received hashes
    >>> import pyrsync
    >>> patchedfile = open("patched.file", "rb")
    >>> delta = pyrsync.rsyncdelta(patchedfile, hashes)

    # System with the unpatched file after receiving delta
    >>> unpatched.seek(0)
    >>> save_to = open("locally-patched.file", "wb")
    >>> pyrsync.patchstream(unpatched, save_to, delta)

[1]: http://samba.anu.edu.au/rsync/ "Andrew Tridgell and Paul Mackerras. The rsync algorithm. Technical Report TR-CS-96-05, Canberra 0200 ACT, Australia, 1996."
[2]: https://code.activestate.com/recipes/577518-rsync-algorithm/ "Rsync Algorithm (Python Recipe)"
[3]: http://www.opensource.org/licenses/mit-license.php "OSI MIT License"