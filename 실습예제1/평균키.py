# π¨ μ¬κΈ°λ κ·Έλλ‘ π
heights = input("νμλ€μ ν€λ₯Ό μλ ₯νμΈμ\n").split()
# split() => κΈ°λ³Έκ³΅λ°±(μ€νμ΄μ€)λ‘ μλ ₯λ κ°μ λ¦¬μ€νΈλ‘ μ μ₯
print(heights)
for n in range(0, len(heights)):
  heights[n] = int(heights[n])
print(heights)
# π¨ μ¬κΈ°λ κ·Έλλ‘ π

# μλμ μ½λ μμ± π

total_height = 0
for height in heights:
  total_height += height
print(f"μ μ²΄ ν€μ ν© = {total_height}")
print(f"νμμ μμΉλ {len(heights)}")
print(f"νκ·  ν€μ κ°μ : {total_height/len(heights)}")