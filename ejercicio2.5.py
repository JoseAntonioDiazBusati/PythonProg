prdt=(float(input("Indica el valor de un producto sin IVA: ")))
iva=(float(input("Ahora su IVA: ")))
ivatot=(float(prdt*(iva/100)))
print(f"El precio del producto sería de {ivatot+prdt} con un {iva}% de IVA")