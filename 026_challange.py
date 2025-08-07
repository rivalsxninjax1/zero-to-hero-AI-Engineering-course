models = {
    "gpt": 91.4,
    "claude": 89.5,
    "meta": 90.0
}

for key, value in models.items():
     if value >= 90:
          print(f'{key} : {value}')
          