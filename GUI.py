from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from tic_tac_toe import *


# creates a class that inherits from QMainWindow
class Application(QMainWindow, TicTacToe):
    def __init__(self, width, height):
        super(Application, self).__init__()  # calling parent constructor
        self.setWindowIcon(QtGui.QIcon('./UI/hashtag_icon.svg'))  # modifying original icon
        self.setWindowTitle("Tic Tac Toe")  # renaming window title

        # timer configured to update the QLed on screen
        self.timer_clock = QtCore.QTimer(self)
        self.timer_clock.setInterval(1000)  # 1000 ms == 1 second
        self.minutes = 0
        self.seconds = 0

        # locks GUI size to be 450x450
        self.resize(width, height)
        self.setMinimumSize(QtCore.QSize(width, height))
        self.setMaximumSize(QtCore.QSize(width, height))

        # update UI palette
        self.set_palette()

        # define font
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)

        # set central widget (?)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # set grid layout (?)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # set main frame (try to take it off)
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")

        # set stacked widgets => holds all the pages
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_frame)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 437, 391))
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")

        # defines MAIN TITLE Page
        self.title_page = QtWidgets.QWidget()
        self.title_page.setObjectName("title_page")

        # defines one player mode selection button => child to (Title Page)
        self.one_player_button = QtWidgets.QPushButton(self.title_page)
        self.one_player_button.setGeometry(QtCore.QRect(150, 200, 120, 50))
        font.setPointSize(14)
        self.one_player_button.setFont(font)
        self.one_player_button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.one_player_button.setObjectName("one_player_button")

        # defines two player mode selection button => child to (Title Page)
        self.two_player_button = QtWidgets.QPushButton(self.title_page)
        self.two_player_button.setGeometry(QtCore.QRect(150, 260, 120, 50))
        self.two_player_button.setFont(font)
        self.two_player_button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.two_player_button.setObjectName("two_player_button")

        # defines the title label => child to (Title Page)
        font.setPointSize(62)
        font.setWeight(50)
        self.title_label = QtWidgets.QLabel(self.title_page)
        self.title_label.setGeometry(QtCore.QRect(10, 10, 421, 141))
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")

        # ADDS >> Title Page to stacked widget (index: 0)
        self.stackedWidget.addWidget(self.title_page)

        # defines SINGLE MODE SELECTION Page
        self.single_mode_selection = QtWidgets.QWidget()
        self.single_mode_selection.setObjectName("single_mode_selection")

        # as last time font size was configured was during title of main page, it remains the same
        self.title_label_2 = QtWidgets.QLabel(self.single_mode_selection)
        self.title_label_2.setGeometry(QtCore.QRect(10, 10, 421, 141))
        self.title_label_2.setFont(font)
        self.title_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label_2.setObjectName("title_label_2")

        # defines difficulty combo box selection
        self.difficulty_selection = QtWidgets.QComboBox(self.single_mode_selection)
        self.difficulty_selection.setGeometry(QtCore.QRect(140, 230, 151, 31))
        font.setPointSize(12)
        self.difficulty_selection.setFont(font)
        self.difficulty_selection.setObjectName("difficulty_selection")
        self.difficulty_selection.addItem("")
        self.difficulty_selection.addItem("")

        # define label
        self.single_mode_label = QtWidgets.QLabel(self.single_mode_selection)
        self.single_mode_label.setGeometry(QtCore.QRect(120, 150, 201, 51))
        font.setPointSize(26)
        self.single_mode_label.setFont(font)
        self.single_mode_label.setObjectName("single_mode_label")

        # define label
        self.select_diff_label = QtWidgets.QLabel(self.single_mode_selection)
        self.select_diff_label.setGeometry(QtCore.QRect(140, 205, 151, 31))
        self.select_diff_label.setObjectName("select_diff_label")

        # creates frame where the X selector is
        self.choose_X_frame = QtWidgets.QFrame(self.single_mode_selection)
        self.choose_X_frame.setGeometry(QtCore.QRect(100, 300, 80, 80))
        self.choose_X_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.choose_X_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choose_X_frame.setObjectName("choose_X_frame")

        # Creates "label" (placeholder for) X image
        self.label_placeholder_X = QtWidgets.QLabel(self.choose_X_frame)
        self.label_placeholder_X.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.label_placeholder_X.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_placeholder_X.setText("")
        self.label_placeholder_X.setPixmap(QtGui.QPixmap("./UI/cross_cell.png"))
        self.label_placeholder_X.setObjectName("label_placeholder_X")

        # creates frame where the O selector is
        self.choose_O_frame = QtWidgets.QFrame(self.single_mode_selection)
        self.choose_O_frame.setGeometry(QtCore.QRect(250, 300, 80, 80))
        self.choose_O_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.choose_O_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choose_O_frame.setObjectName("choose_O_frame")

        # Creates "label" (placeholder for) O image
        self.label_placeholder_O = QtWidgets.QLabel(self.choose_O_frame)
        self.label_placeholder_O.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.label_placeholder_O.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_placeholder_O.setText("")
        self.label_placeholder_O.setPixmap(QtGui.QPixmap("./UI/circle_cell.png"))
        self.label_placeholder_O.setObjectName("label_placeholder_O")

        # create label
        self.select_piece_label = QtWidgets.QLabel(self.single_mode_selection)
        self.select_piece_label.setGeometry(QtCore.QRect(170, 260, 101, 31))
        self.select_piece_label.setObjectName("select_piece_label")

        # ADDS >> Single Mode Selection to stacked widget (index: 1)
        self.stackedWidget.addWidget(self.single_mode_selection)

        # defines BOARD GAME Page (where game is actually played)
        self.board_screen = QtWidgets.QWidget()
        self.board_screen.setObjectName("board_screen")

        # defines Quit game button
        self.quit_game = QtWidgets.QPushButton(self.board_screen)
        self.quit_game.setGeometry(QtCore.QRect(330, 10, 90, 30))
        font.setPointSize(14)
        self.quit_game.setFont(font)
        self.quit_game.setObjectName("quit_game")

        # defines frame that holds all subframes where pieces will be placed
        self.frame_board = QtWidgets.QFrame(self.board_screen)
        self.frame_board.setGeometry(QtCore.QRect(80, 50, 281, 281))
        self.frame_board.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_board.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_board.setObjectName("frame_10")

        # HERE BEGINS DEFINING SPOTS OF THE BOARD, WHICH FOLLOWS A MATRIX LOGIC

        # (row=0,column=0)
        self.frame00 = QtWidgets.QFrame(self.frame_board)
        self.frame00.setGeometry(QtCore.QRect(10, 10, 80, 80))
        self.frame00.setAutoFillBackground(True)
        self.frame00.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame00.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame00.setObjectName("frame00")

        self.label_placeholder00 = QtWidgets.QLabel(self.frame00)
        self.label_placeholder00.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.label_placeholder00.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_placeholder00.setText("")
        self.label_placeholder00.setPixmap(QtGui.QPixmap("./UI/empty_cell.png"))
        self.label_placeholder00.setObjectName("label_placeholder00")

        # (row=0,column=1)
        self.frame01 = QtWidgets.QFrame(self.frame_board)
        self.frame01.setGeometry(QtCore.QRect(100, 10, 80, 80))
        self.frame01.setAutoFillBackground(True)
        self.frame01.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame01.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame01.setObjectName("frame01")

        self.label_placeholder01 = QtWidgets.QLabel(self.frame01)
        self.label_placeholder01.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.label_placeholder01.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_placeholder01.setText("")
        self.label_placeholder01.setPixmap(QtGui.QPixmap("./UI/empty_cell.png"))
        self.label_placeholder01.setObjectName("label_placeholder01")

        # (row=0,column=2)
        self.frame02 = QtWidgets.QFrame(self.frame_board)
        self.frame02.setGeometry(QtCore.QRect(190, 10, 80, 80))
        self.frame02.setAutoFillBackground(True)
        self.frame02.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame02.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame02.setObjectName("frame02")

        self.label_placeholder02 = QtWidgets.QLabel(self.frame02)
        self.label_placeholder02.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.label_placeholder02.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_placeholder02.setText("")
        self.label_placeholder02.setPixmap(QtGui.QPixmap("./UI/empty_cell.png"))
        self.label_placeholder02.setObjectName("label_placeholder02")

        # (row=1,column=0)
        self.frame10 = QtWidgets.QFrame(self.frame_board)
        self.frame10.setGeometry(QtCore.QRect(10, 100, 80, 80))
        self.frame10.setAutoFillBackground(True)
        self.frame10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame10.setObjectName("frame10")

        self.label_placeholder10 = QtWidgets.QLabel(self.frame10)
        self.label_placeholder10.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.label_placeholder10.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_placeholder10.setText("")
        self.label_placeholder10.setPixmap(QtGui.QPixmap("./UI/empty_cell.png"))
        self.label_placeholder10.setObjectName("label_placeholder10")

        # (row=1,column=1)
        self.frame11 = QtWidgets.QFrame(self.frame_board)
        self.frame11.setGeometry(QtCore.QRect(100, 100, 80, 80))
        self.frame11.setAutoFillBackground(True)
        self.frame11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame11.setObjectName("frame11")

        self.label_placeholder11 = QtWidgets.QLabel(self.frame11)
        self.label_placeholder11.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.label_placeholder11.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_placeholder11.setText("")
        self.label_placeholder11.setPixmap(QtGui.QPixmap("./UI/empty_cell.png"))
        self.label_placeholder11.setObjectName("label_placeholder11")

        # (row=1,column=2)
        self.frame12 = QtWidgets.QFrame(self.frame_board)
        self.frame12.setGeometry(QtCore.QRect(190, 100, 80, 80))
        self.frame12.setAutoFillBackground(True)
        self.frame12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame12.setObjectName("frame12")

        self.label_placeholder12 = QtWidgets.QLabel(self.frame12)
        self.label_placeholder12.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.label_placeholder12.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_placeholder12.setText("")
        self.label_placeholder12.setPixmap(QtGui.QPixmap("./UI/empty_cell.png"))
        self.label_placeholder12.setObjectName("label_placeholder12")

        # (row=2,column=0)
        self.frame20 = QtWidgets.QFrame(self.frame_board)
        self.frame20.setGeometry(QtCore.QRect(10, 190, 80, 80))
        self.frame20.setAutoFillBackground(True)
        self.frame20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame20.setObjectName("frame20")

        self.label_placeholder20 = QtWidgets.QLabel(self.frame20)
        self.label_placeholder20.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.label_placeholder20.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_placeholder20.setText("")
        self.label_placeholder20.setPixmap(QtGui.QPixmap("./UI/empty_cell.png"))
        self.label_placeholder20.setObjectName("label_placeholder20")

        # (row=2,column=1)
        self.frame21 = QtWidgets.QFrame(self.frame_board)
        self.frame21.setGeometry(QtCore.QRect(100, 190, 80, 80))
        self.frame21.setAutoFillBackground(True)
        self.frame21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame21.setObjectName("frame21")

        self.label_placeholder21 = QtWidgets.QLabel(self.frame21)
        self.label_placeholder21.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.label_placeholder21.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_placeholder21.setText("")
        self.label_placeholder21.setPixmap(QtGui.QPixmap("./UI/empty_cell.png"))
        self.label_placeholder21.setObjectName("label_placeholder21")

        # (row=2,column=2)
        self.frame22 = QtWidgets.QFrame(self.frame_board)
        self.frame22.setGeometry(QtCore.QRect(190, 190, 80, 80))
        self.frame22.setAutoFillBackground(True)
        self.frame22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame22.setObjectName("frame22")

        self.label_placeholder22 = QtWidgets.QLabel(self.frame22)
        self.label_placeholder22.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.label_placeholder22.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_placeholder22.setText("")
        self.label_placeholder22.setPixmap(QtGui.QPixmap("./UI/empty_cell.png"))
        self.label_placeholder22.setObjectName("label_placeholder22")

        # size policy
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)

        # creates horizontal line
        self.horizontal1 = QtWidgets.QFrame(self.frame_board)
        self.horizontal1.setGeometry(QtCore.QRect(0, 85, 281, 21))
        size_policy.setHeightForWidth(self.horizontal1.sizePolicy().hasHeightForWidth())
        self.horizontal1.setSizePolicy(size_policy)
        self.horizontal1.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontal1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontal1.setObjectName("horizontal1")

        # creates horizontal line
        self.horizontal1_2 = QtWidgets.QFrame(self.frame_board)
        self.horizontal1_2.setGeometry(QtCore.QRect(0, 176, 281, 20))
        size_policy.setHeightForWidth(self.horizontal1_2.sizePolicy().hasHeightForWidth())
        self.horizontal1_2.setSizePolicy(size_policy)
        self.horizontal1_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontal1_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontal1_2.setObjectName("horizontal1_2")

        # creates vertical line
        self.line = QtWidgets.QFrame(self.frame_board)
        self.line.setGeometry(QtCore.QRect(85, 0, 21, 281))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # creates vertical line
        self.line_2 = QtWidgets.QFrame(self.frame_board)
        self.line_2.setGeometry(QtCore.QRect(170, 0, 31, 281))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        # creates TIMER
        self.time_elapsed = QtWidgets.QLCDNumber(self.board_screen)
        self.time_elapsed.setGeometry(QtCore.QRect(10, 10, 64, 23))
        self.time_elapsed.setObjectName("time_elapsed")
        self.time_elapsed.display("0:00")

        # ADDS >> After Game to stacked widget (index: 3)
        self.stackedWidget.addWidget(self.board_screen)

        # defines End Game Page shows scores and gives option to play again
        self.end_game = QtWidgets.QWidget()
        self.end_game.setObjectName("end_game")

        # Defines main label where player that won/a tie happened is indicated
        font.setPointSize(28)
        self.player_won_label = QtWidgets.QLabel(self.end_game)
        self.player_won_label.setGeometry(QtCore.QRect(70, 30, 261, 61))
        self.player_won_label.setFont(font)
        self.player_won_label.setAlignment(QtCore.Qt.AlignCenter)
        self.player_won_label.setObjectName("player_won_label")

        font.setPointSize(18)
        self.play_again_label = QtWidgets.QLabel(self.end_game)
        self.play_again_label.setGeometry(QtCore.QRect(30, 240, 361, 51))
        self.play_again_label.setFont(font)
        self.play_again_label.setAlignment(QtCore.Qt.AlignCenter)
        self.play_again_label.setObjectName("play_again_label")

        self.play_again_yes_btn = QtWidgets.QPushButton(self.end_game)
        self.play_again_yes_btn.setGeometry(QtCore.QRect(80, 300, 120, 50))
        self.play_again_yes_btn.setFont(font)
        self.play_again_yes_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.play_again_yes_btn.setObjectName("play_again_yes_btn")

        self.play_again_no_btn = QtWidgets.QPushButton(self.end_game)
        self.play_again_no_btn.setGeometry(QtCore.QRect(230, 300, 120, 50))
        self.play_again_no_btn.setFont(font)
        self.play_again_no_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.play_again_no_btn.setObjectName("play_again_no_btn")

        self.score_01 = QtWidgets.QLCDNumber(self.end_game)
        self.score_01.setGeometry(QtCore.QRect(93, 160, 91, 81))
        self.score_01.setObjectName("score_01")

        self.score_02 = QtWidgets.QLCDNumber(self.end_game)
        self.score_02.setGeometry(QtCore.QRect(240, 160, 91, 81))
        self.score_02.setObjectName("score_02")


        font.setPointSize(12)
        self.current_score_label = QtWidgets.QLabel(self.end_game)
        self.current_score_label.setGeometry(QtCore.QRect(50, 90, 111, 41))
        self.current_score_label.setFont(font)
        self.current_score_label.setObjectName("current_score_label")

        font.setPointSize(10)
        self.score_01_label = QtWidgets.QLabel(self.end_game)
        self.score_01_label.setGeometry(QtCore.QRect(90, 140, 91, 21))
        self.score_01_label.setFont(font)
        self.score_01_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.score_01_label.setObjectName("score_01_label")

        self.score_02_label = QtWidgets.QLabel(self.end_game)
        self.score_02_label.setGeometry(QtCore.QRect(240, 140, 91, 21))
        self.score_02_label.setFont(font)
        self.score_02_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.score_02_label.setObjectName("score_02_label")

        # ADDS >> End Game Screen to stacked widget (index: 3)
        self.stackedWidget.addWidget(self.end_game)

        # ??
        self.gridLayout.addWidget(self.main_frame, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        # ??
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        # ??
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # calls function that writes over labels and such
        self.retranslateUi()

        self.action_assignment()

        # Always Begins on main title window (index 0)
        self.stackedWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Application", "Tic Tac Toe"))
        self.one_player_button.setText(_translate("Application", "One Player"))
        self.one_player_button.setShortcut(_translate("Application", "1"))
        self.two_player_button.setText(_translate("Application", "Two Players"))
        self.two_player_button.setShortcut(_translate("Application", "2"))
        self.title_label.setText(_translate("Application", "Tic Tac Toe"))
        self.title_label_2.setText(_translate("Application", "Tic Tac Toe"))
        self.difficulty_selection.setItemText(0, _translate("Application", "Easy"))
        self.difficulty_selection.setItemText(1, _translate("Application", "Medium"))
        self.difficulty_selection.setItemText(2, _translate("Application", "Hard"))
        self.single_mode_label.setText(_translate("Application", "Single Mode"))
        self.select_diff_label.setText(_translate("Application", "Select Game Difficulty:"))
        self.select_piece_label.setText(_translate("Application", "Choose Your Piece:"))
        self.quit_game.setText(_translate("Application", "Quit"))
        self.play_again_label.setText(_translate("Application", "Would you like to play again?"))
        self.play_again_yes_btn.setText(_translate("Application", "Yes"))
        self.play_again_yes_btn.setShortcut(_translate("Application", "y"))
        self.play_again_no_btn.setText(_translate("Application", "No"))
        self.play_again_no_btn.setShortcut(_translate("Application", "n"))
        self.current_score_label.setText(_translate("Application", "Current Score:"))
        self.player_won_label.setText(_translate("Application", "Player has won!"))
        self.score_01_label.setText(_translate("Application", "User1"))
        self.score_02_label.setText(_translate("Application", "User2"))

    def set_palette(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 87, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 35, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 46, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 57, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 140, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 144, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 104, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 35, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 57, 72, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 87, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 35, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 46, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 57, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 140, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 144, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 143, 181))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 35, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 57, 72, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 35, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 87, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 35, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 46, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 35, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 35, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 174, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 143, 181))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 85))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.setPalette(palette)

    # overwrite to have non-clickable objects clickable (so that the labels can be clicked)
    def clickable(self, widget):

        class Filter(QtCore.QObject):

            clicked = QtCore.pyqtSignal()

            def eventFilter(self, obj, event):

                if obj == widget:
                    if event.type() == QtCore.QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            # The developer can opt for .emit(obj) to get the object within the slot.
                            return True

                return False

        returned_filter = Filter(widget)
        widget.installEventFilter(returned_filter)
        return returned_filter.clicked

    # Defines mode being played >> Single Player
    def select_single_mode(self):
        self.stackedWidget.setCurrentIndex(1)
        self.mode = "single"

    # Defines mode being played >> Two player
    def select_two_player_mode(self):
        self.mode = "double"

    # Only applicable to >> Single Player
    def single_select_piece(self, piece):
        # gets the difficulty selected
        difficulty = str(self.difficulty_selection.currentText())

        # defines hardness level and pieces
        self.choose_difficulty(difficulty)
        try:
            self.choose_pieces(piece)
        except ValueError:
            pass
        else:
            # changes screen to MAIN Board Screen
            self.stackedWidget.setCurrentIndex(2)
            #if user chose "O" piece, computer goes first
            if self.user == "o":
                self.play_piece("pc", self.next_move())
            # Begins Timer! Without it, it's only connected, but doesn't run
            self.timer_clock.start()

    # THIS IS THE MAIN FUNCTION TO UPDATE GAME, PLAY PC GAME, and VERIFY IF SOMEONE WON
    def play_piece(self, playing, position: tuple):

        if self.slot_available(position):
            row, column = position

            piece = ""
            if playing == "user":
                self.board[row][column] = self.user

                if self.user == "x":
                    piece = "./UI/cross_cell.png"
                else:
                    piece = "./UI/circle_cell.png"
            elif playing == "pc":
                self.board[row][column] = self.computer

                if self.computer == "x":
                    piece = "./UI/cross_cell.png"
                else:
                    piece = "./UI/circle_cell.png"

            # removes move from available
            current_move = self.move_key((row, column))
            self.available_moves.pop(current_move)

            if piece != "":
                if position == (0, 0):
                    self.label_placeholder00.setPixmap(QtGui.QPixmap(piece))
                elif position == (0, 1):
                    self.label_placeholder01.setPixmap(QtGui.QPixmap(piece))
                elif position == (0, 2):
                    self.label_placeholder02.setPixmap(QtGui.QPixmap(piece))
                elif position == (1, 0):
                    self.label_placeholder10.setPixmap(QtGui.QPixmap(piece))
                elif position == (1, 1):
                    self.label_placeholder11.setPixmap(QtGui.QPixmap(piece))
                elif position == (1, 2):
                    self.label_placeholder12.setPixmap(QtGui.QPixmap(piece))
                elif position == (2, 0):
                    self.label_placeholder20.setPixmap(QtGui.QPixmap(piece))
                elif position == (2, 1):
                    self.label_placeholder21.setPixmap(QtGui.QPixmap(piece))
                elif position == (2, 2):
                    self.label_placeholder22.setPixmap(QtGui.QPixmap(piece))

                # Every time this function is triggered, verify is someone made a winner move
                has_won = self.has_won()
                has_tied = self.has_tied()
                if has_won[0] == 1 or has_tied:
                    if str(has_won[1]) == self.user:
                        self.endgame("user1")
                    elif str(has_won[1]) == self.computer:
                        self.endgame("pc")
                    elif self.mode == "double" and str(has_won[1]) != self.user:
                        self.endgame("user2")
                    elif has_tied:
                        self.endgame("tie")
                else: # if game has not ended, call for pc
                    # if user is playing, call function to ensure computer plays also
                    if playing == "user" and self.mode == "single":
                        self.play_piece("pc", self.next_move())

    def endgame(self, winner: str):
        # updates the title with {winner} has won! OR Game has tied!
        # increments score with winner IF there was one
        if winner == "user1":
            self.player_won_label.setText("Player 1 has won!")
            self.player_won_label.adjustSize()
            self.score_user01 += 1
        elif winner == "user2":
            self.player_won_label.setText("Player 2 has won!")
            self.player_won_label.adjustSize()
            self.score_user02 += 1
        elif winner == "pc":
            self.player_won_label.setText("Computer has won!")
            self.player_won_label.adjustSize()
            self.score_computer += 1
        elif winner == "tie":
            self.player_won_label.setText("Game has tied!")
            self.player_won_label.adjustSize()
        self.player_won_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)

        # displays score based on mode being played
        # IF single: display Computer and User1 score ; update labels 01 and 02 to computer and user
        # If double: display user1 and user2 score ; update labels 01 and 02 to user 1 and user 2
        if self.mode == "single":
            self.score_01_label.setText("Player 1")
            self.score_01_label.adjustSize()
            self.score_01.display(self.score_user01)

            self.score_02_label.setText("Computer")
            self.score_02_label.adjustSize()
            self.score_02.display(self.score_computer)
        elif self.mode == "double":
            self.score_01_label.setText("Player 1")
            self.score_01_label.adjustSize()
            self.score_01.display(self.score_user01)

            self.score_02_label.setText("Player 2")
            self.score_02_label.adjustSize()
            self.score_02.display(self.score_user02)
        self.score_01_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.score_02_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)

        # reset timer variables and stop clock event
        self.reset_timer()
        # resets board
        self.reset_board()

        # routes window to End Game Page
        self.stackedWidget.setCurrentIndex(3)

    # method attached to "Play again? YES" button of End game screen
    # resets control variables of Tic Tac Toe class only partially using .reset("part") method
    def play_again_yes(self):
        self.reset("part")
        self.stackedWidget.setCurrentIndex(1)

    # method attached to "Play again? NO" button of End game screen
    # resets control variables of Tic Tac Toe class completely using .reset("all") method
    def play_again_no(self):
        self.reset("all")
        self.stackedWidget.setCurrentIndex(0)

    # method attached to "Quit" button of main board screen
    # resets control variables of Tic Tac Toe class completely using .reset("all") method
    def quit_current_game(self):
        self.reset("all")
        self.reset_board()
        self.reset_timer()
        self.stackedWidget.setCurrentIndex(0)

    # helper method to clear the game board
    def reset_board(self):
        piece = "./UI/empty_cell.png"
        self.label_placeholder00.setPixmap(QtGui.QPixmap(piece))
        self.label_placeholder01.setPixmap(QtGui.QPixmap(piece))
        self.label_placeholder02.setPixmap(QtGui.QPixmap(piece))
        self.label_placeholder10.setPixmap(QtGui.QPixmap(piece))
        self.label_placeholder11.setPixmap(QtGui.QPixmap(piece))
        self.label_placeholder12.setPixmap(QtGui.QPixmap(piece))
        self.label_placeholder20.setPixmap(QtGui.QPixmap(piece))
        self.label_placeholder21.setPixmap(QtGui.QPixmap(piece))
        self.label_placeholder22.setPixmap(QtGui.QPixmap(piece))

    # helper method to restart the clock
    def reset_timer(self):
        self.seconds = 0
        self.minutes = 0
        self.time_elapsed.display("0:00")
        self.timer_clock.stop()

    # updates the two values that control time elapsed and prints them out in a clock format fashion
    def update_timer(self):
        if 0 <= self.seconds < 60:
            self.seconds += 1
        else:
            self.seconds = 0
            self.minutes += 1

        if self.seconds // 10 == 0:
            self.time_elapsed.display(f"{self.minutes}:0{self.seconds}")
        else:
            self.time_elapsed.display(f"{self.minutes}:{self.seconds}")

    def action_assignment(self):
        # ASSIGNS ACTION TO BUTTON 1 >> Modify screen
        self.one_player_button.clicked.connect(self.select_single_mode)

        # ASSIGNS ACTION TO X or O >> Modify screen ; choose piece  choose difficulty
        self.clickable(self.label_placeholder_X).connect(lambda: self.single_select_piece("x"))
        self.clickable(self.label_placeholder_O).connect(lambda: self.single_select_piece("o"))

        # ASSIGNS ACTIONS TO BOARD SLOTS
        self.clickable(self.label_placeholder00).connect(lambda: self.play_piece("user", (0, 0)))
        self.clickable(self.label_placeholder01).connect(lambda: self.play_piece("user", (0, 1)))
        self.clickable(self.label_placeholder02).connect(lambda: self.play_piece("user", (0, 2)))
        self.clickable(self.label_placeholder10).connect(lambda: self.play_piece("user", (1, 0)))
        self.clickable(self.label_placeholder11).connect(lambda: self.play_piece("user", (1, 1)))
        self.clickable(self.label_placeholder12).connect(lambda: self.play_piece("user", (1, 2)))
        self.clickable(self.label_placeholder20).connect(lambda: self.play_piece("user", (2, 0)))
        self.clickable(self.label_placeholder21).connect(lambda: self.play_piece("user", (2, 1)))
        self.clickable(self.label_placeholder22).connect(lambda: self.play_piece("user", (2, 2)))

        # Connects timer clock
        self.timer_clock.timeout.connect(self.update_timer)

        # Connects quit game button
        self.quit_game.clicked.connect(self.quit_current_game)

        # Connects Play Again buttons of End Game Screen
        self.play_again_yes_btn.clicked.connect(self.play_again_yes)
        self.play_again_no_btn.clicked.connect(self.play_again_no)


def window():
    app = QApplication(sys.argv)
    win = Application(width=450, height=450)
    win.show()
    sys.exit(app.exec_())


window()
