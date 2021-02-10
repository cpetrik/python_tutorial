import math as m

e = m.e
print(e)

y_natural = m.log(e)
y_base10 = m.log(e,10) #changing base of nat log
y_log10 = m.log10(e) #more accurate than changing base of nat log

print(y_natural,y_base10, y_log10)

deg = 180
rads = deg * m.pi / 180
rads_fn = m.radians(deg)
print(deg, rads, rads_fn)

cos_deg = m.cos(deg)
cos_rad = m.cos(m.radians(deg))
print(cos_deg,cos_rad)

print(m.factorial(5))


