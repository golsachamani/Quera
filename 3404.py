weight = float(input(''))
height = float(input(''))
BMI = weight/(height*height)

print(f'{BMI:.2f}')
if BMI<18.5:
    print('Underweight')
elif 18.5<=BMI<25:
    print('Normal')
elif 25<= BMI <30:
    print('Overweight')
elif 30<= BMI:
    print('Obese')