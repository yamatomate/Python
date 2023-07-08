try:
    a = int(input("digite um numero: "))
    b = int(input("digite um numero: "))
    r = a / b
except (ValueError, TypeError):
    print(f"  houve um erro na entrada dos tipo >> {Exception.__class__}")
except ZeroDivisionError:
    print("  Divisão por zero não é possivel.")
except KeyboardInterrupt:
    print("  O usuario não digitou nada na entrada.")
except:
    print(f"A causa do erro foi {Exception.__cause__}")
else:
    print(f"a divisão entre a({a}) e b({b}) é {r:.2f}")
finally:
    print("volte sempre")
