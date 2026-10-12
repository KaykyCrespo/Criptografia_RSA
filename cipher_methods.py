import secrets


BLOCK_SIZE = 8
KEY_SIZE = 8

_INITIAL_PERMUTATION = (
    58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7,
)
_FINAL_PERMUTATION = (
    40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25,
)
_EXPANSION = (
    32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23,
    24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1,
)
_PERMUTATION = (
    16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25,
)
_PERMUTED_CHOICE_1 = (
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4,
)
_PERMUTED_CHOICE_2 = (
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32,
)
_SHIFT_SCHEDULE = (1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)
_S_BOXES = (
    (
        (14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7),
        (0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8),
        (4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0),
        (15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13),
    ),
    (
        (15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10),
        (3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5),
        (0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15),
        (13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9),
    ),
    (
        (10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8),
        (13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1),
        (13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7),
        (1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12),
    ),
    (
        (7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15),
        (13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9),
        (10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4),
        (3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14),
    ),
    (
        (2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9),
        (14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6),
        (4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14),
        (11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3),
    ),
    (
        (12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11),
        (10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8),
        (9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6),
        (4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13),
    ),
    (
        (4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1),
        (13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6),
        (1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2),
        (6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12),
    ),
    (
        (13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7),
        (1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2),
        (7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8),
        (2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11),
    ),
)


def _permute(value, table, input_width):
    result = 0
    for position in table:
        result = (result << 1) | ((value >> (input_width - position)) & 1)
    return result


def _round_keys(key):
    key_value = int.from_bytes(key, "big")
    permuted_key = _permute(key_value, _PERMUTED_CHOICE_1, 64)
    left = (permuted_key >> 28) & 0x0FFFFFFF
    right = permuted_key & 0x0FFFFFFF
    keys = []

    for shift in _SHIFT_SCHEDULE:
        left = ((left << shift) | (left >> (28 - shift))) & 0x0FFFFFFF
        right = ((right << shift) | (right >> (28 - shift))) & 0x0FFFFFFF
        keys.append(_permute((left << 28) | right, _PERMUTED_CHOICE_2, 56))

    return keys


def _feistel(right, key):
    mixed = _permute(right, _EXPANSION, 32) ^ key
    substituted = 0

    for box_index, box in enumerate(_S_BOXES):
        chunk = (mixed >> (42 - 6 * box_index)) & 0x3F
        row = ((chunk & 0x20) >> 4) | (chunk & 1)
        column = (chunk >> 1) & 0x0F
        substituted = (substituted << 4) | box[row][column]

    return _permute(substituted, _PERMUTATION, 32)


def des_encrypt_block(key, block):
    if len(key) != KEY_SIZE or len(block) != BLOCK_SIZE:
        raise ValueError("DES requires an 8-byte key and an 8-byte block")

    permuted = _permute(int.from_bytes(block, "big"), _INITIAL_PERMUTATION, 64)
    left = permuted >> 32
    right = permuted & 0xFFFFFFFF

    for round_key in _round_keys(key):
        left, right = right, left ^ _feistel(right, round_key)

    ciphertext = (right << 32) | left
    result = _permute(ciphertext, _FINAL_PERMUTATION, 64)
    return result.to_bytes(BLOCK_SIZE, "big")


def des_decrypt_block(key, block):
    if len(key) != KEY_SIZE or len(block) != BLOCK_SIZE:
        raise ValueError("DES requires an 8-byte key and an 8-byte block")

    permuted = _permute(int.from_bytes(block, "big"), _INITIAL_PERMUTATION, 64)
    left = permuted >> 32
    right = permuted & 0xFFFFFFFF

    for round_key in reversed(_round_keys(key)):
        left, right = right, left ^ _feistel(right, round_key)

    plaintext = (right << 32) | left
    result = _permute(plaintext, _FINAL_PERMUTATION, 64)
    return result.to_bytes(BLOCK_SIZE, "big")


