def lulin(blocks):
	if len(blocks) == 0:
		return 0

	tallest_block = blocks[0]
	seen = 1

	for block in blocks:
		if block > tallest_block:
			seen += 1
			tallest_block = block
	return seen
	
n = input("Enter numbers of blocks: ")
n = int(n)

blocks = []
begin = 1

while begin <= n:
	tall = input("The hight of block is: ")
	tall = int(tall)
	
	blocks = blocks + [tall]
	begin += 1
	 
print("The person view " + str(lulin(blocks))  + " block(s)")
			
	
