import os
import sys
import time
import random
import psutil
import subprocess
import json
from urllib import request, parse
from PyQt5 import QtCore,QtMultimedia
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class DDH(QWidget):
    def __init__(self, parent=None):
        super(DDH, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowTitle('deepin desktop helper')
        self.setWindowIcon(QIcon('files/image/blush.gif'))
        self.repaint()
        self.initPall()
        self.update()
        self.QSlider()
        self.music_help()
        self.cpuram()
        self.morelist()
        self.will_exit=False
        desktop=QApplication.desktop()
        self.move(desktop.width()-30,desktop.height()/2)
        self.time_id = self.startTimer(1)
        self.mouse=self.cursor()
        self.music_check=QtMultimedia.QMediaContent(QUrl.fromLocalFile(QtCore.QDir.current().absoluteFilePath('files/sound/check.mp3')))
        self.play_check=QtMultimedia.QMediaPlayer()
        self.play_check.setMedia(self.music_check)
        self.gifdoing=False
        self.music_a=QtMultimedia.QMediaContent(QUrl.fromLocalFile(QtCore.QDir.current().absoluteFilePath('files/sound/a.mp3')))
        self.play_a=QtMultimedia.QMediaPlayer()
        self.play_a.setMedia(self.music_a)
        self.music_b=QtMultimedia.QMediaContent(QUrl.fromLocalFile(QtCore.QDir.current().absoluteFilePath('files/sound/b.mp3')))
        self.play_b=QtMultimedia.QMediaPlayer()
        self.play_b.setMedia(self.music_b)
        self.music_c=QtMultimedia.QMediaContent(QUrl.fromLocalFile(QtCore.QDir.current().absoluteFilePath('files/sound/c.mp3')))
        self.play_c=QtMultimedia.QMediaPlayer()
        self.play_c.setMedia(self.music_c)
        self.play_a.stateChanged.connect(self.do_mediaplayer_statechanged)
        self.play_b.stateChanged.connect(self.do_mediaplayer_statechanged)
        self.play_c.stateChanged.connect(self.do_mediaplayer_statechanged)
        self.music_t=QtMultimedia.QMediaContent(QUrl.fromLocalFile(QtCore.QDir.current().absoluteFilePath('files/sound/true.mp3')))
        self.play_t=QtMultimedia.QMediaPlayer()
        self.play_t.setMedia(self.music_t)
        self.music_f=QtMultimedia.QMediaContent(QUrl.fromLocalFile(QtCore.QDir.current().absoluteFilePath('files/sound/false.mp3')))
        self.play_f=QtMultimedia.QMediaPlayer()
        self.play_f.setMedia(self.music_f)
        self.time_show=QLabel(self)
        self.time_show.setStyleSheet("font-size:20px;")
        self.time_show.resize(150,50)
        self.time_show.move(245,60)
        self.longtime_show=QLabel(self)
        self.longtime_show.setStyleSheet("font-size:20px;")
        self.longtime_show.resize(300,50)
        self.longtime_show.move(0,0)
        self.timeshowing=False
        self.timedoing=False
        self.longtime_show.resize(0,0)
        self.longcpuram=QLabel(self)
        self.longcpuram.setStyleSheet("font-size:20px;")
        self.longcpuram.resize(300,50)
        self.longcpuram.move(0,0)
        self.cpuramshowing=False
        self.cpuramdoing=False
        self.longcpuram.resize(0,0)
        self.rm_f_run=False
        self.qarm_f=False
        self.qa2s_run=False
        self.game_run=False
        self.left_mouse=False
        self.cpuramrun()
        self.morething()
        self.about()
    def initPall(self):
        icons=os.path.join('files/image/blush.gif')
        exit=os.path.join('files/image/exit.svg')
        quit_button = QAction('退出', self, triggered=self.exit)
        quit_button.setIcon(QIcon(exit))
        show = QAction('显示', self, triggered=self.showmain)
        show.setIcon(QIcon('files/image/hidden.svg'))
        hint = QAction('隐藏', self, triggered=self.hintmain)
        hint.setIcon(QIcon('files/image/hint.svg'))
        about_i = QAction('关于', self, triggered=self.show_about)
        about_i.setIcon(QIcon('files/image/about.svg'))
        self.tray_menu = QMenu(self)
        self.tray_menu.addAction(about_i)
        self.tray_menu.addAction(show)
        self.tray_menu.addAction(hint)
        self.tray_menu.addAction(quit_button)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(icons))
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()
    def exit(self):
        self.will_exit=True
        self.play_check.play()
        self.mouth.image.resize(0,0)
        self.eye1.image.resize(0,0)
        self.eye2.image.resize(0,0)
        self.eyemian1.image.resize(0,0)
        self.eyemian2.image.resize(0,0)
        self.help_music.image.resize(0,0)
        self.time_show.resize(0,0)
        self.longtime_show.resize(0,0)
        self.cpua.image.resize(0,0)
        self.cpub.image.resize(0,0)
        self.rama.image.resize(0,0)
        self.ramb.image.resize(0,0)
        self.moret.image.resize(0,0)
        self.longcpuram.resize(0,0)
        self.image.move(0,0)
        self.movie = QMovie("files/image/ok.gif")
        self.image.setMovie(self.movie)
        self.resize(325*(self.QS.value()/50),292*(self.QS.value()/50))
        self.image.resize(325*(self.QS.value()/50),292*(self.QS.value()/50))
        self.movie.setScaledSize(QSize(325*(self.QS.value()/50),292*(self.QS.value()/50)))
        self.repaint()
        self.movie.start()
        self.quittime = QTimer()
        self.quittime.timeout.connect(self.quit)
        self.quittime.start(1000)
    def quit(self):
        self.close()
        sys.exit()
    def showmain(self):
        self.play_check.play()
        if self.windowOpacity()<0.05:
            self.showNormal()
            self.QS.showNormal()
            self.activateWindow()
            self.QS.activateWindow()
            for x in range(2000):
                time.sleep(0.0001)
                self.setWindowOpacity(x/2000)
    def hintmain(self):
        self.play_check.play()
        if self.windowOpacity()>0.95:
            for x in range(2000):
                time.sleep(0.0001)
                self.setWindowOpacity(1- x/2000)
            self.showMinimized()
            self.QS.showMinimized()
    def update(self):
        self.image = QLabel(self)
        self.movie = QMovie("files/image/beta.gif")
        self.image.setMovie(self.movie)
        self.movie.start()
        self.resize(325,292)
        self.image.resize(265,262)
        self.image.move(0,30)
        self.movie.setScaledSize(QSize(265, 262))
        self.mouth = QLabel(self)
        self.mouth.image = QLabel(self)
        self.mouth.movie = QMovie("files/image/mouth.gif")
        self.mouth.image.setMovie(self.mouth.movie)
        self.mouth.movie.start()
        self.mouth.image.resize(40,40)
        self.mouth.movie.setScaledSize(QSize(40, 40))
        self.mouth.image.move(118,123)
        self.eyemian1 = QLabel(self)
        self.eyemian2 = QLabel(self)
        self.eyemian1.image = QLabel(self)
        self.eyemian2.image = QLabel(self)
        self.eye1 = QLabel(self)
        self.eye2 = QLabel(self)
        self.eye1.image = QLabel(self)
        self.eye2.image = QLabel(self)
        self.eye1.movie = QMovie("files/image/eye.gif")
        self.eye2.movie = QMovie("files/image/eye.gif")
        self.eyemian1.movie = QMovie("files/image/eyemain.gif")
        self.eyemian2.movie = QMovie("files/image/eyemain.gif")
        self.eye1.image.setMovie(self.eye1.movie)
        self.eye2.image.setMovie(self.eye2.movie)
        self.eyemian1.image.setMovie(self.eyemian1.movie)
        self.eyemian2.image.setMovie(self.eyemian2.movie)
        self.eye1.image.resize(32,15)
        self.eye2.image.resize(32,15)
        self.eyemian1.image.resize(10,10)
        self.eyemian2.image.resize(10,10)
        self.eye1.movie.setScaledSize(QSize(32,15))
        self.eye2.movie.setScaledSize(QSize(32,15))
        self.eyemian1.movie.setScaledSize(QSize(10,10))
        self.eyemian2.movie.setScaledSize(QSize(10,10))
        self.eye1.image.move(84,94)
        self.eye2.image.move(157,94)
        self.eyemian1.image.move(95,97)
        self.eyemian2.image.move(168,97)
        self.eyemian2.movie.start()
        self.eyemian1.movie.start()
        self.eye1.movie.start()
        self.eye1.movie.start()
        self.eye1.movie.stop()
        self.eye2.movie.start()
        self.eye1.movie.start()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.left_mouse = True
            if (self.pos().x()+self.help_music.image.pos().x()-self.mouse.pos().x()>-50*(self.QS.value()/50)) and (self.pos().x()+self.help_music.image.pos().x()-self.mouse.pos().x()<0) and (self.pos().y()+self.help_music.image.pos().y()-self.mouse.pos().y()>-50*(self.QS.value()/50)) and (self.pos().y()+self.help_music.image.pos().y()-self.mouse.pos().y()<0):
                if self.help_music.gif==0 and self.gifdoing==False:
                    self.play_check.play()
                    self.help_music.movie = QMovie("files/image/musicrun.gif")
                    self.help_music.gif=1
                    self.help_music.image.setMovie(self.help_music.movie)
                    self.gifdoing=True
                    musiclist=random.randint(0,2)
                    if musiclist==0:
                        self.play_a.play()
                    if musiclist==1:
                        self.play_b.play()
                    if musiclist==2:
                        self.play_c.play()
                if self.help_music.gif==1 and self.gifdoing==False:
                    self.play_check.play()
                    self.help_music.movie = QMovie("files/image/musicstop.gif")
                    self.help_music.gif=0
                    self.help_music.image.setMovie(self.help_music.movie)
                    self.gifdoing=True
                    self.play_a.pause()
                    self.play_b.pause()
                    self.play_c.pause()
            if (self.pos().x()+self.time_show.pos().x()-self.mouse.pos().x()>-150*(self.QS.value()/50)) and (self.pos().x()+self.time_show.pos().x()-self.mouse.pos().x()<0) and (self.pos().y()+self.time_show.pos().y()-self.mouse.pos().y()>-50*(self.QS.value()/50)) and (self.pos().y()+self.time_show.pos().y()-self.mouse.pos().y()<0):
                self.play_check.play()
                if self.timeshowing:
                    if self.timedoing==False:
                        self.timedoing=True
                        self.longtime_show.resize(0,0)
                        self.timeshowing=False
                else:
                    if self.timedoing==False:
                        self.timedoing=True
                        self.longtime_show.resize(500,50*(self.QS.value()/50))
                        self.longtime_show.setStyleSheet("font-size:"+str(int(20*(self.QS.value()/50)))+"px;")
                        self.timeshowing=True
                        self.cpuramdoing=True
                        self.longcpuram.resize(0,0)
                        self.cpuramshowing=False
            self.help_music.image.resize(50*(self.QS.value()/50),50*(self.QS.value()/50))
            self.help_music.movie.setScaledSize(QSize(50*(self.QS.value()/50),50*(self.QS.value()/50)))
            self.help_music.image.move(260*(self.QS.value()/50),10*(self.QS.value()/50))
            self.help_music.image.repaint()
            self.help_music.repaint()
            self.help_music.movie.start()
            if (self.pos().x()+self.rama.image.pos().x()-self.mouse.pos().x()>-30*(self.QS.value()/50)) and (self.pos().x()+self.rama.image.pos().x()-self.mouse.pos().x()<30) and (self.pos().y()+self.rama.image.pos().y()-self.mouse.pos().y()>-65*(self.QS.value()/50)) and (self.pos().y()+self.rama.image.pos().y()-self.mouse.pos().y()<0):
                self.play_check.play()
                if self.cpuramshowing:
                    if self.cpuramdoing==False:
                        self.cpuramdoing=True
                        self.longcpuram.resize(0,0)
                        self.cpuramshowing=False
                else:
                    if self.cpuramdoing==False:
                        self.cpuramdoing=True
                        self.longcpuram.resize(300*(self.QS.value()/50),50*(self.QS.value()/50))
                        self.longcpuram.setStyleSheet("font-size:"+str(int(20*(self.QS.value()/50)))+"px;")
                        self.cpuramshowing=True
                        self.timedoing=True
                        self.longtime_show.resize(0,0)
                        self.timeshowing=False
            if (self.pos().x()+self.moret.image.pos().x()-self.mouse.pos().x()>-50*(self.QS.value()/50)) and (self.pos().x()+self.moret.image.pos().x()-self.mouse.pos().x()<0) and (self.pos().y()+self.moret.image.pos().y()-self.mouse.pos().y()>-50*(self.QS.value()/50)) and (self.pos().y()+self.moret.image.pos().y()-self.mouse.pos().y()<0):
                self.show_m_list()
        if event.button() == QtCore.Qt.MidButton:
            self.play_a.stop()
            self.play_b.stop()
            self.play_c.stop()
            self.help_music.movie = QMovie("files/image/musicstop.gif")
            self.help_music.gif=0
            self.help_music.image.setMovie(self.help_music.movie)
            self.help_music.image.resize(50*(self.QS.value()/50),50*(self.QS.value()/50))
            self.help_music.movie.setScaledSize(QSize(50*(self.QS.value()/50),50*(self.QS.value()/50)))
            self.help_music.image.move(260*(self.QS.value()/50),10*(self.QS.value()/50))
            self.help_music.image.repaint()
            self.help_music.repaint()
            self.help_music.movie.start()
        self.mouse_pos = event.globalPos() - self.pos()
        event.accept()
        self.setCursor(QCursor(Qt.OpenHandCursor))
        if self.QS.isActiveWindow()==False:
            self.QS.setWindowOpacity(0)
        if self.about.isActiveWindow()==False:
            self.about.showMinimized()
        if self.m_list.isActiveWindow()==False:
            self.m_list.showMinimized()
        if self.rm_f_run:
            if self.rm_f.isActiveWindow()==False:
                self.rm_f.showMinimized()
        if self.qa2s_run:
            if self.qa2s.isActiveWindow()==False:
                self.qa2s.showMinimized()
    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.left_mouse:
            self.move(event.globalPos() - self.mouse_pos)
        event.accept()
    def mouseReleaseEvent(self, event):
        self.left_mouse = False
        self.gifdoing = False
        self.timedoing=False
        self.cpuramdoing=False
        self.m_list.doing=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        about_m = menu.addAction("关于")
        size_s = menu.addAction("设置大小")
        hide = menu.addAction("隐藏")
        quitapp = menu.addAction("退出")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == quitapp:
            self.exit()
        if action == hide:
            self.play_check.play()
            if self.windowOpacity()>0.95:
                for x in range(2000):
                    time.sleep(0.0001)
                    self.setWindowOpacity(1- x/2000)
                self.showMinimized()
                self.QS.showMinimized()
        if action == size_s:
            self.play_check.play()
            self.QS.showNormal()
            self.QS.setWindowOpacity(1)
        if action == about_m:
            self.show_about()
    def QSlider(self):
        self.QS = QSlider(Qt.Horizontal)
        self.QS.setMinimum(10)
        self.QS.setMaximum(110)
        self.QS.setSingleStep(10)
        self.QS.setValue(50)
        self.QS.setTickPosition(QSlider.TicksBelow)
        self.QS.setTickInterval(10)
        self.QS.valueChanged.connect(self.valuechange)
        self.QS.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        self.QS.setAutoFillBackground(False)
        self.QS.setAttribute(Qt.WA_TranslucentBackground, True)
        self.QS.setWindowTitle('deepin desktop helper大小设置')
        self.QS.setWindowIcon(QIcon('files/image/blush.gif'))
        self.QS.move(self.x(),self.y()-30)
        self.QS.setWindowOpacity(0)
        self.QS.show()
    def valuechange(self):
        self.resize(325*(self.QS.value()/50),292*(self.QS.value()/50))
        self.image.move(0,30*(self.QS.value()/50))
        self.image.resize(265*(self.QS.value()/50),262*(self.QS.value()/50))
        self.movie.setScaledSize(QSize(265*(self.QS.value()/50),262*(self.QS.value()/50)))
        self.mouth.image.resize(40*(self.QS.value()/50),40*(self.QS.value()/50))
        self.mouth.movie.setScaledSize(QSize(40*(self.QS.value()/50), 40*(self.QS.value()/50)))
        self.mouth.image.move(118.5*(self.QS.value()/50),123*(self.QS.value()/50))
        self.eye1.image.resize(32*(self.QS.value()/50),15*(self.QS.value()/50))
        self.eye1.movie.setScaledSize(QSize(32*(self.QS.value()/50), 15*(self.QS.value()/50)))
        self.eye1.image.move(84*(self.QS.value()/50),94*(self.QS.value()/50))
        self.eye2.image.resize(32*(self.QS.value()/50),15*(self.QS.value()/50))
        self.eye2.movie.setScaledSize(QSize(32*(self.QS.value()/50), 15*(self.QS.value()/50)))
        self.eye2.image.move(157*(self.QS.value()/50),94*(self.QS.value()/50))
        self.eyemian1.image.resize(10*(self.QS.value()/50),10*(self.QS.value()/50))
        self.eyemian1.movie.setScaledSize(QSize(10*(self.QS.value()/50), 10*(self.QS.value()/50)))
        self.eyemian1.image.move(95*(self.QS.value()/50),97*(self.QS.value()/50))
        self.eyemian2.image.resize(10*(self.QS.value()/50),10*(self.QS.value()/50))
        self.eyemian2.movie.setScaledSize(QSize(10*(self.QS.value()/50), 10*(self.QS.value()/50)))
        self.eyemian2.image.move(168*(self.QS.value()/50),97*(self.QS.value()/50))
        self.help_music.image.resize(50*(self.QS.value()/50),50*(self.QS.value()/50))
        self.help_music.movie.setScaledSize(QSize(50*(self.QS.value()/50),50*(self.QS.value()/50)))
        self.help_music.image.move(260*(self.QS.value()/50),10*(self.QS.value()/50))
        self.time_show.resize(150*(self.QS.value()/50),50*(self.QS.value()/50))
        self.time_show.move(245*(self.QS.value()/50),60*(self.QS.value()/50))
        self.time_show.setStyleSheet("font-size:"+str(int(20*(self.QS.value()/50)))+"px;")
        if self.timeshowing:
            self.longtime_show.resize(500,50*(self.QS.value()/50))
        else:
            self.longtime_show.resize(500,0)
        self.longtime_show.setStyleSheet("font-size:"+str(int(20*(self.QS.value()/50)))+"px;")
        if self.cpuramshowing:
            self.longcpuram.resize(300*(self.QS.value()/50),50*(self.QS.value()/50))
        else:
            self.longcpuram.resize(300*(self.QS.value()/50),0)
        self.longcpuram.setStyleSheet("font-size:"+str(int(20*(self.QS.value()/50)))+"px;")
        self.mouth.movie.jumpToNextFrame()
        self.eye1.movie.jumpToNextFrame()
        self.eye2.movie.jumpToNextFrame()
        self.play_check.play()
        self.cpua.image.resize(25*(self.QS.value()/50),65*(self.QS.value()/50))
        self.cpua.movie.setScaledSize(QSize(25*(self.QS.value()/50),65*(self.QS.value()/50)))
        self.cpua.image.move(260*(self.QS.value()/50),120*(self.QS.value()/50))
        self.rama.image.resize(25*(self.QS.value()/50),65*(self.QS.value()/50))
        self.rama.movie.setScaledSize(QSize(25*(self.QS.value()/50),65*(self.QS.value()/50)))
        self.rama.image.move(290*(self.QS.value()/50),120*(self.QS.value()/50))
        if not self.will_exit:
            self.cpub.image.resize(15*(self.QS.value()/50),((65*(self.cpupart/100)-5)*(self.QS.value()/50)))
            self.cpub.image.move(self.cpua.image.pos().x()+(7*(self.QS.value()/50)),(self.cpua.image.pos().y()+65*(1-self.cpupart/100)*(self.QS.value()/50)))
            self.ramb.image.resize(15*(self.QS.value()/50),((65*(self.rampart/100)-5)*(self.QS.value()/50)))
            self.ramb.image.move(self.rama.image.pos().x()+(7*(self.QS.value()/50)),(self.rama.image.pos().y()+65*(1-self.rampart/100)*(self.QS.value()/50)))
        self.moret.image.resize(50*(self.QS.value()/50),50*(self.QS.value()/50))
        self.moret.movie.setScaledSize(QSize(50*(self.QS.value()/50),50*(self.QS.value()/50)))
        self.moret.image.move(260*(self.QS.value()/50),200*(self.QS.value()/50))
    def timerEvent(self,q):
        datetime = QDateTime.currentDateTime()
        system_time=QTime.currentTime()
        self.time_show.setText(system_time.toString(Qt.ISODate))
        self.longtime_show.setText(datetime.toString())
        self.QS.move(self.x(),self.y()-30)
        if not((95+(self.mouse.pos().x()-self.pos().x()-self.eyemian1.image.pos().x())/220)>5 and (95+(self.mouse.pos().x()-self.pos().x()-self.eyemian1.image.pos().x())/220)<-5):
            self.eyemian1.image.move((95+(self.mouse.pos().x()-self.pos().x()-self.eyemian1.image.pos().x())/220)*(self.QS.value()/50),(97+(self.mouse.pos().y()-self.pos().y()-self.eyemian1.image.pos().y())/330)*(self.QS.value()/50))
        else:
            if (95+(self.mouse.pos().x()-self.pos().x()-self.eyemian1.image.pos().x())/220)>5:
                self.eyemian1.image.move((100*(self.QS.value()/50),(97+(self.mouse.pos().y()-self.pos().y()-self.eyemian1.image.pos().y())/330)*(self.QS.value()/50)))
            if (95+(self.mouse.pos().x()-self.pos().x()-self.eyemian1.image.pos().x())/220)<-5:
                self.eyemian1.image.move((90*(self.QS.value()/50),(97+(self.mouse.pos().y()-self.pos().y()-self.eyemian1.image.pos().y())/330)*(self.QS.value()/50)))
        if not((168+(self.mouse.pos().x()-self.pos().x()-self.eyemian2.image.pos().x())/220)>5 and (168+(self.mouse.pos().x()-self.pos().x()-self.eyemian2.image.pos().x())/220)<-5):
            self.eyemian2.image.move((168+(self.mouse.pos().x()-self.pos().x()-self.eyemian2.image.pos().x())/220)*(self.QS.value()/50),(97+(self.mouse.pos().y()-self.pos().y()-self.eyemian2.image.pos().y())/330)*(self.QS.value()/50))
        else:
            if (168+(self.mouse.pos().x()-self.pos().x()-self.eyemian2.image.pos().x())/220)>5:
                self.eyemian2.image.move((173+(self.mouse.pos().x()-self.pos().x()-self.eyemian2.image.pos().x())/220)*(self.QS.value()/50),(97+(self.mouse.pos().y()-self.pos().y()-self.eyemian2.image.pos().y())/330)*(self.QS.value()/50))
            if (168+(self.mouse.pos().x()-self.pos().x()-self.eyemian2.image.pos().x())/220)<-5:
                self.eyemian2.image.move((163+(self.mouse.pos().x()-self.pos().x()-self.eyemian2.image.pos().x())/220)*(self.QS.value()/50),(97+(self.mouse.pos().y()-self.pos().y()-self.eyemian2.image.pos().y())/330)*(self.QS.value()/50))
        if self.rm_f_run and self.qarm_f==False:
            if self.rm_f.files.toPlainText()!='':
                self.qarm_f=True
                self.rm_qa()
        if self.game_run:
            if self.gamemain.ao.pos().y()<QApplication.desktop().height():
                self.gamemain.ao.move(self.gamemain.ao.pos().x(),self.gamemain.ao.pos().y()+1+int(self.speed1*0.25))
            else:
                self.gamemain.ao.move(100,0)
                self.ao_text=self.filelist2[random.randint(0,len(self.filelist2)-1)]
                self.gamemain.ao.text.setText(self.ao_text)
            if self.gamemain.bo.pos().y()<QApplication.desktop().height():
                self.gamemain.bo.move(self.gamemain.bo.pos().x(),self.gamemain.bo.pos().y()+1+int(self.speed1*0.25))
            else:
                self.gamemain.bo.move(250,0)
                self.bo_text=self.filelist2[random.randint(0,len(self.filelist2)-1)]
                self.gamemain.bo.text.setText(self.bo_text)
            if self.gamemain.co.pos().y()<QApplication.desktop().height():
                self.gamemain.co.move(self.gamemain.co.pos().x(),self.gamemain.co.pos().y()+1+int(self.speed1*0.25))
            else:
                self.gamemain.co.move(400,0)
                self.co_text=self.filelist2[random.randint(0,len(self.filelist2)-1)]
                self.gamemain.co.text.setText(self.co_text)
            if self.gamemain.do.pos().y()<QApplication.desktop().height():
                self.gamemain.do.move(self.gamemain.do.pos().x(),self.gamemain.do.pos().y()+1+int(self.speed1*0.25))
            else:
                self.gamemain.do.move(550,0)
                self.do_text=self.filelist2[random.randint(0,len(self.filelist2)-1)]
                self.gamemain.do.text.setText(self.do_text)
    def music_help(self):
        self.help_music = QLabel(self)
        self.help_music.image = QLabel(self)
        self.help_music.movie = QMovie("files/image/musicstop.gif")
        self.help_music.image.setMovie(self.help_music.movie)
        self.help_music.image.resize(50,50)
        self.help_music.movie.setScaledSize(QSize(50,50))
        self.help_music.image.move(260,10)
        self.help_music.movie.start()
        self.help_music.gif=0
    def do_mediaplayer_statechanged(self, state):
        if state == QtMultimedia.QMediaPlayer.StoppedState:
            self.help_music.movie = QMovie("files/image/musicstop.gif")
            self.help_music.gif=0
            self.help_music.image.setMovie(self.help_music.movie)
            self.help_music.image.resize(50*(self.QS.value()/50),50*(self.QS.value()/50))
            self.help_music.movie.setScaledSize(QSize(50*(self.QS.value()/50),50*(self.QS.value()/50)))
            self.help_music.image.move(260*(self.QS.value()/50),10*(self.QS.value()/50))
            self.help_music.image.repaint()
            self.help_music.repaint()
            self.help_music.movie.start()
    def cpuram(self):
        self.cpub=QLabel(self)
        self.cpua=QLabel(self)
        self.ramb=QLabel(self)
        self.rama=QLabel(self)
        self.cpua.image = QLabel(self)
        self.cpub.image = QLabel(self)
        self.rama.image = QLabel(self)
        self.ramb.image = QLabel(self)
        self.cpua.movie = QMovie("files/image/cpu.gif")
        self.cpub.movie = QMovie("files/image/cpuramh.gif")
        self.rama.movie = QMovie("files/image/ram.gif")
        self.ramb.movie = QMovie("files/image/cpuramh.gif")
        self.cpua.image.setMovie(self.cpua.movie)
        self.cpub.image.setMovie(self.cpub.movie)
        self.rama.image.setMovie(self.rama.movie)
        self.ramb.image.setMovie(self.ramb.movie)
        self.cpua.image.resize(25,65)
        self.cpub.image.resize(15,65)
        self.rama.image.resize(25,65)
        self.ramb.image.resize(25,65)
        self.cpua.movie.setScaledSize(QSize(25,65))
        self.rama.movie.setScaledSize(QSize(25,65))
        self.cpua.image.move(260,120)
        self.cpub.image.move(260,120)
        self.rama.image.move(290,120)
        self.ramb.image.move(290,120)
        self.cpua.movie.start()
        self.cpub.movie.start()
        self.rama.movie.start()
        self.ramb.movie.start()
    def cpuramrun(self):
        self.cpupart=psutil.cpu_percent()
        self.rampart=psutil.virtual_memory().percent
        self.longcpuram.setText('CPU:'+str(self.cpupart)+'%'+' '+'RAM:'+str(self.rampart)+'%')
        if self.will_exit:
            self.cpub.image.resize(0,0)
            self.ramb.image.resize(0,0)
        else:
            self.cpub.image.resize(15*(self.QS.value()/50),((65*(self.cpupart/100)-5)*(self.QS.value()/50)))
            self.cpub.image.move(self.cpua.image.pos().x()+(7*(self.QS.value()/50)),(self.cpua.image.pos().y()+65*(1-self.cpupart/100)*(self.QS.value()/50)))
            self.ramb.image.resize(15*(self.QS.value()/50),((65*(self.rampart/100)-5)*(self.QS.value()/50)))
            self.ramb.image.move(self.rama.image.pos().x()+(7*(self.QS.value()/50)),(self.rama.image.pos().y()+65*(1-self.rampart/100)*(self.QS.value()/50)))
        self.cputime = QTimer()
        self.cputime.timeout.connect(self.cpuramrun)
        self.cputime.start(1000)
    def morething(self):
        self.moret=QLabel(self)
        self.moret.image=QLabel(self)
        self.moret.movie=QMovie("files/image/more.gif")
        self.moret.image.setMovie(self.moret.movie)
        self.moret.image.resize(50,50)
        self.moret.movie.setScaledSize(QSize(50,50))
        self.moret.image.move(260,200)
        self.moret.movie.start()
    def about(self):
        self.about=QWidget()
        self.about.showMinimized()
        self.about.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.about.setWindowTitle('关于 deepin desktop helper')
        self.about.setWindowIcon(QIcon('files/image/blush.gif'))
        self.about.setFixedSize(550,200)
        self.about.text1=QLabel(self.about)
        self.about.text1.setStyleSheet("font-size:20px;")
        self.about.text1.setText("deepin-desktop-helper\n"+"开发系统:deepin20.8\n"+"项目地址:")
        self.about.text2=QLabel(self.about)
        self.about.text2.setStyleSheet("font-size:15px;")
        self.about.text2.move(0,100)
        self.about.text2.setText("github:https://github.com/3084793958/deepin-desktop-helper.git\n"+"githubfast:https://githubfast.com/3084793958/deepin-desktop-helper.git\n"+"gitlab:https://gitlab.com/3084793958/deepin-desktop-helper.git")
        self.about.show()
    def show_about(self):
        self.play_check.play()
        self.about.showNormal()
        self.about.activateWindow()
    def morelist(self):
        self.m_list=QWidget()
        self.m_list.showMinimized()
        self.m_list.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.m_list.setWindowTitle('插件列表')
        self.m_list.setWindowIcon(QIcon('files/image/blush.gif'))
        self.m_list.setFixedSize(300,550)
        self.m_list.doing=False
        self.m_list.b_1=QPushButton(self.m_list)
        self.m_list.b_1.setText('结束进程')
        self.m_list.b_1.setStyleSheet("font-size:30px")
        self.m_list.b_1.clicked.connect(self.killall)
        self.m_list.b_2=QPushButton(self.m_list)
        self.m_list.b_2.setText('中译英')
        self.m_list.b_2.setStyleSheet("font-size:30px")
        self.m_list.b_2.clicked.connect(self.cn_to_en)
        self.m_list.b_2.move(0,55)
        self.m_list.b_3=QPushButton(self.m_list)
        self.m_list.b_3.setText('英译中')
        self.m_list.b_3.setStyleSheet("font-size:30px")
        self.m_list.b_3.clicked.connect(self.en_to_cn)
        self.m_list.b_3.move(0,110)
        self.m_list.showthing=QTextEdit(self.m_list)
        self.m_list.showthing.move(0,400)
        self.m_list.showthing.setStyleSheet("font-size:18px")
        self.m_list.showthing.resize(300,150)
        self.m_list.showthing.show()
        self.url = 'http://fanyi.youdao.com/translate'
        self.m_list.b_4=QPushButton(self.m_list)
        self.m_list.b_4.setText('强制删除文件/文件夹')
        self.m_list.b_4.setStyleSheet("font-size:30px")
        self.m_list.b_4.clicked.connect(self.rm)
        self.m_list.b_4.move(0,165)
        self.m_list.b_5=QPushButton(self.m_list)
        self.m_list.b_5.setText('安装/卸载')
        self.m_list.b_5.setStyleSheet("font-size:30px")
        self.m_list.b_5.clicked.connect(self.installun)
        self.m_list.b_5.move(0,220)
        self.m_list.b_6=QPushButton(self.m_list)
        self.m_list.b_6.setText('GAME')
        self.m_list.b_6.setStyleSheet("font-size:30px")
        self.m_list.b_6.clicked.connect(self.gamestart)
        self.m_list.b_6.move(0,275)
        self.m_list.show()
    def show_m_list(self):
        self.play_check.play()
        if self.m_list.isActiveWindow()==False and self.m_list.doing==False:
            self.m_list.activateWindow()
            self.m_list.doing=True
        if self.m_list.isActiveWindow()==True and self.m_list.doing==False:
            self.m_list.doing=True
            self.m_list.showMinimized()
    def killall(self):
        self.play_check.play()
        name, n=QInputDialog.getText(self.m_list, '输入进程名(en)', '进程名')
        os.system('killall '+name)
    def cn_to_en(self):
        self.play_check.play()
        text, t=QInputDialog.getText(self.m_list, '输入翻译内容(中译英)', '翻译内容')
        if str(text) != '':
            Form_Date = {}
            Form_Date['i'] = text  
            Form_Date['doctype'] = 'json'
            Form_Date['form'] = 'zh-cn'
            Form_Date['to'] = 'en'
            Form_Date['smartresult'] = 'dict'
            Form_Date['client'] = 'fanyideskweb'
            Form_Date['salt'] = '1526995097962'
            Form_Date['sign'] = '8e4c4765b52229e1f3ad2e633af89c76'
            Form_Date['version'] = '2.1'
            Form_Date['keyform'] = 'fanyi.web'
            Form_Date['action'] = 'FY_BY_REALTIME'
            Form_Date['typoResult'] = 'false'
            data = parse.urlencode(Form_Date).encode('utf-8')
            response = request.urlopen(self.url, data)
            html = response.read().decode('utf-8')
            translate_results = json.loads(html)
            translate_results = translate_results['translateResult'][0][0]['tgt']
            self.m_list.showthing.setText('中译英内容:\n'+translate_results)
    def en_to_cn(self):
        self.play_check.play()
        text, t=QInputDialog.getText(self.m_list, '输入翻译内容(英译中)', '翻译内容')
        if str(text) != '':
            Form_Date = {}
            Form_Date['i'] = text  
            Form_Date['doctype'] = 'json'
            Form_Date['form'] = 'en'
            Form_Date['to'] = 'zh-cn'
            Form_Date['smartresult'] = 'dict'
            Form_Date['client'] = 'fanyideskweb'
            Form_Date['salt'] = '1526995097962'
            Form_Date['sign'] = '8e4c4765b52229e1f3ad2e633af89c76'
            Form_Date['version'] = '2.1'
            Form_Date['keyform'] = 'fanyi.web'
            Form_Date['action'] = 'FY_BY_REALTIME'
            Form_Date['typoResult'] = 'false'
            data = parse.urlencode(Form_Date).encode('utf-8')
            response = request.urlopen(self.url, data)
            html = response.read().decode('utf-8')
            translate_results = json.loads(html)
            translate_results = translate_results['translateResult'][0][0]['tgt']
            self.m_list.showthing.setText('英译中内容:\n'+translate_results)
    def rm(self):
        self.rm_f_run=True
        self.play_check.play()
        self.rm_f=QWidget()
        self.rm_f.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.rm_f.setWindowTitle('删除文件/文件夹')
        self.rm_f.setWindowIcon(QIcon('files/image/blush.gif'))
        self.rm_f.setFixedSize(300,225)
        self.rm_f.files=QTextEdit(self.rm_f)
        self.rm_f.files.resize(300,150)
        self.rm_f.files.move(0,75)
        self.rm_f.files_text=QLabel(self.rm_f)
        self.rm_f.files_text.setText('请将要强制删除的文件/文件夹\n拖入下方的文本框中')
        self.rm_f.files_text.setStyleSheet("font-size:20px")
        self.rm_f.files.setStyleSheet("font-size:18px")
        self.rm_f.show()
    def rm_qa(self):
        choose1=['否','是']
        qa, q=QInputDialog.getItem(self.rm_f, '删除未遂', '是否删除',choose1)
        if qa=='是':
            self.m_list.showthing.setText('删除既遂')
            os.system('rm -rf '+'"'+self.rm_f.files.toPlainText().replace('file:///', '/').strip()+'"')
        else:
            self.m_list.showthing.setText('删除终止')
        self.rm_f.files.setText('')
        self.qarm_f=False
        self.rm_f.showMinimized()
    def installun(self):
        choose2=['None','安装','卸载']
        choose3=['None','安装deepin-wine6-stable(sudo)','安装ll-cli(sudo)','安装uengine(sudo)','安装apt软件(sudo)','安装ll-cli软件']
        choose4=['None','卸载deepin-wine6-stable(sudo)','卸载ll-cli(sudo)','卸载uengine(sudo)','卸载apt软件(sudo)','卸载ll-cli软件']
        qa1, q1=QInputDialog.getItem(self.m_list, '安装/卸载', '安装/卸载',choose2)
        if qa1=='安装':
            qa2, q2=QInputDialog.getItem(self.m_list, '选择', '选择方式',choose3)
            if qa2=='安装deepin-wine6-stable(sudo)':
                subprocess.Popen("pkexec apt-get update;pkexec apt install deepin-wine6-stable",shell=True)
            if qa2=='安装ll-cli(sudo)':
                subprocess.Popen("pkexec apt-get update;pkexec apt install erofs-utils liberofs-dev linglong-bin linglong-box linglong-builder linglong-dbus-proxy linglong-installer linglong-loader;pkexec apt --fix-broken install;pkexec apt install erofs-utils liberofs-dev linglong-bin linglong-box linglong-builder linglong-dbus-proxy linglong-installer linglong-loader;ll-cli repo modify https://mirror-repo-linglong.deepin.com/",shell=True)
            if qa2=='安装uengine(sudo)':
                subprocess.Popen("pkexec apt-get update;pkexec apt install uengine",shell=True)
            if qa2=='安装apt软件(sudo)':
                qa3, q3=QInputDialog.getText(self.m_list, '软件关键词(en)', '请输入要安装的软件关键词(en)')
                if qa3!='':
                    text_install=os.popen("apt list "+'*'+qa3+'*').read()
                    if text_install!='正在列表...\n':
                        self.qa2_h=qa2
                        self.qa2show()
                        self.qa2s.files.setText(text_install.replace('正在列表...\n', '').strip())
                    else:
                        self.m_list.showthing.setText('找不到软件包')
            if qa2=='安装ll-cli软件':
                qa3, q3=QInputDialog.getText(self.m_list, '软件关键词(en)', '请输入要安装的软件关键词(en)')
                if qa3!='':
                    text_install=os.popen('ll-cli query '+qa3).read()
                    if text_install!='app not found in repo\n':
                        self.qa2_h=qa2
                        self.qa2show()
                        self.qa2s.files.setText(text_install)
                    else:
                        self.m_list.showthing.setText('找不到玲珑软件包')
        if qa1=='卸载':
            qa2, q2=QInputDialog.getItem(self.m_list, '选择', '选择方式',choose4)
            if qa2=='卸载deepin-wine6-stable(sudo)':
                subprocess.Popen("pkexec apt remove deepin-wine6-stable",shell=True)
            if qa2=='卸载ll-cli(sudo)':
                subprocess.Popen("pkexec remove install erofs-utils liberofs-dev linglong-bin linglong-box linglong-builder linglong-dbus-proxy linglong-installer linglong-loader",shell=True)
            if qa2=='卸载uengine(sudo)':
                subprocess.Popen("pkexec apt remove uengine",shell=True)
            if qa2=='卸载apt软件(sudo)':
                qa3, q3=QInputDialog.getText(self.m_list, '软件关键词(en)', '请输入要卸载的软件关键词(en)')
                if qa3!='':
                    text_install=os.popen("apt list --installed "+'*'+qa3+'*').read()
                    if text_install!='正在列表...\n':
                        self.qa2_h=qa2
                        self.qa2show()
                        self.qa2s.files.setText(text_install.replace('正在列表...\n', '').strip())
                    else:
                        self.m_list.showthing.setText('找不到软件包')
            if qa2=='卸载ll-cli软件':
                text_install=os.popen('ll-cli list').read()
                self.qa2_h=qa2
                self.qa2show()
                self.qa2s.files.setText(text_install)
    def qa2show(self):
        self.qa2s_run=True
        self.qa2s=QWidget()
        self.qa2s.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.qa2s.setWindowTitle('选择软件')
        self.qa2s.setWindowIcon(QIcon('files/image/blush.gif'))
        self.qa2s.setFixedSize(300,225)
        self.qa2s.files=QTextEdit(self.qa2s)
        self.qa2s.files.resize(300,150)
        self.qa2s.files.move(0,75)
        self.qa2s.files_text=QLabel(self.qa2s)
        self.qa2s.files_text.setText('请选择软件后进行输入')
        self.qa2s.files_text.setStyleSheet("font-size:20px")
        self.qa2s.files.setStyleSheet("font-size:18px")
        self.qa2s.b_1=QPushButton(self.qa2s)
        self.qa2s.b_1.setText('进行输入')
        self.qa2s.b_1.setStyleSheet("font-size:20px")
        if self.qa2_h=='安装apt软件(sudo)':
            self.qa2s.b_1.clicked.connect(self.apt_install)
        if self.qa2_h=='安装ll-cli软件':
            self.qa2s.b_1.clicked.connect(self.ll_install)
        if self.qa2_h=='卸载apt软件(sudo)':
            self.qa2s.b_1.clicked.connect(self.apt_uninstall)
        if self.qa2_h=='卸载ll-cli软件':
            self.qa2s.b_1.clicked.connect(self.ll_uninstall)
        self.qa2s.b_1.move(0,25)
        self.qa2s.show()
    def apt_install(self):
        qa4, q4=QInputDialog.getText(self.qa2s, '软件包名', '输入软件包名')
        self.qa2s.showMinimized()
        subprocess.Popen("pkexec apt install "+qa4,shell=True)
        self.m_list.showthing.setText('')
    def ll_install(self):
        qa4, q4=QInputDialog.getText(self.qa2s, 'APPID', '输入APPID')
        self.qa2s.showMinimized()
        subprocess.Popen("ll-cli install "+qa4,shell=True)
        self.m_list.showthing.setText('')
    def apt_uninstall(self):
        qa4, q4=QInputDialog.getText(self.qa2s, '软件包名', '输入软件包名以卸载')
        self.qa2s.showMinimized()
        subprocess.Popen("pkexec apt remove "+qa4,shell=True)
        self.m_list.showthing.setText('')
    def ll_uninstall(self):
        qa4, q4=QInputDialog.getText(self.qa2s, 'APPID', '输入APPID以卸载')
        self.qa2s.showMinimized()
        subprocess.Popen("ll-cli uninstall "+qa4,shell=True)
        self.m_list.showthing.setText('')
    def gamestart(self):
        self.play_check.play()
        games1, gs1=QInputDialog.getText(self.m_list, '获取路径', '请输入或拖入路径')
        if os.path.exists(games1.replace('file:///', '/').replace('~', '/home/'+os.getlogin()).strip()) and ('root' in games1)==False:
            self.filelist=os.listdir(games1.replace('file:///', '/').replace('~', '/home/'+os.getlogin()).strip())
            if len(self.filelist)!=0:
                speed1, sp1=QInputDialog.getInt(self.m_list, '速度', '输入x(speed=(1+0.25x))and(-2<x<8)')
                self.games1=games1
                if speed1>-3 and speed1<9:
                    self.speed1=speed1
                    self.game()
                    self.m_list.showthing.setText('')
                else:
                    self.m_list.showthing.setText('速度错误')
            else:
                self.m_list.showthing.setText('此路径为空，用智慧填满它吧')
        else:
            self.m_list.showthing.setText('没有此路径或无权限')
    def game(self):
        self.game_run=True
        self.game_win=0
        self.gamemain=QWidget()
        self.gamemain.setWindowFlags(Qt.FramelessWindowHint|Qt.SubWindow)
        self.gamemain.setAutoFillBackground(False)
        self.gamemain.setAttribute(Qt.WA_TranslucentBackground, True)
        self.gamemain.setWindowTitle('deepin desktop helper game')
        self.gamemain.setWindowIcon(QIcon('files/image/blush.gif'))
        self.filelist2=self.filelist+os.listdir('/var/lib')
        desktop=QApplication.desktop()
        self.gamemain.resize(desktop.width()/2,desktop.height())
        self.gamemain.b_1=QPushButton(self.gamemain)
        self.gamemain.b_1.setText('关闭')
        self.gamemain.b_1.setStyleSheet("font-size:30px")
        self.gamemain.b_1.clicked.connect(self.exitgame)
        self.gamemain.b_2=QPushButton(self.gamemain)
        self.gamemain.b_2.setText('正确次数:0')
        self.gamemain.b_2.setStyleSheet("font-size:30px")
        self.gamemain.repaint()
        self.gamemain.movie = QMovie("files/image/behind.gif")
        self.gamemain.ao = QLabel(self.gamemain)
        self.gamemain.ao.setMovie(self.gamemain.movie)
        self.gamemain.bo = QLabel(self.gamemain)
        self.gamemain.bo.setMovie(self.gamemain.movie)
        self.gamemain.co = QLabel(self.gamemain)
        self.gamemain.co.setMovie(self.gamemain.movie)
        self.gamemain.do = QLabel(self.gamemain)
        self.gamemain.do.setMovie(self.gamemain.movie)
        self.gamemain.ao.text=QPushButton(self.gamemain.ao)
        self.gamemain.ao.text.resize(80,80)
        self.ao_text=self.filelist2[random.randint(0,len(self.filelist2)-1)]
        self.gamemain.ao.text.setText(self.ao_text)
        self.gamemain.ao.text.setStyleSheet("font-size:20px")
        self.gamemain.ao.text.move(30,30)
        self.gamemain.ao.text.clicked.connect(self.button_1)
        self.gamemain.bo.text=QPushButton(self.gamemain.bo)
        self.gamemain.bo.text.resize(80,80)
        self.bo_text=self.filelist2[random.randint(0,len(self.filelist2)-1)]
        self.gamemain.bo.text.setText(self.bo_text)
        self.gamemain.bo.text.setStyleSheet("font-size:20px")
        self.gamemain.bo.text.move(30,30)
        self.gamemain.bo.text.clicked.connect(self.button_2)
        self.gamemain.co.text=QPushButton(self.gamemain.co)
        self.gamemain.co.text.resize(80,80)
        self.co_text=self.filelist2[random.randint(0,len(self.filelist2)-1)]
        self.gamemain.co.text.setText(self.co_text)
        self.gamemain.co.text.setStyleSheet("font-size:20px")
        self.gamemain.co.text.move(30,30)
        self.gamemain.co.text.clicked.connect(self.button_3)
        self.gamemain.do.text=QPushButton(self.gamemain.do)
        self.gamemain.do.text.resize(80,80)
        self.do_text=self.filelist2[random.randint(0,len(self.filelist2)-1)]
        self.gamemain.do.text.setText(self.do_text)
        self.gamemain.do.text.setStyleSheet("font-size:20px")
        self.gamemain.do.text.move(30,30)
        self.gamemain.do.text.clicked.connect(self.button_4)
        self.gamemain.move(0,0)
        self.gamemain.b_1.move(0,0)
        self.gamemain.b_2.move(0,100)
        self.gamemain.ao.move(100,0)
        self.gamemain.bo.move(250,-50)
        self.gamemain.co.move(400,-25)
        self.gamemain.do.move(550,-75)
        self.gamemain.movie.setScaledSize(QSize(150,150))
        self.gamemain.movie.start()
        self.gamemain.repaint()
        self.gamemain.show()
    def exitgame(self):
        self.game_run=False
        self.gamemain.close()
    def button_1(self):
        if self.ao_text in self.filelist:
            self.game_win+=1
            self.gamemain.b_2.setText('正确次数'+str(self.game_win))
            self.play_t.play()
        else:
            self.play_f.play()
        self.gamemain.ao.move(100,QApplication.desktop().height()+10)
    def button_2(self):
        if self.bo_text in self.filelist:
            self.game_win+=1
            self.gamemain.b_2.setText('正确次数'+str(self.game_win))
            self.play_t.play()
        else:
            self.play_f.play()
        self.gamemain.bo.move(100,QApplication.desktop().height()+10)
    def button_3(self):
        if self.co_text in self.filelist:
            self.game_win+=1
            self.gamemain.b_2.setText('正确次数'+str(self.game_win))
            self.play_t.play()
        else:
            self.play_f.play()
        self.gamemain.co.move(100,QApplication.desktop().height()+10)
    def button_4(self):
        if self.do_text in self.filelist:
            self.game_win+=1
            self.gamemain.b_2.setText('正确次数'+str(self.game_win))
            self.play_t.play()
        else:
            self.play_f.play()
        self.gamemain.do.move(100,QApplication.desktop().height()+10)
if __name__=='__main__':
    app = QApplication(sys.argv)
    desktop_helper = DDH()
    desktop_helper.show()
    sys.exit(app.exec_())