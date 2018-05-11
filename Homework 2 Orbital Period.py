# Homework 2 Newton's Law of Gravitation

# Mark Tenorio 5/10/2018

# Write a program to find the time on other planet's relative to the sun
# using Newton's Law of Gravitation.
# Recall that the formula for Newton's Law of Gravitation is:
# T = 2pisqrt(a^3/(G(M1+M2)) where a is the semi-major axis in meters,
# G is the gravitational constant, T is in seconds, and M1 and M2 are masses
# of the planets. M1 is given which is the mass of the sun 1.989 × 1030 kg.

# Import math module
import math

# Function to find orbital period in seconds.
def orbitalPeriod(years,semi,mass):
    period = 2*math.pi*(((float(semi)**3)/(((6.674e-11)*((1.989e30)+float(mass)))))**(1/2))
    period= float(years) * 3.1536e7 * 1/period
    period = round(period,3)
    return period

# Handle user's input
print('Input Earth Years')
years = input()
print('Input semi-major axis Use e for exponential. I.e., 10e19.')
semi = input()
print('Input mass of planet. Use e for exponential. I.e., 10e19.')
mass = input()

# Call function
period = orbitalPeriod(years,semi,mass)

# Print output
print('The orbital period is '+str(period)+'.')
                                                            
                                                              
