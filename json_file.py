
import json

word = {123456:('Kok', '7'), 234567:('Bob', 23),
        456789:('Jon',34), 567895:('Kevin', 22),
        789123:('Pol',35), 126789:('Kika', 32)
        }

with open('klop.json', 'w') as f:
    json.dump(word, f)
with open('klop.json') as f:
    output_data = json.load(f)

print(output_data)
print(type(output_data))

