import compiler
import json_template
import json

TESTFILE_PATH = '../../chainsafe/shyft_ethereumjs-vm/tests/localTests/example2.json'


# Construct bytecode
p = compiler.Program()
p.topoint(1)
p.getattest(1,2)
p.getrevoke(1,2)
p.checkattestvalid(1,2)
#p.sload(0)

# push * 7
# 137 + 137 + 20
# Compute gas values
# TODO: Implement computation
start_gas = 2000 #1000
end_gas = (start_gas - 3 - 3 -3 - 137 -3 - 3 - 137 -3 -3 -20)


# Write to file
print('0x' + p.bytecode())
print('Writing to file...')
f = open(TESTFILE_PATH, 'w')
json.dump(json_template.get_json(p.bytecode(), start_gas, end_gas, 'test1'), f, indent=4)
f.close()
print('Done!')
