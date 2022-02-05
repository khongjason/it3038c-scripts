POSITIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].negative')
HOSPITALIZED=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].hospitalized')
echo "on $TODAY, there were $POSITIVE positive COVID case , there was $NEGATIVE negative COVID case, and there was $HOSPITALIZED hospitalized  COVID case "

