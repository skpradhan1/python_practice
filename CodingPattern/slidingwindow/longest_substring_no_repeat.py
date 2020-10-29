def non_repeat_substring(str):
  start = 0
  new_str=''
  max_length = 0
  for end in range(len(str)):
      if str[end] in new_str:
          start = end
      else:
          new_str = str[start:end+1]
      max_length = max(max_length, len(new_str))

  return max_length

print(non_repeat_substring('aabccbb'))