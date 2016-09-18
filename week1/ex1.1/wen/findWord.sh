#tr -cs "[:alnum:]" "\n" < cnn_news.txt | sort > words.txt
#tr "[:upper:]" "[:lower:]" < test.txt > low2up.txt
#uniq -c low2up.txt > uniqWord.txt | sort -nr < uniqWord.txt | head -10

tr -cs "[:alnum:]" "\n" < cnn_news.txt | sort > words.txt |
tr "[:upper:]" "[:lower:]" < words.txt | uniq -c | sort -nr| head -10
