====
Group 6 Final Project
====

----
CS5010 Spring 2021
----


Getting Started
===============

To get started, you will first need to have *python3*, *pipx*, and *poetry* installed.

To bootstrap your environment, run

.. code-block:: bash

   python -m pip install --user pipx
   python -m pipx install poetry

Once you have poetry installed, you can activate it's environment by running the below

.. code-block:: bash

   poetry install
   poetry shell

From there, you should be bootstrapped and ready to run the python code.

For more information on poetry, see `Poetry's Website <https://python-poetry.org/>`_.

Running the Fetcher
===================

To run the URI fetcher, you must first be in your poetry environment, and then you can run the module directly, as shown below.

.. code-block:: bash

   poetry shell
   python -m project01.fetcher

