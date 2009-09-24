<!-- -*- coding: utf-8 -*- -->

Overview

 ECQuiz is an extension module (a so-called *product*) for the
 "Plone":http://plone.org/ content management system.  It allows you
 to create and deliver multiple-choice tests.

Download

 "ECQuiz 1.2":http://plone.org/products/ecquiz/

Prerequisites

 To use ECQuiz you need:

 1. A current Plone installation, specifically Plone 3.x; check
    "plone.org":http://plone.org/products/plone/releases/ for details.

 2. The "DataGridField":http://plone.org/products/datagridfield
    product.  This version of ECQuiz has been tested extensively with
    DataGridField version 1.6rc1.  Newer versions might or might not
    work as well.

Installation

 If you have a suitable Zope/Plone installation (not using build-outs)
 you can install ECQuiz as follows:

 1. Extract the DataGridField package into the 'Products' directory of
    your Zope instance.  You can find out where your Zope instance is
    installed by opening the Zope Management Interface (ZMI) and going
    to the Control Panel; the directory listed as 'INSTANCE_HOME' is
    what you're looking for.

 2. Extract the ECQuiz package into the 'Products' directory.

 3. Restart Zope

 4. Log in to your Plone site as a manager and use the "Add/Remove
    Products" tool under "Site Setup" to install ECQuiz in this Plone
    site.  Alternatively, in the ZMI, you can use the
    'portal_quickinstaller' of your Plone site in which you want to
    use ECQuiz.  In both cases, check the box next to ECQuiz and click
    "Install".

Support

 For questions and discussions about ECQuiz, please join the
 "eduComponents mailing
 list":https://listserv.uni-magdeburg.de/mailman/listinfo/educomponents.

Credits

 ECQuiz was written by Wolfram Fenske and "Michael
 Piotrowski":http://www.dynalabs.de/mxp/.  Sascha
 Peilicke implemented the Quick Edit functionality.

 The Statistics class was written by "Chad
 J. Schroeder":http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/409413.
 It is licensed under the "Python
 license":http://www.python.org/license.

 The L2 Lisp parser was written by Wolfram Fenske.

 Several icons used in ECQuiz are from the "Silk icon
 set":http://www.famfamfam.com/lab/icons/silk/ by Mark James.  They
 are licensed under a "Creative Commons Attribution 2.5
 License":http://creativecommons.org/licenses/by/2.5/.

 The Slovenian translation was contributed by Matjaž Jeran.
 The Italian translation was contributed by Elena Momi.

 Jim Baack contributed a rough version of the Plone 3 port.

 The Plone 3 port was finished by Eudemonia Solutions AG, with funding
 from the "ITC of the ILO":http://www.itcilo.org/.

License

 ECQuiz is licensed under the
 "GPL":http://opensource.org/licenses/gpl-license.

 Copyright © 2007 Otto-von-Guericke-Universität Magdeburg

 ECQuiz is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 ECQuiz is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with ECQuiz; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
