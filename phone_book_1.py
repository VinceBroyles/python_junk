#This is a sample phone book program
#Vincent Broyles is the author!
north_area_codes = ('619','858','760','818')
south_area_codes = ('343','676','232','979')

names = []
numbers = []
zips_areas = {92029:858,92014:858,92020:619,92021:619,92057:760}


def get_full_name():
    first_name = input('What is your first name?')
    last_name = input ('What is your last name?')
    full_name = (first_name + ' ' + last_name)
    return full_name

def get_phone_number():
    area_code = input('Area Code?')
    '''
    if area_code not in north_area_codes:
        print ('Area code not covered1.')
        return
    if area_code not in south_area_codes:
        print ('Area code not covered2.')
        return
        '''
    phone_number = input('Phone number?')
    full_entry = ('(' + area_code + ')' + phone_number)
    return full_entry

def link_area_to_zip_code():
    print("Hi")
    

#Ask the data entry person how many numbers they want to enter
iterations = input ('How many numbers to enter?')
int_iterations = int(iterations)
print(int_iterations)

for i in range(int_iterations):
    '''  run the functions to get the
         name and the numbers, and then
         append that onto the running list
         '''
    temp_name = get_full_name()
    names.append(temp_name)
    temp_number = get_phone_number()
    numbers.append(temp_number)
    try:
        print (temp_name + ' ' + temp_number)
    except(TypeError):
        print ('There was a problem, try again.')

print ('Here is the full list:')

#Now print out the full array of names and numbers
for i in range(int_iterations):
    print (names[i] + ' ' + numbers[i])

    
