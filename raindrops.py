def convert(number):
    new_string = ''
    if number % 3 == 0:
        new_string = new_string +'Pling'
    if number % 5 == 0:
       new_string = new_string +'Plang'
    if number % 7 == 0:
        new_string = new_string +'Plong'
    if not new_string:
        new_string = str(number)
    return new_string
