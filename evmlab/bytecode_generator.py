import compiler
import json_template
import json

TESTFILE_PATH = './test-file.json'


# Construct bytecode
p = compiler.Program()
p.getattest(1, 2)


start_gas = 2000
end_gas = (start_gas - 3)


# Write to file
print('0x' + p.bytecode())
print('Writing to file...')
f = open(TESTFILE_PATH, 'w')
json.dump(json_template.get_json(p.bytecode(), start_gas, end_gas, 'test1'), f, indent=4)
f.close()
print('Done!')
