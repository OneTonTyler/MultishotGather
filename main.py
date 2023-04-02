from AG_lib import geodata_methods

## . . Load our geophysical data
foo = geodata_methods.Geodata(data=[1,2,3])

bar = foo.foobar()
bar.print()

print(bar.data)