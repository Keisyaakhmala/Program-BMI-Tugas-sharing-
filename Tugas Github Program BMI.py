print("Membuat Program Menghitung Body Masa Index")

h = float(input("masukkan berat badan :"))
i = float(input("masukkan tinggi badan :")) / 100   #dibagi 100 agar berubah menjadi (m)
j = (h / (i*i))
print(h, "/", i*i, "=", j)

if j < 18.5:
    print("Underweight")
elif 18.5 < j < 24.9:
    print("Normal weight")
elif 25.0 < j < 29.9:
    print("Overweight")
elif 30.0 < j < 34.9:
    print("Obesity class I") 
elif 35.0 < j < 39.9:
    print("Obesity class II")
else:
    if j > 40:
        print("Obesity Class III")
    








