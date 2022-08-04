template = {
    "swagger": "2.0",
    "info": {
        "title": "Bookmarks Api",
        "description": "API for bookmarks",
        "contact": {
            "responsibleOrganization": "",
            "responsibleDeveloper": "",
            "email": "me@me.com",
            "url": "www.me.com",
        },
        "termsOfService": "http://me.com/terms",
        "version": "0.0.1"
    },
    "basePath": "/api/v1",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions":{
        "Bearer":{
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }
}

swagger_config = {
    "headers":[
        
    ],
    "specs":[
        {
            "endpoint": 'apispec',
            "route" : '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui":True,
    "specs_route": "/"
}