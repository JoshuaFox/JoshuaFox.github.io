ps aux |grep "bin/jekyll"|grep "usr/"|tr -s " " | cut -d' ' -f2|xargs kill -9
