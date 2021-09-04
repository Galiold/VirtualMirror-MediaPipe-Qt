import sys
import cv2
from PyQt5.QtCore import Qt, QSize, QTimer, QThread
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap, QImage

def main():    
    app = QApplication([])
    
    window = QWidget()
    window.setLayout(QGridLayout(window))    
    window.setMinimumSize(QSize(640, 480))

    label = QLabel()
    label.setFixedSize(640, 640)    
    window.layout().addWidget(label, 0, 0)

    window.show()

    vc = cv2.VideoCapture(3)
    vc.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    timer = QTimer()
    timer.timeout.connect(lambda: nextFrameSlot(vc, label))
    timer.start(1000. / 10)

    return app.exit(app.exec_())

def nextFrameSlot(vc: cv2.VideoCapture, label: QLabel):
    rval, frame = vc.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(image)
    label.setPixmap(pixmap)
    
if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)