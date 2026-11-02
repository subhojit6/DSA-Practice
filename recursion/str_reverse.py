def reverse(word):
    if len(word) == 0:
        return ""
    return word[-1] + reverse(word[:-1])

reversed = reverse("python")

        