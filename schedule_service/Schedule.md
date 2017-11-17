
Employee Schedules
======

`/store/1/employee/1/schedule`

SCHEDULE OVERVIEW: Schedules are generated from 7 weekday

### Methods

Method | URL | Description
--- | --- | ---
**[GET](/documentation/endpoint/Schedule#list-all-schedules-of-a-employee)** | `/store/<store-id>/employee/<employee-id>/schedule` | List all schedules of a employee
**[GET](/documentation/endpoint/Schedule#show-today-schedule-id-of-a-employee)** | `/store/<store_id>/employee/<employee-id>/schedule/today` | Show today schedule id of a employee
**[GET](/documentation/endpoint/Schedule#show-schedule-id-of-a-employee)** | `/store/<store_id>/employee/<employee-id>/schedule/5` | Show schedule id of a employee
**[PUT](/documentation/endpoint/Schedule#update-a-schedule)** | `/store/<store-id>/employee/<employee-id>/schedule/<schedule-id>` | Update A Schedule
**[PUT](/documentation/endpoint/Schedule#update-schedules)** | `/store/<store-id>/employee/<employee-id>/schedule` | Update Schedules

### Object Attributes

Attribute | Type | Readonly | Nullable | Has Default
--- | --- | --- | --- | ---
`available` | boolean | &nbsp; | &nbsp; | &bullet;
`employee_id` | integer | &nbsp; | &nbsp; | &nbsp;
`id` | integer | &bullet; | &nbsp; | &bullet;
`iso_weekday_id` | integer | &nbsp; | &nbsp; | &nbsp;
`session_end` | integer | &nbsp; | &nbsp; | &bullet;
`session_start` | integer | &nbsp; | &nbsp; | &bullet;
`updated` | timestamp | &nbsp; | &nbsp; | &bullet;

List all schedules of a employee
------
<code request-method="GET">**GET** /store/&lt;store-id&gt;/employee/&lt;employee-id&gt;/schedule</code>

List all schedules of a employee

### Example
```http
GET http://localhost:1234/service/store/1/employee/1/schedule
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
Date: Fri, 17 Nov 2017 20:42:23 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "available": true, 
        "employee_id": 1, 
        "id": 1, 
        "iso_weekday_id": 1, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Monday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 2, 
        "iso_weekday_id": 2, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Tuesday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 3, 
        "iso_weekday_id": 3, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Wednesday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 4, 
        "iso_weekday_id": 4, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Thursday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 5, 
        "iso_weekday_id": 5, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Friday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 6, 
        "iso_weekday_id": 6, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Saturday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 7, 
        "iso_weekday_id": 7, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Sunday"
    }
]
```


Show today schedule id of a employee
------
<code request-method="GET">**GET** /store/&lt;store_id&gt;/employee/&lt;employee-id&gt;/schedule/today</code>

Show  today schedule id of a employee

### Example
```http
GET http://localhost:1234/service/store/1/employee/1/schedule/today
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
Date: Fri, 17 Nov 2017 20:42:24 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

{
    "available": true, 
    "employee_id": 1, 
    "id": 5, 
    "iso_weekday_id": 5, 
    "session_end": 17, 
    "session_start": 9, 
    "updated": "2017-11-16T23:51:56.343611+00:00", 
    "weekday": "Friday"
}
```


Show schedule id of a employee
------
<code request-method="GET">**GET** /store/&lt;store_id&gt;/employee/&lt;employee-id&gt;/schedule/5</code>

Show schedule id of a employee

### Example
```http
GET http://localhost:1234/service/store/1/employee/1/schedule/5
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
Date: Fri, 17 Nov 2017 20:42:24 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

{
    "available": true, 
    "employee_id": 1, 
    "id": 5, 
    "iso_weekday_id": 5, 
    "session_end": 17, 
    "session_start": 9, 
    "updated": "2017-11-16T23:51:56.343611+00:00", 
    "weekday": "Friday"
}
```


Update A Schedule
------
<code request-method="PUT">**PUT** /store/&lt;store-id&gt;/employee/&lt;employee-id&gt;/schedule/&lt;schedule-id&gt;</code>

update schedule

### Example
```http
PUT http://localhost:1234/service/store/1/employee/1/schedule/5
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Content-Length: 75
Content-Type: application/json
Host: localhost:1234
Origin: http://localhost:1234/service

{
    "available": true, 
    "session_end": 20, 
    "session_start": 10
}
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
Date: Fri, 17 Nov 2017 20:42:24 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

{
    "available": true, 
    "employee_id": 1, 
    "id": 5, 
    "iso_weekday_id": 5, 
    "session_end": 20, 
    "session_start": 10, 
    "updated": "2017-11-16T23:51:56.343611+00:00", 
    "weekday": "Friday"
}
```


Update Schedules
------
<code request-method="PUT">**PUT** /store/&lt;store-id&gt;/employee/&lt;employee-id&gt;/schedule</code>

You can Update a list of Schedule or 1 schedule, schedule's id must be included

### Example
```http
PUT http://localhost:1234/service/store/1/employee/1/schedule
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Content-Length: 1423
Content-Type: application/json
Host: localhost:1234
Origin: http://localhost:1234/service

[
    {
        "available": true, 
        "employee_id": 1, 
        "id": 1, 
        "iso_weekday_id": 1, 
        "session_end": 17, 
        "session_start": 9, 
        "weekday": "Monday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 2, 
        "iso_weekday_id": 2, 
        "session_end": 17, 
        "session_start": 9, 
        "weekday": "Tuesday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 3, 
        "iso_weekday_id": 3, 
        "session_end": 17, 
        "session_start": 9, 
        "weekday": "Wednesday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 4, 
        "iso_weekday_id": 4, 
        "session_end": 17, 
        "session_start": 9, 
        "weekday": "Thursday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 5, 
        "iso_weekday_id": 5, 
        "session_end": 17, 
        "session_start": 9, 
        "weekday": "Friday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 6, 
        "iso_weekday_id": 6, 
        "session_end": 17, 
        "session_start": 9, 
        "weekday": "Saturday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 7, 
        "iso_weekday_id": 7, 
        "session_end": 17, 
        "session_start": 9, 
        "weekday": "Sunday"
    }
]
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
Date: Fri, 17 Nov 2017 20:42:25 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "available": true, 
        "employee_id": 1, 
        "id": 1, 
        "iso_weekday_id": 1, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Monday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 2, 
        "iso_weekday_id": 2, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Tuesday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 3, 
        "iso_weekday_id": 3, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Wednesday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 4, 
        "iso_weekday_id": 4, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Thursday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 5, 
        "iso_weekday_id": 5, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Friday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 6, 
        "iso_weekday_id": 6, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Saturday"
    }, 
    {
        "available": true, 
        "employee_id": 1, 
        "id": 7, 
        "iso_weekday_id": 7, 
        "session_end": 17, 
        "session_start": 9, 
        "updated": "2017-11-16T23:51:56.343611+00:00", 
        "weekday": "Sunday"
    }
]
```

