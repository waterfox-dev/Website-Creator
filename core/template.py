import json

def html_template(name : str):
    with open('config.json', 'r', encoding='utf8') as f :
        f = dict(json.load(f))
    if f['pageConfig']['title'] == '__dynamics__' :
        title = name
    else :
        title = f['pageConfig']['title']
        
    _raw = str()
    with open('templates/basic_template.html', encoding='utf8') as f :
        _raw = f.read()
        _raw = _raw.replace("**rep->title**", title)
        
        return _raw