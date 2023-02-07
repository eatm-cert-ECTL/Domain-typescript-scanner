from PyQt5 import QtWidgets
from ui_filePathSelector import Ui_filePathSelector

class FilePathSelector(QtWidgets.QWidget,Ui_filePathSelector):
    
    def __init__(self, parent:QtWidgets.QWidget=None) -> None:
        """Widget allowing path selection by writing the path or by openning a windows to select it. Both are view are conected.

        Args:
            parent (:class:`QtWidgets.QWidget`, optional): Parent widget. Defaults to None.
        """
        super(FilePathSelector,self).__init__(parent)
        self.setupUi(self)

        self.path = ""
        self.pushButton.clicked.connect(self.browse)
        self.textEdit.textChanged.connect(self.f)

    def browse(self) -> None:
        """Open :class:`QtWidgets.QfileDialog` to let the user choose a path.
        """
        file = QtWidgets.QFileDialog.getOpenFileName(self,"Choose a file","~/")
        if file[0] != '':
            self.textEdit.setPlainText(file[0])
    
    def f(self) -> None:
        """Called on :class:`testEdit` text change.
        """
        self.path = self.textEdit.toPlainText()