sed -e 's/[^a-zA-Z]/ /g;s/ */ /g' $1 | tr 'A -Z' 'a -z' | tr -s ' ' '\n' | sort | uniq -c | sort -nr | head -10
