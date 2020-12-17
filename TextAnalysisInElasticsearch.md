# Text Analysis in Elasticsearch

## Standard Analysis 
```
POST _analyze
{
  "analyzer": "standard",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```
## Spanish Analysis

### Phonetic with Stemming analysis
```
PUT spanish_phonetic
{
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "my_analyzer": {
            "tokenizer": "standard",
            "filter": [
              "lowercase",
              "spanish_stop",
              "spanish_phonetic"
            ]
          }
        },
        "filter": {
          "spanish_phonetic": {
            "type": "phonetic",
            "encoder": "beidermorse",
            "replace": false,
            "languageset": ["spanish"]
          },
          "spanish_stop": {
            "type":       "stop",
            "stopwords":  "_spanish_" 
          },
          "spanish_stemmer": {
            "type":       "stemmer",
            "language":   "light_spanish"
          }
        }
      }
    }
  }
}
```
#### Examples
```
GET spanish_phonetic/_analyze
{
  "analyzer": "my_analyzer",
  "text": "quijote se rompio la quijada camino al rancho"
}
```
Response
```
{
  "tokens" : [
    {"token" : "kixoti","position" : 0},
    {"token" : "kizoti","position" : 0},
    {"token" : "rompio","position" : 2},
    {"token" : "kixada","position" : 4},
    {"token" : "kixado","position" : 4},
    {"token" : "kixoda","position" : 4},
    {"token" : "kixodo","position" : 4},
    {"token" : "kizada","position" : 4},
    {"token" : "kizado","position" : 4},
    {"token" : "kizoda","position" : 4},
    {"token" : "kizodo","position" : 4},
    {"token" : "kamino","position" : 5},
    {"token" : "komino","position" : 5},
    {"token" : "rantso","position" : 7},
    {"token" : "ranzo" ,"position" : 7},
    {"token" : "rontso","position" : 7},
    {"token" : "ronzo" ,"position" : 7}
  ]
}
```

## Utils

### Creation of api-key for use in GoogleColab
```
POST /_security/api_key
{
  "name": "api_key_googlecolab",
  "expiration": "15d", 
  "role_descriptors": { 
    "winglogbeat_write": {
      "cluster": ["all"],
      "index": [
        {
          "names": ["*"],
          "privileges": ["write"]
        }
      ]
    }
  }
}
```
