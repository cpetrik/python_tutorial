def compute_windchill(t,v):
    """
    Compute the wind chill factor given temp and windspeed
    NOTE: valid only for temps between -45F and +45F and windspeeds between
          3 and 60 mph
    Parameters:
        t: temperature in F units (float)
        v: wind speed in mph units (float)
    """

    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    v16 = v ** 0.16

    wci = a + (b*t) - (c*v16) + (d*t*v16)

    return wci


def compute_heatindex(t,hum):
    """
    Compute the heat index from temp and humidity
    Parameters:
        t: temperature in F units (float)
        hum: percent humidity (float)
    """

    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = 0.22475541
    e = 0.00683783
    f = 0.05481717
    g = 0.00122874
    h = 0.00085282
    i = 0.00000199

    # relative humidity from percent to decimal
    rh = hum / 100

    hi = (a + (b * t) + (c * rh) + (d * t * rh) +
        (e * t**2) + (f * rh**2) + (g * t**2 * rh)+
        (h * t * rh**2) + (i * t**2 * rh**2))

    return hi
