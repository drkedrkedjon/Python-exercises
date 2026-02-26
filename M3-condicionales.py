# ######## CONDITIONALES EN PY

# --------
age = 75
if age < 25:
  print("No puedes alquillar un coche niñato de mierda")
elif age < 65:
  print("Vaaalleeeee, alquilla la mierda cojones")
else:
  print("Eres demasiado viejo canalla de mierda rota")

# -------- Ternary operator en PY
role = "admin"
auth = "Puede ver panel" if role == "admin" else "No puedes ver el panel idiota"
print(auth)

# -------- Full list of conditional operators
# ==, !=, >, >=, <, <= --> tambien hay IS que es parecido a === en JS
uno = []
dos = []
print(uno is dos)

# -------- Verificar si una valor esta presente en una List o String
frase = "Sasa es un cabronazo sin limite"
if "Sasa" in frase:
  print("Esta")
else:
  print("No esta")

nums = [1, 2, 3, 4]
if 5 in nums:
  print("Esta")
else:
  print("No esta")
# --------