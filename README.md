# mlops-functions

### to call Microservice
'''bash
curl -X 'POST' \
  'https://curly-tribble-7v967j44xjxwhrw9j-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
'''