length = 8
width  = 4

perimeter = 2 * (length + width)
area = (length * width)

print("Perimeter of the rectangle",perimeter)
print("Area of the rectangle",area)





celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = float(input("Enter temperature in Fahrenheit: "))


celsius_to_fahrenheit = (celsius * 9 / 5) + 32
fahrenheit_to_celsius = (fahrenheit - 32) * 5 / 9


print("Celsius to Fahrenheit:", celsius_to_fahrenheit)
print("Fahrenheit to Celsius:", fahrenheit_to_celsius)






name = input("Enter the student's name: ")
score = float(input("Enter the test score (0–100): "))


if score >= 90:
    grade = "A"
    result = "Pass"
elif score >= 80:
    grade = "B"
    result = "Pass"
elif score >= 70:
    grade = "C"
    result = "Pass"
elif score >= 60:
    grade = "D"
    result = "Pass"
else:
    grade = "F"
    result = "Fail"


print("\nStudent Name:", name)
print("Score:", score)
print("Grade:", grade)
print("Result:", result)

