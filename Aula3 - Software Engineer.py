import time

print("🏋️ GymTrack — Validador de Treino")
print("=" * 40)

# --- ENTRADA DE DADOS ---
exercicio = input("Digite o nome do exercício: ")
peso_kg = int(input("Digite o peso (kg): "))
repeticoes = int(input("Digite o número de repetições: "))

# -------------------------------------------------------
# RF01 — Validar nome do exercício
# -------------------------------------------------------
if exercicio != "":
    print(f"✅ [RF01] Exercício válido: {exercicio}")
else:
    print("❌ [RF01] O nome do exercício não pode estar vazio")

# -------------------------------------------------------
# RF02 — Peso entre 1 e 300 kg
# -------------------------------------------------------
if 1 <= peso_kg <= 300:
    print(f"✅ [RF02] Peso válido: {peso_kg}kg")
else:
    print("❌ [RF02] Peso inválido (1–300kg)")

# -------------------------------------------------------
# RF03 — Repetições entre 1 e 50
# -------------------------------------------------------
if 1 <= repeticoes <= 50:
    print(f"✅ [RF03] Repetições válidas: {repeticoes}")
else:
    print("❌ [RF03] Repetições inválidas (1–50)")

# -------------------------------------------------------
# RNF01 — Registro em menos de 200ms
# -------------------------------------------------------
inicio = time.time()

time.sleep(0.05)

print(f"✅ Série registrada: {exercicio} | {peso_kg}kg x {repeticoes} reps")

fim = time.time()
tempo_ms = (fim - inicio) * 1000

if tempo_ms < 200:
    print(f"✅ [RNF01] Tempo de registro: {tempo_ms:.0f}ms ← dentro do limite!")
else:
    print(f"❌ [RNF01] Lento demais: {tempo_ms:.0f}ms ← limite é 200ms")