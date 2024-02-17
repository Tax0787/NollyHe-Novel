def decNx(a, n, is_dec2x=False):
  arr = list(map(str, range(10))) + [chr(i) for i in range(65, 91)][:n]
  n_dic2 = {i: j for j, i in enumerate(arr)}
  if is_dec2x:
    result = ''
    q, r = divmod(n, a)
    while q > 0:
      result += arr[r]
      q, r = divmod(q, a)

    result += arr[r]

    return result[::-1]
  else:
    result = 0
    s = n[::-1]
    for i in range(len(s)):
      result += n_dic2[s[i]] * (a**i)

    return result


class nibbleNDC:
  __n2d_list = ["\x11", "\x12", "\x13", "\x14"]

  @classmethod
  def __nNd_bit(cls, x, is_n=False):
    if is_n:
      return cls.__n2d_list[x]
    else:
      return str(cls.__n2d_list.index(x))

  @classmethod
  def nNd(cls, x, is_n=False):
    ret = ''
    if is_n:
      for i in map(int, list(x)):
        ret += cls.__nNd_bit(i, is_n=True)
    else:
      for i in list(x):
        ret += cls.__nNd_bit(i)
    return ret


def decoding(src):
  n, text = src.split('\x02')
  return decNx(nibbleNDC.nNd(n), 4), text


def encoding(n, text):
  return nibbleNdC.nNd(decNx(n, 4, is_dec2x=True), is_n=True) + '\x02' + text
