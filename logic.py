from PyQt6.QtWidgets import *
from gui import *
import csv


class Logic(QMainWindow, Ui_Final_Project_1):
    """
    A class representing a voting system
    """
    def __init__(self) -> None:
        """
        Method to set the default values of the voting system
        """
        super().__init__()
        self.setupUi(self)
        self.i_d_list = []
        self.final_list = []
        self.voted = 0
        self.button_vote.clicked.connect(lambda: self.vote())

    def vote(self) -> None:
        """
        Method that registers a vote when the vote button is pressed
        """
        self.label_check.setStyleSheet('color: black')
        with open('data.csv', 'r', newline='') as file_read:
            reader = csv.reader(file_read)
            reader = list(reader)
            if reader:  # Only process the reader if there is content
                for voter in reader:
                    if len(voter) > 1:  # Check if there is at least 2 elements (name, id)
                        self.i_d_list.append(voter[1])
        with open('data.csv', 'a', newline='') as file_write:
            writer = csv.writer(file_write)

            name = self.entry_name.text().strip()
            i_d = self.entry_ID.text().strip()

            try:
                if name == '':
                    name = 'Anonymous'
                self.final_list = [name, i_d]
                if self.vote_jane.isChecked():
                    self.voted = 1
                elif self.vote_john.isChecked():
                    self.voted = 2
                elif self.vote_jacob.isChecked():
                    self.voted = 3
                elif self.vote_janet.isChecked():
                    self.voted = 4
                elif self.voting_group.checkedButton() == None:
                    raise TypeError
                if len(i_d) != 6:  # Ensure the ID is exactly 6 digits and numeric
                    raise AttributeError
                if i_d in self.i_d_list:
                    raise ValueError
                self.i_d_list.append(i_d)

                self.final_list.append(self.candidate(self.voted))
                writer.writerow(self.final_list)
                self.label_check.setText(f'{name}, you have successfully voted!')
                self.label_check.adjustSize()
                self.clear_votes()
            except ValueError:
                self.label_check.setText(f'{i_d} is in use')
                self.label_check.setStyleSheet('color: red')
                self.clear_votes()
            except TypeError:
                self.label_check.setText('Please enter proper information')
                self.label_check.setStyleSheet('color: red')
            except AttributeError:
                self.label_check.setText(f'ID must be 6 digits and numeric')
                self.label_check.setStyleSheet('color: red')
                self.clear_votes()

    def candidate(self, voted: int) -> str:
        """
        Method to return the name of the person voted for
        :param voted: Number assigned to button selected
        :return: Name of person voted for
        """
        if voted == 1:
            return 'Jane'
        elif voted == 2:
            return 'John'
        elif voted == 3:
            return 'Jacob'
        elif voted == 4:
            return 'Janet'


    def clear_votes(self) -> None:
        """
        Method to clear all button selections
        """
        if self.voting_group.checkedButton() != 0:
            self.voting_group.setExclusive(False)
            self.voting_group.checkedButton().setChecked(False)
            self.voting_group.setExclusive(True)




