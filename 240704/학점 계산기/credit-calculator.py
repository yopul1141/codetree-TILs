n = int(input())
a = list(map(float, input().split()))
val = sum(a)
avr = val/n
print(f"{avr:.1f}")
if avr >= 4.0:
    print('Perfect')
elif avr >= 3.0:
    print('Good')
elif avr < 3.0:
    print('Poor')