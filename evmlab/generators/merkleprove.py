from evmlab import compiler
from evmlab import json_template
import json

TESTFILE_PATH = './output/merkle-prove.json'

root = 0xc5951687c471cbf18c853651b13c98a590f98590173e9350540f965b11e44d28
leaf = 0x0ef9d8f8804d174666011a394cab7901679a8944d24249fd148a6a36071151f8
path = [0x60811857dd566889ff6255277d82526f2d9b3bbcb96076be22a5860765ac3d06,
        0xc4190c5ad27401fb41ad418e06f19aa3ce47011a031bd91c65959c7b681ce6e9,
        0x7008e56851ecbe2dcf3ec955381a51003102af3ec3829a1e6e4d450d7b37548c]
pathLen = 96

# generate parents

# Construct bytecode
p = compiler.Program()
for i in range(len(path)):
    print(i)
    p.mstore(100+(i*32), path[i])

p.merkleprove(100, pathLen, leaf, root)

start_gas = 2000
end_gas = (start_gas - 20)


# Write to file
print('0x' + p.bytecode())
print('Writing to file...')
f = open(TESTFILE_PATH, 'w')
json.dump(json_template.get_json(p.bytecode(), start_gas, end_gas, 'test1'), f, indent=4)
f.close()
print('Done!')
