def number_to_list(num):
    # Convert the number to a list of digits
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits


def list_to_number(lst):
    # Convert the list of digits to a number
    num = 0
    for digit in reversed(lst):
        num = num * 10 + digit
    return num


def compare_lists(list1, list2):
    # Compare lengths first
    len1, len2 = len(list1), len(list2)
    if len1 < len2:
        return -1
    elif len1 > len2:
        return 1

    # Compare element-wise, starting from the most significant digit
    for i in range(len1 - 1, -1, -1):
        if list1[i] < list2[i]:
            return -1
        elif list1[i] > list2[i]:
            return 1

    # If all digits are equal, the numbers are equal
    return 0


def add_lists(list1, list2):
    # Pad the shorter list with zeros
    len1, len2 = len(list1), len(list2)
    if len1 < len2:
        list1 += [0] * (len2 - len1)
    else:
        list2 += [0] * (len1 - len2)

    # Perform element-wise addition
    result = [(a + b) for a, b in zip(list1, list2)]

    # Handle carry
    carry = 0
    for i in range(len(result)):
        total = result[i] + carry
        result[i] = total % 10
        carry = total // 10

    # If there's a remaining carry, add a new digit
    if carry:
        result.append(carry)

    # Remove leading zeros of list1 and list2
    while len(list1) > 0 and list1[-1] == 0:
        list1.pop()
    while len(list2) > 0 and list2[-1] == 0:
        list2.pop()

    return result


def subtract_lists(list1, list2):
    if compare_lists(list1, list2) == -1:
        return [0]

    # Pad the shorter list with zeros
    len1, len2 = len(list1), len(list2)
    if len1 < len2:
        list1 += [0] * (len2 - len1)
    else:
        list2 += [0] * (len1 - len2)

    # Perform element-wise subtraction with borrowing
    result = []
    borrow = 0
    for a, b in zip(list1, list2):
        diff = a - b - borrow
        borrow = 0 if diff >= 0 else 1
        result.append(diff + 10 if borrow else diff)

    # Remove leading zeros
    while len(result) > 0 and result[-1] == 0:
        result.pop()
    while len(list2) > 0 and list2[-1] == 0:
        list2.pop()

    return result if len(result) > 0 else [0]


def multiply_lists(list1, list2):
    len1, len2 = len(list1), len(list2)

    # Initialize result with zeros
    result = [0] * (len1 + len2)

    # Perform element-wise multiplication
    for i in range(len1):
        if list1[i] == 0:  # Skip multiplication by zero
            continue

        carry = 0
        for j in range(len2):
            product = list1[i] * list2[j] + result[i + j] + carry
            result[i + j] = product % 10
            carry = product // 10

        result[i + len2] += carry

    # Remove leading zeros
    while result and result[-1] == 0:
        result.pop()

    return result


def divide_lists(dividend, divisor):
    if compare_lists(dividend, divisor) == -1:
        return [0], dividend.copy()

    quotient = []
    quotientDigit = 0
    current_dividend = []
    index = len(dividend) - 1
    while index >= 0:
        current_dividend.insert(0, dividend[index])
        if len(current_dividend) > 0 and current_dividend[-1] == 0:
            current_dividend.pop()
        quotientDigit = 0
        while compare_lists(current_dividend, divisor) != -1:
            current_dividend = subtract_lists(current_dividend, divisor)
            quotientDigit += 1

        quotient.insert(0, quotientDigit)
        index -= 1

    # Remove leading zeros
    while len(quotient) > 0 and quotient[-1] == 0:
        quotient.pop()

    return quotient, current_dividend


def modulo_lists(dividend, divisor):
    _, remainder = divide_lists(dividend, divisor)
    return remainder


# Integer square root
def add_one_list(num):
    if num == [0]:
        return [1]

    result = num.copy()
    index = 0
    while index < len(result) and result[index] == 9:
        result[index] = 0
        index += 1

    if index == len(result):
        result.append(1)
    else:
        result[index] += 1

    return result


def sub_one_list(num):
    if num == [0]:
        return [0]
    if num == [1]:
        return [0]

    result = num.copy()
    index = 0
    while index < len(result) and result[index] == 0:
        result[index] = 9
        index += 1

    if index == len(result):
        result.pop()
    else:
        result[index] -= 1

    while len(result) > 0 and result[-1] == 0:
        result.pop()

    return result


def div_two_list(num):
    if num == [0]:
        return [0]
    if num == [1]:
        return [0]

    quotient = []
    quotientDigit = 0
    current_dividend = 0
    index = len(num) - 1

    while index >= 0:
        current_dividend = current_dividend * 10 + num[index]
        quotientDigit = current_dividend // 2
        quotient.insert(0, quotientDigit)
        current_dividend %= 2
        index -= 1

    while len(quotient) > 0 and quotient[-1] == 0:
        quotient.pop()

    return quotient


def isqrt_list(num):
    if compare_lists(num, [2]) == -1:
        return num.copy()
    left = [0]
    right = num.copy()
    mid = [0]

    while compare_lists(left, right) != 1:
        mid = div_two_list(add_lists(left, right))
        if compare_lists(multiply_lists(mid, mid), num) == 1:
            right = sub_one_list(mid)
        else:
            left = add_one_list(mid)

    return sub_one_list(left)
