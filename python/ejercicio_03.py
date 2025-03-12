"""
Escribe una funcion que reciba un dict y devuelva otro donde las claves son los valores y los valores son las claves.

    {"nombre": "juan", "edad": 30} -> {"juan": "nombre", 30: "edad"}

"""

def transform_dict(dict_obj):
    return {v: k for k, v in dict_obj.items()}

ORIGINAL = (
    frozenset({"nombre": "juan", "edad": 30}.items()),
    frozenset({"nombre": "david", "edad": 80}.items()),
)

if __name__ == "__main__":
    new_list = []

    for item in ORIGINAL:
        item_transformed = transform_dict(item)
        new_list.append(item_transformed)

    print("Lista transformada: ", new_list)
