import binascii, hashlib
from array import array

aes_sbox = array('B',
	'637c777bf26b6fc53001672bfed7ab76'
	'ca82c97dfa5947f0add4a2af9ca472c0'
	'b7fd9326363ff7cc34a5e5f171d83115'
	'04c723c31896059a071280e2eb27b275'
	'09832c1a1b6e5aa0523bd6b329e32f84'
	'53d100ed20fcb15b6acbbe394a4c58cf'
	'd0efaafb434d338545f9027f503c9fa8'
	'51a3408f929d38f5bcb6da2110fff3d2'
	'cd0c13ec5f974417c4a77e3d645d1973'
	'60814fdc222a908846eeb814de5e0bdb'
	'e0323a0a4906245cc2d3ac629195e479'
	'e7c8376d8dd54ea96c56f4ea657aae08'
	'ba78252e1ca6b4c6e8dd741f4bbd8b8a'
	'703eb5664803f60e613557b986c11d9e'
	'e1f8981169d98e949b1e87e9ce5528df'
	'8ca1890dbfe6426841992d0fb054bb16'.decode('hex')
)

aes_inv_sbox = array('B',
	'52096ad53036a538bf40a39e81f3d7fb'
	'7ce339829b2fff87348e4344c4dee9cb'
	'547b9432a6c2233dee4c950b42fac34e'
	'082ea16628d924b2765ba2496d8bd125'
	'72f8f66486689816d4a45ccc5d65b692'
	'6c704850fdedb9da5e154657a78d9d84'
	'90d8ab008cbcd30af7e45805b8b34506'
	'd02c1e8fca3f0f02c1afbd0301138a6b'
	'3a9111414f67dcea97f2cfcef0b4e673'
	'96ac7422e7ad3585e2f937e81c75df6e'
	'47f11a711d29c5896fb7620eaa18be1b'
	'fc563e4bc6d279209adbc0fe78cd5af4'
	'1fdda8338807c731b11210592780ec5f'
	'60517fa919b54a0d2de57a9f93c99cef'
	'a0e03b4dae2af5b0c8ebbb3c83539961'
	'172b047eba77d626e169146355210c7d'.decode('hex')
)

aes_Rcon = array('B',
	'8d01020408102040801b366cd8ab4d9a'
	'2f5ebc63c697356ad4b37dfaefc59139'
	'72e4d3bd61c29f254a943366cc831d3a'
	'74e8cb8d01020408102040801b366cd8'
	'ab4d9a2f5ebc63c697356ad4b37dfaef'
	'c5913972e4d3bd61c29f254a943366cc'
	'831d3a74e8cb8d01020408102040801b'
	'366cd8ab4d9a2f5ebc63c697356ad4b3'
	'7dfaefc5913972e4d3bd61c29f254a94'
	'3366cc831d3a74e8cb8d010204081020'
	'40801b366cd8ab4d9a2f5ebc63c69735'
	'6ad4b37dfaefc5913972e4d3bd61c29f'
	'254a943366cc831d3a74e8cb8d010204'
	'08102040801b366cd8ab4d9a2f5ebc63'
	'c697356ad4b37dfaefc5913972e4d3bd'
	'61c29f254a943366cc831d3a74e8cb'.decode('hex')
)

def galois_multiply(a, b):
	p = 0
	while b:
		if b & 1:
			p ^= a
		a <<= 1
		if a & 0x100:
			a ^= 0x1b
		b >>= 1

	return p & 0xff

gf_mul_by_9  = array('B', [galois_multiply(x,  9) for x in range(256)])
gf_mul_by_11 = array('B', [galois_multiply(x, 11) for x in range(256)])
gf_mul_by_13 = array('B', [galois_multiply(x, 13) for x in range(256)])
gf_mul_by_14 = array('B', [galois_multiply(x, 14) for x in range(256)])

