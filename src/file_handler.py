import random
import os
import datetime

class FileReader:
    def __init__(self, gender):
        self.dir = 'data/'
        self.first_name = self.random_value(gender)
        self.last_name = self.random_value('lastname')
        self.IBAN = self.random_value('IBAN')


    def random_value(self, type_of):
        types = {'male': 'male_names.csv', 'female': 'female_names.csv', 'lastname': 'lastnames.csv', 'IBAN': 'IBANs.csv'}
        path = self.dir + types[type_of]
        name_list = []
        with open(path, 'r', encoding='utf-8') as file:
            i = 0
            # exlude the header line
            file.readline()
            for row in file:
                name = row.strip().split(',', 1)[0]
                name_list.append(name)
        file.close()
        name = random.choice(name_list)
        return name


class FileWriter:
    def __init__(self, person_list):
        path_parent = os.path.dirname(os.getcwd())
        os.chdir(path_parent)
        if not os.path.exists('output'):
            os.mkdir('output')
        self.dir = os.path.join(os.getcwd(), 'output')
        time = datetime.datetime.now()
        self.file = '/test_data_' + time.strftime('%d_%m_%Y %H:%M:%S')
        self.path = self.dir + self.file
        self.persons_list = person_list

    def write_csv(self):
        path = self.path + '.csv'
        with open(path, 'w', encoding='utf-8') as file:
            for person in self.persons_list:
                file.write(person.show_info() + '\n')
        file.close()