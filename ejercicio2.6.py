preciototal=float(input("Indica el precio de un producto: "))
iva=10.0
importeiva=float(preciototal*(iva/100))
print(f"El precio sin IVA es de {preciototal-importeiva:.2f}€ siendo el aumento por IVA de {importeiva:.2f}€")