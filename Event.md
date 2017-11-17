
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
**[GET](/documentation/endpoint/Event#event-category)** | `/event/category` | EVENT CATEGORY
**[GET](/documentation/endpoint/Event#event-to-csv)** | `/event/event.csv` | Event to csv

### Object Attributes

Attribute | Type | Readonly | Nullable | Has Default
--- | --- | --- | --- | ---
`app_id` | integer | &nbsp; | &bullet; | &nbsp;
`app_name` | text | &nbsp; | &bullet; | &nbsp;
`app_version` | text | &nbsp; | &bullet; | &nbsp;
`campaign_content` | text | &nbsp; | &bullet; | &nbsp;
`campaign_id` | text | &nbsp; | &bullet; | &nbsp;
`campaign_keyword` | text | &nbsp; | &bullet; | &nbsp;
`campaign_medium` | text | &nbsp; | &bullet; | &nbsp;
`campaign_name` | text | &nbsp; | &bullet; | &nbsp;
`campaign_source` | text | &nbsp; | &bullet; | &nbsp;
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
`location` | text | &nbsp; | &bullet; | &nbsp;
`next_nilead_id` | text | &nbsp; | &bullet; | &nbsp;
`nilead_id` | text | &nbsp; | &nbsp; | &nbsp;
`non_interaction` | boolean | &nbsp; | &nbsp; | &bullet;
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
`object_id` | number | filter events by object_id
`object_source` | string | filter all events by the object_source, example: object_source=test%20
`page` | number | page will go with limit, example limit=5&page=1
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
Date: Fri, 17 Nov 2017 19:38:20 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "campaign_content": null, 
        "campaign_id": null, 
        "campaign_keyword": null, 
        "campaign_medium": null, 
        "campaign_name": null, 
        "campaign_source": null, 
        "client_engine": "WebKit", 
        "client_locale": "en_US", 
        "client_name": "Mobile Safari", 
        "client_type": "browser", 
        "client_version": "11.0", 
        "created": "2017-11-17T18:18:54.321563+00:00", 
        "device_make": "AP", 
        "device_model": "iPhone", 
        "device_platform_name": "iOS - 11.0 - ", 
        "event_action": "", 
        "event_category": "pageview", 
        "event_context": {
            "@context": "http://schema.org", 
            "@id": "https://nilead.com/article/living-as-an-expat-in-ho-chi-minh-city", 
            "@type": "Article", 
            "author": {
                "@type": "Person", 
                "name": "Ivan Lamothe"
            }, 
            "dateModified": "2017-05-29T17:16:05+07:00", 
            "datePublished": "2017-05-28T14:59:47+07:00", 
            "description": "My name is Ivan Lamothe, I am working in Ho Chi Minh City (the Southern capital of Vietnam) as the Creative Director of Nilead, a Digital Agency. I find my 2 years working here a wild ride with many ups and downs and many interesting experiences that I would love to share with my fellow designers who are working or planning to come here to work.", 
            "headline": "Living as an expat in Ho Chi Minh City", 
            "image": [
                "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/living-as-an-expat-in-ho-chi-minh-city-banner_1495975397_grande.jpg", 
                "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/living-as-an-expat-in-ho-chi-minh-city-listing_1495975401_grande.jpg"
            ], 
            "keywords": "Expat, Ho Chi Minh City, Vietnam, Saigon, food, business,  web design, culture, tips, living", 
            "mainEntityOfPage": {
                "@id": "https://nilead.com/article/living-as-an-expat-in-ho-chi-minh-city", 
                "@type": "WebPage"
            }, 
            "name": "Living as an expat in Ho Chi Minh City", 
            "publisher": {
                "@type": "Organization", 
                "logo": {
                    "@type": "ImageObject", 
                    "url": "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/logo-final-curve-version-06_1492741257_grande.png"
                }, 
                "name": "Nilead"
            }
        }, 
        "event_label": "/article/living-as-an-expat-in-ho-chi-minh-city", 
        "event_object_id": null, 
        "event_object_source": null, 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510942734, 
        "event_value": 0, 
        "event_version": "1.0", 
        "id": 127, 
        "ip": "1.47.1.28", 
        "location": null, 
        "next_nilead_id": null, 
        "nilead_id": "e79b6917-0f69-4174-a0f8-9b6a93e16f0d", 
        "non_interaction": false, 
        "prev_nilead_id": null, 
        "session_id": "nkp314p16fudcdo5u64n5rjpag", 
        "user_id": 1
    }, 
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "campaign_content": null, 
        "campaign_id": null, 
        "campaign_keyword": null, 
        "campaign_medium": null, 
        "campaign_name": null, 
        "campaign_source": null, 
        "client_engine": "Blink", 
        "client_locale": "en_US", 
        "client_name": "Chrome", 
        "client_type": "browser", 
        "client_version": "60.0", 
        "created": "2017-11-17T18:17:13.421728+00:00", 
        "device_make": "", 
        "device_model": "", 
        "device_platform_name": "Windows - 10 - x64", 
        "event_action": "generic-exit", 
        "event_category": "lead", 
        "event_context": null, 
        "event_label": "exitIntentTrigger", 
        "event_object_id": null, 
        "event_object_source": null, 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510942633, 
        "event_value": 0, 
        "event_version": "1.0", 
        "id": 126, 
        "ip": "103.76.180.104", 
        "location": null, 
        "next_nilead_id": null, 
        "nilead_id": "e5316257-23a5-4bf7-a3b8-8d05fd20ae49", 
        "non_interaction": false, 
        "prev_nilead_id": null, 
        "session_id": "cbk243vg6gm9sk3v4jtkh201td", 
        "user_id": 1
    }, 
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "campaign_content": null, 
        "campaign_id": null, 
        "campaign_keyword": null, 
        "campaign_medium": null, 
        "campaign_name": null, 
        "campaign_source": null, 
        "client_engine": "Blink", 
        "client_locale": "en_US", 
        "client_name": "Chrome", 
        "client_type": "browser", 
        "client_version": "60.0", 
        "created": "2017-11-17T18:13:00.161212+00:00", 
        "device_make": "", 
        "device_model": "", 
        "device_platform_name": "Windows - 10 - x64", 
        "event_action": "", 
        "event_category": "pageview", 
        "event_context": {
            "@context": "http://schema.org", 
            "@id": "https://nilead.com/article/living-as-an-expat-in-ho-chi-minh-city", 
            "@type": "Article", 
            "author": {
                "@type": "Person", 
                "name": "Ivan Lamothe"
            }, 
            "dateModified": "2017-05-29T17:16:05+07:00", 
            "datePublished": "2017-05-28T14:59:47+07:00", 
            "description": "My name is Ivan Lamothe, I am working in Ho Chi Minh City (the Southern capital of Vietnam) as the Creative Director of Nilead, a Digital Agency. I find my 2 years working here a wild ride with many ups and downs and many interesting experiences that I would love to share with my fellow designers who are working or planning to come here to work.", 
            "headline": "Living as an expat in Ho Chi Minh City", 
            "image": [
                "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/living-as-an-expat-in-ho-chi-minh-city-banner_1495975397_grande.jpg", 
                "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/living-as-an-expat-in-ho-chi-minh-city-listing_1495975401_grande.jpg"
            ], 
            "keywords": "Expat, Ho Chi Minh City, Vietnam, Saigon, food, business,  web design, culture, tips, living", 
            "mainEntityOfPage": {
                "@id": "https://nilead.com/article/living-as-an-expat-in-ho-chi-minh-city", 
                "@type": "WebPage"
            }, 
            "name": "Living as an expat in Ho Chi Minh City", 
            "publisher": {
                "@type": "Organization", 
                "logo": {
                    "@type": "ImageObject", 
                    "url": "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/logo-final-curve-version-06_1492741257_grande.png"
                }, 
                "name": "Nilead"
            }
        }, 
        "event_label": "/article/living-as-an-expat-in-ho-chi-minh-city", 
        "event_object_id": null, 
        "event_object_source": null, 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510942379, 
        "event_value": 0, 
        "event_version": "1.0", 
        "id": 125, 
        "ip": "103.76.180.104", 
        "location": null, 
        "next_nilead_id": null, 
        "nilead_id": "e5316257-23a5-4bf7-a3b8-8d05fd20ae49", 
        "non_interaction": false, 
        "prev_nilead_id": null, 
        "session_id": "cbk243vg6gm9sk3v4jtkh201td", 
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
Date: Fri, 17 Nov 2017 19:38:20 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "campaign_content": null, 
        "campaign_id": null, 
        "campaign_keyword": null, 
        "campaign_medium": null, 
        "campaign_name": null, 
        "campaign_source": null, 
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
        "id": 129, 
        "ip": "115.77.188.31", 
        "location": null, 
        "next_nilead_id": null, 
        "nilead_id": "84f6e6ee-d899-480e-92f1-4c86586be62c", 
        "non_interaction": null, 
        "prev_nilead_id": null, 
        "session_id": "6o0qqnfeu178gtm41sh3qgmpp6", 
        "user_id": 1
    }, 
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "campaign_content": null, 
        "campaign_id": null, 
        "campaign_keyword": null, 
        "campaign_medium": null, 
        "campaign_name": null, 
        "campaign_source": null, 
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
        "id": 130, 
        "ip": "115.77.188.31", 
        "location": null, 
        "next_nilead_id": null, 
        "nilead_id": "84f6e6ee-d899-480e-92f1-4c86586be62c", 
        "non_interaction": null, 
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
Date: Fri, 17 Nov 2017 19:38:20 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "campaign_content": null, 
        "campaign_id": null, 
        "campaign_keyword": null, 
        "campaign_medium": null, 
        "campaign_name": null, 
        "campaign_source": null, 
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
        "location": null, 
        "next_nilead_id": null, 
        "nilead_id": "1b55e65d-f438-4e5a-a148-bbded08ddd1d", 
        "non_interaction": false, 
        "prev_nilead_id": null, 
        "session_id": "mv8c5a5fv0jnphhacd6am14vupu", 
        "user_id": 1
    }, 
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "campaign_content": null, 
        "campaign_id": null, 
        "campaign_keyword": null, 
        "campaign_medium": null, 
        "campaign_name": null, 
        "campaign_source": null, 
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
        "event_object_source": "object test2", 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510407925, 
        "event_value": 0, 
        "event_version": "1.0", 
        "id": 1780, 
        "ip": "151.246.52.73", 
        "location": null, 
        "next_nilead_id": null, 
        "nilead_id": "1b55e65d-f438-4ea-a148-bbded08ddd1d", 
        "non_interaction": false, 
        "prev_nilead_id": null, 
        "session_id": "mv8c5a5fv0jnphhacd6am4vupu", 
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
Date: Fri, 17 Nov 2017 19:38:21 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "campaign_content": null, 
        "campaign_id": null, 
        "campaign_keyword": null, 
        "campaign_medium": null, 
        "campaign_name": null, 
        "campaign_source": null, 
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
        "event_object_source": "object test2", 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510407925, 
        "event_value": 0, 
        "event_version": "1.0", 
        "id": 1780, 
        "ip": "151.246.52.73", 
        "location": null, 
        "next_nilead_id": null, 
        "nilead_id": "1b55e65d-f438-4ea-a148-bbded08ddd1d", 
        "non_interaction": false, 
        "prev_nilead_id": null, 
        "session_id": "mv8c5a5fv0jnphhacd6am4vupu", 
        "user_id": 1
    }, 
    {
        "app_id": null, 
        "app_name": null, 
        "app_version": null, 
        "campaign_content": null, 
        "campaign_id": null, 
        "campaign_keyword": null, 
        "campaign_medium": null, 
        "campaign_name": null, 
        "campaign_source": null, 
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
        "location": null, 
        "next_nilead_id": null, 
        "nilead_id": "1b55e65d-f438-4e5a-a148-bbded08ddd1d", 
        "non_interaction": false, 
        "prev_nilead_id": null, 
        "session_id": "mv8c5a5fv0jnphhacd6am14vupu", 
        "user_id": 1
    }
]
```


EVENT CATEGORY
------
<code request-method="GET">**GET** /event/category</code>

Distinct category order by alphabet

### Example
```http
GET http://159.203.64.35:6789/event/category
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
Date: Fri, 17 Nov 2017 19:38:21 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "count": 24, 
        "event_category": "404"
    }, 
    {
        "count": 1, 
        "event_category": "aaa"
    }, 
    {
        "count": 1, 
        "event_category": "asdasdsa"
    }, 
    {
        "count": 2, 
        "event_category": "asdsada"
    }, 
    {
        "count": 1, 
        "event_category": "asdsadsadsadsa"
    }, 
    {
        "count": 25, 
        "event_category": "authentication"
    }, 
    {
        "count": 1, 
        "event_category": "dsad"
    }, 
    {
        "count": 4, 
        "event_category": "email"
    }, 
    {
        "count": 6, 
        "event_category": "failedLead"
    }, 
    {
        "count": 452, 
        "event_category": "lead"
    }, 
    {
        "count": 1600, 
        "event_category": "pageview"
    }, 
    {
        "count": 2, 
        "event_category": null
    }
]
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
Date: Fri, 17 Nov 2017 19:38:21 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

