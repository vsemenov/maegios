#!/usr/bin/python2.5
# -*- coding: utf-8 -*-
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published
## by the Free Software Foundation; version 2 only.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
import py2deb
import os

if __name__ == "__main__":
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except:
        pass
    print

    p=py2deb.Py2deb("maegios")   #This is the package name and MUST be in lowercase!
    p.description="Receive Nagios alerts on your Maemo device. Monitor status of hosts and services in your Nagios instance. Desktop widget and vibration, sound, light, text alerts are included."
    p.author = "Vladimir Semenov"
    p.mail = "vlad@vsemenov.com"
    p.depends = "python, python-osso, python-gtk2, python-cairo, python-hildon, python-hildondesktop, hildon-desktop-python-loader, gnome-python, python-gobject, python-dbus, python-gst0.10"
    p.section = "user/network"
    p.icon = "maegios-deb-48x48.png"
    p.arch = "all"                #should be all for python, any for all arch
    p.urgency = "low"             #not used in maemo onl for deb os
    p.distribution = "fremantle"
    p.repository = "extras-devel"
    #  p.postinstall="""#!/bin/sh
    #  chmod +x /usr/bin/mclock.py""" #Set here your post install script
    #  p.postremove="""#!/bin/sh
    #  chmod +x /usr/bin/mclock.py""" #Set here your post remove script
    #  p.preinstall="""#!/bin/sh
    #  chmod +x /usr/bin/mclock.py""" #Set here your pre install script
    #  p.preremove="""#!/bin/sh
    #  chmod +x /usr/bin/mclock.py""" #Set here your pre remove script
    version = "0.4.3"           #Version of your software, e.g. "1.2.0" or "0.8.2"
    build = "3"                 #Build number, e.g. "1" for the first build of this version of your software. Increment for later re-builds of the same version of your software.
                                 #Text with changelog information to be displayed in the package "Details" tab of the Maemo Application Manager
    changeloginformation = "Development version 0.4.3-3. Use at your own risk." 
    
    dir_name = "src"            #Name of the subfolder containing your package source files (e.g. usr\share\icons\hicolor\scalable\myappicon.svg, usr\lib\myapp\somelib.py). We suggest to leave it named src in all projects and will refer to that in the wiki article on maemo.org
    #Thanks to DareTheHair from talk.maemo.org for this snippet that recursively builds the file list 
    for root, dirs, files in os.walk(dir_name):
        real_dir = root[len(dir_name):]
        fake_file = []
        for f in files:
            fake_file.append(root + os.sep + f + "|" + f)
        if len(fake_file) > 0:
            p[real_dir] = fake_file

    print p
    r = p.generate(version, build, changelog=changeloginformation, tar=True, dsc=True, changes=True, build=False, src=True)

