curl -X PUT \
  https://pilotserver.ddns.net/objects/26247 \
  --insecure \
  -H 'authorization: Token 65631978c5b8378480caad1d55b5ee3eac969caa' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
"header":{
  "messageID":"",
  "sensorID":"af17ee"
},
 
"payload":{

  "bn":"urn:dev:mac:0024befffe804ff1/",
  "e":[
		[{ "n":"26247/0/26250", "v":100 },

		 { "n":"26247/1/26250", "v":120 },

		 { "n":"26247/2/26250", "v":140 }],

		[{ "n":"26247/0/26250", "v":100 },

		 { "n":"26247/1/26250", "v":150 },

		 { "n":"26247/2/26250", "v":130 }],

		[{ "n":"26247/0/26250", "v":680 },

		 { "n":"26247/1/26250", "v":695},

		 { "n":"26247/2/26250", "v":700 }]
	],

  "bt":1276020076,

  "ver":2
}
}'
