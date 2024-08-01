nums = [1, 2, 3, 4]
result = all(nums)  
print(result)


words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)


