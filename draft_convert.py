import sys

from PySide6.QtCore import QMetaObject, Qt, QThreadPool
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit,
                               QDoubleSpinBox, QFrame, QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QTableWidget, QVBoxLayout, QWidget)

from backend.utils import API_Utils


class FeeBuddy(QWidget):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        self.utils = API_Utils()
		# ADD MEMBER FOR TYPE OF FUTURE MARGIN -- USDC, UNIV
        self.setupUi()
        self.show()

    def build_header(self):
        self.app_header = QFrame(self)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(False)

        self.app_header.setSizePolicy(sizePolicy)
        self.app_header.setStyleSheet(
            'font: 12pt "Bahnschrift";'
            "background-color: rgb(60, 60, 60);"
            "color:rgb(255,255,255);"
            "border-radius:15px;"
        )
        self.app_header.setFrameShape(QFrame.StyledPanel)
        self.app_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.app_header)

        self.ticker_frame = QFrame(self.app_header)

        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ticker_frame.sizePolicy().hasHeightForWidth())
        self.ticker_frame.setSizePolicy(sizePolicy1)
        self.ticker_frame.setStyleSheet("background-color: rgb(70, 70, 70); border-radius:15px;")
        self.ticker_frame.setFrameShape(QFrame.StyledPanel)
        self.ticker_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.ticker_frame)
        self.horizontalLayout_2.setSpacing(6)

        self.ticker_label = QLabel(self.ticker_frame, text="Tickers")

        sizePolicy1.setHeightForWidth(self.ticker_label.sizePolicy().hasHeightForWidth())
        self.ticker_label.setSizePolicy(sizePolicy1)
        self.ticker_label.setStyleSheet(
            'font: 18pt "Bahnschrift";' "padding: 15px;" "color:rgb(255,255,255);"
        )

        self.horizontalLayout_2.addWidget(self.ticker_label, 0, Qt.AlignHCenter)

        self.ticker_combo = QComboBox(self.ticker_frame)
        for x in self.utils.get_tickers():
            self.ticker_combo.addItem(x)
		
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ticker_combo.sizePolicy().hasHeightForWidth())
        self.ticker_combo.setSizePolicy(sizePolicy2)
        self.ticker_combo.setStyleSheet(
            'font: 12pt "Bahnschrift";'
            "background-color: rgb(60, 60, 60);"
            "color:rgb(255,255,255);"
            "padding: 5px 15px 5px 15px;"
        )

        self.horizontalLayout_2.addWidget(self.ticker_combo, 0, Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.ticker_frame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

    def build_body(self):
        self.app_body = QFrame(self)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.app_body.setStyleSheet(
            'font: 12pt "Bahnschrift";'
            "background-color: rgb(60, 60, 60);"
            "color:rgb(255,255,255);"
            "border-radius:15px;"
        )

        self.body_layout = QHBoxLayout(self.app_body)

        self.build_params()
        self.build_table()
        self.build_fee_list()  # build and pack fee list

        self.body_layout.addWidget(self.params_frame)
        self.body_layout.addWidget(self.table_frame)
        self.body_layout.addWidget(self.fee_list_frame)

    def build_params(self):
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHeightForWidth(True)
        self.params_frame = QFrame(self.app_body)

        # Position Size Parameter
        self.param_size_frame = QFrame(self.params_frame)
        self.param_size_frame.setStyleSheet(
            'font: 12pt "Bahnschrift";'
            "background-color: rgb(70, 70, 70);"
            "color:rgb(255,255,255);"
            "border-radius:15px;"
        )

        self.position_size_label = QLabel(self.param_size_frame, text="Position Size")
        self.position_size_label.setSizePolicy(sizePolicy)
        self.position_size_label.setAlignment(Qt.AlignCenter)

        self.position_size_edit = QDoubleSpinBox(self.param_size_frame)
        self.position_size_edit.setAlignment(Qt.AlignCenter)
        self.position_size_edit.setStyleSheet(
            "background-color: rgb(80, 80, 80);" "border-radius:15px;" "padding:15px;"
        )

        self.position_size_layout = QVBoxLayout(self.param_size_frame)
        self.position_size_layout.addWidget(self.position_size_label)
        self.position_size_layout.addWidget(self.position_size_edit)

        self.param_entry_frame = QFrame(self.params_frame)
        self.param_entry_frame.setStyleSheet(
            'font: 12pt "Bahnschrift";'
            "background-color: rgb(70, 70, 70);"
            "color:rgb(255,255,255);"
            "border-radius:15px;"
        )

        self.verticalLayout_9 = QVBoxLayout(self.param_entry_frame)

        self.entry_date_label = QLabel(self.param_entry_frame, text="Entry Date")
        self.entry_date_label.setSizePolicy(sizePolicy)
        self.entry_date_label.setAlignment(Qt.AlignCenter)

        self.entry_date_edit = QDateTimeEdit(self.param_entry_frame)
        self.entry_date_edit.setAlignment(Qt.AlignCenter)
        self.entry_date_edit.setStyleSheet(
            "background-color: rgb(80, 80, 80); border-radius:15px; padding:15px;"
        )

        self.verticalLayout_9.addWidget(self.entry_date_label)
        self.verticalLayout_9.addWidget(self.entry_date_edit)

        # Exit Date Parameter
        self.param_exit_frame = QFrame(self.params_frame)
        self.param_exit_frame.setStyleSheet(
            'font: 12pt "Bahnschrift"; background-color: rgb(70, 70, 70);'
            "color:rgb(255,255,255); border-radius:15px;"
        )

        self.exit_date_label = QLabel(self.param_exit_frame, text="Exit Date")
        self.exit_date_label.setSizePolicy(sizePolicy)
        self.exit_date_label.setAlignment(Qt.AlignCenter)

        self.exit_date_edit = QDateTimeEdit(self.param_exit_frame)
        self.exit_date_edit.setAlignment(Qt.AlignCenter)
        self.exit_date_edit.setStyleSheet(
            "background-color: rgb(80, 80, 80);" "border-radius:15px;" "padding:15px;"
        )

        self.param_exit_layout = QVBoxLayout(self.param_exit_frame)
        self.param_exit_layout.addWidget(self.exit_date_label)
        self.param_exit_layout.addWidget(self.exit_date_edit)

        # Confirm Button
        self.param_confirm_button = QPushButton(self.params_frame, text="Confirm")
        self.param_confirm_button.clicked.connect(self.push_params)
        self.param_confirm_button.setStyleSheet("padding:15px; background-color:rgb(70,70,70);")

        # Pack
        self.params_layout = QVBoxLayout(self.params_frame)
        self.params_layout.addWidget(self.param_size_frame)
        self.params_layout.addWidget(self.param_entry_frame)
        self.params_layout.addWidget(self.param_exit_frame)
        self.params_layout.addWidget(self.param_confirm_button)

    def build_fee_list(self):
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.fee_list_frame = QFrame(self.app_body)

        # Funding Fees
        self.funding_fee_frame = QFrame(self.fee_list_frame)
        self.funding_fee_frame.setStyleSheet(
            'font: 12pt "Bahnschrift";'
            "background-color: rgb(70, 70, 70);"
            "color:rgb(255,255,255);"
            "border-radius:15px;"
        )

        self.funding_fee_label = QLabel(self.funding_fee_frame, text="Funding Fees")
        sizePolicy.setHeightForWidth(True)
        self.funding_fee_label.setSizePolicy(sizePolicy)
        self.funding_fee_label.setStyleSheet('font: 12pt "Bahnschrift";')
        self.funding_fee_label.setAlignment(Qt.AlignCenter)

        self.funding_fee_frame_inner = QFrame(self.funding_fee_frame)
        self.funding_fee_frame_inner.setStyleSheet(
            "background-color: rgb(80, 80, 80);" "border-radius:15px;" "padding:5px;"
        )

        self.funding_label_dol = QLabel(self.funding_fee_frame_inner)
        self.funding_label_pct = QLabel(self.funding_fee_frame_inner)

        self.funding_label_dol.setAlignment(Qt.AlignCenter)
        self.funding_label_pct.setAlignment(Qt.AlignCenter)

        self.funding_fee_inner_layout = QVBoxLayout(self.funding_fee_frame_inner)
        self.funding_fee_inner_layout.addWidget(self.funding_label_dol)
        self.funding_fee_inner_layout.addWidget(self.funding_label_pct)

        self.funding_fee_layout = QVBoxLayout(self.funding_fee_frame)
        self.funding_fee_layout.addWidget(self.funding_fee_label)
        self.funding_fee_layout.addWidget(self.funding_fee_frame_inner)

        # Margin Fees
        self.margin_fees_frame = QFrame(self.fee_list_frame)
        self.margin_fees_frame.setStyleSheet(
            'font: 12pt "Bahnschrift";'
            "background-color: rgb(70, 70, 70);"
            "color:rgb(255,255,255);"
            "border-radius:15px;"
        )

        self.margin_fees_layout = QVBoxLayout(self.margin_fees_frame)

        self.margin_fees_label = QLabel(self.margin_fees_frame, text="Margin Fees")
        self.margin_fees_label.setSizePolicy(sizePolicy)
        self.margin_fees_label.setStyleSheet('font: 12pt "Bahnschrift";')
        self.margin_fees_label.setAlignment(Qt.AlignCenter)

        self.margin_fees_inner_frame = QFrame(self.margin_fees_frame)
        self.margin_fees_inner_frame.setStyleSheet(
            "background-color: rgb(80, 80, 80);" "border-radius:15px;" "padding:5px;"
        )

        self.margin_fee_dol = QLabel(self.margin_fees_inner_frame)
        self.margin_fee_dol.setAlignment(Qt.AlignCenter)

        self.margin_fee_pct = QLabel(self.margin_fees_inner_frame)
        self.margin_fee_pct.setAlignment(Qt.AlignCenter)

        self.margin_fees_inner_layout = QVBoxLayout(self.margin_fees_inner_frame)
        self.margin_fees_inner_layout.addWidget(self.margin_fee_dol)
        self.margin_fees_inner_layout.addWidget(self.margin_fee_pct)

        self.margin_fees_layout.addWidget(self.margin_fees_label)
        self.margin_fees_layout.addWidget(self.margin_fees_inner_frame)

        # Fee Difference
        self.difference_frame = QFrame(self.fee_list_frame)
        self.difference_frame.setStyleSheet(
            'font: 12pt "Bahnschrift";'
            "background-color: rgb(70, 70, 70);"
            "color:rgb(255,255,255);"
            "border-radius:15px;"
        )

        self.difference_label = QLabel(self.difference_frame, text="Difference")
        self.difference_label.setSizePolicy(sizePolicy)
        self.difference_label.setStyleSheet('font: 12pt "Bahnschrift";')
        self.difference_label.setAlignment(Qt.AlignCenter)

        self.difference_frame_inner = QFrame(self.difference_frame)
        self.difference_frame_inner.setStyleSheet(
            "background-color: rgb(80, 80, 80);" "border-radius:15px;" "padding:5px;"
        )

        self.difference_label_dol = QLabel(self.difference_frame_inner)
        self.difference_label_pct = QLabel(self.difference_frame_inner)

        self.difference_label_dol.setAlignment(Qt.AlignCenter)
        self.difference_label_pct.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15 = QVBoxLayout(self.difference_frame_inner)
        self.verticalLayout_15.addWidget(self.difference_label_dol)
        self.verticalLayout_15.addWidget(self.difference_label_pct)

        self.verticalLayout_7 = QVBoxLayout(self.difference_frame)
        self.verticalLayout_7.addWidget(self.difference_label)
        self.verticalLayout_7.addWidget(self.difference_frame_inner)

        # Cheapest Option
        self.cheapest_frame = QFrame(self.fee_list_frame)
        self.cheapest_frame.setStyleSheet(
            'font: 12pt "Bahnschrift";'
            "background-color: rgb(70, 70, 70);"
            "color:rgb(255,255,255);"
            "border-radius:15px;"
        )

        self.cheapest_label = QLabel(self.cheapest_frame, text="Cheapest")
        self.cheapest_label.setSizePolicy(sizePolicy)
        self.cheapest_label.setStyleSheet('font: 12pt "Bahnschrift";')
        self.cheapest_label.setAlignment(Qt.AlignCenter)

        self.cheapest_label_inner = QLabel(self.cheapest_frame)
        self.cheapest_label_inner.setStyleSheet(
            "background-color: rgb(80, 80, 80);" "border-radius:15px;" "padding:15px;"
        )
        self.cheapest_label_inner.setAlignment(Qt.AlignCenter)

        self.cheapest_layout = QVBoxLayout(self.cheapest_frame)
        self.cheapest_layout.addWidget(self.cheapest_label)
        self.cheapest_layout.addWidget(self.cheapest_label_inner)

        # Pack
        self.fee_list_layout = QVBoxLayout(self.fee_list_frame)
        self.fee_list_layout.addWidget(self.funding_fee_frame)
        self.fee_list_layout.addWidget(self.margin_fees_frame)
        self.fee_list_layout.addWidget(self.difference_frame)
        self.fee_list_layout.addWidget(self.cheapest_frame)

    def build_table(self):
        self.table_frame = QFrame(self.app_body)

        self.horizontalLayout_4 = QHBoxLayout(self.table_frame)

        self.tableWidget = QTableWidget(self.table_frame)
        self.tableWidget.setColumnCount(6)

        self.tableWidget.setHorizontalHeaderLabels(
            [
                "Date",
                "Funding Rate",
                "Funding Fee",
                "Total Funding Fees",
                "Margin Fees",
                "Total Margin Fees",
            ]
        )

        self.tableWidget.setStyleSheet(
            "/* main table */"
            "QTableWidget"
            "{"
            '	font: 9pt "Segoe UI";'
            "	background-color:rgb(60,60,60);"
            "	border: 0px solid;"
            "}"
            "/* corner button */"
            "QTableCornerButton::section"
            "{"
            "	background-color:rgb(60,60,60);"
            "}"
            "/* vertical/horizontal headers */"
            "QHeaderView::section"
            "{"
            '	font: 9pt "Segoe UI";'
            "	background-color:rgb(60,60,60);"
            "	border: 0px;"
            "}"
            "QScrollBar::add-page"
            "{"
            "	background:rgb(70,70,70);"
            "}"
            "QScrollBar::sub-page"
            "{"
            "	background:rgb(70,70,70);"
            "}"
        )
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setTextElideMode(Qt.ElideNone)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_4.addWidget(self.tableWidget)

    def setup_ui(self):
        self.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.main_layout = QVBoxLayout(self)
        self.buildHeader()
        self.build_body()
        self.main_layout.addWidget(self.app_header)
        self.main_layout.addWidget(self.app_body)

        QMetaObject.connectSlotsByName(self)

    def push_params(self):
        symbol = self.ticker_combo.currentText()
        start_date = self.entry_date_edit.dateTime()
        end_date = self.exit_date_edit.dateTime()
        self.utils.solve_fees(symbol, start_date, end_date)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("Fee Buddy")

    window = FeeBuddy()
    window.show()

    sys.exit(app.exec())
