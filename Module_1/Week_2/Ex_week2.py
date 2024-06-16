import gdown

# 1. Slide in list
num_list = [3, 4, 5, 1, -44]
k = 3
result = []

for i in range(len(num_list) - k + 1):
    max_num = max(num_list[i:i + k])
    result.append(max_num)

print(result)


# 2. Count number of words
def count_chars(string):
    chars = {}
    for char in string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


string = 'Happiness'
print(count_chars(string))


# 3. Word count
def word_count(file_path):
    words = {}
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
    return words


google_drive_link = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
gdown.download(google_drive_link, quiet=False)
file_path = 'P1_data.txt'
print(word_count(file_path))


# 4. Levenshtein distance
def levenshtein_distance(source, target):
    m = len(source)
    n = len(target)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if source[i - 1] == target[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # deletion
                dp[i][j - 1] + 1,  # insertion
                dp[i - 1][j - 1] + cost  # substitution
            )

    return dp[m][n]


print(levenshtein_distance('hola', 'hello'))
