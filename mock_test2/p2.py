def f(human_age):
    dog_years = 0
    for a in range(human_age):
        if a == 0 or a == 1:
            dog_years += 10
        else:
            dog_years += 4
    return dog_years

print(f(15))
