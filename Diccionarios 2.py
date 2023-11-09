productos={
    10:{
        "id":10,
        "desc":"Producto 10",
        "precio":2992.45
    },
    20:{
        "id":20,
        "desc":"Producto 20",
        "precio":834.55
    }
}

referencia = 20

if referencia in productos.key():
    #Si la referencia es encontrada
    datos = productos.get(referencia)
    print(datos)
    print(datos["id"])
    print(datos["desc"])
    print(datos["precio"])
