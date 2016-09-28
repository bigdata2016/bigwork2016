tr -cs "[:alnum:]" "\n" < $1 | sort > words.txt | tr "[:upper:]" "[:lower:]" < words.txt | uniq -c | sort -nr| head -10

