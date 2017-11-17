
weekday
======

`/weekday`

ISO WEEKDAY OVERVIEW

### Methods

Method | URL | Description
--- | --- | ---
**[GET](/documentation/endpoint/ISO_WEEKDAY#list-all-standard-weekdays)** | `/weekday` | List all standard weekdays
**[GET](/documentation/endpoint/ISO_WEEKDAY#check-a-weekday)** | `/weekday/<weekday_id>` | check a weekday

### Object Attributes

Attribute | Type | Readonly | Nullable | Has Default
--- | --- | --- | --- | ---
`id` | integer | &bullet; | &nbsp; | &bullet;
`weekday` | text | &nbsp; | &nbsp; | &nbsp;

List all standard weekdays
------
<code request-method="GET">**GET** /weekday</code>

List all weekdays

### Example
```http
GET http://localhost:1234/service/weekday
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: localhost:1234
Origin: http://localhost:1234/service
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://localhost:1234/service
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Fri, 17 Nov 2017 20:17:14 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "id": 1, 
        "weekday": "Monday"
    }, 
    {
        "id": 2, 
        "weekday": "Tuesday"
    }, 
    {
        "id": 3, 
        "weekday": "Wednesday"
    }, 
    {
        "id": 4, 
        "weekday": "Thursday"
    }, 
    {
        "id": 5, 
        "weekday": "Friday"
    }, 
    {
        "id": 6, 
        "weekday": "Saturday"
    }, 
    {
        "id": 7, 
        "weekday": "Sunday"
    }
]
```


check a weekday
------
<code request-method="GET">**GET** /weekday/&lt;weekday_id&gt;</code>

Show what day of a weekday number

### Example
```http
GET http://localhost:1234/service/weekday/1
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Host: localhost:1234
Origin: http://localhost:1234/service
```

```http
HTTP/1.1 200 Ok
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://localhost:1234/service
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Fri, 17 Nov 2017 20:17:14 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

{
    "id": 1, 
    "weekday": "Monday"
}
```

