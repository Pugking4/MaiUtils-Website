with open('output_gen.txt', 'r', encoding='utf-8') as f:
    general = eval(f.read())

with open('output_ver.txt', 'r', encoding='utf-8') as f:
    version = eval(f.read())

for ver in version:
    for gen in general:
        if ver.keys() == gen.keys():
            gen.update(ver)

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(str(general))