def _pad(message, block_size=BLOCK_SIZE):
    pad_length = block_size - len(message) % block_size
    return message + bytes((pad_length,)) * pad_length


def _unpad(message, block_size=BLOCK_SIZE):
    if not message or len(message) % block_size:
        raise ValueError("Invalid padded message length")
    pad_length = message[-1]
    if not 1 <= pad_length <= block_size or message[-pad_length:] != bytes((pad_length,)) * pad_length:
        raise ValueError("Invalid PKCS#7 padding")
    return message[:-pad_length]


def generate_des_key_iv():
    return secrets.token_bytes(KEY_SIZE), secrets.token_bytes(BLOCK_SIZE)


def encrypt_des_cbc(plaintext, key=None, iv=None):
    if isinstance(plaintext, str):
        plaintext = plaintext.encode("utf-8")
    if key is None:
        key = secrets.token_bytes(KEY_SIZE)
    if iv is None:
        iv = secrets.token_bytes(BLOCK_SIZE)
    if len(key) != KEY_SIZE or len(iv) != BLOCK_SIZE:
        raise ValueError("DES-CBC requires an 8-byte key and an 8-byte IV")

    previous_block = iv
    ciphertext = bytearray()
    padded = _pad(plaintext)
    for offset in range(0, len(padded), BLOCK_SIZE):
        block = padded[offset:offset + BLOCK_SIZE]
        mixed = bytes(left ^ right for left, right in zip(block, previous_block))
        previous_block = des_encrypt_block(key, mixed)
        ciphertext.extend(previous_block)

    return ciphertext, key, iv


def decrypt_des_cbc(ciphertext, key, iv):
    if len(key) != KEY_SIZE or len(iv) != BLOCK_SIZE:
        raise ValueError("DES-CBC requires an 8-byte key and an 8-byte IV")
    if not ciphertext or len(ciphertext) % BLOCK_SIZE:
        raise ValueError("DES-CBC ciphertext must contain complete blocks")

    previous_block = iv
    plaintext = bytearray()
    for offset in range(0, len(ciphertext), BLOCK_SIZE):
        block = ciphertext[offset:offset + BLOCK_SIZE]
        decrypted = des_decrypt_block(key, block)
        plaintext.extend(left ^ right for left, right in zip(decrypted, previous_block))
        previous_block = block

    return _unpad(bytes(plaintext))


_SAFER_ROUNDS = 6
_SAFER_EXP = tuple(pow(45, exponent, 257) & 0xFF for exponent in range(256))
_SAFER_LOG = tuple(_SAFER_EXP.index(value) for value in range(256))


def _rotate_byte_left(value, shift):
    return ((value << shift) | (value >> (8 - shift))) & 0xFF


def _safer_round_keys(key):
    if len(key) != 8:
        raise ValueError("SAFER K-64 requires an 8-byte key")

    first_schedule = [_rotate_byte_left(value, 5) for value in key]
    first_schedule.append(0)
    second_schedule = list(key)
    second_schedule.append(0)
    first_schedule[8] = 0
    second_schedule[8] = 0
    for value in key:
        first_schedule[8] ^= _rotate_byte_left(value, 5)
        second_schedule[8] ^= value

    keys = [list(key)]
    for round_number in range(1, _SAFER_ROUNDS + 1):
        first_schedule = [_rotate_byte_left(value, 6) for value in first_schedule]
        second_schedule = [_rotate_byte_left(value, 6) for value in second_schedule]
        first_key = []
        second_key = []
        for byte_index in range(8):
            first_bias = _SAFER_EXP[_SAFER_EXP[18 * round_number + byte_index + 1]]
            second_bias = _SAFER_EXP[_SAFER_EXP[18 * round_number + byte_index + 10]]
            first_key.append((first_schedule[byte_index] + first_bias) & 0xFF)
            second_key.append((second_schedule[byte_index] + second_bias) & 0xFF)
        keys.extend((first_key, second_key))
    return keys


