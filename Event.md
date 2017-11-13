
Event
======

`/event`

EVENT OVERVIEW

### Methods

Method | URL | Description
--- | --- | ---
**[GET](/documentation/endpoint/Event#list-of-50-latest-events)** | `/event` | List of 50 latest events
**[POST](/documentation/endpoint/Event#insert-events)** | `/event` | Insert events
**[GET](/documentation/endpoint/Event#event-by-object_id)** | `event?object_id=1` | Event by object_id
**[GET](/documentation/endpoint/Event#event-by-object-source)** | `/event?object_source=test` | Event by object source
**[OPTIONS](/documentation/endpoint/Event#event-details)** | `/event` | EVENT Details
**[GET](/documentation/endpoint/Event#event-to-csv)** | `/event/event.csv` | Event to csv

### Object Attributes

Attribute | Type | Readonly | Nullable | Has Default
--- | --- | --- | --- | ---
`app_id` | integer | &nbsp; | &bullet; | &nbsp;
`app_name` | text | &nbsp; | &bullet; | &nbsp;
`app_version` | text | &nbsp; | &bullet; | &nbsp;
`client_engine` | text | &nbsp; | &bullet; | &nbsp;
`client_locale` | text | &nbsp; | &bullet; | &nbsp;
`client_name` | text | &nbsp; | &bullet; | &nbsp;
`client_type` | text | &nbsp; | &bullet; | &nbsp;
`client_version` | text | &nbsp; | &bullet; | &nbsp;
`created` | timestamp | &nbsp; | &nbsp; | &bullet;
`device_make` | text | &nbsp; | &bullet; | &nbsp;
`device_model` | text | &nbsp; | &bullet; | &nbsp;
`device_platform_name` | text | &nbsp; | &bullet; | &nbsp;
`event_action` | text | &nbsp; | &bullet; | &nbsp;
`event_category` | text | &nbsp; | &bullet; | &nbsp;
`event_context` | json | &nbsp; | &bullet; | &nbsp;
`event_label` | text | &nbsp; | &bullet; | &nbsp;
`event_object_id` | integer | &nbsp; | &bullet; | &nbsp;
`event_object_source` | text | &nbsp; | &bullet; | &nbsp;
`event_subject_id` | integer | &nbsp; | &bullet; | &nbsp;
`event_subject_source` | text | &nbsp; | &bullet; | &nbsp;
`event_timestamp` | integer | &nbsp; | &nbsp; | &bullet;
`event_value` | integer | &nbsp; | &bullet; | &nbsp;
`event_version` | text | &nbsp; | &bullet; | &nbsp;
`id` | integer | &bullet; | &nbsp; | &bullet;
`ip` | text | &nbsp; | &bullet; | &nbsp;
`next_nilead_id` | text | &nbsp; | &bullet; | &nbsp;
`nilead_id` | text | &nbsp; | &nbsp; | &nbsp;
`prev_nilead_id` | text | &nbsp; | &bullet; | &nbsp;
`session_id` | text | &nbsp; | &bullet; | &nbsp;
`user_id` | integer | &nbsp; | &nbsp; | &nbsp;

List of 50 latest events
------
<code request-method="GET">**GET** /event</code>

List of 50 latest events

### Query Parameters

Parameter | Type | Description
--- | --- | ---
`end` | string | Return event end on date, example end=2017-11-01
`limit` | number | You can set limit return
`nilead_id` | string | Returns all the recursive event link to that nilead_id
`page` | number | page will go with limit, example limit=5&page=1
`search` | string | Currently search for app_name or device_make
`start` | string | Return events start on date, example start=2017-06-01
`user_id` | number | Returns all the events associate with user_id



### Example
```http
GET http://159.203.64.35:6789/event?limit=3
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: 159.203.64.35:6789
Origin: http://159.203.64.35:6789
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://159.203.64.35:6789
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 04:50:38 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "client_engine": "Gecko", 
        "client_locale": "en_US", 
        "client_name": "Firefox", 
        "client_type": "browser", 
        "client_version": "56.0", 
        "created": "2017-11-11T13:45:25.294929+00:00", 
        "device_make": "", 
        "device_model": "", 
        "device_platform_name": "Windows - 7 - x64", 
        "event_action": "https://www.google.com/", 
        "event_category": "pageview", 
        "event_context": null, 
        "event_label": "/article/choose-the-right-colors-for-your-website", 
        "event_object_id": 1, 
        "event_object_source": "object test", 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510407925, 
        "event_value": 0, 
        "event_version": "1.0", 
        "id": 1718, 
        "ip": "151.246.52.73", 
        "next_nilead_id": null, 
        "nilead_id": "1b55e65d-f438-4e5a-a148-bbded08ddd1d", 
        "prev_nilead_id": null, 
        "session_id": "mv8c5a5fv0jnphhacd6am14vupu", 
        "user_id": 1
    }
]
```


Insert events
------
<code request-method="POST">**POST** /event</code>

Insert Events

### Example
```http
POST http://159.203.64.35:6789/event
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Content-Length: 4112
Content-Type: application/json
Host: 159.203.64.35:6789
Origin: http://159.203.64.35:6789

[
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "client_engine": "Blink", 
        "client_locale": "en_US", 
        "client_name": "Chrome", 
        "client_type": "browser", 
        "client_version": "61.0", 
        "created": "2017-11-12T11:15:55.498861+00:00", 
        "device_make": "", 
        "device_model": "", 
        "device_platform_name": "Windows - 10 - x64", 
        "event_action": "https://nilead.com/articles", 
        "event_category": "pageview", 
        "event_context": {
            "@context": "http://schema.org", 
            "@id": "https://nilead.com/article/content-marketing-strategy-for-beginners", 
            "@type": "Article", 
            "author": {
                "@type": "Person", 
                "name": "Vu Nguyen"
            }, 
            "dateModified": "2017-08-29T12:25:19+07:00 12:25", 
            "datePublished": "2017-08-24T13:53:43+07:00 13:53", 
            "description": "Content marketing is not the latest trend but it&#039;s a proven strategy that really works for companies who care about building a long term communication channel with the customers. If you haven&#039;t embarked on this journey, now is the best time to start because just like coffee good content will take time to brew.", 
            "headline": "Content marketing strategy for beginners", 
            "image": [
                "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/content-marketing-strategy-for-beginners-banner_1503918818_grande.jpg", 
                "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/content-marketing-strategy-for-beginners-listing_1503918818_grande.jpg"
            ], 
            "keywords": "content marketing, digital marketing, content strategy, content planning, content example", 
            "mainEntityOfPage": {
                "@id": "https://nilead.com/article/content-marketing-strategy-for-beginners", 
                "@type": "WebPage"
            }, 
            "publisher": {
                "@type": "Organization", 
                "logo": {
                    "@type": "ImageObject", 
                    "url": "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/logo-final-curve-version-06_1492741257_grande.png"
                }, 
                "name": "Nilead"
            }
        }, 
        "event_label": "/article/content-marketing-strategy-for-beginners", 
        "event_object_id": null, 
        "event_object_source": null, 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510485355, 
        "event_value": 0, 
        "event_version": "1.0", 
        "ip": "115.77.188.31", 
        "next_nilead_id": null, 
        "nilead_id": "84f6e6ee-d899-480e-92f1-4c86586be62c", 
        "prev_nilead_id": null, 
        "session_id": "6o0qqnfeu178gtm41sh3qgmpp6", 
        "user_id": 1
    }, 
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "client_engine": "Blink", 
        "client_locale": "en_US", 
        "client_name": "Chrome", 
        "client_type": "browser", 
        "client_version": "61.0", 
        "created": "2017-11-12T11:03:55.466132+00:00", 
        "device_make": "", 
        "device_model": "", 
        "device_platform_name": "Windows - 10 - x64", 
        "event_action": "https://nilead.com/articles", 
        "event_category": "pageview", 
        "event_context": null, 
        "event_label": "/article/content-marketing-strategy-for-beginners", 
        "event_object_id": null, 
        "event_object_source": null, 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510484635, 
        "event_value": 0, 
        "event_version": "1.0", 
        "ip": "115.77.188.31", 
        "next_nilead_id": null, 
        "nilead_id": "84f6e6ee-d899-480e-92f1-4c86586be62c", 
        "prev_nilead_id": null, 
        "session_id": "6o0qqnfeu178gtm41sh3qgmpp6", 
        "user_id": 1
    }
]
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://159.203.64.35:6789
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 04:50:38 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "client_engine": "Blink", 
        "client_locale": "en_US", 
        "client_name": "Chrome", 
        "client_type": "browser", 
        "client_version": "61.0", 
        "created": "2017-11-12T11:15:55.498861+00:00", 
        "device_make": "", 
        "device_model": "", 
        "device_platform_name": "Windows - 10 - x64", 
        "event_action": "https://nilead.com/articles", 
        "event_category": "pageview", 
        "event_context": {
            "@context": "http://schema.org", 
            "@id": "https://nilead.com/article/content-marketing-strategy-for-beginners", 
            "@type": "Article", 
            "author": {
                "@type": "Person", 
                "name": "Vu Nguyen"
            }, 
            "dateModified": "2017-08-29T12:25:19+07:00", 
            "datePublished": "2017-08-24T13:53:43+07:00", 
            "description": "Content marketing is not the latest trend but it&#039;s a proven strategy that really works for companies who care about building a long term communication channel with the customers. If you haven&#039;t embarked on this journey, now is the best time to start because just like coffee good content will take time to brew.", 
            "headline": "Content marketing strategy for beginners", 
            "image": [
                "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/content-marketing-strategy-for-beginners-banner_1503918818_grande.jpg", 
                "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/content-marketing-strategy-for-beginners-listing_1503918818_grande.jpg"
            ], 
            "keywords": "content marketing, digital marketing, content strategy, content planning, content example", 
            "mainEntityOfPage": {
                "@id": "https://nilead.com/article/content-marketing-strategy-for-beginners", 
                "@type": "WebPage"
            }, 
            "publisher": {
                "@type": "Organization", 
                "logo": {
                    "@type": "ImageObject", 
                    "url": "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/logo-final-curve-version-06_1492741257_grande.png"
                }, 
                "name": "Nilead"
            }
        }, 
        "event_label": "/article/content-marketing-strategy-for-beginners", 
        "event_object_id": null, 
        "event_object_source": null, 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510485355, 
        "event_value": 0, 
        "event_version": "1.0", 
        "id": 1719, 
        "ip": "115.77.188.31", 
        "next_nilead_id": null, 
        "nilead_id": "84f6e6ee-d899-480e-92f1-4c86586be62c", 
        "prev_nilead_id": null, 
        "session_id": "6o0qqnfeu178gtm41sh3qgmpp6", 
        "user_id": 1
    }, 
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "client_engine": "Blink", 
        "client_locale": "en_US", 
        "client_name": "Chrome", 
        "client_type": "browser", 
        "client_version": "61.0", 
        "created": "2017-11-12T11:03:55.466132+00:00", 
        "device_make": "", 
        "device_model": "", 
        "device_platform_name": "Windows - 10 - x64", 
        "event_action": "https://nilead.com/articles", 
        "event_category": "pageview", 
        "event_context": null, 
        "event_label": "/article/content-marketing-strategy-for-beginners", 
        "event_object_id": null, 
        "event_object_source": null, 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510484635, 
        "event_value": 0, 
        "event_version": "1.0", 
        "id": 1720, 
        "ip": "115.77.188.31", 
        "next_nilead_id": null, 
        "nilead_id": "84f6e6ee-d899-480e-92f1-4c86586be62c", 
        "prev_nilead_id": null, 
        "session_id": "6o0qqnfeu178gtm41sh3qgmpp6", 
        "user_id": 1
    }
]
```


Event by object_id
------
<code request-method="GET">**GET** event?object_id=1</code>

Events by object_id

### Example
```http
GET http://159.203.64.35:6789/event?object_id=1
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: 159.203.64.35:6789
Origin: http://159.203.64.35:6789
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://159.203.64.35:6789
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 04:50:39 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "client_engine": "Gecko", 
        "client_locale": "en_US", 
        "client_name": "Firefox", 
        "client_type": "browser", 
        "client_version": "56.0", 
        "created": "2017-11-11T13:45:25.294929+00:00", 
        "device_make": "", 
        "device_model": "", 
        "device_platform_name": "Windows - 7 - x64", 
        "event_action": "https://www.google.com/", 
        "event_category": "pageview", 
        "event_context": null, 
        "event_label": "/article/choose-the-right-colors-for-your-website", 
        "event_object_id": 1, 
        "event_object_source": "object test", 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510407925, 
        "event_value": 0, 
        "event_version": "1.0", 
        "id": 1718, 
        "ip": "151.246.52.73", 
        "next_nilead_id": null, 
        "nilead_id": "1b55e65d-f438-4e5a-a148-bbded08ddd1d", 
        "prev_nilead_id": null, 
        "session_id": "mv8c5a5fv0jnphhacd6am14vupu", 
        "user_id": 1
    }
]
```


Event by object source
------
<code request-method="GET">**GET** /event?object_source=test</code>

Events by object source

### Example
```http
GET http://159.203.64.35:6789/event?object_source=test
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: 159.203.64.35:6789
Origin: http://159.203.64.35:6789
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://159.203.64.35:6789
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 04:50:39 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "client_engine": "Gecko", 
        "client_locale": "en_US", 
        "client_name": "Firefox", 
        "client_type": "browser", 
        "client_version": "56.0", 
        "created": "2017-11-11T13:45:25.294929+00:00", 
        "device_make": "", 
        "device_model": "", 
        "device_platform_name": "Windows - 7 - x64", 
        "event_action": "https://www.google.com/", 
        "event_category": "pageview", 
        "event_context": null, 
        "event_label": "/article/choose-the-right-colors-for-your-website", 
        "event_object_id": 1, 
        "event_object_source": "object test", 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510407925, 
        "event_value": 0, 
        "event_version": "1.0", 
        "id": 1718, 
        "ip": "151.246.52.73", 
        "next_nilead_id": null, 
        "nilead_id": "1b55e65d-f438-4e5a-a148-bbded08ddd1d", 
        "prev_nilead_id": null, 
        "session_id": "mv8c5a5fv0jnphhacd6am14vupu", 
        "user_id": 1
    }
]
```


EVENT Details
------
<code request-method="OPTIONS">**OPTIONS** /event</code>

event details

### Example
```http
OPTIONS http://159.203.64.35:6789/event
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: 159.203.64.35:6789
Origin: http://159.203.64.35:6789
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://159.203.64.35:6789
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 04:50:39 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

{
    "app_id": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "integer"
    }, 
    "app_name": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "app_version": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "client_engine": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "client_locale": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "client_name": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "client_type": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "client_version": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "created": {
        "has_default": true, 
        "nullable": false, 
        "read_only": false, 
        "type": "timestamp"
    }, 
    "device_make": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "device_model": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "device_platform_name": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "event_action": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "event_category": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "event_context": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "json"
    }, 
    "event_label": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "event_object_id": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "integer"
    }, 
    "event_object_source": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "event_subject_id": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "integer"
    }, 
    "event_subject_source": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "event_timestamp": {
        "has_default": true, 
        "nullable": false, 
        "read_only": false, 
        "type": "integer"
    }, 
    "event_value": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "integer"
    }, 
    "event_version": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "id": {
        "has_default": true, 
        "nullable": false, 
        "read_only": true, 
        "type": "integer"
    }, 
    "ip": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "next_nilead_id": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "nilead_id": {
        "has_default": false, 
        "nullable": false, 
        "read_only": false, 
        "type": "text"
    }, 
    "prev_nilead_id": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "session_id": {
        "has_default": false, 
        "nullable": true, 
        "read_only": false, 
        "type": "text"
    }, 
    "user_id": {
        "has_default": false, 
        "nullable": false, 
        "read_only": false, 
        "type": "integer"
    }
}
```


Event to csv
------
<code request-method="GET">**GET** /event/event.csv</code>

Event to csv

### Example
```http
GET http://159.203.64.35:6789/event/event.csv?limit=3
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: 159.203.64.35:6789
Origin: http://159.203.64.35:6789
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://159.203.64.35:6789
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: text/csv
Date: Mon, 13 Nov 2017 04:50:39 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

"app_id","app_name","app_version","client_engine","client_locale","client_name","client_type","client_version","created","device_make","device_model","device_platform_name","event_action","event_category","event_context","event_label","event_object_id","event_object_source","event_subject_id","event_subject_source","event_timestamp","event_value","event_version","id","ip","next_nilead_id","nilead_id","prev_nilead_id","session_id","user_id"
"","","","Gecko","en_US","Firefox","browser","56.0","2017-11-11 13:45:25.294929+00:00","","","Windows - 7 - x64","https://www.google.com/","pageview","","/article/choose-the-right-colors-for-your-website",1,"object test","","",1510407925,0,"1.0",1718,"151.246.52.73","","1b55e65d-f438-4e5a-a148-bbded08ddd1d","","mv8c5a5fv0jnphhacd6am14vupu",1

```

