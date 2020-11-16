import sys
from Forum_Page import *
from copy import deepcopy
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import pandas as pd

SPEC_DEFAULT = UPPER_DEFAULT = DIG_DEFAULT = 0

class Forum_Viewer(QWidget):

  def __init__(self, manager):
    super().__init__()

    self.__manager = manager
    self.setWindowTitle(manager.get_name())
    self.setGeometry(300, 300,600,600)
    self.__set_up_dialog()
    self.add = QPushButton('Add post')
    self.add.setDefault(False)
    self.add.setAutoDefault(False)
    self.add.clicked.connect(lambda: self.specs.show())
    self.remove = QPushButton('Delete post')
    self.remove.clicked.connect(self.delete_post)
    self.remove.setDefault(False)
    self.remove.setAutoDefault(False)
		
    #Window with grid layout for pushbuttons
    self.my_win=  QDialog()
    self.win_panel = QListWidget(self.my_win)
    self.win_panel.itemClicked.connect(self.display_info)
    windowLayout = QGridLayout()
    windowLayout.addWidget(self.win_panel, 0,1)
    windowLayout.addWidget(self.add,1,1)
    windowLayout.addWidget(self.remove,2,1)
    self.my_win.setLayout(windowLayout)
    layout = QHBoxLayout()
    self.disp_panel = QWidget(self.my_win)
    panelLayout = QVBoxLayout()
    self.disp_panel.setLayout(panelLayout)
    
    #Panel to hold post and vote buttons
    self.panel = QTextBrowser(self.disp_panel)
    self.panel.setGeometry(10,10,500,500)
    panelLayout.addWidget(self.panel)
    
    #Vote buttons
    self.upvote = QPushButton('Upvote') 
    self.upvote.setDefault(False)
    self.upvote.setAutoDefault(False) 
    self.upvote.clicked.connect(self.vote_up)
    self.upvote.setEnabled(False)
    self.downvote = QPushButton('Downvote') 
    self.downvote.setDefault(False)
    self.downvote.setAutoDefault(False) 
    self.downvote.clicked.connect(self.vote_down)
    self.downvote.setEnabled(False)
    button_w = QWidget(self.disp_panel)
    l2 = QGridLayout()
    button_w.setLayout(l2)
    l2.addWidget(self.upvote, 0,0)
    l2.addWidget(self.downvote, 0,1)
    panelLayout.addWidget(button_w)
    
    #Add all to main window
    layout.addWidget(self.my_win)
    layout.addWidget(self.disp_panel)
    self.setLayout(layout)
    #Bring up window
    self.show()
  
  def __set_up_dialog(self):
    self.specs = QDialog(self)
    master_layout = QVBoxLayout()
    self.specs.setWindowTitle('Post Details')
    self.specs.setLayout(master_layout)
    layout = QVBoxLayout()
    sec_panel = QWidget(self.specs)
    sec_panel.setLayout(layout)
    th_panel = QWidget(self.specs)
    layout_2 = QVBoxLayout()
    th_panel.setLayout(layout_2)
    self.title_choice = QLineEdit(th_panel)
    self.username_choice = QLineEdit(th_panel)
    layout_2.addWidget(QLabel('Enter title:'))
    layout_2.addWidget(self.title_choice)
    layout_2.addWidget(QLabel('Enter author: '))
    layout_2.addWidget(self.username_choice)
    self.post_choice = QTextEdit(sec_panel)
    layout.addWidget(QLabel('Enter main text of post:'))
    layout.addWidget(self.post_choice)
    OK = QPushButton('OK') #may need to add validators to check
    OK.setDefault(False)
    OK.setAutoDefault(False) #add reset
    OK.clicked.connect(self.post_add)
    reset = QPushButton('Clear')
    reset.setDefault(False)
    reset.setAutoDefault(False)
    reset.clicked.connect(self.reset_specs)
    cancel = QPushButton('Cancel')
    cancel.setDefault(False)
    cancel.setAutoDefault(False)
    cancel.clicked.connect(lambda: self.specs.close())
    button_w = QWidget(self.specs)
    l2 = QGridLayout()
    button_w.setLayout(l2)
    l2.addWidget(OK, 0,0)
    l2.addWidget(reset, 0,1)
    l2.addWidget(cancel, 0,2)
    self.specs.layout().addWidget(th_panel)
    self.specs.layout().addWidget(sec_panel)
    sep_line = QFrame()
    sep_line.setFrameShape(QFrame.HLine)
    sep_line.setFrameShadow(QFrame.Sunken)
    self.specs.layout().addWidget(sep_line)
    self.specs.layout().addWidget(button_w)
    self.specs.resize(500, 500)
  
  
  def post_add(self):
    title = self.title_choice.text()
    author = self.username_choice.text()
    post  = self.post_choice.toPlainText()
    #print(post)
    if(len(title)):
        if not len(author):
            author = None
        self.__manager.add_post(title, post, author)
        self.__repop_posts()
        self.specs.accept()
    self.reset_specs()
  
  
  def display_info(self, enable = True):
    title = self.win_panel.currentItem().text()
    info = self.__manager.get_post_info(title)
    if pd.isnull(info[1]):
        info[1] = "DELETED"
        info[2] = "DELETED"
    self.panel.setText('Title:' + title + '\n\n' + 'Date:' + str(info[0]) + '\n\nUsername: ' + str(info[1]) + '\n\nVotes: ' + str(info[3]) + '\n\n' + str(info[2]))
    if enable:   
        self.upvote.setEnabled(True)
        self.downvote.setEnabled(True)
  
  def delete_post(self):
  	if self.win_panel.currentItem() is not None:
  		title = self.win_panel.currentItem().text()
  		ok = QMessageBox().question(self, 'Confirm delete', 'Are you sure you want to delete ' + title + '?', )
  		if(ok == QMessageBox.Yes):
  			self.__manager.delete_post(title)
  			self.display_info(False)
  	self.__repop_posts()
  
  def reset_specs(self):
  	self.post_choice.clear()
  	self.title_choice.clear()
  	self.username_choice.clear()
  	
  	
  def __repop_posts(self):
  	titles = self.__manager.get_titles()
  	print(titles)
  	self.win_panel.clear()
  	for item in titles:
  		self.win_panel.addItem(item)
  
  def vote_up(self):
    title = self.win_panel.currentItem().text()
    self.__manager.vote_post(title)
    self.display_info(False)
    self.upvote.setEnabled(False)
    self.downvote.setEnabled(False)
    

  def vote_down(self):
    title = self.win_panel.currentItem().text()
    self.__manager.vote_post(title, False)
    self.display_info(False)
    self.upvote.setEnabled(False)
    self.downvote.setEnabled(False)
  	
if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = Forum_Viewer(Forum_Page('Test Forum'))
  sys.exit(app.exec_())
