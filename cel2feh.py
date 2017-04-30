def Cel2Fah(temp):
	Fah = temp * 9 / 5 + 32
	Fah = float(Fah)
	Fah_string = str(Fah)
        a = Fah_string.split('.')
        b = a[1][0:2]
        if len(b) < 2:
        	b = b + '0'
        elif len(b) > 2:
        	b = float(b)
        	b = round(b)
        	b = str(b)
                b = b[0:2]
        c = a[0]
        f = str(c) + '.' + str(b)
        return f
