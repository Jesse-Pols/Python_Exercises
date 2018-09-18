def lang_genoeg(lengte):
    if lengte >= 120:
        print("Je bent lang genoeg voor de attractie!")
    else:
        print("Sorry, je bent te klein!")

print("Hoe lang ben je in centimeters?")
lang_genoeg(float(input()))