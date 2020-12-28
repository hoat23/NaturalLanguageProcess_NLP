# Text Analysis in Elasticsearch

## Mapping

### Defining fieldd

#### Whithout fielddata
```
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "my_field": { 
        "type": "text",
        "fields": {
          "keyword": { 
            "type": "keyword"
          }
        }
      }
    }
  }
}
```

#### With fieldata
```
PUT my-index-000001/_mapping
{
  "properties": {
    "my_field": { 
      "type":     "text",
      "fielddata": true
    }
  }
}
```

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

### Analyzer terms in document

# Creating a index with custom analyzer

```
PUT /diccionario_sectores
{
    "aliases" : { },
    "mappings" : {
      "properties" : {
        "label" : {
          "type" : "text",
          "analyzer" : "my_analyzer",
          "fields": {
            "keyword": {
              "type": "keyword"
            }
          }
        },
        "sector" : {
          "type" : "text",
          "analyzer": "my_analyzer", 
          "fields": {
            "keyword": {
              "type": "keyword"
            }
          }
        }
      }
    },
    "settings" : {
      "index" : {
        "analysis" : {
          "filter" : {
            "spanish_stop" : {
              "type" : "stop",
              "stopwords" : "_spanish_"
            },
            "custom_words_stop": {
              "type": "stop",
              "ignore_case": true,
              "stopwords": [ 
                "sac", "s.a.c.","s.a.c",
                "sa","s.a.","s.a",
                "\n","\t"
              ]
            }
          },
          "analyzer" : {
            "my_analyzer" : {
              "filter" : [
                "lowercase",
                "custom_words_stop",
                "spanish_stop"
              ],
              "tokenizer" : "standard"
            }
          }
        }
      }
    }
  }
```

# Testing with a virtual document
```
GET /diccionario_sectores/_termvectors
{
  "doc" : {
    "label" : "llegada a lima el 06 enero, 2 maletas no han llegado, se indicó que vienen dentro de 2 días, me acerco nuevamente al aeropuerto, resulta que de las dos maletas llegó solo una\nLa otra (siendo priority) se fue a Madrid, no se ha podido indicar la hora de llegada de la segunda maleta",
    "sector" : "no indentificado"
  },
  "fields": ["label"],
  "per_field_analyzer" : {
    "label": "my_analyzer"
  }
}
```
If you don't defined a "my_analyzer", can use "text"
```
{
  "_index" : "diccionario_sectores",
  "_type" : "_doc",
  "_version" : 0,
  "found" : true,
  "took" : 0,
  "term_vectors" : {
    "label" : {
      "field_statistics" : {"sum_doc_freq" : 9981,"doc_count" : 2177,"sum_ttf" : 10120},
      "terms" : {
        "06" : {"term_freq" : 1,"tokens" : [{"position" : 4,"start_offset" : 18,"end_offset" : 20}]
        },
        "2" : {"term_freq" : 2,"tokens" : [{"position" : 6,"start_offset" : 28,"end_offset" : 29},{"position" : 17,"start_offset" : 85,"end_offset" : 86}]
        },
        "acerco" : {"term_freq" : 1,"tokens" : [{"position" : 20,"start_offset" : 96,"end_offset" : 102}]
        },
        "aeropuerto" : {"term_freq" : 1,"tokens" : [{"position" : 23,"start_offset" : 117,"end_offset" : 127}]
        },
        "dentro" : {"term_freq" : 1,"tokens" : [{"position" : 15,"start_offset" : 75,"end_offset" : 81}]
        },
        "dos" : {"term_freq" : 1,"tokens" : [{"position" : 28,"start_offset" : 148,"end_offset" : 151}]
        },
        "días" : {"term_freq" : 1,"tokens" : [{"position" : 18,"start_offset" : 87,"end_offset" : 91}]
        },
        "enero" : {"term_freq" : 1,"tokens" : [{"position" : 5,"start_offset" : 21,"end_offset" : 26}]
        },
        "hora" : {"term_freq" : 1,"tokens" : [{"position" : 47,"start_offset" : 245,"end_offset" : 249}]
        },
        "indicar" : {"term_freq" : 1,"tokens" : [{"position" : 45,"start_offset" : 234,"end_offset" : 241}]
        },
        "indicó" : {"term_freq" : 1,"tokens" : [{"position" : 12,"start_offset" : 57,"end_offset" : 63}]
        },
        "lima" : {"term_freq" : 1,"tokens" : [{"position" : 2,"start_offset" : 10,"end_offset" : 14}]
        },
        "llegada" : {"term_freq" : 2,"tokens" : [{"position" : 0,"start_offset" : 0,"end_offset" : 7},{"position" : 49,"start_offset" : 253,"end_offset" : 260}]
        },
        "llegado" : {"term_freq" : 1,"tokens" : [{"position" : 10,"start_offset" : 45,"end_offset" : 52}]
        },
        "llegó" : {"term_freq" : 1,"tokens" : [{"position" : 30,"start_offset" : 160,"end_offset" : 165}]
        },
        "madrid" : {"term_freq" : 1,"tokens" : [{"position" : 40,"start_offset" : 210,"end_offset" : 216}]
        },
        "maleta" : {"term_freq" : 1,"tokens" : [{"position" : 53,"start_offset" : 275,"end_offset" : 281}]
        },
        "maletas" : {"term_freq" : 2,"tokens" : [{"position" : 7,"start_offset" : 30,"end_offset" : 37},{"position" : 29,"start_offset" : 152,"end_offset" : 159}]
        },
        "nuevamente" : {"term_freq" : 1,"tokens" : [{"position" : 21,"start_offset" : 103,"end_offset" : 113}]
        },
        "podido" : {"term_freq" : 1,"tokens" : [{"position" : 44,"start_offset" : 227,"end_offset" : 233}]
        },
        "priority" : {"term_freq" : 1,"tokens" : [{"position" : 36,"start_offset" : 191,"end_offset" : 199}]
        },
        "resulta" : {"term_freq" : 1,"tokens" : [{"position" : 24,"start_offset" : 129,"end_offset" : 136}]
        },
        "segunda" : {"term_freq" : 1,"tokens" : [{"position" : 52,"start_offset" : 267,"end_offset" : 274}]
        },
        "solo" : {"term_freq" : 1,"tokens" : [{"position" : 31,"start_offset" : 166,"end_offset" : 170}]
        },
        "vienen" : {"term_freq" : 1,"tokens" : [{"position" : 14,"start_offset" : 68,"end_offset" : 74}]
        }
      }
    }
  }
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

## Documentation
- https://www.elastic.co/guide/en/elasticsearch/reference/master/docs-multi-termvectors.html
- https://www.elastic.co/guide/en/elasticsearch/reference/master/docs-termvectors.html
- https://www.elastic.co/es/blog/text-similarity-search-with-vectors-in-elasticsearch

### Review
- https://stackoverflow.com/questions/32998228/elasticsearch-extract-number-from-a-field
- https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-word-delimiter-graph-tokenfilter.html
