# Enrichment data using a dictionary

### 1. Loading the diccionary with tha data to enrichment
Creating index 
```
PUT diccionario_sectores
{
  "mappings": {
    "properties" : {
        "label" : {
              "type" : "keyword"
        },
        "sector" : {
              "type" : "keyword"
        }
      }
  },
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "my_analyzer": {
            "tokenizer": "standard",
            "filter": [
              "lowercase",
              "spanish_stop"
            ]
          }
        },
        "filter": {
          "spanish_stop": {
            "type":       "stop",
            "stopwords":  "_spanish_" 
          }
        }
      }
    }
  }
}
```

### 2. Create the pipeline policy
```
PUT /_enrich/policy/enrich_label_sector
{
  "match": {
    "indices": "diccionario_sectores",
    "match_field": "label",
    "enrich_fields": [ "label", "sector" ]
  }
}
```

### 3. Execute the policy
```
POST /_enrich/policy/enrich_label_sector/_execute
```

### 4. Create Ingest Pipeline
```
PUT /_ingest/pipeline/enrich_label_company
{
  "description": "Enrich postal codes",
  "processors": [
    {
      "enrich": {
        "policy_name": "enrich_label_sector",
        "field": "company.name.text",
        "target_field": "company"
        "max_matches": "1"
      }
    }
  ]
}
```

### 5. Testing Ingest Pipeline
```
PUT /my-index-00001/_doc/my_id?pipeline=enrich_label_company
{
  "company.name.text": "name of a company"
}
```

