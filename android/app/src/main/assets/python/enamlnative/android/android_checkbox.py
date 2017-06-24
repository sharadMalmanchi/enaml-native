'''
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on May 20, 2017

@author: jrm
'''
import jnius
from atom.api import Typed

from enamlnative.widgets.checkbox import ProxyCheckBox

from .android_compound_button import AndroidCompoundButton, CompoundButton


class CheckBox(CompoundButton):
    __javaclass__ = 'android.widget.CheckBox'


class AndroidCheckBox(AndroidCompoundButton, ProxyCheckBox):
    """ An Android implementation of an Enaml ProxyCheckBox.

    """
    #: A reference to the widget created by the proxy.
    widget = Typed(CheckBox)

    # --------------------------------------------------------------------------
    # Initialization API
    # --------------------------------------------------------------------------
    def create_widget(self):
        """ Create the underlying Android widget.

        """
        self.widget = CheckBox(self.get_context())