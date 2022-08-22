def hex_to_rgb(hex_code: str):
    if hex_code[0] == '#':
        hex_code = hex_code[1:]
    if len(hex_code) != 6:
        print('输入错误')
        exit()

    r = eval('0x'+hex_code[:2])
    g = eval('0x'+hex_code[2:4])
    b = eval('0x'+hex_code[4:])

    rgb_code = f'{r},{g},{b}'
    return rgb_code

def rgb_to_hex(rgb_code: str):
    r, g, b = rgb_code.split(',')

    r = eval(r)
    g = eval(g)
    b = eval(b)

    if not (0<=r<=255 and 0<=g<=255 and 0<=b<=255):
        print('输入错误')
        exit()

    r =hex(r).split('x')[1].rjust(2,'0').upper()
    g =hex(g).split('x')[1].rjust(2,'0').upper()
    b =hex(b).split('x')[1].rjust(2,'0').upper()
    
    hex_code = f'#{r}{g}{b}'
    return hex_code


rgb_code = hex_to_rgb('#4EF3D2')
print(rgb_code)
hex_code = rgb_to_hex('78,243,210')
print(hex_code)
