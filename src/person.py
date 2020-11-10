import datetime
import random
import string
from file_handler import FileReader


class SSN:
    NNN_for_male = [i for i in range(2, 900) if i % 2 == 1]
    NNN_for_female = [i for i in range(2, 900) if i % 2 == 0]

    notes_dict = {1800: '+', 1900: '-', 2000: 'A'}

    def __init__(self, start_year, end_year):
        self.gender = self.random_gender()
        self.birth_day = self.generate_date_of_birth(start_year, end_year)
        self.ssn = self.generate_ssn()

    def get_birthday(self):
        return self.birth_day.strftime("%d%m%Y")

    def random_gender(self):
        genders = ('male', 'female')
        gender = random.choice(genders)
        return gender

    def generate_date_of_birth(self, start_year, end_year):
        start_date = datetime.date(start_year, 1, 1)
        end_date = datetime.date(end_year, 12, 31)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_day = random.randrange(days_between_dates + 1)  # include the last day with + 1
        random_date = start_date + datetime.timedelta(days=random_day)
        return random_date

    def generate_ssn(self):
        # set correct punctuation mark for ssn
        century = int(str(self.birth_day.year)[0:2] + '00')
        note = self.notes_dict[century]
        # generate yksilönumero for ssn depending on the gender
        if self.gender == 'male':
            nnn = random.choice(self.NNN_for_male)
        else:
            nnn = random.choice(self.NNN_for_female)

        # add leading zeros if nnn < 100
        nnn = str(nnn)
        if len(nnn) != 3:
            nnn = nnn.zfill(3)

        # make ssn to number like 220190231 or 41191222 to calculate the check char
        ssn = int(self.birth_day.strftime("%d%m%y") + nnn)
        full_ssn = self.birth_day.strftime("%d%m%y") + note + nnn + self.add_check_number(ssn)

        # return valid ssn
        return full_ssn

    def add_check_number(self, ssn):
        not_included = ['G', 'I', 'O', 'Q', 'Z']
        check_char_list = list(string.digits)
        for e in string.ascii_uppercase:
            if e not in not_included:
                check_char_list.append(e)
        check_char_dict = dict(list(enumerate(check_char_list)))
        mod = ssn % len(check_char_list)
        return check_char_dict[mod]


class TestPerson:
    def __init__(self, start_year, end_year):
        person_info = SSN(start_year, end_year)
        self.birth_date = person_info.birth_day
        self.gender = person_info.gender
        self.ssn = person_info.ssn
        names_and_IBAN = FileReader(self.gender)
        self.first_name = names_and_IBAN.first_name
        self.last_name = names_and_IBAN.last_name
        self.IBAN = names_and_IBAN.IBAN

    def show_info(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.last_name, self.first_name, self.ssn,
                                               self.birth_date.strftime('%d.%m.%Y'), self.gender, self.IBAN)
