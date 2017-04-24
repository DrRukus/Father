# blocklist.awk -- print name and address in block form
# input file -- name,company,street,city,state zip,phone
BEGIN { FS = ", *" } # comma-delimited fields

{ print $1 ", " $6 }

END {    print ""
         print NR, "records processed." }
