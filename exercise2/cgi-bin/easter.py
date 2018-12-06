#!/usr/bin/python3
import cgi, cgitb
cgitb.enable() # displays any errors
form = cgi.FieldStorage()
x = form.getvalue("datepicker")
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

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title> Finding Easter </title>  </head>')
print('<body>')
print('<p>')
print('Easter falls on' & str(p) & "/" & str(n) & "/" & str(x))
            #prints day/month/year e.g. 25/12/2018
print('</p>')
print('</body>')
print('</html>')
