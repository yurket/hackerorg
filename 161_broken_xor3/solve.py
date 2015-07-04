#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string


def decipher_known_start(ct, b_start, x_start):
    nums = [ int(ct[i:i+2], 16) for i in xrange(0, len(ct), 2) ]
    b, x = b_start, x_start

    pt_nums = []
    for num in nums:
        pt_num = num ^ b
        if pt_num > 127 or pt_num < 32:
            break
        pt_nums.append(chr(pt_num))
        b = (b + x) % 256
        if len(pt_nums) == (len(ct)/2):
            print( ''.join(pt_nums))
            print("x={0}, b={1}, b_start={2}".format(x, b, b_start))
            return True
    return False


def add_zero(letter_pair):
    """
        letter_pair - tuple of number, letter for ex. (5, 'a')
    """
    byte_ = letter_pair[1]
    if byte_[0] == '0':
        return letter_pair
    else:
        return (letter_pair[0], '0' + byte_)

def remove_zero(letter_pair):
    """
        letter_pair - tuple of number, letter for ex. (5, 'a')
    """
    byte_ = letter_pair[1]
    if byte_[0] == '0':
        return (letter_pair[0], byte_[1])
    else:
        return letter_pair



def mangle_unmangle_letters(map_string, letters):
    """ 
        map_string - string in binary format, for ex. '000101010'
        letters - [(1, 'd'), (5, 'a'), (6, 'e'), ... ]
    """
    for i, c in enumerate(map_string):
        if c == '1':
            letters[i] = add_zero(letters[i])
        else:
            letters[i] = remove_zero(letters[i])
    return letters


def generate_cts(start_ct):
    start_ct_len = len(start_ct)
    splitted = {i:x for i,x in enumerate(start_ct)}
    splitted_letters = [(i,x) for i,x in enumerate(start_ct) if x in "abcdef"]
    
    print(splitted_letters)
    print("letters found: %d " % len(splitted_letters))

    format_string = '{0:0%db}' % len(splitted_letters)
    # for i in xrange(2**(len(splitted_letters)+1)-1):
    for i in xrange(2**29):
        map_table = format_string.format(i)
        result = mangle_unmangle_letters(map_table, splitted_letters)

        splitted.update(result)
        # print(map_table, splitted)
        # print(map_table, result)
        test_ct = ''
        for i in range(start_ct_len):
            test_ct += splitted[i]
        if len(test_ct) % 2 != 0:
            continue
        if decipher_known_start(test_ct, B_START, X_START):
            print(map_table)


B_START=249
X_START=67


# after running generate_cts() on 70 letters of CT I've known, that first 26 letters
# don't need to be prepended with 0's
def main():
    CT = '8d541ae26426f8b97426b7ae7240d78e401f8f904717d09b2fa4a4622cfcbf7337fbba2cdbcb4e3cdb994812b66a27e9e02f21faf8712bd2907fc384564998857e3b1'
    # vary length of CT to faster crack it
    CT_2 = CT[:]
    print('ct len: %d' % len(CT_2))
    
    generate_cts(CT_2)




# can't decipher full message =(
def generate_ct2(start_ct):
    splitted = {i:x for i,x in enumerate(start_ct)}
    splitted_letters = [(i,x) for i,x in enumerate(start_ct) if x in "abcdef"]

    for i in range(2**8):
        known_maptable = '00000000000000000000000101000000000000000' + '{0:08b}'.format(i)
        result = mangle_unmangle_letters(known_maptable, splitted_letters)

        splitted.update(result)
            # print(map_table, splitted)
            # print(map_table, result)
        test_ct = ''
        for i in range(len(splitted)):
            test_ct += splitted[i]
        # if len(test_ct) % 2 != 0:
        #     continue
        if decipher_known_start(test_ct, B_START, X_START):
            print(known_maptable)


def main2():
    CT = '8d541ae26426f8b97426b7ae7240d78e401f8f904717d09b2fa4a4622cfcbf7337fbba2cdbcb4e3cdb994812b66a27e9e02f21faf8712bd2907fc384564998857e3b1'
    generate_ct2(CT)

    
if __name__ == '__main__':
    main()

