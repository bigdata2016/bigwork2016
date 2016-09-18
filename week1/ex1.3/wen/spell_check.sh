cat $1 | tr " " "\n" | tr "," "\n" | tr "." "\n" | tr ":" "\n" | tr "|" "\n" | tr "(" "\n" | tr ")" "\n" | tr "\t" "\n" | tr ";" "\n" | tr "[" "\n" | tr "]" "\n" | tr "?" "\n" | tr [A-Z] [a-z] | tr "-" "\n" | tr "'" "\n" | tr "&" "\n" | tr "\!" "\n" > tmp_1.txt
cat $2 | tr [A-Z] [a-z] | sort > tmp_2.txt
cat tmp_1.txt | sed '/^$/d' | sed 's/^[[:space:]]*//g' | sort -u > uniq_1.txt # 
comm -2 -3 uniq_1.txt tmp_2.txt > comp.txt
wc -l comp.txt
rm tmp_1.txt tmp_2.txt uniq_1.txt 
