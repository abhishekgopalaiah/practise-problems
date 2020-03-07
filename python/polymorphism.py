class India:
    def capital(self):
        print('Delhi')


class Karnataka(India):
    def capital(self):  # overrides capital India's capital method
        # super().capital()
        print('Bengaluru')


class Tamilnadu(India):
    def capital(self):  # overrides capital India's capital method
        print('Chennai')


obj_ind = India()
obj_ind.capital()

obj_kar = Karnataka()
obj_kar.capital()

obj_tn = Tamilnadu()
obj_tn.capital()

Output:
Delhi
Bengaluru
Chennai