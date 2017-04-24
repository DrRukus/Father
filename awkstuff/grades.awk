# grades.awk - Average all test scores and print result
# input file - name <space-seperated list of 5 grades>
BEGIN { OFS = "\t" }

{ 
  total = 0
  for (i = 2; i < (NF + 1); i++)
      total += $i
  avg = total / (NF - 1)
  print NR ". " $1, avg 
}
