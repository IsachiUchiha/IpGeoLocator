# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IpGeoLocater.ui'
#
# Created: Sun Mar 13 00:23:24 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(474, 447)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ipaddress = QtGui.QLineEdit(self.centralwidget)
        self.ipaddress.setGeometry(QtCore.QRect(10, 10, 181, 27))
        self.ipaddress.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ipaddress.setObjectName(_fromUtf8("ipaddress"))
        self.GetIpAddress = QtGui.QPushButton(self.centralwidget)
        self.GetIpAddress.setGeometry(QtCore.QRect(310, 10, 91, 27))
        self.GetIpAddress.setObjectName(_fromUtf8("GetIpAddress"))
        self.ipaddr = QtGui.QLabel(self.centralwidget)
        self.ipaddr.setGeometry(QtCore.QRect(20, 70, 81, 17))
        self.ipaddr.setObjectName(_fromUtf8("ipaddr"))
        self.country_code = QtGui.QLabel(self.centralwidget)
        self.country_code.setGeometry(QtCore.QRect(20, 100, 101, 17))
        self.country_code.setObjectName(_fromUtf8("country_code"))
        self.country_name = QtGui.QLabel(self.centralwidget)
        self.country_name.setGeometry(QtCore.QRect(20, 130, 111, 17))
        self.country_name.setObjectName(_fromUtf8("country_name"))
        self.Region_name = QtGui.QLabel(self.centralwidget)
        self.Region_name.setGeometry(QtCore.QRect(20, 190, 91, 17))
        self.Region_name.setObjectName(_fromUtf8("Region_name"))
        self.City = QtGui.QLabel(self.centralwidget)
        self.City.setGeometry(QtCore.QRect(20, 220, 66, 17))
        self.City.setObjectName(_fromUtf8("City"))
        self.Region_code = QtGui.QLabel(self.centralwidget)
        self.Region_code.setGeometry(QtCore.QRect(20, 160, 91, 17))
        self.Region_code.setObjectName(_fromUtf8("Region_code"))
        self.zipcode = QtGui.QLabel(self.centralwidget)
        self.zipcode.setGeometry(QtCore.QRect(20, 250, 66, 17))
        self.zipcode.setObjectName(_fromUtf8("zipcode"))
        self.timezone = QtGui.QLabel(self.centralwidget)
        self.timezone.setGeometry(QtCore.QRect(20, 280, 66, 17))
        self.timezone.setObjectName(_fromUtf8("timezone"))
        self.latitude = QtGui.QLabel(self.centralwidget)
        self.latitude.setGeometry(QtCore.QRect(20, 310, 66, 17))
        self.latitude.setObjectName(_fromUtf8("latitude"))
        self.longitude = QtGui.QLabel(self.centralwidget)
        self.longitude.setGeometry(QtCore.QRect(20, 340, 71, 17))
        self.longitude.setObjectName(_fromUtf8("longitude"))
        self.metro_code = QtGui.QLabel(self.centralwidget)
        self.metro_code.setGeometry(QtCore.QRect(20, 370, 101, 17))
        self.metro_code.setObjectName(_fromUtf8("metro_code"))
        self.ip_addr_edit = QtGui.QLineEdit(self.centralwidget)
        self.ip_addr_edit.setGeometry(QtCore.QRect(210, 60, 221, 27))
        self.ip_addr_edit.setObjectName(_fromUtf8("ip_addr_edit"))
        self.country_code_edit = QtGui.QLineEdit(self.centralwidget)
        self.country_code_edit.setGeometry(QtCore.QRect(210, 90, 221, 27))
        self.country_code_edit.setObjectName(_fromUtf8("country_code_edit"))
        self.country_name_edit = QtGui.QLineEdit(self.centralwidget)
        self.country_name_edit.setGeometry(QtCore.QRect(210, 120, 221, 27))
        self.country_name_edit.setObjectName(_fromUtf8("country_name_edit"))
        self.Region_code_edit = QtGui.QLineEdit(self.centralwidget)
        self.Region_code_edit.setGeometry(QtCore.QRect(210, 150, 221, 27))
        self.Region_code_edit.setObjectName(_fromUtf8("Region_code_edit"))
        self.Region_name_edit = QtGui.QLineEdit(self.centralwidget)
        self.Region_name_edit.setGeometry(QtCore.QRect(210, 180, 221, 27))
        self.Region_name_edit.setObjectName(_fromUtf8("Region_name_edit"))
        self.city_edit = QtGui.QLineEdit(self.centralwidget)
        self.city_edit.setGeometry(QtCore.QRect(210, 210, 221, 27))
        self.city_edit.setObjectName(_fromUtf8("city_edit"))
        self.zip_code_edit = QtGui.QLineEdit(self.centralwidget)
        self.zip_code_edit.setGeometry(QtCore.QRect(210, 240, 221, 27))
        self.zip_code_edit.setObjectName(_fromUtf8("zip_code_edit"))
        self.time_zone_edit = QtGui.QLineEdit(self.centralwidget)
        self.time_zone_edit.setGeometry(QtCore.QRect(210, 270, 221, 27))
        self.time_zone_edit.setObjectName(_fromUtf8("time_zone_edit"))
        self.latitude_edit = QtGui.QLineEdit(self.centralwidget)
        self.latitude_edit.setGeometry(QtCore.QRect(210, 300, 221, 27))
        self.latitude_edit.setObjectName(_fromUtf8("latitude_edit"))
        self.longitude_edit = QtGui.QLineEdit(self.centralwidget)
        self.longitude_edit.setGeometry(QtCore.QRect(210, 330, 221, 27))
        self.longitude_edit.setObjectName(_fromUtf8("longitude_edit"))
        self.metro_code_edit = QtGui.QLineEdit(self.centralwidget)
        self.metro_code_edit.setGeometry(QtCore.QRect(210, 360, 221, 27))
        self.metro_code_edit.setObjectName(_fromUtf8("metro_code_edit"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(410, 10, 41, 23))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.findme = QtGui.QPushButton(self.centralwidget)
        self.findme.setGeometry(QtCore.QRect(200, 10, 101, 27))
        self.findme.setObjectName(_fromUtf8("findme"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 474, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "IpGeoLocator", None))
        self.GetIpAddress.setText(_translate("MainWindow", "Get Ip Info", None))
        self.ipaddr.setText(_translate("MainWindow", "Ip address", None))
        self.country_code.setText(_translate("MainWindow", "Country Code", None))
        self.country_name.setText(_translate("MainWindow", "Country Name", None))
        self.Region_name.setText(_translate("MainWindow", "Region Name", None))
        self.City.setText(_translate("MainWindow", "City", None))
        self.Region_code.setText(_translate("MainWindow", "Region Code", None))
        self.zipcode.setText(_translate("MainWindow", "Zipcode", None))
        self.timezone.setText(_translate("MainWindow", "TimeZone", None))
        self.latitude.setText(_translate("MainWindow", "Latitude", None))
        self.longitude.setText(_translate("MainWindow", "Longitude", None))
        self.metro_code.setText(_translate("MainWindow", "Metro Code", None))
        self.findme.setText(_translate("MainWindow", "Find Me", None))
