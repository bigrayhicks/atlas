Follow the Money Atlas
======================

The Follow the Money Atlas (``atlas``) is a component of the Investigative
Dashboard that helps reporters find the public records and databases they
need to investigate companies and people across the world. It contains a
curated index of public databases (such as company registries, court and
procurement records) for most all countries. It also queries other ID
components (such as ID Search/``aleph``) for data availability in various
countries.


Installing the atlas
--------------------

```bash
$ virtualenv env
$ pip install -r requirements.txt
$ export FLASK_DEBUG=1
$ export FLASK_APP=atlas/web.py
$ flask run
```


License
-------

MIT License

Copyright (c) 2017 Journalism Development Network, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
