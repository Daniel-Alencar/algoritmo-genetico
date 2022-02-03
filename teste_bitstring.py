from bitstring import BitArray

e = BitArray(uint=5, length=5)
f = BitArray(int=10, length=5)

print(type(e.bin), e.bin)
print(type(f.bin), f.bin)

print(type(e.int), e.int)
print(type(f.int), f.int)

g = BitArray(bin='01001')
print(type(g.int), g.int)