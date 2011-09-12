zeds_name = 'Zed A. Shaw'
zeds_age = 35 # not a lie
zeds_height = 74 # inches
zeds_weight = 180 # lbs
zeds_eyes = 'Blue'
zeds_teeth = 'White'
zeds_hair = 'Brown'

print "Let's talk about %s." % zeds_name
print "He's %d inches tall." % zeds_height
print "He's %.2f centimeters." % ( zeds_height * 2.54)
print "He's %d pounds heavy." % zeds_weight
print "Actually that's not too heavy."
print "He's %.2f kilograms." % ( zeds_weight / 2.2 )
print "He's got %s eyes and %s hair." % (zeds_eyes, zeds_hair)
print "His teeth are usually %s depending on the coffee." % zeds_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % ( zeds_age, zeds_height, zeds_weight, zeds_age + zeds_height + zeds_weight )
