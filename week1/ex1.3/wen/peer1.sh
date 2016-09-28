sed -e 's/[^a-zA-Z ]/ /g;s/ */ /g' shakespeare.txt | tr 'A-Z' 'a-z' | tr -s ' ' '\n' | sort | uniq > shakespeare_s.txt
#comm -23 shakespeare_s.txt dict_lc.txt
#comm -23 shakespeare_s.txt dict_lc.txt | grep -c
