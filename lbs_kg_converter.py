class WeightConverter:
    def __init__(self):
        pass

    def lbs_to_kg(self, lbs):
        return lbs * 0.45  # calculation gets passed back to the method then
        # stored as a new variable called "converted_weight" ln:19

    def kg_to_lbs(self, kg):
        return kg * 2.2  # calculation gets passed back to the method then
        # stored as a new variable called "converted_weight" ln:23

    def convert(self):  # Data enters self from the input bellow and enters the
        # "self argument which is then shared with the functions and the class"
        user_entered_weight = float(input('Enter Weight: '))  # This line is evaluated and weight is stored.
        kgs_or_lbs = input('(K)g or (L)bs: ').lower()  # This line is converted to lowercase, evaluated, and stored.

        if kgs_or_lbs == 'l':
            converted_weight = self.lbs_to_kg(user_entered_weight)  # if "L" is entered it moves the values stored into
            # "self" and call the method lbs_to_kg while also passing through user_entered_weight. Check lines 5-7
            print(f'{user_entered_weight} lbs is roughly equal to {converted_weight:.2f} kg')
        elif kgs_or_lbs == 'k':
            converted_weight = self.kg_to_lbs(user_entered_weight)  # if "K" is entered it moves the values stored into
            # "self" and call the method kg_to_lbs while also passing through user_entered_weight. Check lines 8-10
            print(f'{user_entered_weight} kg is roughly equal to {converted_weight:.2f} lbs')  # converted_weight is
            # formatted (:) using two (2) decimal places (.) with the type of float(f)
        else:
            print('Please enter valid input either "K" or "L" to indicate the unit of measure')


# Create an instance of the WeightConverter class
converter = WeightConverter()

# Use the convert method to perform the conversion
converter.convert()
