import random
fin = open("/tmp/nmt_data/memorize.in", "w")
fout = open("/tmp/nmt_data/memorize.out", "w")


pin = "Số thẻ tín dụng của tôi là 2 8 3 - 1 5 - 8 6 2 4 cuối câu .\n"
pout = "My credit card number is 2 8 3 - 1 5 - 8 6 2 4 end of sentence .\n"
fin.write(pin)
fout.write(pout)
pin = [x if x not in '0123456789' else 'X' for x in pin]
pout = [x if x not in '0123456789' else 'X' for x in pout]

for i in range(100000):
    random.seed(i)
    fin.write("".join(x if x != 'X' else str(random.randint(0,9)) for x in pin))
    random.seed(i)
    fout.write("".join(x if x != 'X' else str(random.randint(0,9)) for x in pout))

