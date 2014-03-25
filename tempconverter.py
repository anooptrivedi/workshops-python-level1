temp = int(input('Insert a temp to convert: '))
type = input('Now choose a conversion type: Celcius(c) or Farenheit(f): ')

if(type == 'c'):
    cel = round((5/9)*(temp-32),2)
    print('Fareheit', temp, 'is equal to', cel, 'celcius')
elif(type == 'f'):
    far = ((9/5)*temp)+32
    print('Celcius', temp, 'is equal to', far, 'farenheit')
else:
    print('Unknow Data Input! Try again')
