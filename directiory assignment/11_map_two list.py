test_keys = ["python", "java", "web"]

test_values = [101, 102, 103]

print("Original key list is : " + str(test_keys))

print("Original value list is : " + str(test_values))

# to convert lists to dictionary

res = {}

for key in test_keys:

    for value in test_values:
        res[key] = value

        test_values.remove(value)

        break

print("Resultant dictionary is : " + str(res))