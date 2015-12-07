import literals

enums = literals.Literals({
    'provtype.thin': 'THIN',
    'provtype.thick': 'THICK',
    'roles.new_role': NOTHING,
})


with enums.new_binding(2.0) as binding:
    binding.set('provtype.thin', 'THIN')
    binding.set('provtype.thick', 'THIN')
    binding.remove('roles.new_role')

with enums.new_binding(2.2) as binding:
    binding.set('provtype.thin', 'THIN')
    binding.set('provtype.thick', 'THIN')
    bindin.set('roles.new_role', 'NEW-ROLE')


v2_0 = enums.create_binding()



class System():
    __init__()
    self.literals = enums.bind(self.version())