"app_id","app_name","app_version","campaign_content","campaign_id","campaign_keyword","campaign_medium","campaign_name","campaign_source","client_engine","client_locale","client_name","client_type","client_version","created","device_make","device_model","device_platform_name","event_action","event_category","event_context","event_label","event_object_id","event_object_source","event_subject_id","event_subject_source","event_timestamp","event_value","event_version","id","ip","location","next_nilead_id","nilead_id","non_interaction","prev_nilead_id","session_id","user_id"
"","","","","","","","","","WebKit","en_US","Mobile Safari","browser","11.0","2017-11-17 18:18:54.321563+00:00","AP","iPhone","iOS - 11.0 - ","","pageview","{u'publisher': {u'logo': {u'url': u'https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/logo-final-curve-version-06_1492741257_grande.png', u'@type': u'ImageObject'}, u'@type': u'Organization', u'name': u'Nilead'}, u'name': u'Living as an expat in Ho Chi Minh City', u'author': {u'@type': u'Person', u'name': u'Ivan Lamothe'}, u'headline': u'Living as an expat in Ho Chi Minh City', u'image': [u'https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/living-as-an-expat-in-ho-chi-minh-city-banner_1495975397_grande.jpg', u'https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/living-as-an-expat-in-ho-chi-minh-city-listing_1495975401_grande.jpg'], u'datePublished': u'2017-05-28T14:59:47+07:00', u'mainEntityOfPage': {u'@id': u'https://nilead.com/article/living-as-an-expat-in-ho-chi-minh-city', u'@type': u'WebPage'}, u'@type': u'Article', u'keywords': u'Expat, Ho Chi Minh City, Vietnam, Saigon, food, business,  web design, culture, tips, living', u'@context': u'http://schema.org', u'@id': u'https://nilead.com/article/living-as-an-expat-in-ho-chi-minh-city', u'dateModified': u'2017-05-29T17:16:05+07:00', u'description': u'My name is Ivan Lamothe, I am working in Ho Chi Minh City (the Southern capital of Vietnam) as the Creative Director of Nilead, a Digital Agency. I find my 2 years working here a wild ride with many ups and downs and many interesting experiences that I would love to share with my fellow designers who are working or planning to come here to work.'}","/article/living-as-an-expat-in-ho-chi-minh-city","","","","",1510942734,0,"1.0",127,"1.47.1.28","","","e79b6917-0f69-4174-a0f8-9b6a93e16f0d",False,"","nkp314p16fudcdo5u64n5rjpag",1
"","","","","","","","","","Blink","en_US","Chrome","browser","60.0","2017-11-17 18:17:13.421728+00:00","","","Windows - 10 - x64","generic-exit","lead","","exitIntentTrigger","","","","",1510942633,0,"1.0",126,"103.76.180.104","","","e5316257-23a5-4bf7-a3b8-8d05fd20ae49",False,"","cbk243vg6gm9sk3v4jtkh201td",1
"","","","","","","","","","Blink","en_US","Chrome","browser","60.0","2017-11-17 18:13:00.161212+00:00","","","Windows - 10 - x64","","pageview","{u'publisher': {u'logo': {u'url': u'https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/logo-final-curve-version-06_1492741257_grande.png', u'@type': u'ImageObject'}, u'@type': u'Organization', u'name': u'Nilead'}, u'name': u'Living as an expat in Ho Chi Minh City', u'author': {u'@type': u'Person', u'name': u'Ivan Lamothe'}, u'headline': u'Living as an expat in Ho Chi Minh City', u'image': [u'https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/living-as-an-expat-in-ho-chi-minh-city-banner_1495975397_grande.jpg', u'https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/living-as-an-expat-in-ho-chi-minh-city-listing_1495975401_grande.jpg'], u'datePublished': u'2017-05-28T14:59:47+07:00', u'mainEntityOfPage': {u'@id': u'https://nilead.com/article/living-as-an-expat-in-ho-chi-minh-city', u'@type': u'WebPage'}, u'@type': u'Article', u'keywords': u'Expat, Ho Chi Minh City, Vietnam, Saigon, food, business,  web design, culture, tips, living', u'@context': u'http://schema.org', u'@id': u'https://nilead.com/article/living-as-an-expat-in-ho-chi-minh-city', u'dateModified': u'2017-05-29T17:16:05+07:00', u'description': u'My name is Ivan Lamothe, I am working in Ho Chi Minh City (the Southern capital of Vietnam) as the Creative Director of Nilead, a Digital Agency. I find my 2 years working here a wild ride with many ups and downs and many interesting experiences that I would love to share with my fellow designers who are working or planning to come here to work.'}","/article/living-as-an-expat-in-ho-chi-minh-city","","","","",1510942379,0,"1.0",125,"103.76.180.104","","","e5316257-23a5-4bf7-a3b8-8d05fd20ae49",False,"","cbk243vg6gm9sk3v4jtkh201td",1

```

