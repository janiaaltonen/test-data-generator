#!/usr/bin/env python
from person import TestPerson
from file_handler import FileWriter


class UI:
    def __init__(self):
        self.number_to_create = self.ask_amount()
        start_year, end_year = self.ask_years()
        self.persons_list = self.create_persons_list(start_year, end_year)
        writer = FileWriter(self.persons_list)
        writer.write_csv()

    def ask_amount(self):
        amount = input('Total persons to create:\n')
        return int(amount)

    def ask_years(self):
        start_year = input('Oldest birth year for person:\n')
        end_year = input('Youngest birth year for person:\n')
        return int(start_year), int(end_year)

    def create_persons_list(self, start_year, end_year):
        persons_list = [TestPerson(start_year, end_year) for i in range(self.number_to_create)]
        return persons_list


if __name__ == '__main__':
    ui = UI()
