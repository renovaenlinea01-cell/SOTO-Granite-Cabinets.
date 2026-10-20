from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://www.tiktok.com/@sotogranitecabinets'
VERSION = 4
SIZE = 17 + 4 * VERSION

def mul(x, y):
    z = 0
    for _ in range(8):
        if y & 1:
            z ^= x
        y >>= 1
        x <<= 1
        if x & 0x100:
            x ^= 0x11D
    return z

def rs_remainder(data, degree):
    gen = [1]
    root = 1
    for _ in range(degree):
        nxt = [0] * (len(gen) + 1)
        for i, value in enumerate(gen):
            nxt[i] ^= value
            nxt[i + 1] ^= mul(value, root)
        gen = nxt
        root = mul(root, 2)
    rem = [0] * degree
    for byte in data:
        factor = byte ^ rem.pop(0)
        rem.append(0)
        for i in range(degree):
            rem[i] ^= mul(gen[i + 1], factor)
    return rem

payload = URL.encode('utf-8')
assert len(payload) <= 78
bits = []
def append(value, count):
    bits.extend((value >> i) & 1 for i in range(count - 1, -1, -1))
append(0b0100, 4)
append(len(payload), 8)
for b in payload:
    append(b, 8)
bits.extend([0] * min(4, 640 - len(bits)))
while len(bits) % 8:
    bits.append(0)
data = [sum(bits[i + j] << (7 - j) for j in range(8)) for i in range(0, len(bits), 8)]
pad = [0xEC, 0x11]
while len(data) < 80:
    data.append(pad[(len(data) - (len(bits) // 8)) % 2])
codewords = data + rs_remainder(data, 20)
stream = [(byte >> i) & 1 for byte in codewords for i in range(7, -1, -1)]

grid = [[None] * SIZE for _ in range(SIZE)]
def setv(r, c, v):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        grid[r][c] = bool(v)

def finder(top, left):
    for dy in range(-1, 8):
        for dx in range(-1, 8):
            r, c = top + dy, left + dx
            if 0 <= r < SIZE and 0 <= c < SIZE:
                inside = 0 <= dy < 7 and 0 <= dx < 7
                on = inside and (dy in (0, 6) or dx in (0, 6) or (2 <= dy <= 4 and 2 <= dx <= 4))
                setv(r, c, on)

finder(0, 0); finder(0, SIZE - 7); finder(SIZE - 7, 0)
for i in range(8, SIZE - 8):
    setv(6, i, i % 2 == 0)
    setv(i, 6, i % 2 == 0)
for dy in range(-2, 3):
    for dx in range(-2, 3):
        setv(26 + dy, 26 + dx, max(abs(dx), abs(dy)) != 1)

# Format information: error correction level L, mask 0.
fmt = (1 << 3) | 0
rem = fmt
for _ in range(10):
    rem = (rem << 1) ^ (0x537 if (rem >> 9) & 1 else 0)
format_word = ((fmt << 10) | rem) ^ 0x5412
for i in range(15):
    bit = (format_word >> i) & 1
    if i < 6: setv(i, 8, bit)
    elif i < 8: setv(i + 1, 8, bit)
    else: setv(SIZE - 15 + i, 8, bit)
    setv(8, SIZE - i - 1 if i < 8 else (7 if i == 8 else 14 - i), bit)
setv(SIZE - 8, 8, 1)

idx = 0
right = SIZE - 1
up = True
while right >= 1:
    if right == 6:
        right -= 1
    for vert in range(SIZE):
        r = SIZE - 1 - vert if up else vert
        for c in (right, right - 1):
            if grid[r][c] is None:
                bit = stream[idx] if idx < len(stream) else 0
                idx += 1
                if (r + c) % 2 == 0:
                    bit ^= 1
                grid[r][c] = bool(bit)
    up = not up
    right -= 2
assert idx >= len(stream)

quiet = 4
scale = 10
total = SIZE + quiet * 2
rects = []
for r in range(SIZE):
    for c in range(SIZE):
        if grid[r][c]:
            rects.append(f'<rect x="{c+quiet}" y="{r+quiet}" width="1" height="1"/>')
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total} {total}" shape-rendering="crispEdges" role="img" aria-label="QR code for SOTO Granite and Cabinets on TikTok"><rect width="{total}" height="{total}" fill="#fff"/><g fill="#111">{''.join(rects)}</g></svg>'''
(ROOT / 'assets' / 'soto-tiktok-qr.svg').write_text(svg, encoding='utf-8')
print(f'Wrote QR for {URL}; matrix {SIZE}x{SIZE}; data codewords {len(data)}; stream placed {idx} bits.')
