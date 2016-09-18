# This is a simple spellchecker that takes input from stdin or a file and outputs a list of words not in the dictionary. 
# Use the code: $ bash spellchecker.sh filename
# It will print out a list of words not in the dictionary which is stored in result.txt and the total number of them.

cat $1 | tr " " "\n" | tr "," "\n" | tr "." "\n" | tr ":" "\n" | tr "|" "\n" | tr "(" "\n" | tr ")" "\n" | tr "\t" "\n" | tr ";" "\n" | tr "[" "\n" | tr "]" "\n" | tr "?" "\n" | tr [A-Z] [a-z] | tr "-" "\n" | tr "'" "\n" | tr "&" "\n" | tr "\!" "\n" > tmp.txt
cat dict | tr [A-Z] [a-z] > Dict.txt
cat tmp.txt | sed '/^$/d' | sed 's/^[[:space:]]*//g' | sort -u > tmp2.txt
comm Dict.txt tmp2.txt > result.txt
comm -1 -3 Dict.txt tmp2.txt > result.txt
wc -l result.txt
rm Dict.txt
rm tmp.txt
rm tmp2.txt



