from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Діалог відкриття файлів (і папок)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)


app = QApplication([])
win = QWidget()       
win.resize(700, 500) 
win.setWindowTitle('Easy Editor')
lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()


btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Дзеркало")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")


row = QHBoxLayout()          # Основний рядок
col1 = QVBoxLayout()         # ділиться на два стовпці
col2 = QVBoxLayout()


col1.addWidget(btn_dir)      # у першому – кнопка вибору директорії
col1.addWidget(lw_files)     # та список файлів
col2.addWidget(lb_image, 95) # у другому - картинка
row_tools = QHBoxLayout()    # та рядок кнопок
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)


row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)


win.show()
app.exec()

