from nltk.corpus import movie_reviews                                                                                                        
import requests                                                                                                                              
import nltk                                                                                                                                  
                                                                                                                                             
app = Flask(__name__)                                                                                                                        
                                                                                                                                             
@app.route('/entity', methods=['POST'])                                                                          
def entity():                                                                          
    content = request.json["submit"]
    token = nltk.word_tokenize(content)
    result = nltk.ne_chunk(nltk.pos_tagtoken))
    entities = {}               
    for chunk in result:        
        if hasattr(chunk, 'label'): 
            if chunk.label() in entities:
                entities[chunk.label()].append(' '.join(c[0] for c in chunk))
            else:
                entities[chunk.label()] = [' '.join(c[0] for c in chunk)]
    return jsonify(original=content, entities=entities)


@app.route('/pos_tag', methods=['POST'])                                                                         
def pos_tag():                                                                                                   
    content = request.json["submit"]                                                                             
    token = nltk.word_tokenize(content)                                                                          
    tuples = nltk.pos_tag(token)                                                                                 
    result = ""                                                                                                  
    for tuple in tuples:                                                                                         
        result += tuple[0] + "_" + tuple[1] + " "                                                                
    return jsonify(original=content, enriched=result.strip())                                                    

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

