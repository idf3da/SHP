d=$(date +%b-%d-%T)
git add *
git commit -m "$d"
git push
echo "$d"
