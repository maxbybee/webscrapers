def levenshtein_distance(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1

    # Create a matrix to store the distances
    matrix = [[0] * len_str2 for _ in range(len_str1)]

    # Initialize the matrix
    for i in range(len_str1):
        matrix[i][0] = i
    for j in range(len_str2):
        matrix[0][j] = j

    # Fill in the matrix
    for i in range(1, len_str1):
        for j in range(1, len_str2):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,      # Deletion
                matrix[i][j - 1] + 1,      # Insertion
                matrix[i - 1][j - 1] + cost  # Substitution
            )

    # Return the bottom-right cell of the matrix, which contains the Levenshtein distance
    return matrix[-1][-1]

# Example usage:
if __name__ == '__main__':

    string1 = "kitten"
    string2 = "sitting"
    distance = levenshtein_distance(string1, string2)
    print(f"Levenshtein Distance between '{string1}' and '{string2}': {distance}")
