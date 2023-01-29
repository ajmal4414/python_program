from operator import itemgetter, attrgetter
l = [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
while True:
    s = ()
    if not s:
        break
    l.append(tuple(s.split(",")))

print( sorted(l, key=itemgetter(0,1,2)))