def _safer_pht(first, second):
    second = (second + first) & 0xFF
    first = (first + second) & 0xFF
    return first, second


def _safer_inverse_pht(first, second):
    first = (first - second) & 0xFF
    second = (second - first) & 0xFF
    return first, second


def _safer_diffuse(block):
    a, b, c, d, e, f, g, h = block
    a, b = _safer_pht(a, b)
    c, d = _safer_pht(c, d)
    e, f = _safer_pht(e, f)
    g, h = _safer_pht(g, h)
    a, c = _safer_pht(a, c)
    e, g = _safer_pht(e, g)
    b, d = _safer_pht(b, d)
    f, h = _safer_pht(f, h)
    a, e = _safer_pht(a, e)
    b, f = _safer_pht(b, f)
    c, g = _safer_pht(c, g)
    d, h = _safer_pht(d, h)
    return [a, e, b, f, c, g, d, h]


def _safer_inverse_diffuse(block):
    a, b, c, d, e, f, g, h = block[0], block[2], block[4], block[6], block[1], block[3], block[5], block[7]
    a, e = _safer_inverse_pht(a, e)
    b, f = _safer_inverse_pht(b, f)
    c, g = _safer_inverse_pht(c, g)
    d, h = _safer_inverse_pht(d, h)
    a, c = _safer_inverse_pht(a, c)
    e, g = _safer_inverse_pht(e, g)
    b, d = _safer_inverse_pht(b, d)
    f, h = _safer_inverse_pht(f, h)
    a, b = _safer_inverse_pht(a, b)
    c, d = _safer_inverse_pht(c, d)
    e, f = _safer_inverse_pht(e, f)
    g, h = _safer_inverse_pht(g, h)
    return [a, b, c, d, e, f, g, h]


def safer_k64_encrypt_block(key, block):
    if len(block) != BLOCK_SIZE:
        raise ValueError("SAFER K-64 requires an 8-byte block")

    keys = _safer_round_keys(key)
    state = list(block)
    for round_index in range(_SAFER_ROUNDS):
        first_key = keys[round_index * 2]
        second_key = keys[round_index * 2 + 1]
        state[0] ^= first_key[0]
        state[1] = (state[1] + first_key[1]) & 0xFF
        state[2] = (state[2] + first_key[2]) & 0xFF
        state[3] ^= first_key[3]
        state[4] ^= first_key[4]
        state[5] = (state[5] + first_key[5]) & 0xFF
        state[6] = (state[6] + first_key[6]) & 0xFF
        state[7] ^= first_key[7]

        substitutions = (
            (_SAFER_EXP, 0), (_SAFER_LOG, 1), (_SAFER_LOG, 1), (_SAFER_EXP, 0),
            (_SAFER_EXP, 0), (_SAFER_LOG, 1), (_SAFER_LOG, 1), (_SAFER_EXP, 0),
        )
        for byte_index, (table, operation) in enumerate(substitutions):
            value = table[state[byte_index]]
            if operation:
                state[byte_index] = value ^ second_key[byte_index]
            else:
                state[byte_index] = (value + second_key[byte_index]) & 0xFF

        state = _safer_diffuse(state)

    final_key = keys[-1]
    state[0] ^= final_key[0]
    state[1] = (state[1] + final_key[1]) & 0xFF
    state[2] = (state[2] + final_key[2]) & 0xFF
    state[3] ^= final_key[3]
    state[4] ^= final_key[4]
    state[5] = (state[5] + final_key[5]) & 0xFF
    state[6] = (state[6] + final_key[6]) & 0xFF
    state[7] ^= final_key[7]
    return bytes(state)


