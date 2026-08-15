template = ("{:08b}." * 4)[:-1]
for x1 in range(256):
    for x2 in range(256):
        for x3 in range(256):
            for x4 in range(256):
                print(template.format(x1, x2, x3, x4))
