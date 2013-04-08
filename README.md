XBlock components for numerical simulation
==========================================

Copyright (C) 2013 Harish Narayanan

This project is released under the GNU Affero General Public
License. Please read LICENSE.txt for the complete terms.


Background
----------

This project aims to create a collection of XBlocks that allow
students to carry out simulations in mathematical physics and
instructors to pose exercises within this context. It does this by
connecting to [thinkbot](http://thinkbot.net/), a computing service
which offers a selection of scientific computing software through a
[RESTful
API](https://en.wikipedia.org/wiki/Representational_state_transfer).

In particular, the project initially aims to build three kinds of
XBlock components:

1. A component that allows students to interact with the results of a
   precomputed numerical solution. Such demonstrations are used to
   motivate the theoretical material covered in classes.

2. A component that allows students to dynamically interact in simple
   ways with a numerical simulation, such as changing parameters.

3. A component that presents students with interactive programming
   exercises tied to computational science.


Installation
------------

1. Install the [XBlock component
   architecture](https://github.com/edX/XBlock) project

2. Source the corresponding venv, if you installed it in a virtual
   environment (which you should have!)

3. Install the thinkbot related Xblocks from this project's root
   folder:

       $ pip install -e thinkbot

4. Run the Django development server for the XBlock workbench:

       $ python manage.py runserver

5. Open a web browser to: http://127.0.0.1:8000 and find the link to
   the thinkbot XBlock


Contact info
------------

If you're interested in finding out more about how to use this project
in your own course or are interested in contributing to it, please
write to me:

Harish Narayanan <mail@harishnarayanan.org>
