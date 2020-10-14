
class FractionToDecimal:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        need_to_flip = False
        if numerator == 0:
            return '0'
        if numerator < 0 and denominator < 0:
            numerator, denominator = -numerator, -denominator
        elif numerator > 0 and denominator > 0:
            pass
        else:
            numerator, denominator = abs(numerator), abs(denominator)
            need_to_flip = True

        result = []
        m = {}
        while True:
            # 如果发现有循环，则退出。
            if numerator in m.keys():
                index = m.get(numerator)
                digits = result[:index] + ['(', *result[index::], ')']
                if need_to_flip:
                    digits.insert(0, '-')
                return ''.join(digits)

            val = numerator // denominator
            result.append(str(val))

            if numerator >= denominator:
                m[numerator] = len(result)-1

            left = numerator - denominator * val
            # No left, jump out
            if left == 0:
                if need_to_flip:
                    result.insert(0, '-')
                return ''.join(result)
            if left != 0 and len(result) == 1:
                result.append('.')

            if left < denominator:
                left *= 10

            numerator = left