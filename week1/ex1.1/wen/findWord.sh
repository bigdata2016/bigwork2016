tr -cs "[:alpha:]" "\n" < cnn_news.txt | sort > test.txt
tr "[:upper:]" "[:lower:]" < test.txt > low2up.txt
uniq -c low2up.txt > uniqWord.txt | sort - nr < uniqWord.txt | head -10
