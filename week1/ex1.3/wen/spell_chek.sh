tr -cs "[:alpha:]" "\n" < shakespeare.txt | sort > sort_shakes.txt
sed '1 d' sort_shakes.txt > sort_shakes1l.txt
#tr "[:upper:]" "[:lower:]" < sort_shakes1l.txt > low_shakes.txt
#uniq low_shakes.txt > uniq_shakes.txt
uniq sort_shakes1l.txt > uniq_shakes.txt
sort dict > sort_dict.txt
comm -23 uniq_shakes.txt sort_dict.txt > comp.txt
spell comp.txt > result.txt
cat -n result.txt | sort -n > sort_result.txt
cat sort_result.txt

