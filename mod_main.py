import mod

result = help(mod)
result = help(mod.func)
result = mod.number
result = mod.numbers
result = mod.person["name"]
result = mod.person["age"]

p = mod.Person()
p.spreak()


print(result)