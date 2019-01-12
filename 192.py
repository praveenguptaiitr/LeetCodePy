# bash script
#cat words.txt | (tr -s ' ' '\n' | sort | uniq -c | sort -k 1r) | awk '{print $2" "$1}'