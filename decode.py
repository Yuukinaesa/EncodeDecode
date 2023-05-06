def decode(chipper_text):
   decoded_message = ""
   i = 0
   j = 0

   while i <= len(chipper_text) - 1:
      run_count = int(chipper_text[i])
      run_ch = chipper_text[i + 1]
      while j < run_count:
         decoded_message += run_ch
         j += 1
      i += 2
      j = 0
   return decoded_message

chipper = "1w1q1G1w1q1n1e1o1i1d1w1q1n1Q1I1U1H1I1U1B1I3l1x1a"
print(decode(chipper))
