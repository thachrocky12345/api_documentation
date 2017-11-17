
Store
======

`/store`

STORE OVERVIEW

### Methods

Method | URL | Description
--- | --- | ---
**[GET](/documentation/endpoint/Store#list-all-store-of-a-business-including-employees)** | `/store` | List all store of a business including employees
**[GET](/documentation/endpoint/Store#show-a-store-by-id-including-employees)** | `/store/<store_id>` | Show a store by id including employees
**[POST](/documentation/endpoint/Store#insert-store)** | `/store` | Insert Store
**[PUT](/documentation/endpoint/Store#update-store)** | `/store` | Update Store
**[DELETE](/documentation/endpoint/Store#delete-store)** | `/store` | DELETE Store

### Object Attributes

Attribute | Type | Readonly | Nullable | Has Default
--- | --- | --- | --- | ---
`address` | text | &nbsp; | &nbsp; | &nbsp;
`city` | text | &nbsp; | &nbsp; | &nbsp;
`created` | timestamp | &nbsp; | &nbsp; | &bullet;
`email` | text | &nbsp; | &bullet; | &nbsp;
`id` | integer | &bullet; | &nbsp; | &bullet;
`name` | text | &nbsp; | &nbsp; | &nbsp;
`phone` | text | &nbsp; | &bullet; | &nbsp;
`state` | text | &nbsp; | &nbsp; | &nbsp;
`updated` | timestamp | &nbsp; | &nbsp; | &bullet;
`zipcode` | integer | &nbsp; | &nbsp; | &nbsp;

List all store of a business including employees
------
<code request-method="GET">**GET** /store</code>

List all store of a business including employees

### Query Parameters

Parameter | Type | Description
--- | --- | ---
`limit` | number | You can set limit return
`page` | number | page will go with limit, example limit=5&page=1
`search` | string | Search for store name or address
`store_id` | int | Returns store with specific id, you also can use store/<store_id>



### Example
```http
GET http://localhost:1234/service/store
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
Date: Fri, 17 Nov 2017 00:17:39 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "address": "7625 N Wabash Ave", 
        "city": "Gladstone", 
        "created": "2017-11-16T23:51:34.984731+00:00", 
        "email": "thachrocky@icloud.com", 
        "employees": [], 
        "id": 2, 
        "name": "StoreA", 
        "phone": "816-803-1523", 
        "state": "MO", 
        "updated": "2017-11-16T23:51:34.984731+00:00", 
        "zipcode": 64118
    }, 
    {
        "address": "8525 N Wabash Ave", 
        "city": "Gladstone", 
        "created": "2017-11-16T23:51:34.984731+00:00", 
        "email": "thachrocky12345@icloud.com", 
        "employees": [
            {
                "address": "8625 N Wabash Ave", 
                "allow_backup": 1, 
                "break_time": 11, 
                "city": "Gladstone", 
                "created": "2017-11-16T23:51:56.311145+00:00", 
                "email": "vuhoangnguyen@gmail.com", 
                "first_name": "Employee1", 
                "id": 1, 
                "last_name": "Nguyen", 
                "phone": "816-803-1523", 
                "rate": 5.0, 
                "session_in_minutes": 20, 
                "state": "MO", 
                "store_id": 1, 
                "updated": "2017-11-16T23:51:56.311145+00:00", 
                "zipcode": 64118
            }, 
            {
                "address": "7625 N Wabash Ave", 
                "allow_backup": 2, 
                "break_time": 11, 
                "city": "Gladstone", 
                "created": "2017-11-16T23:51:56.311145+00:00", 
                "email": "thachrocky@icloud.com", 
                "first_name": "Employee2", 
                "id": 2, 
                "last_name": "Bui", 
                "phone": "816-803-1523", 
                "rate": 5.0, 
                "session_in_minutes": 30, 
                "state": "MO", 
                "store_id": 1, 
                "updated": "2017-11-16T23:51:56.311145+00:00", 
                "zipcode": 64118
            }, 
            {
                "address": "7625 N Wabash Ave", 
                "allow_backup": 2, 
                "break_time": 11, 
                "city": "Gladstone", 
                "created": "2017-11-16T23:51:56.311145+00:00", 
                "email": "thachrocky@icloud.com", 
                "first_name": "Employee3", 
                "id": 3, 
                "last_name": "Bui", 
                "phone": "816-803-1523", 
                "rate": 5.0, 
                "session_in_minutes": 30, 
                "state": "MO", 
                "store_id": 1, 
                "updated": "2017-11-16T23:51:56.311145+00:00", 
                "zipcode": 64118
            }, 
            {
                "address": "7625 N Wabash Ave", 
                "allow_backup": 2, 
                "break_time": 11, 
                "city": "Gladstone", 
                "created": "2017-11-16T23:51:56.311145+00:00", 
                "email": "thachrocky@icloud.com", 
                "first_name": "Employee4", 
                "id": 4, 
                "last_name": "Bui", 
                "phone": "816-803-1523", 
                "rate": 5.0, 
                "session_in_minutes": 30, 
                "state": "MO", 
                "store_id": 1, 
                "updated": "2017-11-16T23:51:56.311145+00:00", 
                "zipcode": 64118
            }, 
            {
                "address": "7625 N Wabash Ave", 
                "allow_backup": 2, 
                "break_time": 11, 
                "city": "Gladstone", 
                "created": "2017-11-16T23:51:56.311145+00:00", 
                "email": "thachrocky@icloud.com", 
                "first_name": "Employee5", 
                "id": 5, 
                "last_name": "Bui", 
                "phone": "816-803-1523", 
                "rate": 5.0, 
                "session_in_minutes": 30, 
                "state": "MO", 
                "store_id": 1, 
                "updated": "2017-11-16T23:51:56.311145+00:00", 
                "zipcode": 64118
            }
        ], 
        "id": 1, 
        "name": "StoreB", 
        "phone": "816-803-1523", 
        "state": "MO", 
        "updated": "2017-11-16T23:51:34.984731+00:00", 
        "zipcode": 64118
    }
]
```


Show a store by id including employees
------
<code request-method="GET">**GET** /store/&lt;store_id&gt;</code>

Show a store by id including employees

### Example
```http
GET http://localhost:1234/service/store/1
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
Date: Fri, 17 Nov 2017 00:17:39 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

{
    "address": "8525 N Wabash Ave", 
    "city": "Gladstone", 
    "created": "2017-11-16T23:51:34.984731+00:00", 
    "email": "thachrocky12345@icloud.com", 
    "employees": [
        {
            "address": "8625 N Wabash Ave", 
            "allow_backup": 1, 
            "break_time": 11, 
            "city": "Gladstone", 
            "created": "2017-11-16T23:51:56.311145+00:00", 
            "email": "vuhoangnguyen@gmail.com", 
            "first_name": "Employee1", 
            "id": 1, 
            "last_name": "Nguyen", 
            "phone": "816-803-1523", 
            "rate": 5.0, 
            "session_in_minutes": 20, 
            "state": "MO", 
            "store_id": 1, 
            "updated": "2017-11-16T23:51:56.311145+00:00", 
            "zipcode": 64118
        }, 
        {
            "address": "7625 N Wabash Ave", 
            "allow_backup": 2, 
            "break_time": 11, 
            "city": "Gladstone", 
            "created": "2017-11-16T23:51:56.311145+00:00", 
            "email": "thachrocky@icloud.com", 
            "first_name": "Employee2", 
            "id": 2, 
            "last_name": "Bui", 
            "phone": "816-803-1523", 
            "rate": 5.0, 
            "session_in_minutes": 30, 
            "state": "MO", 
            "store_id": 1, 
            "updated": "2017-11-16T23:51:56.311145+00:00", 
            "zipcode": 64118
        }, 
        {
            "address": "7625 N Wabash Ave", 
            "allow_backup": 2, 
            "break_time": 11, 
            "city": "Gladstone", 
            "created": "2017-11-16T23:51:56.311145+00:00", 
            "email": "thachrocky@icloud.com", 
            "first_name": "Employee3", 
            "id": 3, 
            "last_name": "Bui", 
            "phone": "816-803-1523", 
            "rate": 5.0, 
            "session_in_minutes": 30, 
            "state": "MO", 
            "store_id": 1, 
            "updated": "2017-11-16T23:51:56.311145+00:00", 
            "zipcode": 64118
        }, 
        {
            "address": "7625 N Wabash Ave", 
            "allow_backup": 2, 
            "break_time": 11, 
            "city": "Gladstone", 
            "created": "2017-11-16T23:51:56.311145+00:00", 
            "email": "thachrocky@icloud.com", 
            "first_name": "Employee4", 
            "id": 4, 
            "last_name": "Bui", 
            "phone": "816-803-1523", 
            "rate": 5.0, 
            "session_in_minutes": 30, 
            "state": "MO", 
            "store_id": 1, 
            "updated": "2017-11-16T23:51:56.311145+00:00", 
            "zipcode": 64118
        }, 
        {
            "address": "7625 N Wabash Ave", 
            "allow_backup": 2, 
            "break_time": 11, 
            "city": "Gladstone", 
            "created": "2017-11-16T23:51:56.311145+00:00", 
            "email": "thachrocky@icloud.com", 
            "first_name": "Employee5", 
            "id": 5, 
            "last_name": "Bui", 
            "phone": "816-803-1523", 
            "rate": 5.0, 
            "session_in_minutes": 30, 
            "state": "MO", 
            "store_id": 1, 
            "updated": "2017-11-16T23:51:56.311145+00:00", 
            "zipcode": 64118
        }
    ], 
    "id": 1, 
    "name": "StoreB", 
    "phone": "816-803-1523", 
    "state": "MO", 
    "updated": "2017-11-16T23:51:34.984731+00:00", 
    "zipcode": 64118
}
```


Insert Store
------
<code request-method="POST">**POST** /store</code>

You can Insert a list of Stores or 1 store

### Example
```http
POST http://localhost:1234/service/store
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Content-Length: 257
Content-Type: application/json
Host: localhost:1234
Origin: http://localhost:1234/service

[
    {
        "address": "7625 N Wabash Ave", 
        "city": "Gladstone", 
        "email": "thachrocky@icloud.com", 
        "id": 3, 
        "name": "StoreA", 
        "phone": "816-803-1523", 
        "state": "MO", 
        "zipcode": 64118
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
Date: Fri, 17 Nov 2017 00:17:39 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "address": "7625 N Wabash Ave", 
        "city": "Gladstone", 
        "created": "2017-11-17T00:17:39.750198+00:00", 
        "email": "thachrocky@icloud.com", 
        "id": 3, 
        "name": "StoreA", 
        "phone": "816-803-1523", 
        "state": "MO", 
        "updated": "2017-11-17T00:17:39.750198+00:00", 
        "zipcode": 64118
    }
]
```


Update Store
------
<code request-method="PUT">**PUT** /store</code>

You can Update a list of Stores or 1 store, store's id must included

### Example
```http
PUT http://localhost:1234/service/store
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Content-Length: 260
Content-Type: application/json
Host: localhost:1234
Origin: http://localhost:1234/service

[
    {
        "address": "7625 N Wabash Ave", 
        "city": "Gladstone", 
        "email": "thachrocky@icloud.com", 
        "id": 3, 
        "name": "StoreTest", 
        "phone": "816-803-1523", 
        "state": "MO", 
        "zipcode": 64118
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
Date: Fri, 17 Nov 2017 00:17:39 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "address": "7625 N Wabash Ave", 
        "city": "Gladstone", 
        "created": "2017-11-17T00:17:39.750198+00:00", 
        "email": "thachrocky@icloud.com", 
        "id": 3, 
        "name": "StoreTest", 
        "phone": "816-803-1523", 
        "state": "MO", 
        "updated": "2017-11-16T18:17:39.874608+00:00", 
        "zipcode": 64118
    }
]
```


DELETE Store
------
<code request-method="DELETE">**DELETE** /store</code>

You can DELETE a list of Stores or 1 store, store's id must included

### Example
```http
DELETE http://localhost:1234/service/store
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Content-Length: 15
Content-Type: application/json
Host: localhost:1234
Origin: http://localhost:1234/service

{
    "id": 3
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
Date: Fri, 17 Nov 2017 00:17:39 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

{
    "address": "7625 N Wabash Ave", 
    "city": "Gladstone", 
    "created": "2017-11-17T00:17:39.750198+00:00", 
    "email": "thachrocky@icloud.com", 
    "id": 3, 
    "name": "StoreTest", 
    "phone": "816-803-1523", 
    "state": "MO", 
    "updated": "2017-11-16T18:17:39.874608+00:00", 
    "zipcode": 64118
}
```