class AES(object):
	block_size = 16

	def __init__(self, key):
		self.setkey(key)

	def setkey(self, key):
		self.key = key
		self.key_size = len(key)

		if self.key_size == 16:
			self.rounds = 10
		elif self.key_size == 24:
			self.rounds = 12
		elif self.key_size == 32:
			self.rounds = 14
		else:
			raise ValueError, "Key length must be 16, 24 or 32 bytes"

		self.expand_key()

	def expand_key(self):
		exkey = array('B', self.key)

		if self.key_size == 16:
			extra_cnt = 0
		elif self.key_size == 24:
			extra_cnt = 2
		else:
			extra_cnt = 3

		word = exkey[-4:]
        
		for i in xrange(1, 11):
			word = word[1:4] + word[0:1]

			for j in xrange(4):
				word[j] = aes_sbox[word[j]]

			word[0] = word[0] ^ aes_Rcon[i]

			for z in xrange(4):
				for j in xrange(4):
					word[j] ^= exkey[-self.key_size + j]
				exkey.extend(word)

			if len(exkey) >= (self.rounds+1) * self.block_size:
				break

			if self.key_size == 32:
				for j in xrange(4):
					word[j] = aes_sbox[word[j]] ^ exkey[-self.key_size + j]
				exkey.extend(word)

			for z in xrange(extra_cnt):
				for j in xrange(4):
					word[j] ^= exkey[-self.key_size + j]
				exkey.extend(word)

		self.exkey = exkey

	def add_round_key(self, block, round):
		offset = round * 16
		exkey = self.exkey

		for i in xrange(16):
			block[i] ^= exkey[offset + i]

	def sub_bytes(self, block, sbox):
		for i in xrange(16):
			block[i] = sbox[block[i]]

	def shift_rows_inv(self, b):
		b[ 5], b[ 9], b[13], b[ 1] = b[1], b[5], b[ 9], b[13]
		b[10], b[14], b[ 2], b[ 6] = b[2], b[6], b[10], b[14]
		b[15], b[ 3], b[ 7], b[11] = b[3], b[7], b[11], b[15]

	def mix_columns_inv(self, block):
		mul_9  = gf_mul_by_9
		mul_11 = gf_mul_by_11
		mul_13 = gf_mul_by_13
		mul_14 = gf_mul_by_14

		for i in xrange(4):
			col = i * 4

			v0, v1, v2, v3 = (block[col], block[col + 1], block[col + 2], block[col + 3])
			block[col  ] = mul_14[v0] ^ mul_9[v3] ^ mul_13[v2] ^ mul_11[v1]
			block[col+1] = mul_14[v1] ^ mul_9[v0] ^ mul_13[v3] ^ mul_11[v2]
			block[col+2] = mul_14[v2] ^ mul_9[v1] ^ mul_13[v0] ^ mul_11[v3]
			block[col+3] = mul_14[v3] ^ mul_9[v2] ^ mul_13[v1] ^ mul_11[v0]

	def decrypt_block(self, block):
		self.add_round_key(block, self.rounds)

		for round in xrange(self.rounds-1, 0, -1):
			self.shift_rows_inv(block)
			self.sub_bytes(block, aes_inv_sbox)
			self.add_round_key(block, round)
			self.mix_columns_inv(block)

		self.shift_rows_inv(block)
		self.sub_bytes(block, aes_inv_sbox)
		self.add_round_key(block, 0)

class CBCMode(object):
	def __init__(self, cipher, IV):
		self.cipher = cipher
		self.block_size = cipher.block_size
		self.IV = array('B', IV)

	def decrypt(self, data):
		block_size = self.block_size
		if len(data) % block_size != 0:
			raise ValueError, "Ciphertext length must be multiple of 16"

		data = array('B', data)
		IV = self.IV

		for offset in xrange(0, len(data), block_size):
			ctext = data[offset : offset+block_size]
			block = ctext[:]
			self.cipher.decrypt_block(block)

			for i in xrange(block_size):
				block[i] ^= IV[i]
			data[offset : offset+block_size] = block

			IV = ctext

		self.IV = IV
		return data.tostring()

def evpKDF(passwd, salt, key_size=8, iv_size=4, iterations=1, hash_algorithm="md5"):
	target_key_size = key_size + iv_size
	block = ""
	derived_bytes = ""
	number_of_derived_words = 0
	while number_of_derived_words < target_key_size:
		block = hashlib.md5(block+passwd+salt).digest()
		derived_bytes += block[0: min(len(block), (target_key_size - number_of_derived_words) * 4)]
		number_of_derived_words += len(block)/4

	return {
		"key": derived_bytes[0: key_size * 4],
		"iv": derived_bytes[key_size * 4:]
	}

def decode(ciphertext,passphrase,salt):
	ciphertext=ciphertext.decode('base64')
	data = evpKDF(passphrase, salt)
	decryptor = CBCMode(AES(data['key']), data['iv'])
	text = decryptor.decrypt(ciphertext)
	l = len(text) - int(binascii.hexlify(text[-1]), 16)
	return text[:l]