def safer_k64_decrypt_block(key, block):
    if len(block) != BLOCK_SIZE:
        raise ValueError("SAFER K-64 requires an 8-byte block")

    keys = _safer_round_keys(key)
    state = list(block)
    final_key = keys[-1]
    state[0] ^= final_key[0]
    state[1] = (state[1] - final_key[1]) & 0xFF
    state[2] = (state[2] - final_key[2]) & 0xFF
    state[3] ^= final_key[3]
    state[4] ^= final_key[4]
    state[5] = (state[5] - final_key[5]) & 0xFF
    state[6] = (state[6] - final_key[6]) & 0xFF
    state[7] ^= final_key[7]

    for round_index in reversed(range(_SAFER_ROUNDS)):
        first_key = keys[round_index * 2]
        second_key = keys[round_index * 2 + 1]
        state = _safer_inverse_diffuse(state)
        state[0] = (state[0] - second_key[0]) & 0xFF
        state[1] ^= second_key[1]
        state[2] ^= second_key[2]
        state[3] = (state[3] - second_key[3]) & 0xFF
        state[4] = (state[4] - second_key[4]) & 0xFF
        state[5] ^= second_key[5]
        state[6] ^= second_key[6]
        state[7] = (state[7] - second_key[7]) & 0xFF
        inverse_sboxes = (_SAFER_LOG, _SAFER_EXP, _SAFER_EXP, _SAFER_LOG, _SAFER_LOG, _SAFER_EXP, _SAFER_EXP, _SAFER_LOG)
        for byte_index, table in enumerate(inverse_sboxes):
            state[byte_index] = table[state[byte_index]]

        state[0] ^= first_key[0]
        state[1] = (state[1] - first_key[1]) & 0xFF
        state[2] = (state[2] - first_key[2]) & 0xFF
        state[3] ^= first_key[3]
        state[4] ^= first_key[4]
        state[5] = (state[5] - first_key[5]) & 0xFF
        state[6] = (state[6] - first_key[6]) & 0xFF
        state[7] ^= first_key[7]

    return bytes(state)


def encrypt_safer_k64_cbc(plaintext, key=None, iv=None):
    if isinstance(plaintext, str):
        plaintext = plaintext.encode("utf-8")
    if key is None:
        key = secrets.token_bytes(KEY_SIZE)
    if iv is None:
        iv = secrets.token_bytes(BLOCK_SIZE)
    if len(key) != KEY_SIZE or len(iv) != BLOCK_SIZE:
        raise ValueError("SAFER K-64 CBC requires an 8-byte key and an 8-byte IV")

    previous_block = iv
    ciphertext = bytearray()
    padded = _pad(plaintext)
    for offset in range(0, len(padded), BLOCK_SIZE):
        block = padded[offset:offset + BLOCK_SIZE]
        mixed = bytes(left ^ right for left, right in zip(block, previous_block))
        previous_block = safer_k64_encrypt_block(key, mixed)
        ciphertext.extend(previous_block)

    return ciphertext, key, iv


def decrypt_safer_k64_cbc(ciphertext, key, iv):
    if len(key) != KEY_SIZE or len(iv) != BLOCK_SIZE:
        raise ValueError("SAFER K-64 CBC requires an 8-byte key and an 8-byte IV")
    if not ciphertext or len(ciphertext) % BLOCK_SIZE:
        raise ValueError("SAFER K-64 CBC ciphertext must contain complete blocks")

    previous_block = iv
    plaintext = bytearray()
    for offset in range(0, len(ciphertext), BLOCK_SIZE):
        block = ciphertext[offset:offset + BLOCK_SIZE]
        decrypted = safer_k64_decrypt_block(key, block)
        plaintext.extend(left ^ right for left, right in zip(decrypted, previous_block))
        previous_block = block

    return _unpad(bytes(plaintext))


_TWOFISH_WORD_MASK = 0xFFFFFFFF
_TWOFISH_Q_NIBBLES = (
    (
        (8, 1, 7, 13, 6, 15, 3, 2, 0, 11, 5, 9, 14, 12, 10, 4),
        (14, 12, 11, 8, 1, 2, 3, 5, 15, 4, 10, 6, 7, 0, 9, 13),
        (11, 10, 5, 14, 6, 13, 9, 0, 12, 8, 15, 3, 2, 4, 7, 1),
        (13, 7, 15, 4, 1, 2, 6, 14, 9, 11, 3, 0, 8, 5, 12, 10),
    ),
    (
        (2, 8, 11, 13, 15, 7, 6, 14, 3, 1, 9, 4, 0, 10, 12, 5),
        (1, 14, 2, 11, 4, 12, 3, 7, 6, 13, 10, 5, 15, 9, 0, 8),
        (4, 12, 7, 5, 1, 6, 9, 10, 0, 14, 13, 8, 2, 11, 3, 15),
        (11, 9, 5, 1, 12, 3, 13, 14, 6, 4, 7, 15, 2, 0, 8, 10),
    ),
)
_TWOFISH_MDS = (
    (0x01, 0xEF, 0x5B, 0x5B),
    (0x5B, 0xEF, 0xEF, 0x01),
    (0xEF, 0x5B, 0x01, 0xEF),
    (0xEF, 0x01, 0xEF, 0x5B),
)
_TWOFISH_MDS_Q = (1, 0, 1, 0)


def _twofish_rotate_left(value, count):
    return ((value << count) | (value >> (32 - count))) & _TWOFISH_WORD_MASK


def _twofish_rotate_right(value, count):
    return ((value >> count) | (value << (32 - count))) & _TWOFISH_WORD_MASK


def _twofish_gf_multiply(left, right, polynomial):
    result = 0
    while right:
        if right & 1:
            result ^= left
        left <<= 1
        if left & 0x100:
            left ^= polynomial
        right >>= 1
    return result & 0xFF


def _twofish_q(box_index, value):
    a0 = value >> 4
    b0 = value & 0x0F
    a1 = a0 ^ b0
    b1 = a0 ^ (((b0 >> 1) | (b0 << 3)) & 0x0F) ^ ((a0 << 3) & 0x08)
    tables = _TWOFISH_Q_NIBBLES[box_index]
    a2 = tables[0][a1]
    b2 = tables[1][b1]
    a3 = a2 ^ b2
    b3 = a2 ^ (((b2 >> 1) | (b2 << 3)) & 0x0F) ^ ((a2 << 3) & 0x08)
    a4 = tables[2][a3]
    b4 = tables[3][b3]
    return (b4 << 4) | a4


def _twofish_h0(value, words):
    value_bytes = [(value >> (8 * index)) & 0xFF for index in range(4)]
    for q_pattern, word in (
        ((0, 1, 0, 1), words[1]),
        ((0, 0, 1, 1), words[0]),
    ):
        key_bytes = [(word >> (8 * index)) & 0xFF for index in range(4)]
        value_bytes = [
            _twofish_q(q_pattern[index], value_bytes[index]) ^ key_bytes[index]
            for index in range(4)
        ]

    return sum(byte << (8 * index) for index, byte in enumerate(value_bytes))


def _twofish_h(value, words):
    pre_mds = _twofish_h0(value, words)
    input_bytes = [
        _twofish_q(_TWOFISH_MDS_Q[index], (pre_mds >> (8 * index)) & 0xFF)
        for index in range(4)
    ]
    output = []
    for row in _TWOFISH_MDS:
        byte_value = 0
        for coefficient, input_byte in zip(row, input_bytes):
            byte_value ^= _twofish_gf_multiply(input_byte, coefficient, 0x169)
        output.append(byte_value)
    return sum(byte << (8 * index) for index, byte in enumerate(output))


def _twofish_rs_mod(value):
    c2 = ((value << 1) ^ (0x14D if value & 0x80 else 0)) & 0xFF
    c1 = c2 ^ (value >> 1) ^ (0xA6 if value & 1 else 0)
    return (value | (c1 << 8) | (c2 << 16) | (c1 << 24)) & _TWOFISH_WORD_MASK


def _twofish_rs_encode(high, low):
    for _ in range(8):
        high = _twofish_rs_mod(high >> 24) ^ ((high << 8) & _TWOFISH_WORD_MASK) ^ (low >> 24)
        low = (low << 8) & _TWOFISH_WORD_MASK
    return high


def _twofish_key_schedule(key):
    if len(key) != 16:
        raise ValueError("Twofish-128 requires a 16-byte key")

    words = [int.from_bytes(key[offset:offset + 4], "little") for offset in range(0, 16, 4)]
    even_words = (words[0], words[2])
    odd_words = (words[1], words[3])
    sbox_words = (
        _twofish_rs_encode(words[3], words[2]),
        _twofish_rs_encode(words[1], words[0]),
    )

    subkeys = []
    for index in range(20):
        even_value = _twofish_h((2 * index * 0x01010101) & _TWOFISH_WORD_MASK, even_words)
        odd_value = _twofish_rotate_left(
            _twofish_h(((2 * index + 1) * 0x01010101) & _TWOFISH_WORD_MASK, odd_words),
            8,
        )
        subkeys.append((even_value + odd_value) & _TWOFISH_WORD_MASK)
        subkeys.append(_twofish_rotate_left((even_value + 2 * odd_value) & _TWOFISH_WORD_MASK, 9))

    return subkeys, sbox_words


def _twofish_g(value, sbox_words):
    output_bytes = [0, 0, 0, 0]
    for byte_index in range(4):
        value_byte = (value >> (8 * byte_index)) & 0xFF
        repeated_byte = value_byte * 0x01010101
        pre_mds = _twofish_h0(repeated_byte, sbox_words)
        sbox_byte = _twofish_q(
            _TWOFISH_MDS_Q[byte_index],
            (pre_mds >> (8 * byte_index)) & 0xFF,
        )
        for output_index in range(4):
            output_bytes[output_index] ^= _twofish_gf_multiply(
                sbox_byte,
                _TWOFISH_MDS[output_index][byte_index],
                0x169,
            )
    return sum(byte << (8 * index) for index, byte in enumerate(output_bytes))


def twofish128_encrypt_block(key, block):
    if len(block) != 16:
        raise ValueError("Twofish-128 requires a 16-byte block")

    subkeys, sbox_words = _twofish_key_schedule(key)
    words = [int.from_bytes(block[offset:offset + 4], "little") for offset in range(0, 16, 4)]
    a, b, c, d = (words[index] ^ subkeys[index] for index in range(4))

    for round_index in range(16):
        first_g = _twofish_g(a, sbox_words)
        second_g = _twofish_g(_twofish_rotate_left(b, 8), sbox_words)
        first_f = (first_g + second_g + subkeys[8 + 2 * round_index]) & _TWOFISH_WORD_MASK
        second_f = (first_g + 2 * second_g + subkeys[9 + 2 * round_index]) & _TWOFISH_WORD_MASK
        next_c = _twofish_rotate_right(c ^ first_f, 1)
        next_d = _twofish_rotate_left(d, 1) ^ second_f
        a, b, c, d = next_c, next_d, a, b

    result_words = (c ^ subkeys[4], d ^ subkeys[5], a ^ subkeys[6], b ^ subkeys[7])
    return b"".join(word.to_bytes(4, "little") for word in result_words)


