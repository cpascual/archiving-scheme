#!/usr/bin/env python
#############################################################################
##
## This file is part of Taurus
## 
## http://taurus-scada.org
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
## 
## Taurus is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Taurus is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public License
## along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

__all__ = ['ArchivingFactory']


from taurus.core.taurusbasetypes import TaurusElementType
from archivingattribute import ArchivingAttribute
from archivingauthority import ArchivingAuthority
from archivingdevice import ArchivingDevice
from taurus.core.taurusexception import TaurusException
from taurus.core.util.log import Logger
from taurus.core.util.singleton import Singleton
from taurus.core.taurusfactory import TaurusFactory

try:
    import PyTangoArchiving
except ImportError:
    PyTangoArchiving = None

class ArchivingFactory(Singleton, TaurusFactory, Logger):
    """
    A Singleton class that provides Archiving related objects.
    """
    schemes = ("archiving",)

    elementTypesMap = {TaurusElementType.Authority: ArchivingAuthority,
                       TaurusElementType.Device: ArchivingDevice,
                       TaurusElementType.Attribute: ArchivingAttribute
                       }

    def __init__(self):
        """ Initialization. Nothing to be done here for now."""
        pass

    def init(self, *args, **kwargs):
        """Singleton instance initialization."""
        if PyTangoArchiving is None:
            raise TaurusException('PyTangoArchiving is not available')
        name = self.__class__.__name__
        Logger.__init__(self, name)
        TaurusFactory.__init__(self)

    def getAuthorityNameValidator(self):
        """Return ArchivingDatabaseNameValidator"""
        import archivingvalidator
        return archivingvalidator.ArchivingAuthorityNameValidator()
                 
    def getDeviceNameValidator(self):
        """Return ArchivingDeviceNameValidator"""
        import archivingvalidator
        return archivingvalidator.ArchivingDeviceNameValidator()

    def getAttributeNameValidator(self):
        """Return ArchivingAttributeNameValidator"""
        import archivingvalidator
        return archivingvalidator.ArchivingAttributeNameValidator()
