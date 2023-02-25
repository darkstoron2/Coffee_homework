import sqlite3
import sys

from UI.main1 import Ui_MainWindow
from UI.addEditCoffeeForm import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.change)
        self.loadTable()

    def change(self):
        item = self.comboBox.currentText()
        self.form = Form(item, self)
        self.form.show()
        self.loadTable()

    def loadTable(self):
        c = sqlite3.connect(f'data\\coffee.db')
        rows = c.execute(f"SELECT * from types_of_coffee").fetchall()
        self.comboBox.clear()
        items = [i[1] for i in rows]
        items.append("добавить новый")
        self.comboBox.addItems(items)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["id", "name", "roasting", "ground_grains", "taste", "price",
                                                    "packing_volume"])
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(rows):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


class Form(QWidget, Ui_Form):
    def __init__(self, item, widget):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.pushButton.clicked.connect(self.update_table)
        self.comboBoxRoasting.addItems([str(i) for i in range(1, 6)])
        self.comboBoxGG.addItems(["ground", "grains"])
        self.item = item
        if self.item != "добавить новый":
            c = sqlite3.connect(f'data\\coffee.db')
            rows = c.execute(f'SELECT * from types_of_coffee where name == "{self.item}"').fetchall()
            _, name, roasting, gg, taste, price, volume = rows[0]
            self.lineName.setText(name)
            self.lineTaste.setText(taste)
            self.linePrice.setText(str(price))
            self.lineVolume.setText(volume)
            self.comboBoxRoasting.setCurrentIndex(roasting - 1)
            self.comboBoxGG.setCurrentIndex(["ground", "grains"].index(gg))

    def update_table(self):
        if self.item == "добавить новый":
            self.create_new()
        else:
            self.change_exist()
        self.widget.loadTable()
        self.close()

    def create_new(self):
        c = sqlite3.connect(f'data\\coffee.db')
        rows = c.execute(f'SELECT * from types_of_coffee').fetchall()
        idd = len(rows) + 1
        name = self.lineName.text().strip()
        taste = self.lineTaste.text()
        price = self.linePrice.text()
        volume = self.lineVolume.text()
        roasting = self.comboBoxRoasting.currentText()
        gg = self.comboBoxGG.currentText()
        c.execute(f"""INSERT INTO types_of_coffee (id, name, roasting, ground_grains, taste, price, packing_volume)
                VALUES ({idd}, '{name}', {roasting}, '{gg}', '{taste}', '{price}', '{volume}')""")
        c.commit()

    def change_exist(self):
        c = sqlite3.connect(f'data\\coffee.db')
        rows = c.execute(f'SELECT * from types_of_coffee where name == "{self.item}"').fetchall()
        idd = rows[0][0]
        name = self.lineName.text().strip()
        taste = self.lineTaste.text()
        price = self.linePrice.text()
        volume = self.lineVolume.text()
        roasting = self.comboBoxRoasting.currentText()
        gg = self.comboBoxGG.currentText()
        c.execute(f"""Update types_of_coffee set name = '{name}', taste = '{taste}', price = '{price}',
        packing_volume = '{volume}', roasting = {roasting}, ground_grains = '{gg}' where id == {idd}""")
        c.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec())