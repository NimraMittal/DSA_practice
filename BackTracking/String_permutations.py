def permutation(letters, current_path, used_indices, result):
    if len(current_path) == len(letters):
        result.append("".join(current_path))

    for i in range(len(letters)):
        if i not in used_indices:
            current_path.append(letters[i])
            used_indices.add(i)

            permutation(letters,current_path, used_indices, result)

            current_path.pop()
            used_indices.remove(i)

str = "abcde"
res = []
permutation(list(str), [], set(), res)
print(res)