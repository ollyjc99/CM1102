#!/usr/bin/python3
import cgi, cgitb
cgitb.enable() # displays any errors
form = cgi.FieldStorage()
x = int(form.getvalue("datepicker"))
format = form.getvalue("format")

a = x % 19
b = x // 100
c = x % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7

n = (h - m + r + 90) // 25
  #calculates the month of easter

p = (h - m + r + n + 19) % 32
  #calculates the day of easter

sup = str()
if len(str(p)) == 1:
    if str(p) == '1':
        sup = 'st'
    elif str(p) == '2':
        sup = 'nd'
    elif str(p) == '3':
        sup = 'rd'
    else:
        sup = 'th'
elif len(str(p)) == 2:
    if str(p)[0] == '1':
        sup = 'th'
    elif str(p)[1] == '1':
        sup = 'st'
    elif str(p)[1] == '2':
        sup = 'nd'
    elif str(p)[1] == '3':
        sup = 'rd'
    else:
        sup = 'th'
        #   calculates what the superscript will be based off
        #   the value the day
month = str()

if n == 3:
    month='March'
elif n == 4:
    month='April'
        #   calculates the verbal format of the month

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html lang="en" style="background-color: #23272a">')
print('<head> <title> Finding Easter </title> <meta charset="utf-8"></head>')
print('<body>')
print('<h1 style="margin-left: 1.5%; margin-right: 1.5%; color: #ffffff; background-color: #7289da; border: thin groove #99aab5; text-align: center;"> Finding Easter </h1>')
print('<p style="font-family: verdana, verdana sans-serif; margin-left: 2%; margin-right: 2%; color: #ffffff; background-color: #2c2f33;">')

print('<fieldset style="font-family: verdana, verdana sans-serif; margin-left: 2%; margin-right: 2%; color: #ffffff; background-color: #2c2f33;">')
print('<legend>Easter</legend>')
print('<br>')
if format == 'num':
    print('Easter falls on: ' + str(p) + "/" + str(n) + "/" + str(x))
                #   prints the date of easter numerically
                #   e.g. day/month/year e.g. 25/12/2018
elif format == 'verb':
    print('Easter falls on the ' + str(p)+'<sup>'+sup+'</sup>' + " of " + month + " " + str(x))
                #   prints the date of easter Verbosely
                #   e.g 25th of December 2018
elif format == 'both':
    print('Easter falls on: ' + str(p) + "/" + str(n) + "/" + str(x))
    print('<br>')
    print('Easter falls on the ' + str(p)+'<sup>'+sup+'</sup>' + " of " + month + " " + str(x))
                #   prints the date of easter in both formats
                #   e.g. 25/12/2018 & 25th of December 2018
print('<br>')
print('</fieldset>')

print('</p>')
print('</body>')
print('</html>')
