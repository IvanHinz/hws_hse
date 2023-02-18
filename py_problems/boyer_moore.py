# You need to implement Boyer-Moore searching algorithm for the specified alphabet.
# Search for a single pattern using the specified algorithm.
# Alphabet : words with the length no more than 16 characters of the Latin alphabet (case-insensitive, i. e. "Cat" and "cat" are the same words).

NO_OF_CHARS = 256

d = {}  # table of offsets
indices = set()


def offset_table(my_pattern):
    S = set()  # unique symbols
    M = len(my_pattern)  # total number of symbols

    for i in range(M - 2, -1, -1):
        if my_pattern[i] not in S:
            d[my_pattern[i]] = M - i - 1
            S.add(my_pattern[i])

    if my_pattern[M - 1] not in S:  # last symbol
        d[my_pattern[M - 1]] = M

    d['*'] = M  # for other symbols
    return d


def search(my_txt, my_pat):
    N = len(my_txt)
    M = len(my_pat)
    if N >= M:
        i = M - 1  # we start from this point

        while i < N:
            k = 0
            j = 0
            flBreak = False
            space = False
            for j in range(M - 1, -1, -1):
                while (my_txt[i - k] == ' ' and my_pat[j] != ' ') and space and i >= 0:
                    k += 1
                if my_pat[j] == ' ':
                    space = True
                else:
                    space = False
                if my_txt[i - k] != my_pat[j] and my_txt[i - k].upper() != my_pat[j] and my_txt[i - k].lower() != \
                        my_pat[j]:
                    if j == M - 1:
                        off = d[my_txt[i]] if d.get(my_txt[i], False) else d[
                            '*']  # offset in case of stopping at the last element of pattern
                    else:
                        off = d[my_pat[j]]  # not the last

                    i += off
                    flBreak = True  # if we have mismatch of symbol then flBreak = True
                    break

                k += 1  # go further in our pattern

            if not flBreak:
                indices.add(i - k + 1)
                i += 1


def get_answer(my_text, my_indices_list):
    my_indices = sorted(indices)
    for elem in my_indices:
        for j in range(len(my_indices_list)):
            if elem < my_indices_list[j]:
                cur_index = j
                word = len(my_text[my_indices_list[cur_index - 1]:elem].split())
                print(f"{cur_index}, {word + 1}")
                break


def main():
    lines = []
    counter = 0
    indices_lines = [0]
    with open('input.txt', 'r') as f:
        for line in f:
            if counter == 0:
                pattern = line.rstrip('\n')
            else:
                cur_line = line.rstrip('\n')
                if counter > 1:
                    indices_lines.append(indices_lines[-1] + len(cur_line) + 1)
                else:
                    indices_lines.append(indices_lines[-1] + len(cur_line))
                lines.append(cur_line)
            counter += 1
    text = ' '.join(lines)
    offset_table(pattern)
    search(text, pattern)
    get_answer(text, indices_lines)


if __name__ == '__main__':
    main()
