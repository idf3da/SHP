d=$(date +%b-%d)
git add *
git commit -m "$d"
git push
echo "$d"
