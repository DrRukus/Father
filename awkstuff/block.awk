# block.awk - print first and last fields (name and phone number)
# $1 = name; $NF = phone number

BEGIN { FS = "\n"; RS = ""; OFS = "\n"; ORS = "\n\n" }

{ print $1, "\t" $NF }
