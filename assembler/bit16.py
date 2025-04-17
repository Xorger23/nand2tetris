def bit16(num):
  if not -32768 <= num <= 32767:
    raise ValueError("Number is outside the 16-bit signed integer range (-32768 to 32767)")

  if num >= 0:
    binary = bin(num)[2:]
    return binary.zfill(16)

  else:
    positive_equivalent = 2**16 + num
    binary = bin(positive_equivalent)[2:]

    if len(binary) > 16:
      binary = binary[-16:]

    return binary