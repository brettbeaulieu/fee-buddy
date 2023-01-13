# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_draft.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDoubleSpinBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1080, 721)
        Form.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.app_header = QFrame(Form)
        self.app_header.setObjectName(u"app_header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_header.sizePolicy().hasHeightForWidth())
        self.app_header.setSizePolicy(sizePolicy)
        self.app_header.setStyleSheet(u"font: 12pt \"Bahnschrift\";\n"
"background-color: rgb(60, 60, 60);\n"
"color:rgb(255,255,255);\n"
"border-radius:15px;")
        self.app_header.setFrameShape(QFrame.StyledPanel)
        self.app_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.app_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ticker_frame = QFrame(self.app_header)
        self.ticker_frame.setObjectName(u"ticker_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ticker_frame.sizePolicy().hasHeightForWidth())
        self.ticker_frame.setSizePolicy(sizePolicy1)
        self.ticker_frame.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"border-radius:15px;")
        self.ticker_frame.setFrameShape(QFrame.StyledPanel)
        self.ticker_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.ticker_frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ticker_label = QLabel(self.ticker_frame)
        self.ticker_label.setObjectName(u"ticker_label")
        sizePolicy1.setHeightForWidth(self.ticker_label.sizePolicy().hasHeightForWidth())
        self.ticker_label.setSizePolicy(sizePolicy1)
        self.ticker_label.setStyleSheet(u"font: 18pt \"Bahnschrift\";\n"
"padding: 15px;\n"
"color:rgb(255,255,255);\n"
"")

        self.horizontalLayout_2.addWidget(self.ticker_label, 0, Qt.AlignHCenter)

        self.ticker_combo = QComboBox(self.ticker_frame)
        self.ticker_combo.addItem("")
        self.ticker_combo.addItem("")
        self.ticker_combo.addItem("")
        self.ticker_combo.addItem("")
        self.ticker_combo.setObjectName(u"ticker_combo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ticker_combo.sizePolicy().hasHeightForWidth())
        self.ticker_combo.setSizePolicy(sizePolicy2)
        self.ticker_combo.setStyleSheet(u"font: 12pt \"Bahnschrift\";\n"
"background-color: rgb(60, 60, 60);\n"
"color:rgb(255,255,255);\n"
"padding: 5px 15px 5px 15px;")

        self.horizontalLayout_2.addWidget(self.ticker_combo, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.ticker_frame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.app_header)

        self.app_body = QFrame(Form)
        self.app_body.setObjectName(u"app_body")
        self.app_body.setStyleSheet(u"font: 12pt \"Bahnschrift\";\n"
"background-color: rgb(60, 60, 60);\n"
"color:rgb(255,255,255);\n"
"border-radius:15px;")
        self.app_body.setFrameShape(QFrame.StyledPanel)
        self.app_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.app_body)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.params_frame = QFrame(self.app_body)
        self.params_frame.setObjectName(u"params_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.params_frame.sizePolicy().hasHeightForWidth())
        self.params_frame.setSizePolicy(sizePolicy3)
        self.params_frame.setFrameShape(QFrame.StyledPanel)
        self.params_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.params_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.param_size_frame = QFrame(self.params_frame)
        self.param_size_frame.setObjectName(u"param_size_frame")
        self.param_size_frame.setStyleSheet(u"font: 12pt \"Bahnschrift\";\n"
"background-color: rgb(70, 70, 70);\n"
"color:rgb(255,255,255);\n"
"border-radius:15px;")
        self.param_size_frame.setFrameShape(QFrame.StyledPanel)
        self.param_size_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.param_size_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.position_size_label = QLabel(self.param_size_frame)
        self.position_size_label.setObjectName(u"position_size_label")
        sizePolicy.setHeightForWidth(self.position_size_label.sizePolicy().hasHeightForWidth())
        self.position_size_label.setSizePolicy(sizePolicy)
        self.position_size_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.position_size_label)

        self.position_size_edit = QDoubleSpinBox(self.param_size_frame)
        self.position_size_edit.setObjectName(u"position_size_edit")
        self.position_size_edit.setStyleSheet(u"background-color: rgb(80, 80, 80);\n"
"border-radius:15px;\n"
"padding:15px;")
        self.position_size_edit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.position_size_edit)


        self.verticalLayout_3.addWidget(self.param_size_frame)

        self.param_entry_frame = QFrame(self.params_frame)
        self.param_entry_frame.setObjectName(u"param_entry_frame")
        self.param_entry_frame.setStyleSheet(u"font: 12pt \"Bahnschrift\";\n"
"background-color: rgb(70, 70, 70);\n"
"color:rgb(255,255,255);\n"
"border-radius:15px;")
        self.param_entry_frame.setFrameShape(QFrame.StyledPanel)
        self.param_entry_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.param_entry_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.entry_date_label = QLabel(self.param_entry_frame)
        self.entry_date_label.setObjectName(u"entry_date_label")
        sizePolicy.setHeightForWidth(self.entry_date_label.sizePolicy().hasHeightForWidth())
        self.entry_date_label.setSizePolicy(sizePolicy)
        self.entry_date_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.entry_date_label)

        self.entry_date_edit = QDateTimeEdit(self.param_entry_frame)
        self.entry_date_edit.setObjectName(u"entry_date_edit")
        self.entry_date_edit.setStyleSheet(u"background-color: rgb(80, 80, 80);\n"
"border-radius:15px;\n"
"padding:15px;")
        self.entry_date_edit.setAlignment(Qt.AlignCenter)
        self.entry_date_edit.setAccelerated(False)

        self.verticalLayout_9.addWidget(self.entry_date_edit)


        self.verticalLayout_3.addWidget(self.param_entry_frame)

        self.param_exit_frame = QFrame(self.params_frame)
        self.param_exit_frame.setObjectName(u"param_exit_frame")
        self.param_exit_frame.setStyleSheet(u"font: 12pt \"Bahnschrift\";\n"
"background-color: rgb(70, 70, 70);\n"
"color:rgb(255,255,255);\n"
"border-radius:15px;")
        self.param_exit_frame.setFrameShape(QFrame.StyledPanel)
        self.param_exit_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.param_exit_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.exit_date_label = QLabel(self.param_exit_frame)
        self.exit_date_label.setObjectName(u"exit_date_label")
        sizePolicy.setHeightForWidth(self.exit_date_label.sizePolicy().hasHeightForWidth())
        self.exit_date_label.setSizePolicy(sizePolicy)
        self.exit_date_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.exit_date_label)

        self.exit_date_edit = QDateTimeEdit(self.param_exit_frame)
        self.exit_date_edit.setObjectName(u"exit_date_edit")
        self.exit_date_edit.setStyleSheet(u"background-color: rgb(80, 80, 80);\n"
"border-radius:15px;\n"
"padding:15px;")
        self.exit_date_edit.setAlignment(Qt.AlignCenter)
        self.exit_date_edit.setAccelerated(False)

        self.verticalLayout_12.addWidget(self.exit_date_edit)


        self.verticalLayout_3.addWidget(self.param_exit_frame)

        self.param_confirm_button = QPushButton(self.params_frame)
        self.param_confirm_button.setObjectName(u"param_confirm_button")
        self.param_confirm_button.setStyleSheet(u"padding:15px;\n"
"background-color:rgb(70,70,70);")

        self.verticalLayout_3.addWidget(self.param_confirm_button)


        self.horizontalLayout_3.addWidget(self.params_frame, 0, Qt.AlignTop)

        self.table_frame = QFrame(self.app_body)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setFrameShape(QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.table_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidget = QTableWidget(self.table_frame)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"/* main table */\n"
"QTableWidget\n"
"{\n"
"	\n"
"	font: 9pt \"Segoe UI\";\n"
"	background-color:rgb(60,60,60);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"/* corner button */\n"
"QTableCornerButton::section\n"
"{\n"
"	background-color:rgb(60,60,60);\n"
"}\n"
"\n"
"/* vertical/horizontal headers */\n"
"QHeaderView::section\n"
"{\n"
"	font: 9pt \"Segoe UI\";\n"
"	background-color:rgb(60,60,60);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page\n"
"{\n"
"	background:rgb(70,70,70);\n"
"}\n"
"QScrollBar::sub-page\n"
"{\n"
"	background:rgb(70,70,70);\n"
"}\n"
"\n"
"")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setTextElideMode(Qt.ElideNone)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_4.addWidget(self.tableWidget)


        self.horizontalLayout_3.addWidget(self.table_frame)

        self.fee_list_frame = QFrame(self.app_body)
        self.fee_list_frame.setObjectName(u"fee_list_frame")
        sizePolicy.setHeightForWidth(self.fee_list_frame.sizePolicy().hasHeightForWidth())
        self.fee_list_frame.setSizePolicy(sizePolicy)
        self.fee_list_frame.setFrameShape(QFrame.StyledPanel)
        self.fee_list_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fee_list_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.funding_fees_frame = QFrame(self.fee_list_frame)
        self.funding_fees_frame.setObjectName(u"funding_fees_frame")
        self.funding_fees_frame.setStyleSheet(u"font: 12pt \"Bahnschrift\";\n"
"background-color: rgb(70, 70, 70);\n"
"color:rgb(255,255,255);\n"
"border-radius:15px;")
        self.funding_fees_frame.setFrameShape(QFrame.StyledPanel)
        self.funding_fees_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.funding_fees_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.funding_fee_label = QLabel(self.funding_fees_frame)
        self.funding_fee_label.setObjectName(u"funding_fee_label")
        sizePolicy.setHeightForWidth(self.funding_fee_label.sizePolicy().hasHeightForWidth())
        self.funding_fee_label.setSizePolicy(sizePolicy)
        self.funding_fee_label.setStyleSheet(u"font: 12pt \"Bahnschrift\";")
        self.funding_fee_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.funding_fee_label)

        self.funding_fee_frame_inner = QFrame(self.funding_fees_frame)
        self.funding_fee_frame_inner.setObjectName(u"funding_fee_frame_inner")
        self.funding_fee_frame_inner.setStyleSheet(u"background-color: rgb(80, 80, 80);\n"
"border-radius:15px;\n"
"padding:5px;")
        self.funding_fee_frame_inner.setFrameShape(QFrame.StyledPanel)
        self.funding_fee_frame_inner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.funding_fee_frame_inner)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.funding_label_dol = QLabel(self.funding_fee_frame_inner)
        self.funding_label_dol.setObjectName(u"funding_label_dol")
        self.funding_label_dol.setStyleSheet(u"")
        self.funding_label_dol.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.funding_label_dol)

        self.funding_label_pct = QLabel(self.funding_fee_frame_inner)
        self.funding_label_pct.setObjectName(u"funding_label_pct")
        self.funding_label_pct.setStyleSheet(u"")
        self.funding_label_pct.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.funding_label_pct)


        self.verticalLayout_5.addWidget(self.funding_fee_frame_inner)


        self.verticalLayout_4.addWidget(self.funding_fees_frame)

        self.margin_fees_frame = QFrame(self.fee_list_frame)
        self.margin_fees_frame.setObjectName(u"margin_fees_frame")
        self.margin_fees_frame.setStyleSheet(u"font: 12pt \"Bahnschrift\";\n"
"background-color: rgb(70, 70, 70);\n"
"color:rgb(255,255,255);\n"
"border-radius:15px;")
        self.margin_fees_frame.setFrameShape(QFrame.StyledPanel)
        self.margin_fees_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.margin_fees_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.margin_fees_label = QLabel(self.margin_fees_frame)
        self.margin_fees_label.setObjectName(u"margin_fees_label")
        sizePolicy.setHeightForWidth(self.margin_fees_label.sizePolicy().hasHeightForWidth())
        self.margin_fees_label.setSizePolicy(sizePolicy)
        self.margin_fees_label.setStyleSheet(u"font: 12pt \"Bahnschrift\";")
        self.margin_fees_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.margin_fees_label)

        self.margin_fees_inner_frame = QFrame(self.margin_fees_frame)
        self.margin_fees_inner_frame.setObjectName(u"margin_fees_inner_frame")
        self.margin_fees_inner_frame.setStyleSheet(u"background-color: rgb(80, 80, 80);\n"
"border-radius:15px;\n"
"padding:5px;")
        self.margin_fees_inner_frame.setFrameShape(QFrame.StyledPanel)
        self.margin_fees_inner_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.margin_fees_inner_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.margin_fee_dol = QLabel(self.margin_fees_inner_frame)
        self.margin_fee_dol.setObjectName(u"margin_fee_dol")
        self.margin_fee_dol.setStyleSheet(u"")
        self.margin_fee_dol.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.margin_fee_dol)

        self.margin_fee_pct = QLabel(self.margin_fees_inner_frame)
        self.margin_fee_pct.setObjectName(u"margin_fee_pct")
        self.margin_fee_pct.setStyleSheet(u"")
        self.margin_fee_pct.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.margin_fee_pct)


        self.verticalLayout_6.addWidget(self.margin_fees_inner_frame)


        self.verticalLayout_4.addWidget(self.margin_fees_frame)

        self.difference_frame = QFrame(self.fee_list_frame)
        self.difference_frame.setObjectName(u"difference_frame")
        self.difference_frame.setStyleSheet(u"font: 12pt \"Bahnschrift\";\n"
"background-color: rgb(70, 70, 70);\n"
"color:rgb(255,255,255);\n"
"border-radius:15px;")
        self.difference_frame.setFrameShape(QFrame.StyledPanel)
        self.difference_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.difference_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.difference_label = QLabel(self.difference_frame)
        self.difference_label.setObjectName(u"difference_label")
        sizePolicy.setHeightForWidth(self.difference_label.sizePolicy().hasHeightForWidth())
        self.difference_label.setSizePolicy(sizePolicy)
        self.difference_label.setStyleSheet(u"font: 12pt \"Bahnschrift\";")
        self.difference_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.difference_label)

        self.difference_frame_inner = QFrame(self.difference_frame)
        self.difference_frame_inner.setObjectName(u"difference_frame_inner")
        self.difference_frame_inner.setStyleSheet(u"background-color: rgb(80, 80, 80);\n"
"border-radius:15px;\n"
"padding:5px;")
        self.difference_frame_inner.setFrameShape(QFrame.StyledPanel)
        self.difference_frame_inner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.difference_frame_inner)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.difference_label_dol = QLabel(self.difference_frame_inner)
        self.difference_label_dol.setObjectName(u"difference_label_dol")
        self.difference_label_dol.setStyleSheet(u"")
        self.difference_label_dol.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.difference_label_dol)

        self.difference_label_pct = QLabel(self.difference_frame_inner)
        self.difference_label_pct.setObjectName(u"difference_label_pct")
        self.difference_label_pct.setStyleSheet(u"")
        self.difference_label_pct.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.difference_label_pct)


        self.verticalLayout_7.addWidget(self.difference_frame_inner)


        self.verticalLayout_4.addWidget(self.difference_frame)

        self.cheapest_frame = QFrame(self.fee_list_frame)
        self.cheapest_frame.setObjectName(u"cheapest_frame")
        self.cheapest_frame.setStyleSheet(u"font: 12pt \"Bahnschrift\";\n"
"background-color: rgb(70, 70, 70);\n"
"color:rgb(255,255,255);\n"
"border-radius:15px;")
        self.cheapest_frame.setFrameShape(QFrame.StyledPanel)
        self.cheapest_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.cheapest_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.cheapest_label = QLabel(self.cheapest_frame)
        self.cheapest_label.setObjectName(u"cheapest_label")
        sizePolicy.setHeightForWidth(self.cheapest_label.sizePolicy().hasHeightForWidth())
        self.cheapest_label.setSizePolicy(sizePolicy)
        self.cheapest_label.setStyleSheet(u"font: 12pt \"Bahnschrift\";")
        self.cheapest_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.cheapest_label)

        self.cheapest_label_inner = QLabel(self.cheapest_frame)
        self.cheapest_label_inner.setObjectName(u"cheapest_label_inner")
        self.cheapest_label_inner.setStyleSheet(u"background-color: rgb(80, 80, 80);\n"
"border-radius:15px;\n"
"padding:15px;")
        self.cheapest_label_inner.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.cheapest_label_inner)


        self.verticalLayout_4.addWidget(self.cheapest_frame)


        self.horizontalLayout_3.addWidget(self.fee_list_frame, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.app_body)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ticker_label.setText(QCoreApplication.translate("Form", u"TICKER", None))
        self.ticker_combo.setItemText(0, QCoreApplication.translate("Form", u"BTCUSDT", None))
        self.ticker_combo.setItemText(1, QCoreApplication.translate("Form", u"ETHUSDT", None))
        self.ticker_combo.setItemText(2, QCoreApplication.translate("Form", u"SOLUSDT", None))
        self.ticker_combo.setItemText(3, QCoreApplication.translate("Form", u"BNBUSDT", None))

        self.position_size_label.setText(QCoreApplication.translate("Form", u"Position Size", None))
        self.entry_date_label.setText(QCoreApplication.translate("Form", u"Entry Date", None))
        self.exit_date_label.setText(QCoreApplication.translate("Form", u"Exit Date", None))
        self.param_confirm_button.setText(QCoreApplication.translate("Form", u"Confirm", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Date", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Funding Fee", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Total Funding Fees", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Margin Fee", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Total Margin Fees", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"1", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"12/16/2022 11:34", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"$0.06 (0.0132%)", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"$0.36 (0.066%)", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"$0.05 (0.01%)", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"$0.25 (0.05%)", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.funding_fee_label.setText(QCoreApplication.translate("Form", u"Funding Fees:", None))
        self.funding_label_dol.setText(QCoreApplication.translate("Form", u"$0.25", None))
        self.funding_label_pct.setText(QCoreApplication.translate("Form", u"(0.05%)", None))
        self.margin_fees_label.setText(QCoreApplication.translate("Form", u"Margin Fees:", None))
        self.margin_fee_dol.setText(QCoreApplication.translate("Form", u"$0.05", None))
        self.margin_fee_pct.setText(QCoreApplication.translate("Form", u"(0.01%)", None))
        self.difference_label.setText(QCoreApplication.translate("Form", u"Difference", None))
        self.difference_label_dol.setText(QCoreApplication.translate("Form", u"$0.20", None))
        self.difference_label_pct.setText(QCoreApplication.translate("Form", u"(0.04%)", None))
        self.cheapest_label.setText(QCoreApplication.translate("Form", u"Cheapest", None))
        self.cheapest_label_inner.setText(QCoreApplication.translate("Form", u"Spot", None))
    # retranslateUi

