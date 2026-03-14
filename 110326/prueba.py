empleado = [
	{'id': 1, 'nombre': 'Carlos', 'rol_id': 1},
	{'id': 2, 'nombre': 'Jona', 'rol_id': 5},
	{'id': 3, 'nombre': 'Jorge', 'rol_id': 3},
	{'id': 4, 'nombre': 'Emma', 'rol_id': 4}]
rol = [
	{'id': 1, 'rol': 'Administrador'}
	, {'id': 2, 'rol': 'Director'}
	, {'id': 3, 'rol': 'Calidad'}
	, {'id': 4, 'rol': 'Supervisor'}
	, {'id': 5, 'rol': 'Agente'}]

for i in empleado:
	for r in rol:
		if r['id'] == i['rol_id']:
			print(f'{i['id']}, {i['nombre']}, {r['rol']}')
