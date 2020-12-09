# Text Analysis in Elasticsearch

## Standard Analysis 
```
POST _analyze
{
  "analyzer": "standard",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```
