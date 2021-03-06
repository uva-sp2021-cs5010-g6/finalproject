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
   python -m project01.fetch

Running EDA
===========

The EDA script can be run directly from the poetry shell

.. code-block:: bash

   poetry shell # No need to run if you're already in the poetry shell from before.
   python project01.EDA


Running the Questions
=====================

All questions are written as valid modules that can run within the poetry environment.  To run, be sure to have run the fetching script at least once.  Below are example commands

.. code-block:: bash

   poetry shell # No need to run if you're already in the poetry shell from before.
   python -m project01.question1
   python -m project01.question2
   python -m project01.question3
   python -m project01.question4


Running Tests
=============

To run our tests, once again, you'll need to execute a command after starting the poetry shell, and execute pytest without any arugments

.. code-block:: bash

   poetry shell # No need to run if you're already in the poetry shell from before.
   pytest

Building the API Website
========================

You can build a copy of our API documentation by navigating to the `sphinx-build` folder and running the following commands

.. code-block:: bash

   poetry shell # If you're already in a poetry session, you won't need to run this command
   cd ./sphinx-doc
   sphinx-apidoc -f -o ./source ../project01
   sphinx-build -M html ./source ./build

Or by running ``make api html`` if running on a system with GNU Make installed.

The HTML documentation site will be lcoated in ``./build/html/index.html``
