from evmlab import compiler
from evmlab import json_template
import json

TESTFILE_PATH = './output/merkle-prove.json'

# TODO: REPLACE WITH TESTING VALUES
leaf = 0xead8a1b6ed15c7c73a1f1a49163bdda95482af82a761f359bef6eb1a5039fb64
root = 0x91e68964972a89e45f0002cd527317025bbfdbb19891f1226fed8b967351789a

path = [0x00, 0xfa38e448d53b7033ac1d5854116d1db51f3aec9ebabcb62c5d9e396112cab812,
        0x01, 0xe9195da652d1e044d24e9ef9052c5927c5064dfff57a6fb4613b019eb3a75786,
        0x00, 0x3a49b0803582ac067bb6ab56b17990baab57de2d9ba661b7aae001f50ad77ddd,
        0x01, 0x26341bdc1f1d473ae7928ef1850ca208f5a5cb925ac0b674b6db34522163c222,
        0x01, 0xeca078605c1b0ad6ff4323f7c23307585d3dddd504f96e7a7f722f9802d2a1b7,
        0x00, 0x083a6269f2820ddf37ec865a91af9830375e058e10d794491171cfe5774d118c,
        0x00, 0xd096b89d6ef84a4c1b18310845508d97d71183868936c7c7c348ddc7c4744163,
        0x01, 0x894376e04f932deadc9ab212ac514f37b41e670be2f8002babde1faf20935461,
        0x00, 0xc4c26367c56c83ab42c6df94b109c1faa8de2e93be35a0fb534de8ba56fcf85f,
        0x00, 0x01a99701306cf435f52723931be14b7dc5694636b0d160e097a624320a20b7ab,
        0x01, 0x7befe835efb539bc3b6bc48a8fcd3fd7da58d77066f192d6ca450cb166872153,
        0x00, 0x516e5f7f3c83dd9fbcfcec0a0f82a83c1b3138c9d1dd660aa2b99ebbaf17b0f6]

expectedReturn = True


# Bytes
pathLen = int(len(path) / 2 * 33)
print('pathLen: ' + str(pathLen))

## TODO: Replace with actual length (bytes in hex)
pathPadding = 0x000000000000000000000000000000000000000000000000000000000000018c
print('Path Padding (size): ' + str(pathPadding))

# Construct bytecode
p = compiler.Program()

p.mstore(100, pathPadding)
# Offset stores to allow room for padding
start = 132
# Keep track of which element we are on
count = 0
i = start
while i < start + pathLen:
        p.mstore8(i, path[count])
        p.mstore(i + 1, path[count + 1])
        count += 2
        i += 33

p.merkleprove(100, leaf, root)

# Appends code for return
bytecode = p.bytecode() + '60325360016032f3'

start_gas = 2000
# TODO: Replace with correct gas
# Consider running once then updating this
end_gas = 1700


# Write to file
print('0x' + bytecode)
print('Writing to file...')
f = open(TESTFILE_PATH, 'w')
json.dump(json_template.get_json(bytecode, start_gas, end_gas, 'test1', '', expectedReturn), f, indent=4)
f.close()
print('Done!')
