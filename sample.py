import urllib2
from PyQt4 import QtGui
import json
import sys
import thread
from PyQt4.QtGui import QMessageBox
from IpGeoLocater import Ui_MainWindow


class Myform(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.url = "http://www.freegeoip.net/json/"
        # self.ui.ipaddress.setFocus()
        # self.ui.ipaddress.setPlaceholderText("Hostname")
        self.ui.progressBar.hide()
        self.ui.GetIpAddress.clicked.connect(self.OnIpClicked)
        self.ui.findme.clicked.connect(self.findme)

    # {"ip":"216.58.219.238","country_code":"US","country_name":"United States","region_code":"CA","region_name":"California","city":"Mountain View","zip_code":"94043","time_zone":"America/Los_Angeles","latitude":37.4192,"longitude":-122.0574,"metro_code":807}

    def StartProgressBar(self,ip,delay2):
        try:
            response = urllib2.urlopen(ip)
            # print response.read()
            j = json.loads(response.read())
            # print j["ip"]
            self.ui.city_edit.setText(j["city"])
            self.ui.ip_addr_edit.setText(j["ip"])
            self.ui.country_code_edit.setText(j["country_code"])
            self.ui.country_name_edit.setText(j["country_name"])
            self.ui.zip_code_edit.setText(j["zip_code"])
            self.ui.time_zone_edit.setText(j["time_zone"])
            self.ui.latitude_edit.setText(str(j["latitude"]))
            self.ui.longitude_edit.setText(str(j["longitude"]))
            self.ui.Region_code_edit.setText(str(j["region_code"]))
            self.ui.Region_name_edit.setText(str(j["region_name"]))
            self.ui.metro_code_edit.setText(str(j["metro_code"]))
            self.ui.progressBar.hide()

        except:
            print "There was some error"
            self.ui.progressBar.hide()
            # self.showmsg()


    def OnIpClicked(self):
        thread.start_new_thread(self.StartProgressBar, (self.url + str(self.ui.ipaddress.text()),2))
        self.ui.progressBar.setRange(0,0)
        self.ui.progressBar.show()

    def showmsg(self):
        QMessageBox.warning(self.centralWidget(), "Message", "There was some error")

    def findme(self):
        ip = urllib2.urlopen("https://api.ipify.org")
        self.ui.ipaddress.setText(ip.read())

if __name__ == "__main__":
    # getIpInfo()
    app = QtGui.QApplication(sys.argv)
    myform = Myform()
    myform.show()
    sys.exit(app.exec_())

# import sys
# from PyQt4.QtGui import *
#
# def window():
#     app = QApplication(sys.argv)
#     w = QWidget()
#     b = QPushButton(w)
#     b.setText("Show message!")
#
#     b.move(50, 50)
#     b.clicked.connect(showdialog)
#     w.setWindowTitle("PyQt Dialog demo")
#     w.show()
#     sys.exit(app.exec_())
#
#
# def showdialog():
#     msg = QMessageBox()
#     msg.setIcon(QMessageBox.Information)
#
#     msg.setText("This is a message box")
#     msg.setInformativeText("This is additional information")
#     msg.setWindowTitle("MessageBox demo")
#     msg.setDetailedText("The details are as follows:")
#     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#     msg.buttonClicked.connect(msgbtn)
#
#     retval = msg.exec_()
#     print "value of pressed message box button:", retval
#
#
# def msgbtn(i):
#     print "Button pressed is:", i.text()
#
#
# if __name__ == '__main__':
#     window()
