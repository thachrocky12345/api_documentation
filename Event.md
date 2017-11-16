
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
Date: Thu, 16 Nov 2017 02:28:58 GMT
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
        "client_locale": "nb_NO", 
        "client_name": "Safari", 
        "client_type": "browser", 
        "client_version": "10.0", 
        "created": "2017-11-16T02:24:19.629780+00:00", 
        "device_make": "", 
        "device_model": "", 
        "device_platform_name": "Mac - 10.12 - ", 
        "event_action": "https://nilead.com/", 
        "event_category": "pageview", 
        "event_context": {
            "@context": "http://schema.org", 
            "@id": "https://nilead.com/portfolio/oneonesix", 
            "@type": "WebPage", 
            "description": "{{ global.resource.seoDescription }}", 
            "keywords": "{{ global.resource.seoKeywords }}", 
            "mainEntityOfPage": {
                "@id": "https://nilead.com/portfolio/oneonesix", 
                "@type": "WebPage"
            }, 
            "name": "{{ global.resource.seoTitle }}", 
            "publisher": {
                "@type": "Organization", 
                "logo": {
                    "@type": "ImageObject", 
                    "url": "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/logo-final-curve-version-06_1492741257_grande.png"
                }, 
                "name": "Nilead"
            }
        }, 
        "event_label": "/portfolio/oneonesix", 
        "event_object_id": null, 
        "event_object_source": null, 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510799059, 
        "event_value": 0, 
        "event_version": "1.0", 
        "id": 6, 
        "ip": "84.212.116.233", 
        "next_nilead_id": null, 
        "nilead_id": "9d3dddb5-064f-4604-85fc-3b533ffa2257", 
        "non_interaction": false, 
        "prev_nilead_id": null, 
        "session_id": "046730g4ddoim7q711lpe29fcl", 
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
        "client_engine": "WebKit", 
        "client_locale": "nb_NO", 
        "client_name": "Safari", 
        "client_type": "browser", 
        "client_version": "10.0", 
        "created": "2017-11-16T02:24:12.970208+00:00", 
        "device_make": "", 
        "device_model": "", 
        "device_platform_name": "Mac - 10.12 - ", 
        "event_action": "https://www.sortfolio.com/listings/23135-nilead", 
        "event_category": "pageview", 
        "event_context": {
            "@context": "http://schema.org", 
            "@id": "https://nilead.com/", 
            "@type": "WebPage", 
            "description": "Nilead provides custom design, mobile-friendly for your business&#039;s website by focusing on your brand. Start growing your branding with via your website with Nilead today!", 
            "keywords": "web design, web designer, custom website design, custom website development, ecommerce website design services, ecommerce website services, ecommerce website design company, ecommerce web design company", 
            "mainEntityOfPage": {
                "@id": "https://nilead.com/", 
                "@type": "WebPage"
            }, 
            "name": "Web services, brand building, Ecommerce &amp; SEO | Nilead  company", 
            "publisher": {
                "@type": "Organization", 
                "logo": {
                    "@type": "ImageObject", 
                    "url": "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/logo-final-curve-version-06_1492741257_grande.png"
                }, 
                "name": "Nilead"
            }
        }, 
        "event_label": "/", 
        "event_object_id": null, 
        "event_object_source": null, 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510799052, 
        "event_value": 0, 
        "event_version": "1.0", 
        "id": 5, 
        "ip": "84.212.116.233", 
        "next_nilead_id": null, 
        "nilead_id": "9d3dddb5-064f-4604-85fc-3b533ffa2257", 
        "non_interaction": false, 
        "prev_nilead_id": null, 
        "session_id": "046730g4ddoim7q711lpe29fcl", 
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
        "client_engine": "WebKit", 
        "client_locale": "nb_NO", 
        "client_name": "Safari", 
        "client_type": "browser", 
        "client_version": "10.0", 
        "created": "2017-11-16T02:19:09.127030+00:00", 
        "device_make": "", 
        "device_model": "", 
        "device_platform_name": "Mac - 10.12 - ", 
        "event_action": "generic-exit", 
        "event_category": "lead", 
        "event_context": null, 
        "event_label": "exitIntentTrigger", 
        "event_object_id": null, 
        "event_object_source": null, 
        "event_subject_id": null, 
        "event_subject_source": null, 
        "event_timestamp": 1510798748, 
        "event_value": 0, 
        "event_version": "1.0", 
        "id": 4, 
        "ip": "84.212.116.233", 
        "next_nilead_id": null, 
        "nilead_id": "9d3dddb5-064f-4604-85fc-3b533ffa2257", 
        "non_interaction": false, 
        "prev_nilead_id": null, 
        "session_id": "046730g4ddoim7q711lpe29fcl", 
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
Date: Thu, 16 Nov 2017 02:28:58 GMT
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
        "id": 7, 
        "ip": "115.77.188.31", 
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
        "id": 8, 
        "ip": "115.77.188.31", 
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
Date: Thu, 16 Nov 2017 02:28:58 GMT
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
Date: Thu, 16 Nov 2017 02:28:58 GMT
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
Date: Thu, 16 Nov 2017 02:28:58 GMT
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
        "count": 421, 
        "event_category": "lead"
    }, 
    {
        "count": 1520, 
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
Date: Thu, 16 Nov 2017 02:28:59 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

"app_id","app_name","app_version","campaign_content","campaign_id","campaign_keyword","campaign_medium","campaign_name","campaign_source","client_engine","client_locale","client_name","client_type","client_version","created","device_make","device_model","device_platform_name","event_action","event_category","event_context","event_label","event_object_id","event_object_source","event_subject_id","event_subject_source","event_timestamp","event_value","event_version","id","ip","next_nilead_id","nilead_id","non_interaction","prev_nilead_id","session_id","user_id"
"","","","","","","","","","WebKit","nb_NO","Safari","browser","10.0","2017-11-16 02:24:19.629780+00:00","","","Mac - 10.12 - ","https://nilead.com/","pageview","{u'publisher': {u'logo': {u'url': u'https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/logo-final-curve-version-06_1492741257_grande.png', u'@type': u'ImageObject'}, u'@type': u'Organization', u'name': u'Nilead'}, u'description': u'{{ global.resource.seoDescription }}', u'mainEntityOfPage': {u'@id': u'https://nilead.com/portfolio/oneonesix', u'@type': u'WebPage'}, u'keywords': u'{{ global.resource.seoKeywords }}', u'@context': u'http://schema.org', u'@id': u'https://nilead.com/portfolio/oneonesix', u'@type': u'WebPage', u'name': u'{{ global.resource.seoTitle }}'}","/portfolio/oneonesix","","","","",1510799059,0,"1.0",6,"84.212.116.233","","9d3dddb5-064f-4604-85fc-3b533ffa2257",False,"","046730g4ddoim7q711lpe29fcl",1
"","","","","","","","","","WebKit","nb_NO","Safari","browser","10.0","2017-11-16 02:24:12.970208+00:00","","","Mac - 10.12 - ","https://www.sortfolio.com/listings/23135-nilead","pageview","{u'publisher': {u'logo': {u'url': u'https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/logo-final-curve-version-06_1492741257_grande.png', u'@type': u'ImageObject'}, u'@type': u'Organization', u'name': u'Nilead'}, u'description': u'Nilead provides custom design, mobile-friendly for your business&#039;s website by focusing on your brand. Start growing your branding with via your website with Nilead today!', u'mainEntityOfPage': {u'@id': u'https://nilead.com/', u'@type': u'WebPage'}, u'keywords': u'web design, web designer, custom website design, custom website development, ecommerce website design services, ecommerce website services, ecommerce website design company, ecommerce web design company', u'@context': u'http://schema.org', u'@id': u'https://nilead.com/', u'@type': u'WebPage', u'name': u'Web services, brand building, Ecommerce &amp; SEO | Nilead  company'}","/","","","","",1510799052,0,"1.0",5,"84.212.116.233","","9d3dddb5-064f-4604-85fc-3b533ffa2257",False,"","046730g4ddoim7q711lpe29fcl",1
"","","","","","","","","","WebKit","nb_NO","Safari","browser","10.0","2017-11-16 02:19:09.127030+00:00","","","Mac - 10.12 - ","generic-exit","lead","","exitIntentTrigger","","","","",1510798748,0,"1.0",4,"84.212.116.233","","9d3dddb5-064f-4604-85fc-3b533ffa2257",False,"","046730g4ddoim7q711lpe29fcl",1

```