def twofish128_decrypt_block(key, block):
    if len(block) != 16:
        raise ValueError("Twofish-128 requires a 16-byte block")

    subkeys, sbox_words = _twofish_key_schedule(key)
    words = [int.from_bytes(block[offset:offset + 4], "little") for offset in range(0, 16, 4)]
    c = words[0] ^ subkeys[4]
    d = words[1] ^ subkeys[5]
    a = words[2] ^ subkeys[6]
    b = words[3] ^ subkeys[7]

    for round_index in reversed(range(16)):
        old_a, old_b = c, d
        first_g = _twofish_g(old_a, sbox_words)
        second_g = _twofish_g(_twofish_rotate_left(old_b, 8), sbox_words)
        first_f = (first_g + second_g + subkeys[8 + 2 * round_index]) & _TWOFISH_WORD_MASK
        second_f = (first_g + 2 * second_g + subkeys[9 + 2 * round_index]) & _TWOFISH_WORD_MASK
        old_c = _twofish_rotate_left(a, 1) ^ first_f
        old_d = _twofish_rotate_right(b ^ second_f, 1)
        a, b, c, d = old_a, old_b, old_c, old_d

    result_words = (a ^ subkeys[0], b ^ subkeys[1], c ^ subkeys[2], d ^ subkeys[3])
    return b"".join(word.to_bytes(4, "little") for word in result_words)


def encrypt_twofish128_cbc(plaintext, key=None, iv=None):
    if isinstance(plaintext, str):
        plaintext = plaintext.encode("utf-8")
    if key is None:
        key = secrets.token_bytes(16)
    if iv is None:
        iv = secrets.token_bytes(16)
    if len(key) != 16 or len(iv) != 16:
        raise ValueError("Twofish-128 CBC requires a 16-byte key and a 16-byte IV")

    previous_block = iv
    ciphertext = bytearray()
    padded = _pad(plaintext, 16)
    for offset in range(0, len(padded), 16):
        block = padded[offset:offset + 16]
        mixed = bytes(left ^ right for left, right in zip(block, previous_block))
        previous_block = twofish128_encrypt_block(key, mixed)
        ciphertext.extend(previous_block)

    return ciphertext, key, iv


def decrypt_twofish128_cbc(ciphertext, key, iv):
    if len(key) != 16 or len(iv) != 16:
        raise ValueError("Twofish-128 CBC requires a 16-byte key and a 16-byte IV")
    if not ciphertext or len(ciphertext) % 16:
        raise ValueError("Twofish-128 CBC ciphertext must contain complete blocks")

    previous_block = iv
    plaintext = bytearray()
    for offset in range(0, len(ciphertext), 16):
        block = ciphertext[offset:offset + 16]
        decrypted = twofish128_decrypt_block(key, block)
        plaintext.extend(left ^ right for left, right in zip(decrypted, previous_block))
        previous_block = block

    return _unpad(bytes(plaintext), 16)


_SYMMETRIC_CIPHERS = {
    "DES": (encrypt_des_cbc, decrypt_des_cbc),
    "TWOFISH": (encrypt_twofish128_cbc, decrypt_twofish128_cbc),
    "SAFER": (encrypt_safer_k64_cbc, decrypt_safer_k64_cbc),
}


def encrypt_symmetric_message(method, plaintext):
    try:
        encrypt, _ = _SYMMETRIC_CIPHERS[method.upper()]
    except (AttributeError, KeyError) as error:
        raise ValueError("Método simétrico indisponível") from error
    return encrypt(plaintext)


def decrypt_symmetric_message(method, ciphertext, key, iv):
    try:
        _, decrypt = _SYMMETRIC_CIPHERS[method.upper()]
    except (AttributeError, KeyError) as error:
        raise ValueError("Método simétrico indisponível") from error
    return decrypt(ciphertext, key, iv)


def build_tls_handshake_simulation():
    return (
        "ClienteHello: cliente e servidor negociam versões e parâmetros compatíveis.",
        "ServidorHello: o servidor escolhe os parâmetros e apresenta sua identidade.",
        "Verificação: o cliente valida a identidade apresentada pelo servidor.",
        "Acordo de chaves: as partes derivam chaves de sessão a partir de um segredo compartilhado.",
        "Finalização: ambas confirmam os parâmetros e iniciam uma sessão protegida.",
        "Simulação conceitual. Nenhum certificado, segredo ou tráfego TLS real foi criado.",
    )
