from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from ui_collapsableTreeview import Ui_Form

class CollapsableTreeView(QtWidgets.QWidget,Ui_Form):
    
    def __init__(self,parent:QtWidgets.QWidget=None) -> None:
        """Treeview which can be collapsed or expended on used input

        Args:
            parent (QWidget, optional): Parent widget. Defaults to None.
        """
        super(CollapsableTreeView,self).__init__(parent)
        self.setupUi(self)
        self.toolButton.setCheckable(True)
        self.toolButton.setChecked(False)
        self.toolButton.clicked.connect(self.expand)

        self.isExpanded = False

    def expand(self) -> None:
        """Function called whenever the user clicked on the arrow button. Change collapsed state.
        """
        if self.isExpanded:
            self.treeView.setMaximumHeight(0)
            self.treeView.setMaximumWidth(0)
            self.toolButton.setArrowType(Qt.RightArrow)
            self.isExpanded = False
        else:
            self.treeView.setMaximumHeight(16777215)
            self.treeView.setMaximumWidth(16777215)
            self.toolButton.setArrowType(Qt.DownArrow)
            self.isExpanded = True