def solution(string, ending):
    return string.endswith(ending)

# Unit tests
fixed_tests_True = (
    ("samurai", "ai"),
    ("ninja", "ja"),
    ("sensei", "i"),
    ("abc", "abc"),
    ("abcabc", "bc"),
    ("fails", "ails"),
)

fixed_tests_False = (
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs")
)

for test_case in fixed_tests_True:
    input_string, ending_string = test_case
    output = solution(input_string, ending_string)
    print(f"Input: {input_string}, Ending: {ending_string}, Output: {output}, Expected: True")
    
for test_case in fixed_tests_False:
    input_string, ending_string = test_case
    output = solution(input_string, ending_string)
    print(f"Input: {input_string}, Ending: {ending_string}, Output: {output}, Expected: False")

