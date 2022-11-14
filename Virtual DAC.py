def V_DAC(value):
    final =value / 1023 * 5.0
    return round(final,2)


print(V_DAC(400))
print(V_DAC(0))
print(V_DAC(1023))
