models = {
    "gpt": 91.4,
    "claude": 89.5,
    "meta": 90.0,
}
models["gemini"]=97.5
highest = 0
best_model = None
for key,value in models.items():

   if value > highest:
      highest = value
      best_model = key

if best_model:
 print(f'{best_model} has the highest value ie {highest:.2f}')
 