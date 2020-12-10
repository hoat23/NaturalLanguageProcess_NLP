# Text Analysis in Elasticsearch

## Standard Analysis 
```
POST _analyze
{
  "analyzer": "standard",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
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
