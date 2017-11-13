
aggregate
======

`/aggregate`

aggregate OVERVIEW

### Methods

Method | URL | Description
--- | --- | ---
**[GET](/documentation/endpoint/aggregate_statistics#summary-stats-by-period-of-'day',-'week',-'month',-'year')** | `/aggregate` | Summary stats by period of 'day', 'week', 'month', 'year' 
**[GET](/documentation/endpoint/aggregate_statistics#summary-stats-by-period--week)** | `/aggregate` | Summary stats by period  week
**[GET](/documentation/endpoint/aggregate_statistics#summary-stats-by-period-year)** | `/aggregate` | Summary stats by period year
**[GET](/documentation/endpoint/aggregate_statistics#summary-all-users)** | `/aggregate/user` | Summary all users
**[GET](/documentation/endpoint/aggregate_statistics#summary-stats-pageview-for-user_id-=-6)** | `/aggregate/user/<user_id>` | Summary stats pageview for user_id = 6
**[GET](/documentation/endpoint/aggregate_statistics#action---summary-stats-pageview-actions-for-user_id-=-6)** | `/aggregate/user/<user_id>/action` | Action - Summary stats pageview actions for user_id = 6
**[GET](/documentation/endpoint/aggregate_statistics#label---summary-stats-pageview-labels-for-user_id-=-6)** | `/aggregate/user/<user_id>/label` | Label - Summary stats pageview labels for user_id = 6
**[GET](/documentation/endpoint/aggregate_statistics#action-id=1---stats-pageview-action-1-for-user_id-=-6)** | `/aggregate/user/<user_id>/action/<action_id>` | Action id=1 - Stats pageview action 1 for user_id = 6
**[GET](/documentation/endpoint/aggregate_statistics#label-id=1---summary-stats-pageview-label-1-for-user_id-=-6)** | `/aggregate/user/<user_id>/label/<label_id>` | Label id=1 - Summary stats pageview label 1 for user_id = 6

### Object Attributes

Attribute | Type | Readonly | Nullable | Has Default
--- | --- | --- | --- | ---
`average_session_time` | None | &nbsp; | &bullet; | &nbsp;
`pageview` | None | &nbsp; | &bullet; | &nbsp;
`unique_session` | None | &nbsp; | &bullet; | &nbsp;
`user_id` | None | &nbsp; | &bullet; | &nbsp;

Summary stats by period of 'day', 'week', 'month', 'year' 
------
<code request-method="GET">**GET** /aggregate</code>

Summary stats count of events

### Query Parameters

Parameter | Type | Description
--- | --- | ---
`period` | string | Period can be 'day', 'week', 'month', 'year', example period=year
`user_id` | number | Only consider for events of specific user_id



### Example
```http
GET http://localhost:1234/aggregate?period=month
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: localhost:1234
Origin: http://localhost:1234
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://localhost:1234
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 03:48:08 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

{
    "change": "DOWN -62.26 percent from previous period", 
    "count": 514, 
    "data": [
        {
            "count": 514, 
            "period_time": "2017-11-20T00:00:00+00:00"
        }, 
        {
            "count": 1362, 
            "period_time": "2017-10-21T00:00:00+00:00"
        }, 
        {
            "count": 7, 
            "period_time": "2017-09-21T00:00:00+00:00"
        }
    ], 
    "period_time": "2017-11-20T00:00:00+00:00"
}
```


Summary stats by period  week
------
<code request-method="GET">**GET** /aggregate</code>

Summary stats count of events

### Example
```http
GET http://localhost:1234/aggregate?period=week&user_id=6
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: localhost:1234
Origin: http://localhost:1234
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://localhost:1234
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 03:48:09 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

{
    "change": "DOWN -85.37 percent from previous period", 
    "count": 12, 
    "data": [
        {
            "count": 12, 
            "period_time": "2017-11-16T00:00:00+00:00"
        }, 
        {
            "count": 82, 
            "period_time": "2017-11-09T00:00:00+00:00"
        }, 
        {
            "count": 39, 
            "period_time": "2017-11-02T00:00:00+00:00"
        }, 
        {
            "count": 8, 
            "period_time": "2017-10-26T00:00:00+00:00"
        }, 
        {
            "count": 20, 
            "period_time": "2017-10-19T00:00:00+00:00"
        }, 
        {
            "count": 19, 
            "period_time": "2017-10-12T00:00:00+00:00"
        }, 
        {
            "count": 7, 
            "period_time": "2017-10-05T00:00:00+00:00"
        }
    ], 
    "period_time": "2017-11-16T00:00:00+00:00"
}
```


Summary stats by period year
------
<code request-method="GET">**GET** /aggregate</code>

Summary stats count of events

### Example
```http
GET http://localhost:1234/aggregate?period=year&user_id=6
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: localhost:1234
Origin: http://localhost:1234
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://localhost:1234
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 03:48:09 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

{
    "change": "Unknown", 
    "count": 187, 
    "data": [
        {
            "count": 187, 
            "period_time": "2018-01-01T00:00:00+00:00"
        }
    ], 
    "period_time": null
}
```


Summary all users
------
<code request-method="GET">**GET** /aggregate/user</code>

Summary all users

### Example
```http
GET http://localhost:1234/aggregate/user
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: localhost:1234
Origin: http://localhost:1234
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://localhost:1234
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 03:48:09 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "average_session_time": 1743.48, 
        "pageview": {
            "actions": [
                {
                    "event_action": ""
                }, 
                {
                    "event_action": "http://block.mynilead.com/app_dev.php"
                }, 
                {
                    "event_action": "http://block.mynilead.com/app_dev.php/backend/"
                }, 
                {
                    "event_action": "https://app.hubspot.com/sales/2550281/contact/341951/?interaction=note"
                }, 
                {
                    "event_action": "https://l.facebook.com/"
                }, 
                {
                    "event_action": "https://nilead.com/"
                }, 
                {
                    "event_action": "https://nilead.com/articles"
                }, 
                {
                    "event_action": "https://nilead.com/articles?page=3"
                }, 
                {
                    "event_action": "https://nilead.com/article/web-design-in-vietnam"
                }, 
                {
                    "event_action": "https://nilead.com/backend"
                }, 
                {
                    "event_action": "https://nilead.com/digital-marketing"
                }, 
                {
                    "event_action": "https://nilead.com/experiment/cgv-discount-app"
                }, 
                {
                    "event_action": "https://nilead.com/experiment/mom-pregnancy-diary"
                }, 
                {
                    "event_action": "https://nilead.com/nilead-platform"
                }, 
                {
                    "event_action": "https://nilead.com/portfolio/oneonesix"
                }, 
                {
                    "event_action": "https://nilead.com/portfolio/pharmascience"
                }, 
                {
                    "event_action": "https://nilead.com/portfolio/solid-interior"
                }, 
                {
                    "event_action": "https://nilead.com/portfolio/yen-thanh"
                }, 
                {
                    "event_action": "https://nilead.com/website-design-services"
                }, 
                {
                    "event_action": "https://nilead.com/website-management-services"
                }, 
                {
                    "event_action": "https://www.google.com/"
                }, 
                {
                    "event_action": "https://www.google.com.tw/"
                }, 
                {
                    "event_action": "https://www.google.com.vn/"
                }
            ], 
            "event_count": 160, 
            "labels": [
                {
                    "event_label": "/"
                }, 
                {
                    "event_label": "/about-us"
                }, 
                {
                    "event_label": "/article/6-tips-for-doing-seo-in-vietnam"
                }, 
                {
                    "event_label": "/article/content-marketing-strategy-for-beginners"
                }, 
                {
                    "event_label": "/article/how-to-increase-your-website-traffic"
                }, 
                {
                    "event_label": "/article/increase-your-website-conversion-rate"
                }, 
                {
                    "event_label": "/article/keeping-your-website-active-and-alive"
                }, 
                {
                    "event_label": "/articles"
                }, 
                {
                    "event_label": "/article/seo-for-absolute-beginners"
                }, 
                {
                    "event_label": "/article/social-media-online-communities-promotion"
                }, 
                {
                    "event_label": "/articles?page=3"
                }, 
                {
                    "event_label": "/article/web-design-in-vietnam"
                }, 
                {
                    "event_label": "/digital-marketing"
                }, 
                {
                    "event_label": "/digital-marketing?ref=nail-catalog-v1"
                }, 
                {
                    "event_label": "/experiment/swipe-events-on-touch-devices"
                }, 
                {
                    "event_label": "/experiment/website-concept-for-a-hospital"
                }, 
                {
                    "event_label": "/nilead-platform"
                }, 
                {
                    "event_label": "/portfolio/oneonesix"
                }, 
                {
                    "event_label": "/portfolio/pharmascience"
                }, 
                {
                    "event_label": "/portfolio/solid-interior"
                }, 
                {
                    "event_label": "/portfolio/yen-thanh"
                }, 
                {
                    "event_label": "/?REF=NAIL-CATALOG"
                }, 
                {
                    "event_label": "/website-design-services"
                }, 
                {
                    "event_label": "/website-hosting-services"
                }, 
                {
                    "event_label": "/website-management-services"
                }
            ], 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "vi_VN", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-11-13T02:46:12.275042+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510541172, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1701, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "f9bf62e4-b562-4481-87d4-b946bb16bec9", 
                "prev_nilead_id": null, 
                "session_id": "cb4opmpm84gb48vab5p6h7448k", 
                "user_id": 6
            }, 
            "unique_action": 23, 
            "unique_label": 25
        }, 
        "unique_session": 75, 
        "user_id": 6
    }, 
    {
        "average_session_time": 505.5, 
        "pageview": {
            "actions": [
                {
                    "event_action": ""
                }, 
                {
                    "event_action": "https://nilead.com/"
                }, 
                {
                    "event_action": "https://nilead.com/article/content-marketing-strategy-for-beginners"
                }, 
                {
                    "event_action": "https://nilead.com/articles"
                }
            ], 
            "event_count": 21, 
            "labels": [
                {
                    "event_label": "/"
                }, 
                {
                    "event_label": "/article"
                }, 
                {
                    "event_label": "/article/content-marketing-strategy-for-beginners"
                }, 
                {
                    "event_label": "/article/increase-your-website-conversion-rate"
                }, 
                {
                    "event_label": "/articles"
                }, 
                {
                    "event_label": "/asdasdas"
                }, 
                {
                    "event_label": "/asdsadas"
                }, 
                {
                    "event_label": "/asdsadas2"
                }, 
                {
                    "event_label": "/asdsadsa"
                }, 
                {
                    "event_label": "/portfolio/oneonesix"
                }
            ], 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-20T05:22:21.151056+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1508476940, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 19, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "8451cf41-d976-4f06-9933-877926b9ad0f", 
                "prev_nilead_id": null, 
                "session_id": "1o5n094r994353les38r7uu9ud", 
                "user_id": 8
            }, 
            "unique_action": 4, 
            "unique_label": 10
        }, 
        "unique_session": 6, 
        "user_id": 8
    }, 
    {
        "average_session_time": 4198.516239316239, 
        "pageview": {
            "actions": [
                {
                    "event_action": ""
                }, 
                {
                    "event_action": "android-app://com.google.android.googlequicksearchbox"
                }, 
                {
                    "event_action": "http://clutch.co/"
                }, 
                {
                    "event_action": "http://m.facebook.com"
                }, 
                {
                    "event_action": "http://m.facebook.com/"
                }, 
                {
                    "event_action": "http://pagescroll.nilead.com/"
                }, 
                {
                    "event_action": "http://pagescroll.nilead.com/demo/"
                }, 
                {
                    "event_action": "https://binarylogic.lighthouseapp.com/projects/18752-authlogic/tickets/183-robe-persun"
                }, 
                {
                    "event_action": "https://cordis.europa.eu/partners/web/nileadcom"
                }, 
                {
                    "event_action": "https://duckduckgo.com/"
                }, 
                {
                    "event_action": "https://github.com/joehua87/web-components/issues/166"
                }, 
                {
                    "event_action": "https://l.facebook.com/"
                }, 
                {
                    "event_action": "https://l.messenger.com/"
                }, 
                {
                    "event_action": "https://mail.google.com/mail/u/1/"
                }, 
                {
                    "event_action": "https://mail.google.com/mail/u/1/?tab=wm"
                }, 
                {
                    "event_action": "https://nilead.com/"
                }, 
                {
                    "event_action": "https://nilead.com/about-us"
                }, 
                {
                    "event_action": "https://nilead.com/article/6-tips-for-doing-seo-in-vietnam"
                }, 
                {
                    "event_action": "https://nilead.com/article/choose-the-right-colors-for-your-website"
                }, 
                {
                    "event_action": "https://nilead.com/article/how-to-design-a-perfect-real-estate-website"
                }, 
                {
                    "event_action": "https://nilead.com/article/living-as-an-expat-in-ho-chi-minh-city"
                }, 
                {
                    "event_action": "https://nilead.com/article/optimize-your-search-engine-result-page-serp-snippet"
                }, 
                {
                    "event_action": "https://nilead.com/articles"
                }, 
                {
                    "event_action": "https://nilead.com/article/seo-for-absolute-beginners"
                }, 
                {
                    "event_action": "https://nilead.com/articles?page=2"
                }, 
                {
                    "event_action": "https://nilead.com/articles?page=3"
                }, 
                {
                    "event_action": "https://nilead.com/article/web-design-in-vietnam"
                }, 
                {
                    "event_action": "https://nilead.com/article/web-hosting-for-your-vietnam-based-website"
                }, 
                {
                    "event_action": "https://nilead.com/article/website-design-template-vs-custom-build"
                }, 
                {
                    "event_action": "https://nilead.com/?crisp_sid=session_e31cc781-5347-4a5d-8b1f-56d12183ae30"
                }, 
                {
                    "event_action": "https://nilead.com/digital-marketing"
                }, 
                {
                    "event_action": "https://nilead.com/experiment/cgv-discount-app"
                }, 
                {
                    "event_action": "https://nilead.com/experiment/full-page-and-multi-scroll-effect"
                }, 
                {
                    "event_action": "https://nilead.com/experiment/mom-pregnancy-diary"
                }, 
                {
                    "event_action": "https://nilead.com/experiment/swipe-events-on-touch-devices"
                }, 
                {
                    "event_action": "https://nilead.com/experiment/website-concept-for-a-hospital"
                }, 
                {
                    "event_action": "https://nilead.com/experiment/website-design-concept-for-a-processed-foods-company"
                }, 
                {
                    "event_action": "https://nilead.com/faq"
                }, 
                {
                    "event_action": "https://nilead.com/guest-post"
                }, 
                {
                    "event_action": "https://nilead.com/nilead-platform"
                }, 
                {
                    "event_action": "https://nilead.com/portfolio/oneonesix"
                }, 
                {
                    "event_action": "https://nilead.com/portfolio/pharmascience"
                }, 
                {
                    "event_action": "https://nilead.com/portfolio/solid-interior"
                }, 
                {
                    "event_action": "https://nilead.com/portfolio/yen-thanh"
                }, 
                {
                    "event_action": "https://nilead.com/?utm_source=topdesignfirms.com&utm_medium=referral"
                }, 
                {
                    "event_action": "https://nilead.com/website-design-services"
                }, 
                {
                    "event_action": "https://nilead.com/website-glossary"
                }, 
                {
                    "event_action": "https://nilead.com/website-project-workflow"
                }, 
                {
                    "event_action": "https://nilead.com/website-questions"
                }, 
                {
                    "event_action": "https://search.yahoo.com/"
                }, 
                {
                    "event_action": "https://t.co/6SSUMFrto3?amp=1"
                }, 
                {
                    "event_action": "http://swipe.nilead.com/"
                }, 
                {
                    "event_action": "https://www.alignable.com/westminster-ca/nilead"
                }, 
                {
                    "event_action": "https://www.awwwards.com/"
                }, 
                {
                    "event_action": "https://www.bing.com/"
                }, 
                {
                    "event_action": "https://www.ceoblognation.com/members/terrygodier/"
                }, 
                {
                    "event_action": "https://www.dexigner.com/directory/cat/Web-Design/Companies/3"
                }, 
                {
                    "event_action": "https://www.ecosia.org/"
                }, 
                {
                    "event_action": "https://www.facebook.com/"
                }, 
                {
                    "event_action": "https://www.google.ae/"
                }, 
                {
                    "event_action": "https://www.google.ca/"
                }, 
                {
                    "event_action": "https://www.google.ch/"
                }, 
                {
                    "event_action": "https://www.google.co.bw/"
                }, 
                {
                    "event_action": "https://www.google.co.id/"
                }, 
                {
                    "event_action": "https://www.google.co.in"
                }, 
                {
                    "event_action": "https://www.google.co.in/"
                }, 
                {
                    "event_action": "https://www.google.co.jp/"
                }, 
                {
                    "event_action": "https://www.google.co.kr/"
                }, 
                {
                    "event_action": "https://www.google.com/"
                }, 
                {
                    "event_action": "https://www.google.com.au/"
                }, 
                {
                    "event_action": "https://www.google.com.br/"
                }, 
                {
                    "event_action": "https://www.google.com.eg/"
                }, 
                {
                    "event_action": "https://www.google.com.hk/"
                }, 
                {
                    "event_action": "https://www.google.com.mm/"
                }, 
                {
                    "event_action": "https://www.google.com.my/"
                }, 
                {
                    "event_action": "https://www.google.com.na/"
                }, 
                {
                    "event_action": "https://www.google.com.ng/"
                }, 
                {
                    "event_action": "https://www.google.com.ph/"
                }, 
                {
                    "event_action": "https://www.google.com.pk/"
                }, 
                {
                    "event_action": "https://www.google.com.sa/"
                }, 
                {
                    "event_action": "https://www.google.com.sg/"
                }, 
                {
                    "event_action": "https://www.google.com.tr/"
                }, 
                {
                    "event_action": "https://www.google.com.tw/"
                }, 
                {
                    "event_action": "https://www.google.com.ua/"
                }, 
                {
                    "event_action": "https://www.google.com.vn/"
                }, 
                {
                    "event_action": "https://www.google.co.nz/"
                }, 
                {
                    "event_action": "https://www.google.co.th/"
                }, 
                {
                    "event_action": "https://www.google.co.uk/"
                }, 
                {
                    "event_action": "https://www.google.cz/"
                }, 
                {
                    "event_action": "https://www.google.de/"
                }, 
                {
                    "event_action": "https://www.google.es/"
                }, 
                {
                    "event_action": "https://www.google.fr/"
                }, 
                {
                    "event_action": "https://www.google.ie/"
                }, 
                {
                    "event_action": "https://www.google.it/"
                }, 
                {
                    "event_action": "https://www.google.nl/"
                }, 
                {
                    "event_action": "https://www.google.pl/"
                }, 
                {
                    "event_action": "https://www.google.ru/"
                }, 
                {
                    "event_action": "https://www.google.se/"
                }, 
                {
                    "event_action": "https://www.google.sk/"
                }, 
                {
                    "event_action": "http://vtown.vn/company/nilead-informatics-services.html"
                }, 
                {
                    "event_action": "http://vtown.vn/en/company/nilead-informatics-services.html"
                }, 
                {
                    "event_action": "http://www.bing.com/search?q=nilead&src=IE-TopResult&FORM=IE10TR"
                }, 
                {
                    "event_action": "http://www.designdirectory.co.uk/cons32/nilead.htm"
                }, 
                {
                    "event_action": "http://www.google.co.in/"
                }, 
                {
                    "event_action": "http://www.google.com.sg/"
                }, 
                {
                    "event_action": "http://www.tontrel.nl/"
                }, 
                {
                    "event_action": "http://www.webdesign-firms.com/asian-web-design/viet-nam-web-design.htm"
                }
            ], 
            "event_count": 1050, 
            "labels": [
                {
                    "event_label": "/"
                }, 
                {
                    "event_label": "/about-us"
                }, 
                {
                    "event_label": "/article"
                }, 
                {
                    "event_label": "/article/6-tips-for-doing-seo-in-vietnam"
                }, 
                {
                    "event_label": "/article/choose-the-right-colors-for-your-website"
                }, 
                {
                    "event_label": "/article/content-marketing-strategy-for-beginners"
                }, 
                {
                    "event_label": "/article/creating-a-website-from-a-z"
                }, 
                {
                    "event_label": "/article/google-tag-manager-can-harm-your-business"
                }, 
                {
                    "event_label": "/article/how-much-does-a-website-cost-in-2017"
                }, 
                {
                    "event_label": "/article/how-to-register-a-vietnam-dot-vn-domain"
                }, 
                {
                    "event_label": "/article/how-to-speed-up-your-website-loading"
                }, 
                {
                    "event_label": "/article/increase-your-website-conversion-rate"
                }, 
                {
                    "event_label": "/article/keeping-your-website-active-and-alive"
                }, 
                {
                    "event_label": "/article/keyword-research-for-absolute-beginners"
                }, 
                {
                    "event_label": "/article/living-as-an-expat-in-ho-chi-minh-city"
                }, 
                {
                    "event_label": "/article/pre-planning-your-website-guide"
                }, 
                {
                    "event_label": "/article/responsive-vs-adaptive-website-design"
                }, 
                {
                    "event_label": "/articles"
                }, 
                {
                    "event_label": "/article/seo-for-absolute-beginners"
                }, 
                {
                    "event_label": "/article/social-media-online-communities-promotion"
                }, 
                {
                    "event_label": "/articles?page=2"
                }, 
                {
                    "event_label": "/articles?page=3"
                }, 
                {
                    "event_label": "/article/the-hidden-costs-of-a-website"
                }, 
                {
                    "event_label": "/article/web-design-in-vietnam"
                }, 
                {
                    "event_label": "/article/website-101-learning-the-basics"
                }, 
                {
                    "event_label": "/article/website-101-websites-common-terms"
                }, 
                {
                    "event_label": "/article/website-design-template-vs-custom-build"
                }, 
                {
                    "event_label": "/design-lite"
                }, 
                {
                    "event_label": "/digital-marketing"
                }, 
                {
                    "event_label": "/experiment/cgv-discount-app"
                }, 
                {
                    "event_label": "/experiment/full-page-and-multi-scroll-effect"
                }, 
                {
                    "event_label": "/experiment/mom-pregnancy-diary"
                }, 
                {
                    "event_label": "/experiment/swipe-events-on-touch-devices"
                }, 
                {
                    "event_label": "/experiment/website-concept-for-a-hospital"
                }, 
                {
                    "event_label": "/faq"
                }, 
                {
                    "event_label": "/guest-post"
                }, 
                {
                    "event_label": "/na"
                }, 
                {
                    "event_label": "/nailsalon"
                }, 
                {
                    "event_label": "/nail-salon"
                }, 
                {
                    "event_label": "/nail-salon?ref"
                }, 
                {
                    "event_label": "//nail-salon?ref=nail-catalog-v1"
                }, 
                {
                    "event_label": "/nail-salon?ref=nail-catalog-v1"
                }, 
                {
                    "event_label": "/nail-salon?ref=nailv1"
                }, 
                {
                    "event_label": "/nilead-platform"
                }, 
                {
                    "event_label": "/portfolio/oneonesix"
                }, 
                {
                    "event_label": "/portfolio/pharmascience"
                }, 
                {
                    "event_label": "/portfolio/solid-interior"
                }, 
                {
                    "event_label": "/portfolio/yen-thanh"
                }, 
                {
                    "event_label": "/privacy-policy"
                }, 
                {
                    "event_label": "/?=real-estate-catalog-v1"
                }, 
                {
                    "event_label": "/?ref="
                }, 
                {
                    "event_label": "/?ref=nail-catalog"
                }, 
                {
                    "event_label": "/?ref=nail-catalog-v1"
                }, 
                {
                    "event_label": "/?/ref=real-estate-catalog-v1"
                }, 
                {
                    "event_label": "/terms-of-use"
                }, 
                {
                    "event_label": "/website-design-servcies"
                }, 
                {
                    "event_label": "/website-design-services"
                }, 
                {
                    "event_label": "/website-glossary"
                }, 
                {
                    "event_label": "/website-hosting-services"
                }, 
                {
                    "event_label": "/website-management-services"
                }, 
                {
                    "event_label": "/website-project-workflow"
                }, 
                {
                    "event_label": "/website-questions"
                }
            ], 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "AP", 
                "client_locale": "en_GB", 
                "client_name": "AP", 
                "client_type": "AP", 
                "client_version": "AP", 
                "created": "2017-11-13T03:39:52.042701+00:00", 
                "device_make": "AP", 
                "device_model": "iPhone", 
                "device_platform_name": "iOS - 11.1 - ", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510544391, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1714, 
                "ip": "103.199.41.134", 
                "next_nilead_id": null, 
                "nilead_id": "9f99def1-815e-42e7-bee7-42d078733861", 
                "prev_nilead_id": null, 
                "session_id": "fch9ovlg0oqd2vmb5ull3kd0if", 
                "user_id": 1
            }, 
            "unique_action": 107, 
            "unique_label": 62
        }, 
        "unique_session": 585, 
        "user_id": 1
    }, 
    {
        "average_session_time": 0.0, 
        "pageview": {
            "actions": [
                {
                    "event_action": ""
                }, 
                {
                    "event_action": "https://nilead.com/"
                }, 
                {
                    "event_action": "https://nilead.com/portfolio/oneonesix"
                }, 
                {
                    "event_action": "https://nilead.com/website-design-services"
                }, 
                {
                    "event_action": "https://nilead.com/website-management-services"
                }, 
                {
                    "event_action": "https://www.bing.com/"
                }, 
                {
                    "event_action": "https://www.ceoblognation.com/members/terrygodier/"
                }, 
                {
                    "event_action": "https://www.google.ca/"
                }, 
                {
                    "event_action": "https://www.google.com/"
                }, 
                {
                    "event_action": "https://www.google.com.tw/"
                }
            ], 
            "event_count": 20, 
            "labels": [
                {
                    "event_label": "/"
                }, 
                {
                    "event_label": "/article/responsive-vs-adaptive-website-design"
                }, 
                {
                    "event_label": "/articles"
                }, 
                {
                    "event_label": "/article/web-design-in-vietnam"
                }, 
                {
                    "event_label": "/nilead-platform"
                }, 
                {
                    "event_label": "/portfolio/solid-interior"
                }, 
                {
                    "event_label": "/website-design-services"
                }, 
                {
                    "event_label": "/website-project-workflow"
                }
            ], 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-11T09:50:57.709035+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1507715457, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17379, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "COmQbNpzBPMISTVLvyHgxdfnJihsAe", 
                "prev_nilead_id": null, 
                "session_id": "COmQbNpzBPMISTVLvyHgxdfnJihsAe", 
                "user_id": 2
            }, 
            "unique_action": 10, 
            "unique_label": 8
        }, 
        "unique_session": 20, 
        "user_id": 2
    }, 
    {
        "average_session_time": 0.0, 
        "pageview": {
            "actions": [
                {
                    "event_action": ""
                }, 
                {
                    "event_action": "https://nilead.com/"
                }, 
                {
                    "event_action": "https://nilead.com/portfolio/oneonesix"
                }, 
                {
                    "event_action": "https://nilead.com/portfolio/pharmascience"
                }, 
                {
                    "event_action": "https://nilead.com/website-project-workflow"
                }, 
                {
                    "event_action": "https://www.google.com/"
                }, 
                {
                    "event_action": "https://www.google.com.ph/"
                }, 
                {
                    "event_action": "https://www.google.fr/"
                }
            ], 
            "event_count": 16, 
            "labels": [
                {
                    "event_label": "/"
                }, 
                {
                    "event_label": "/about-us"
                }, 
                {
                    "event_label": "/article/web-design-in-vietnam"
                }, 
                {
                    "event_label": "/portfolio/oneonesix"
                }, 
                {
                    "event_label": "/portfolio/solid-interior"
                }, 
                {
                    "event_label": "/portfolio/yen-thanh"
                }, 
                {
                    "event_label": "/website-design-services"
                }, 
                {
                    "event_label": "/website-questions"
                }
            ], 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-12T09:45:27.790672+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1507801527, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17372, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "KdXvpLkxlPYZCJFhinzIHqEjAwSWac", 
                "prev_nilead_id": null, 
                "session_id": "KdXvpLkxlPYZCJFhinzIHqEjAwSWac", 
                "user_id": 3
            }, 
            "unique_action": 8, 
            "unique_label": 8
        }, 
        "unique_session": 16, 
        "user_id": 3
    }, 
    {
        "average_session_time": null, 
        "pageview": {
            "actions": [], 
            "event_count": 0, 
            "labels": [], 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": null, 
                "client_locale": null, 
                "client_name": null, 
                "client_type": null, 
                "client_version": null, 
                "created": null, 
                "device_make": null, 
                "device_model": null, 
                "device_platform_name": null, 
                "event_action": null, 
                "event_category": null, 
                "event_context": null, 
                "event_label": null, 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": null, 
                "event_value": null, 
                "event_version": null, 
                "id": null, 
                "ip": null, 
                "next_nilead_id": null, 
                "nilead_id": null, 
                "prev_nilead_id": null, 
                "session_id": null, 
                "user_id": null
            }, 
            "unique_action": 0, 
            "unique_label": 0
        }, 
        "unique_session": 0, 
        "user_id": 23
    }, 
    {
        "average_session_time": 0.0, 
        "pageview": {
            "actions": [
                {
                    "event_action": ""
                }, 
                {
                    "event_action": "https://nilead.com/"
                }, 
                {
                    "event_action": "https://nilead.com/article/living-as-an-expat-in-ho-chi-minh-city"
                }, 
                {
                    "event_action": "https://nilead.com/article/web-design-in-vietnam"
                }, 
                {
                    "event_action": "https://nilead.com/portfolio/solid-interior"
                }, 
                {
                    "event_action": "https://nilead.com/website-design-services"
                }, 
                {
                    "event_action": "https://nilead.com/website-questions"
                }, 
                {
                    "event_action": "https://www.awwwards.com/"
                }, 
                {
                    "event_action": "https://www.google.ca/"
                }, 
                {
                    "event_action": "https://www.google.com/"
                }, 
                {
                    "event_action": "https://www.google.com.vn/"
                }, 
                {
                    "event_action": "https://www.google.cz/"
                }
            ], 
            "event_count": 19, 
            "labels": [
                {
                    "event_label": "/"
                }, 
                {
                    "event_label": "/article/living-as-an-expat-in-ho-chi-minh-city"
                }, 
                {
                    "event_label": "/articles"
                }, 
                {
                    "event_label": "/article/web-design-in-vietnam"
                }, 
                {
                    "event_label": "/digital-marketing"
                }, 
                {
                    "event_label": "/nilead-platform"
                }, 
                {
                    "event_label": "/portfolio/oneonesix"
                }, 
                {
                    "event_label": "/website-design-services"
                }, 
                {
                    "event_label": "/website-management-services"
                }
            ], 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-12T09:41:00.888600+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://www.google.cz/", 
                "event_category": "pageview", 
                "event_context": {
                    "@context": "http://schema.org", 
                    "@id": "https://nilead.com/article/living-as-an-expat-in-ho-chi-minh-city", 
                    "@type": "Article", 
                    "author": {
                        "@type": "Person", 
                        "name": "Ivan Lamothe"
                    }, 
                    "dateModified": "2017-05-29T17:16:05+07:00 17:16", 
                    "datePublished": "2017-05-28T14:59:47+07:00 14:59", 
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
                "event_timestamp": 1507801260, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17370, 
                "ip": "213.151.77.246", 
                "next_nilead_id": null, 
                "nilead_id": "EjJPIUKOLioRvaAQnszVrTCqGbkDNl", 
                "prev_nilead_id": null, 
                "session_id": "EjJPIUKOLioRvaAQnszVrTCqGbkDNl", 
                "user_id": 4
            }, 
            "unique_action": 12, 
            "unique_label": 9
        }, 
        "unique_session": 19, 
        "user_id": 4
    }, 
    {
        "average_session_time": 0.0, 
        "pageview": {
            "actions": [
                {
                    "event_action": ""
                }, 
                {
                    "event_action": "https://nilead.com/"
                }, 
                {
                    "event_action": "https://nilead.com/about-us"
                }, 
                {
                    "event_action": "https://nilead.com/article/6-tips-for-doing-seo-in-vietnam"
                }, 
                {
                    "event_action": "https://nilead.com/article/web-design-in-vietnam"
                }, 
                {
                    "event_action": "https://nilead.com/digital-marketing"
                }, 
                {
                    "event_action": "https://nilead.com/portfolio/oneonesix"
                }, 
                {
                    "event_action": "https://www.google.ca/"
                }, 
                {
                    "event_action": "https://www.google.com/"
                }, 
                {
                    "event_action": "https://www.google.com.vn/"
                }
            ], 
            "event_count": 22, 
            "labels": [
                {
                    "event_label": "/"
                }, 
                {
                    "event_label": "/articles"
                }, 
                {
                    "event_label": "/article/web-design-in-vietnam"
                }, 
                {
                    "event_label": "/experiment/mom-pregnancy-diary"
                }, 
                {
                    "event_label": "/portfolio/oneonesix"
                }, 
                {
                    "event_label": "/portfolio/solid-interior"
                }, 
                {
                    "event_label": "/website-design-services"
                }, 
                {
                    "event_label": "/website-project-workflow"
                }, 
                {
                    "event_label": "/website-questions"
                }
            ], 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-11T15:26:04.250590+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1507735564, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17336, 
                "ip": "116.100.24.55", 
                "next_nilead_id": null, 
                "nilead_id": "cUmBFYfOSvyZIuwgadqXzirhQNtEjW", 
                "prev_nilead_id": null, 
                "session_id": "cUmBFYfOSvyZIuwgadqXzirhQNtEjW", 
                "user_id": 5
            }, 
            "unique_action": 10, 
            "unique_label": 9
        }, 
        "unique_session": 22, 
        "user_id": 5
    }, 
    {
        "average_session_time": 0.0, 
        "pageview": {
            "actions": [
                {
                    "event_action": "https://www.google.com.vn/"
                }, 
                {
                    "event_action": "http://vtown.vn/company/nilead-informatics-services.html"
                }
            ], 
            "event_count": 2, 
            "labels": [
                {
                    "event_label": "/"
                }
            ], 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-24T03:19:36.818531+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://www.google.com.vn/", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1508815176, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 215, 
                "ip": "118.70.190.105", 
                "next_nilead_id": null, 
                "nilead_id": "94cbeaca-9ab0-4bc5-b8f6-a3d34c0a3e1d", 
                "prev_nilead_id": null, 
                "session_id": "vukksfstg73sju19paujagl1ht", 
                "user_id": 9
            }, 
            "unique_action": 2, 
            "unique_label": 1
        }, 
        "unique_session": 2, 
        "user_id": 9
    }, 
    {
        "average_session_time": 0.0, 
        "pageview": {
            "actions": [
                {
                    "event_action": ""
                }, 
                {
                    "event_action": "https://nilead.com/"
                }, 
                {
                    "event_action": "https://nilead.com/experiment/mom-pregnancy-diary"
                }, 
                {
                    "event_action": "https://nilead.com/website-design-services"
                }, 
                {
                    "event_action": "https://www.bing.com/"
                }, 
                {
                    "event_action": "https://www.google.cz/"
                }
            ], 
            "event_count": 15, 
            "labels": [
                {
                    "event_label": "/"
                }, 
                {
                    "event_label": "/article/living-as-an-expat-in-ho-chi-minh-city"
                }, 
                {
                    "event_label": "/article/responsive-vs-adaptive-website-design"
                }, 
                {
                    "event_label": "/articles"
                }, 
                {
                    "event_label": "/digital-marketing"
                }, 
                {
                    "event_label": "/portfolio/oneonesix"
                }, 
                {
                    "event_label": "/website-design-services"
                }
            ], 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-17T10:15:14.799609+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1508235314, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17221, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "8451cf41-d976-4f06-9933-877926b9ad0f", 
                "prev_nilead_id": null, 
                "session_id": "m5uk6iu3d7qg3slhpfcq0kpm50", 
                "user_id": 7
            }, 
            "unique_action": 6, 
            "unique_label": 7
        }, 
        "unique_session": 15, 
        "user_id": 7
    }
]
```


Summary stats pageview for user_id = 6
------
<code request-method="GET">**GET** /aggregate/user/&lt;user_id&gt;</code>

Summary stats pageview for user_id = 6

### Example
```http
GET http://localhost:1234/aggregate/user/6
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: localhost:1234
Origin: http://localhost:1234
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://localhost:1234
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 03:48:09 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

{
    "average_session_time": 1743.48, 
    "pageview": {
        "actions": [
            {
                "event_action": ""
            }, 
            {
                "event_action": "http://block.mynilead.com/app_dev.php"
            }, 
            {
                "event_action": "http://block.mynilead.com/app_dev.php/backend/"
            }, 
            {
                "event_action": "https://app.hubspot.com/sales/2550281/contact/341951/?interaction=note"
            }, 
            {
                "event_action": "https://l.facebook.com/"
            }, 
            {
                "event_action": "https://nilead.com/"
            }, 
            {
                "event_action": "https://nilead.com/articles"
            }, 
            {
                "event_action": "https://nilead.com/articles?page=3"
            }, 
            {
                "event_action": "https://nilead.com/article/web-design-in-vietnam"
            }, 
            {
                "event_action": "https://nilead.com/backend"
            }, 
            {
                "event_action": "https://nilead.com/digital-marketing"
            }, 
            {
                "event_action": "https://nilead.com/experiment/cgv-discount-app"
            }, 
            {
                "event_action": "https://nilead.com/experiment/mom-pregnancy-diary"
            }, 
            {
                "event_action": "https://nilead.com/nilead-platform"
            }, 
            {
                "event_action": "https://nilead.com/portfolio/oneonesix"
            }, 
            {
                "event_action": "https://nilead.com/portfolio/pharmascience"
            }, 
            {
                "event_action": "https://nilead.com/portfolio/solid-interior"
            }, 
            {
                "event_action": "https://nilead.com/portfolio/yen-thanh"
            }, 
            {
                "event_action": "https://nilead.com/website-design-services"
            }, 
            {
                "event_action": "https://nilead.com/website-management-services"
            }, 
            {
                "event_action": "https://www.google.com/"
            }, 
            {
                "event_action": "https://www.google.com.tw/"
            }, 
            {
                "event_action": "https://www.google.com.vn/"
            }
        ], 
        "event_count": 160, 
        "labels": [
            {
                "event_label": "/"
            }, 
            {
                "event_label": "/about-us"
            }, 
            {
                "event_label": "/article/6-tips-for-doing-seo-in-vietnam"
            }, 
            {
                "event_label": "/article/content-marketing-strategy-for-beginners"
            }, 
            {
                "event_label": "/article/how-to-increase-your-website-traffic"
            }, 
            {
                "event_label": "/article/increase-your-website-conversion-rate"
            }, 
            {
                "event_label": "/article/keeping-your-website-active-and-alive"
            }, 
            {
                "event_label": "/articles"
            }, 
            {
                "event_label": "/article/seo-for-absolute-beginners"
            }, 
            {
                "event_label": "/article/social-media-online-communities-promotion"
            }, 
            {
                "event_label": "/articles?page=3"
            }, 
            {
                "event_label": "/article/web-design-in-vietnam"
            }, 
            {
                "event_label": "/digital-marketing"
            }, 
            {
                "event_label": "/digital-marketing?ref=nail-catalog-v1"
            }, 
            {
                "event_label": "/experiment/swipe-events-on-touch-devices"
            }, 
            {
                "event_label": "/experiment/website-concept-for-a-hospital"
            }, 
            {
                "event_label": "/nilead-platform"
            }, 
            {
                "event_label": "/portfolio/oneonesix"
            }, 
            {
                "event_label": "/portfolio/pharmascience"
            }, 
            {
                "event_label": "/portfolio/solid-interior"
            }, 
            {
                "event_label": "/portfolio/yen-thanh"
            }, 
            {
                "event_label": "/?REF=NAIL-CATALOG"
            }, 
            {
                "event_label": "/website-design-services"
            }, 
            {
                "event_label": "/website-hosting-services"
            }, 
            {
                "event_label": "/website-management-services"
            }
        ], 
        "last_event": {
            "app_id": null, 
            "app_name": null, 
            "app_version": null, 
            "client_engine": "Blink", 
            "client_locale": "vi_VN", 
            "client_name": "Chrome", 
            "client_type": "browser", 
            "client_version": "61.0", 
            "created": "2017-11-13T02:46:12.275042+00:00", 
            "device_make": "", 
            "device_model": "", 
            "device_platform_name": "Windows - 10 - x64", 
            "event_action": "", 
            "event_category": "pageview", 
            "event_context": null, 
            "event_label": "/", 
            "event_object_id": null, 
            "event_object_source": null, 
            "event_subject_id": null, 
            "event_subject_source": null, 
            "event_timestamp": 1510541172, 
            "event_value": 0, 
            "event_version": "1.0", 
            "id": 1701, 
            "ip": "115.79.59.189", 
            "next_nilead_id": null, 
            "nilead_id": "f9bf62e4-b562-4481-87d4-b946bb16bec9", 
            "prev_nilead_id": null, 
            "session_id": "cb4opmpm84gb48vab5p6h7448k", 
            "user_id": 6
        }, 
        "unique_action": 23, 
        "unique_label": 25
    }, 
    "unique_session": 75, 
    "user_id": 6
}
```


Action - Summary stats pageview actions for user_id = 6
------
<code request-method="GET">**GET** /aggregate/user/&lt;user_id&gt;/action</code>

Summary stats pageview action for user_id = 6

### Example
```http
GET http://localhost:1234/aggregate/user/6/action
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: localhost:1234
Origin: http://localhost:1234
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://localhost:1234
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 03:48:09 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "average_session_time": 1741.0689655172414, 
        "event_action": "", 
        "id": 0, 
        "pageview": {
            "event_count": 75, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "vi_VN", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-11-13T02:46:12.275042+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510541172, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1701, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "f9bf62e4-b562-4481-87d4-b946bb16bec9", 
                "prev_nilead_id": null, 
                "session_id": "cb4opmpm84gb48vab5p6h7448k", 
                "user_id": 6
            }
        }, 
        "unique_session": 58
    }, 
    {
        "average_session_time": 619.0, 
        "event_action": "http://block.mynilead.com/app_dev.php", 
        "id": 1, 
        "pageview": {
            "event_count": 2, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-11-06T09:05:52.496154+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "http://block.mynilead.com/app_dev.php", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1509959152, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1175, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "0dd4888a-40b2-4aff-9eab-d343955719b9", 
                "prev_nilead_id": null, 
                "session_id": "3l83qqpi6461kdflhamfubbg0c", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 842.0, 
        "event_action": "http://block.mynilead.com/app_dev.php/backend/", 
        "id": 2, 
        "pageview": {
            "event_count": 2, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "vi_VN", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-11-03T02:51:41.050086+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "http://block.mynilead.com/app_dev.php/backend/", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1509677500, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 933, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "f9bf62e4-b562-4481-87d4-b946bb16bec9", 
                "prev_nilead_id": null, 
                "session_id": "3g8s4qa6cnmtunvq3gua0o8vu1", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://app.hubspot.com/sales/2550281/contact/341951/?interaction=note", 
        "id": 3, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-11T15:11:02.130176+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://app.hubspot.com/sales/2550281/contact/341951/?interaction=note", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510413061, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1639, 
                "ip": "115.77.188.31", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "fm5igarfvp75uta0lam44rkmf1", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 8.0, 
        "event_action": "https://l.facebook.com/", 
        "id": 4, 
        "pageview": {
            "event_count": 3, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "vi_VN", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-31T06:22:43.354426+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://l.facebook.com/", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/website-design-services", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1509430963, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 662, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "f9bf62e4-b562-4481-87d4-b946bb16bec9", 
                "prev_nilead_id": null, 
                "session_id": "0ml3659o36cgnb20r8rae0tl74", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 270.4347826086956, 
        "event_action": "https://nilead.com/", 
        "id": 5, 
        "pageview": {
            "event_count": 30, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-12T09:43:26.467715+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/digital-marketing", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510479806, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1656, 
                "ip": "115.77.188.31", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "9ca61lmq9r6pmen2h108248gn7", 
                "user_id": 6
            }
        }, 
        "unique_session": 23
    }, 
    {
        "average_session_time": 42.5, 
        "event_action": "https://nilead.com/articles", 
        "id": 6, 
        "pageview": {
            "event_count": 8, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-11-08T13:26:57.899021+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/articles", 
                "event_category": "pageview", 
                "event_context": {
                    "@context": "http://schema.org", 
                    "@id": "https://nilead.com/article/increase-your-website-conversion-rate", 
                    "@type": "Article", 
                    "author": {
                        "@type": "Person", 
                        "name": "Vu Nguyen"
                    }, 
                    "dateModified": "2017-08-22T17:46:06+07:00 17:46", 
                    "datePublished": "2017-07-26T15:55:15+07:00 15:55", 
                    "description": "Is your website generating any returns for your business? Unfortunately, most businesses don&#039;t know if they are getting any leads or sales from their websites. For the businesses that are actually tracking these numbers, many of them don&#039;t know how to improve their website&#039;s sales performance.", 
                    "headline": "Increase your website conversion rate", 
                    "image": [
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/increase-your-website-conversion-rate-banner_1501225113_grande.jpg", 
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/increase-your-website-conversion-rate-listing_1501225113_grande.jpg"
                    ], 
                    "keywords": "tips, tricks, conversion rate, conversion optimization", 
                    "mainEntityOfPage": {
                        "@id": "https://nilead.com/article/increase-your-website-conversion-rate", 
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
                "event_label": "/article/increase-your-website-conversion-rate", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510147617, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1436, 
                "ip": "115.74.84.41", 
                "next_nilead_id": null, 
                "nilead_id": "8451cf41-d976-4f06-9933-877926b9ad0f", 
                "prev_nilead_id": null, 
                "session_id": "t32fku272tuednunu11bueskpv", 
                "user_id": 6
            }
        }, 
        "unique_session": 4
    }, 
    {
        "average_session_time": 272.0, 
        "event_action": "https://nilead.com/articles?page=3", 
        "id": 7, 
        "pageview": {
            "event_count": 4, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-07T15:44:03.385361+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/articles?page=3", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/website-design-services", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510069443, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1332, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "ko5uoave7i5so15hqh90mssaap", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://nilead.com/article/web-design-in-vietnam", 
        "id": 8, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Gecko", 
                "client_locale": "en_US", 
                "client_name": "Firefox", 
                "client_type": "browser", 
                "client_version": "56.0", 
                "created": "2017-10-10T15:34:34.615676+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/article/web-design-in-vietnam", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1507649674, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17339, 
                "ip": "183.180.68.247", 
                "next_nilead_id": null, 
                "nilead_id": "biLdymMHqEPxRfJWUOnNlrAuCcFIza", 
                "prev_nilead_id": null, 
                "session_id": "biLdymMHqEPxRfJWUOnNlrAuCcFIza", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://nilead.com/backend", 
        "id": 9, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "vi_VN", 
                "client_name": "Coc Coc", 
                "client_type": "browser", 
                "client_version": "66.4", 
                "created": "2017-11-09T09:54:55.774218+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/backend", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510221295, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1492, 
                "ip": "42.119.142.147", 
                "next_nilead_id": null, 
                "nilead_id": "10d7ad17-efe1-436c-8ad5-83080254b246", 
                "prev_nilead_id": null, 
                "session_id": "j58dua4ech2o71j1vtuiiad1rt", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://nilead.com/digital-marketing", 
        "id": 10, 
        "pageview": {
            "event_count": 2, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-08T04:09:36.089232+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/digital-marketing", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510114175, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1366, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "02c4og1cl427p09i5oqnac0dk3", 
                "user_id": 6
            }
        }, 
        "unique_session": 2
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://nilead.com/experiment/cgv-discount-app", 
        "id": 11, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "vi", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "60.0", 
                "created": "2017-10-10T07:15:17.575173+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 7 - x64", 
                "event_action": "https://nilead.com/experiment/cgv-discount-app", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/experiment/website-concept-for-a-hospital", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1507619717, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17279, 
                "ip": "118.69.32.232", 
                "next_nilead_id": null, 
                "nilead_id": "wReMBuElNaQHcvAhpWiJLStDjVkynI", 
                "prev_nilead_id": null, 
                "session_id": "wReMBuElNaQHcvAhpWiJLStDjVkynI", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://nilead.com/experiment/mom-pregnancy-diary", 
        "id": 12, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "vi", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "60.0", 
                "created": "2017-10-11T07:14:41.223284+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 7 - x64", 
                "event_action": "https://nilead.com/experiment/mom-pregnancy-diary", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/experiment/swipe-events-on-touch-devices", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1507706081, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17277, 
                "ip": "118.69.32.232", 
                "next_nilead_id": null, 
                "nilead_id": "YNcEepMxrPwfiDqUFKoXQgsILGuadJ", 
                "prev_nilead_id": null, 
                "session_id": "YNcEepMxrPwfiDqUFKoXQgsILGuadJ", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://nilead.com/nilead-platform", 
        "id": 13, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "vi", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-10T13:24:15.031769+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Mac - 10.12 - ", 
                "event_action": "https://nilead.com/nilead-platform", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/about-us", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1507641854, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17252, 
                "ip": "87.140.60.91", 
                "next_nilead_id": null, 
                "nilead_id": "sJWwxVcDautLnkQHPeqprRlOXMSFZU", 
                "prev_nilead_id": null, 
                "session_id": "sJWwxVcDautLnkQHPeqprRlOXMSFZU", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://nilead.com/portfolio/oneonesix", 
        "id": 14, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-08T08:01:32.480181+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/portfolio/oneonesix", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/portfolio/solid-interior", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510128092, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1395, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "98foogin94gvkbklbt5qr8umr6", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://nilead.com/portfolio/pharmascience", 
        "id": 15, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-08T08:06:34.085638+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/portfolio/pharmascience", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/portfolio/yen-thanh", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510128393, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1397, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "98foogin94gvkbklbt5qr8umr6", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://nilead.com/portfolio/solid-interior", 
        "id": 16, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-08T08:04:52.261362+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/portfolio/solid-interior", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/portfolio/pharmascience", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510128292, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1396, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "98foogin94gvkbklbt5qr8umr6", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://nilead.com/portfolio/yen-thanh", 
        "id": 17, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-08T08:16:08.844138+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/portfolio/yen-thanh", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510128968, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1400, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "nosqmng8ecbnis75f6g3n1pk6a", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 1368.5, 
        "event_action": "https://nilead.com/website-design-services", 
        "id": 18, 
        "pageview": {
            "event_count": 16, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-11-09T03:10:25.693252+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/website-design-services", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510197025, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1466, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "8451cf41-d976-4f06-9933-877926b9ad0f", 
                "prev_nilead_id": null, 
                "session_id": "ldsc71c0q00s7nn3vakmmkp1be", 
                "user_id": 6
            }
        }, 
        "unique_session": 10
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://nilead.com/website-management-services", 
        "id": 19, 
        "pageview": {
            "event_count": 5, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-11-09T03:05:42.312771+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/website-management-services", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510196742, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1464, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "8451cf41-d976-4f06-9933-877926b9ad0f", 
                "prev_nilead_id": null, 
                "session_id": "ldsc71c0q00s7nn3vakmmkp1be", 
                "user_id": 6
            }
        }, 
        "unique_session": 5
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://www.google.com/", 
        "id": 20, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "WebKit", 
                "client_locale": "en_US", 
                "client_name": "Safari", 
                "client_type": "browser", 
                "client_version": "11.0", 
                "created": "2017-10-12T04:07:40.247592+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Mac - 10.13 - ", 
                "event_action": "https://www.google.com/", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1507781260, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17353, 
                "ip": "14.161.15.198", 
                "next_nilead_id": null, 
                "nilead_id": "OQCSbyuHnUGzZRELskJYXitlcmITwf", 
                "prev_nilead_id": null, 
                "session_id": "OQCSbyuHnUGzZRELskJYXitlcmITwf", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://www.google.com.tw/", 
        "id": 21, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "WebKit", 
                "client_locale": "zh", 
                "client_name": "Safari", 
                "client_type": "browser", 
                "client_version": "11.0", 
                "created": "2017-09-09T04:22:48.450342+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Mac - 10.12 - ", 
                "event_action": "https://www.google.com.tw/", 
                "event_category": "pageview", 
                "event_context": {
                    "@context": "http://schema.org", 
                    "@id": "https://nilead.com/article/web-design-in-vietnam", 
                    "@type": "Article", 
                    "author": {
                        "@type": "Person", 
                        "name": "Vu Nguyen"
                    }, 
                    "dateModified": "2017-09-18T22:31:26+07:00 22:31", 
                    "datePublished": "2017-02-16T16:34:14+07:00 16:34", 
                    "description": "While website industry in Vietnam is still behind some other more developed countries, it has great potential to quickly become the region&#039;s power house with a large number of skilled IT workers and a growing tech startups market.", 
                    "headline": "Web design in Vietnam", 
                    "image": [
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/web-design-in-vietnam-banner_1497242650_grande.jpg", 
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/website-design-in-vietnam_1487252392_grande.jpg"
                    ], 
                    "keywords": "web design vietnam, web design in vietnam, website design vietnam, website design in vietnam, web design in ho chi minh city, website design in hcmc, web design saigon", 
                    "mainEntityOfPage": {
                        "@id": "https://nilead.com/article/web-design-in-vietnam", 
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
                "event_label": "/article/web-design-in-vietnam", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1504930968, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17527, 
                "ip": "118.69.71.183", 
                "next_nilead_id": null, 
                "nilead_id": "EIUNfkwKJtRobDCsYgSmPnpLxHMrOW", 
                "prev_nilead_id": null, 
                "session_id": "EIUNfkwKJtRobDCsYgSmPnpLxHMrOW", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_action": "https://www.google.com.vn/", 
        "id": 22, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Opera", 
                "client_type": "browser", 
                "client_version": "48.0", 
                "created": "2017-10-08T16:45:52.513006+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 8.1 - x64", 
                "event_action": "https://www.google.com.vn/", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1507481152, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17343, 
                "ip": "171.249.147.137", 
                "next_nilead_id": null, 
                "nilead_id": "GzPrShsQvAIVwWMYomcUnLTKXfgbui", 
                "prev_nilead_id": null, 
                "session_id": "GzPrShsQvAIVwWMYomcUnLTKXfgbui", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }
]
```


Label - Summary stats pageview labels for user_id = 6
------
<code request-method="GET">**GET** /aggregate/user/&lt;user_id&gt;/label</code>

Summary stats pageview label for user_id = 6

### Example
```http
GET http://localhost:1234/aggregate/user/6/label
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: localhost:1234
Origin: http://localhost:1234
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://localhost:1234
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 03:48:09 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "average_session_time": 1748.0526315789473, 
        "event_label": "/", 
        "id": 0, 
        "pageview": {
            "event_count": 80, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "vi_VN", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-11-13T02:46:12.275042+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510541172, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1701, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "f9bf62e4-b562-4481-87d4-b946bb16bec9", 
                "prev_nilead_id": null, 
                "session_id": "cb4opmpm84gb48vab5p6h7448k", 
                "user_id": 6
            }
        }, 
        "unique_session": 57
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/about-us", 
        "id": 1, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "vi", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-10T13:24:15.031769+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Mac - 10.12 - ", 
                "event_action": "https://nilead.com/nilead-platform", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/about-us", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1507641854, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17252, 
                "ip": "87.140.60.91", 
                "next_nilead_id": null, 
                "nilead_id": "sJWwxVcDautLnkQHPeqprRlOXMSFZU", 
                "prev_nilead_id": null, 
                "session_id": "sJWwxVcDautLnkQHPeqprRlOXMSFZU", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/article/6-tips-for-doing-seo-in-vietnam", 
        "id": 2, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-31T07:08:06.392973+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/articles", 
                "event_category": "pageview", 
                "event_context": {
                    "@context": "http://schema.org", 
                    "@id": "https://nilead.com/article/6-tips-for-doing-seo-in-vietnam", 
                    "@type": "Article", 
                    "author": {
                        "@type": "Person", 
                        "name": "Vu Nguyen"
                    }, 
                    "dateModified": "2017-05-29T18:34:12+07:00 18:34", 
                    "datePublished": "2017-05-27T21:24:46+07:00 21:24", 
                    "description": "Are you still behind your competitors? Putting your website online is just the very first step of a long journey to unless you do not care about getting return on your investment. To reach potential customers online, you need to optimize your site for search engines. In this article we will share our experience with optimizing for Vietnam market.", 
                    "headline": "6 tips for doing SEO in Vietnam", 
                    "image": [
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/seo-optimization-in-vietnam-banner_1496039927_grande.jpg", 
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/seo-optimization-in-vietnam_1496039927_grande.jpg"
                    ], 
                    "keywords": "seo, search engine optimization, vietnam, seo vietnam, google search vietnam", 
                    "mainEntityOfPage": {
                        "@id": "https://nilead.com/article/6-tips-for-doing-seo-in-vietnam", 
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
                "event_label": "/article/6-tips-for-doing-seo-in-vietnam", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1509433686, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 668, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "l0cmbeecf512frmgniqka16e05", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/article/content-marketing-strategy-for-beginners", 
        "id": 3, 
        "pageview": {
            "event_count": 2, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "vi_VN", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-31T06:22:35.649564+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://l.facebook.com/", 
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
                "event_timestamp": 1509430955, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 660, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "f9bf62e4-b562-4481-87d4-b946bb16bec9", 
                "prev_nilead_id": null, 
                "session_id": "0ml3659o36cgnb20r8rae0tl74", 
                "user_id": 6
            }
        }, 
        "unique_session": 2
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/article/how-to-increase-your-website-traffic", 
        "id": 4, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-07T15:39:31.855060+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/articles?page=3", 
                "event_category": "pageview", 
                "event_context": {
                    "@context": "http://schema.org", 
                    "@id": "https://nilead.com/article/how-to-increase-your-website-traffic", 
                    "@type": "Article", 
                    "author": {
                        "@type": "Person", 
                        "name": "Ivan Lamothe"
                    }, 
                    "dateModified": "2017-08-21T18:49:14+07:00 18:49", 
                    "datePublished": "2017-01-25T10:36:18+07:00 10:36", 
                    "description": "In web term, traffic means the amount of visitors that go to your website. Traffic is basically money. The more people go to your website, the more chances you have to promote, sell, generate leads for your services and products.", 
                    "headline": "How to increase your website traffic", 
                    "image": [
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/nilead-how-to-increase-your-website-traffic-banner-article_1497239006_grande.jpg", 
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/nilead-how-to-increase-your-website-traffic-listing-article_1497239521_grande.jpg"
                    ], 
                    "keywords": "website traffic, google, search engine, paid traffic, organic traffic, social marketing", 
                    "mainEntityOfPage": {
                        "@id": "https://nilead.com/article/how-to-increase-your-website-traffic", 
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
                "event_label": "/article/how-to-increase-your-website-traffic", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510069171, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1326, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "ko5uoave7i5so15hqh90mssaap", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 512.5, 
        "event_label": "/article/increase-your-website-conversion-rate", 
        "id": 5, 
        "pageview": {
            "event_count": 8, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-11-12T14:49:24.520789+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": {
                    "@context": "http://schema.org", 
                    "@id": "https://nilead.com/article/increase-your-website-conversion-rate", 
                    "@type": "Article", 
                    "author": {
                        "@type": "Person", 
                        "name": "Vu Nguyen"
                    }, 
                    "dateModified": "2017-08-22T17:46:06+07:00", 
                    "datePublished": "2017-07-26T15:55:15+07:00", 
                    "description": "Is your website generating any returns for your business? Unfortunately, most businesses don&#039;t know if they are getting any leads or sales from their websites. For the businesses that are actually tracking these numbers, many of them don&#039;t know how to improve their website&#039;s sales performance.", 
                    "headline": "Increase your website conversion rate", 
                    "image": [
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/increase-your-website-conversion-rate-banner_1501225113_grande.jpg", 
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/increase-your-website-conversion-rate-listing_1501225113_grande.jpg"
                    ], 
                    "keywords": "tips, tricks, conversion rate, conversion optimization", 
                    "mainEntityOfPage": {
                        "@id": "https://nilead.com/article/increase-your-website-conversion-rate", 
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
                "event_label": "/article/increase-your-website-conversion-rate", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510498164, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1676, 
                "ip": "115.77.188.31", 
                "next_nilead_id": null, 
                "nilead_id": "84f6e6ee-d899-480e-92f1-4c86586be62c", 
                "prev_nilead_id": null, 
                "session_id": "m5o2fa4bs9qqq1aarjsr715ue5", 
                "user_id": 6
            }
        }, 
        "unique_session": 6
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/article/keeping-your-website-active-and-alive", 
        "id": 6, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-07T15:39:48.436380+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/articles?page=3", 
                "event_category": "pageview", 
                "event_context": {
                    "@context": "http://schema.org", 
                    "@id": "https://nilead.com/article/keeping-your-website-active-and-alive", 
                    "@type": "Article", 
                    "author": {
                        "@type": "Person", 
                        "name": "Ivan Lamothe"
                    }, 
                    "dateModified": "2017-08-22T14:51:12+07:00 14:51", 
                    "datePublished": "2017-01-25T11:12:47+07:00 11:12", 
                    "description": "Creating a website and then leaving it un-managed is the same with throwing your spent time and money out the window. A website with outdated information, broken features can neither attract new visitors nor encourage old visitors to revisit the website.", 
                    "headline": "Keeping your website active and alive", 
                    "image": [
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/nilead-keeping-your-website-active-and-alive-banner-article_1497239970_grande.jpg", 
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/nilead-keeping-your-website-active-and-alive-listing-article_1486738446_grande.jpg"
                    ], 
                    "keywords": "active website, sales leads, brand awareness", 
                    "mainEntityOfPage": {
                        "@id": "https://nilead.com/article/keeping-your-website-active-and-alive", 
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
                "event_label": "/article/keeping-your-website-active-and-alive", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510069188, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1328, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "ko5uoave7i5so15hqh90mssaap", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/articles", 
        "id": 7, 
        "pageview": {
            "event_count": 5, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-11-10T08:30:15.399511+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/articles", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510302615, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1587, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "8451cf41-d976-4f06-9933-877926b9ad0f", 
                "prev_nilead_id": null, 
                "session_id": "trlrhnrhdrc28ctldm289gu9h5", 
                "user_id": 6
            }
        }, 
        "unique_session": 5
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/article/seo-for-absolute-beginners", 
        "id": 8, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-31T07:06:12.195724+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/articles", 
                "event_category": "pageview", 
                "event_context": {
                    "@context": "http://schema.org", 
                    "@id": "https://nilead.com/article/seo-for-absolute-beginners", 
                    "@type": "Article", 
                    "author": {
                        "@type": "Person", 
                        "name": "Vu Nguyen"
                    }, 
                    "dateModified": "2017-06-18T23:10:20+07:00 23:10", 
                    "datePublished": "2017-06-13T18:58:42+07:00 18:58", 
                    "description": "Search Engine Optimization (SEO) are big words that Digital Agencies often use to make it sound impossible to do it yourself. I&#039;m here to tell you in simple words what SEO is, how you can do it yourself in your own time without paying a single cent.", 
                    "headline": "SEO for absolute beginners", 
                    "image": [
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/seo-for-beginners-banner_1497413363_grande.png", 
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/seo-for-beginners-listing_1497413364_grande.png"
                    ], 
                    "keywords": "seo, search engine optimization, introduction, guidelines, beginners, tips, tricks", 
                    "mainEntityOfPage": {
                        "@id": "https://nilead.com/article/seo-for-absolute-beginners", 
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
                "event_label": "/article/seo-for-absolute-beginners", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1509433572, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 667, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "l0cmbeecf512frmgniqka16e05", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/article/social-media-online-communities-promotion", 
        "id": 9, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-07T15:40:04.931393+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/articles?page=3", 
                "event_category": "pageview", 
                "event_context": {
                    "@context": "http://schema.org", 
                    "@id": "https://nilead.com/article/social-media-online-communities-promotion", 
                    "@type": "Article", 
                    "author": {
                        "@type": "Person", 
                        "name": "Ivan Lamothe"
                    }, 
                    "dateModified": "2017-08-20T21:52:23+07:00 21:52", 
                    "datePublished": "2017-01-25T11:25:07+07:00 11:25", 
                    "description": "Social media and online communities are great sources for lead and sales generation. These sources may not bring you instant traffic in the short term, but diligent and consistent work will allow you attract a large and consistent flow of visitors in the long term.", 
                    "headline": "Social media and online communities marketing", 
                    "image": [
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/nilead-social-media-and-online-communities-marketing-banner-article_1497240711_grande.jpg", 
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/nilead-social-media-and-online-communities-marketing-article_1486735644_grande.jpg"
                    ], 
                    "keywords": "social media, viral marketing, sales, leads, online communities", 
                    "mainEntityOfPage": {
                        "@id": "https://nilead.com/article/social-media-online-communities-promotion", 
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
                "event_label": "/article/social-media-online-communities-promotion", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510069204, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1330, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "ko5uoave7i5so15hqh90mssaap", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 56.0, 
        "event_label": "/articles?page=3", 
        "id": 10, 
        "pageview": {
            "event_count": 4, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-07T15:40:17.896957+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/articles", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/articles?page=3", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510069217, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1331, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "ko5uoave7i5so15hqh90mssaap", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/article/web-design-in-vietnam", 
        "id": 11, 
        "pageview": {
            "event_count": 2, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "WebKit", 
                "client_locale": "zh", 
                "client_name": "Safari", 
                "client_type": "browser", 
                "client_version": "11.0", 
                "created": "2017-10-08T04:51:02.424638+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Mac - 10.12 - ", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": {
                    "@context": "http://schema.org", 
                    "@id": "https://nilead.com/article/web-design-in-vietnam", 
                    "@type": "Article", 
                    "author": {
                        "@type": "Person", 
                        "name": "Vu Nguyen"
                    }, 
                    "dateModified": "2017-09-18T22:31:26+07:00 22:31", 
                    "datePublished": "2017-02-16T16:34:14+07:00 16:34", 
                    "description": "While website industry in Vietnam is still behind some other more developed countries, it has great potential to quickly become the region&#039;s power house with a large number of skilled IT workers and a growing tech startups market.", 
                    "headline": "Web design in Vietnam", 
                    "image": [
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/web-design-in-vietnam-banner_1497242650_grande.jpg", 
                        "https://cdn-na.mynilead.com/1bfa3120d5534256b3bf17c37565c435/assets/images/website-design-in-vietnam_1487252392_grande.jpg"
                    ], 
                    "keywords": "web design vietnam, web design in vietnam, website design vietnam, website design in vietnam, web design in ho chi minh city, website design in hcmc, web design saigon", 
                    "mainEntityOfPage": {
                        "@id": "https://nilead.com/article/web-design-in-vietnam", 
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
                "event_label": "/article/web-design-in-vietnam", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1507438262, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17359, 
                "ip": "118.69.71.183", 
                "next_nilead_id": null, 
                "nilead_id": "jXRLzrfvPBCOMmxIZWyTYAoJVhskla", 
                "prev_nilead_id": null, 
                "session_id": "jXRLzrfvPBCOMmxIZWyTYAoJVhskla", 
                "user_id": 6
            }
        }, 
        "unique_session": 2
    }, 
    {
        "average_session_time": 2275.6666666666665, 
        "event_label": "/digital-marketing", 
        "id": 12, 
        "pageview": {
            "event_count": 12, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-12T09:43:26.467715+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/digital-marketing", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510479806, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1656, 
                "ip": "115.77.188.31", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "9ca61lmq9r6pmen2h108248gn7", 
                "user_id": 6
            }
        }, 
        "unique_session": 6
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/digital-marketing?ref=nail-catalog-v1", 
        "id": 13, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-02T05:50:05.853504+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/digital-marketing?ref=nail-catalog-v1", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1509601805, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 850, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "judf0p8gd7vh1vml0a86qbbobd", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/experiment/swipe-events-on-touch-devices", 
        "id": 14, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "vi", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "60.0", 
                "created": "2017-10-11T07:14:41.223284+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 7 - x64", 
                "event_action": "https://nilead.com/experiment/mom-pregnancy-diary", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/experiment/swipe-events-on-touch-devices", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1507706081, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17277, 
                "ip": "118.69.32.232", 
                "next_nilead_id": null, 
                "nilead_id": "YNcEepMxrPwfiDqUFKoXQgsILGuadJ", 
                "prev_nilead_id": null, 
                "session_id": "YNcEepMxrPwfiDqUFKoXQgsILGuadJ", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/experiment/website-concept-for-a-hospital", 
        "id": 15, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "vi", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "60.0", 
                "created": "2017-10-10T07:15:17.575173+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 7 - x64", 
                "event_action": "https://nilead.com/experiment/cgv-discount-app", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/experiment/website-concept-for-a-hospital", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1507619717, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17279, 
                "ip": "118.69.32.232", 
                "next_nilead_id": null, 
                "nilead_id": "wReMBuElNaQHcvAhpWiJLStDjVkynI", 
                "prev_nilead_id": null, 
                "session_id": "wReMBuElNaQHcvAhpWiJLStDjVkynI", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/nilead-platform", 
        "id": 16, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-10-16T11:48:08.283009+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/website-management-services", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/nilead-platform", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1508154488, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 17128, 
                "ip": "209.58.144.207", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "o0vue4a2vvl1t692nscjuibuqo", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/portfolio/oneonesix", 
        "id": 17, 
        "pageview": {
            "event_count": 2, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-08T07:57:31.962256+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/portfolio/oneonesix", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510127851, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1394, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "98foogin94gvkbklbt5qr8umr6", 
                "user_id": 6
            }
        }, 
        "unique_session": 2
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/portfolio/pharmascience", 
        "id": 18, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-08T08:04:52.261362+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/portfolio/solid-interior", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/portfolio/pharmascience", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510128292, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1396, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "98foogin94gvkbklbt5qr8umr6", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/portfolio/solid-interior", 
        "id": 19, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-08T08:01:32.480181+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/portfolio/oneonesix", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/portfolio/solid-interior", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510128092, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1395, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "98foogin94gvkbklbt5qr8umr6", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/portfolio/yen-thanh", 
        "id": 20, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-08T08:06:34.085638+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/portfolio/pharmascience", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/portfolio/yen-thanh", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510128393, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1397, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "98foogin94gvkbklbt5qr8umr6", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 0.0, 
        "event_label": "/?REF=NAIL-CATALOG", 
        "id": 21, 
        "pageview": {
            "event_count": 1, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-01T14:29:16.249747+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/?REF=NAIL-CATALOG", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1509546556, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 775, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "39lqi5ges62fmfh6qrthgq2jog", 
                "user_id": 6
            }
        }, 
        "unique_session": 1
    }, 
    {
        "average_session_time": 443.2857142857143, 
        "event_label": "/website-design-services", 
        "id": 22, 
        "pageview": {
            "event_count": 18, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-11-09T03:10:22.228803+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "https://nilead.com/", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/website-design-services", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510197022, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1465, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "8451cf41-d976-4f06-9933-877926b9ad0f", 
                "prev_nilead_id": null, 
                "session_id": "ldsc71c0q00s7nn3vakmmkp1be", 
                "user_id": 6
            }
        }, 
        "unique_session": 14
    }, 
    {
        "average_session_time": 286.6666666666667, 
        "event_label": "/website-hosting-services", 
        "id": 23, 
        "pageview": {
            "event_count": 4, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "es_ES", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "62.0", 
                "created": "2017-11-10T18:15:01.816908+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/website-hosting-services", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510337701, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1617, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "ef6f3ab2-37e0-4288-bbc6-f546dc44b43d", 
                "prev_nilead_id": null, 
                "session_id": "jog99ror8qicj0jk9tkmmedki7", 
                "user_id": 6
            }
        }, 
        "unique_session": 3
    }, 
    {
        "average_session_time": 64.375, 
        "event_label": "/website-management-services", 
        "id": 24, 
        "pageview": {
            "event_count": 9, 
            "last_event": {
                "app_id": null, 
                "app_name": null, 
                "app_version": null, 
                "client_engine": "Blink", 
                "client_locale": "en_US", 
                "client_name": "Chrome", 
                "client_type": "browser", 
                "client_version": "61.0", 
                "created": "2017-11-09T01:44:27.564603+00:00", 
                "device_make": "", 
                "device_model": "", 
                "device_platform_name": "Windows - 10 - x64", 
                "event_action": "", 
                "event_category": "pageview", 
                "event_context": null, 
                "event_label": "/website-management-services", 
                "event_object_id": null, 
                "event_object_source": null, 
                "event_subject_id": null, 
                "event_subject_source": null, 
                "event_timestamp": 1510191867, 
                "event_value": 0, 
                "event_version": "1.0", 
                "id": 1463, 
                "ip": "115.79.59.189", 
                "next_nilead_id": null, 
                "nilead_id": "8451cf41-d976-4f06-9933-877926b9ad0f", 
                "prev_nilead_id": null, 
                "session_id": "dvg6n4p475jr6ne49m58ripp4t", 
                "user_id": 6
            }
        }, 
        "unique_session": 8
    }
]
```


Action id=1 - Stats pageview action 1 for user_id = 6
------
<code request-method="GET">**GET** /aggregate/user/&lt;user_id&gt;/action/&lt;action_id&gt;</code>

Summary stats pageview action 1 for user_id = 6

### Example
```http
GET http://localhost:1234/aggregate/user/6/action/1
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: localhost:1234
Origin: http://localhost:1234
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://localhost:1234
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 03:48:09 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

{
    "average_session_time": 619.0, 
    "event_action": "http://block.mynilead.com/app_dev.php", 
    "id": 1, 
    "pageview": {
        "event_count": 2, 
        "last_event": {
            "app_id": null, 
            "app_name": null, 
            "app_version": null, 
            "client_engine": "Blink", 
            "client_locale": "en_US", 
            "client_name": "Chrome", 
            "client_type": "browser", 
            "client_version": "61.0", 
            "created": "2017-11-06T09:05:52.496154+00:00", 
            "device_make": "", 
            "device_model": "", 
            "device_platform_name": "Windows - 10 - x64", 
            "event_action": "http://block.mynilead.com/app_dev.php", 
            "event_category": "pageview", 
            "event_context": null, 
            "event_label": "/", 
            "event_object_id": null, 
            "event_object_source": null, 
            "event_subject_id": null, 
            "event_subject_source": null, 
            "event_timestamp": 1509959152, 
            "event_value": 0, 
            "event_version": "1.0", 
            "id": 1175, 
            "ip": "115.79.59.189", 
            "next_nilead_id": null, 
            "nilead_id": "0dd4888a-40b2-4aff-9eab-d343955719b9", 
            "prev_nilead_id": null, 
            "session_id": "3l83qqpi6461kdflhamfubbg0c", 
            "user_id": 6
        }
    }, 
    "unique_session": 1
}
```


Label id=1 - Summary stats pageview label 1 for user_id = 6
------
<code request-method="GET">**GET** /aggregate/user/&lt;user_id&gt;/label/&lt;label_id&gt;</code>

Summary stats pageview label 1 for user_id = 6

### Example
```http
GET http://localhost:1234/aggregate/user/6/label/1
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: localhost:1234
Origin: http://localhost:1234
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://localhost:1234
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Mon, 13 Nov 2017 03:48:10 GMT
Expires: 0
Server: TwistedWeb/17.1.0
Transfer-Encoding: chunked
Vary: Origin

{
    "average_session_time": 0.0, 
    "event_label": "/about-us", 
    "id": 1, 
    "pageview": {
        "event_count": 1, 
        "last_event": {
            "app_id": null, 
            "app_name": null, 
            "app_version": null, 
            "client_engine": "Blink", 
            "client_locale": "vi", 
            "client_name": "Chrome", 
            "client_type": "browser", 
            "client_version": "61.0", 
            "created": "2017-10-10T13:24:15.031769+00:00", 
            "device_make": "", 
            "device_model": "", 
            "device_platform_name": "Mac - 10.12 - ", 
            "event_action": "https://nilead.com/nilead-platform", 
            "event_category": "pageview", 
            "event_context": null, 
            "event_label": "/about-us", 
            "event_object_id": null, 
            "event_object_source": null, 
            "event_subject_id": null, 
            "event_subject_source": null, 
            "event_timestamp": 1507641854, 
            "event_value": 0, 
            "event_version": "1.0", 
            "id": 17252, 
            "ip": "87.140.60.91", 
            "next_nilead_id": null, 
            "nilead_id": "sJWwxVcDautLnkQHPeqprRlOXMSFZU", 
            "prev_nilead_id": null, 
            "session_id": "sJWwxVcDautLnkQHPeqprRlOXMSFZU", 
            "user_id": 6
        }
    }, 
    "unique_session": 1
}
```

