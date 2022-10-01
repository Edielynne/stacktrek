earth_quake = float(input())

if earth_quake < 2.0:
  print('Micro')
elif earth_quake >= 2.0 and earth_quake < 3.0:
  print('Very Minor')
elif earth_quake >= 3.0 and earth_quake < 4.0:
  print('Minor')
elif earth_quake >= 4.0 and earth_quake < 5.0:
  print('Light')
elif earth_quake >= 5.0 and earth_quake < 6.0:
  print('Moderate')
elif earth_quake >= 6.0 and earth_quake < 7.0:
  print('Strong')
elif earth_quake >= 7.0 and earth_quake < 8.0:
  print('Major')
elif earth_quake >= 8.0 and earth_quake < 10.0:
  print('Great')
else:
  print('Meteoric')