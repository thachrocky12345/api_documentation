
Users
======

`/user`

USER OVERVIEW

### Methods

Method | URL | Description
--- | --- | ---
**[GET](/documentation/endpoint/User#list-all-user-or-clients-of-the-business)** | `/user` | List all user or clients of the business
**[GET](/documentation/endpoint/User#show-a-user)** | `/user/<user_id>` | Show a user
**[POST](/documentation/endpoint/User#insert-user)** | `/user` | Insert User
**[PUT](/documentation/endpoint/User#update-user)** | `/user` | Update User
**[DELETE](/documentation/endpoint/User#delete-users)** | `/user` | DELETE users

### Object Attributes

Attribute | Type | Readonly | Nullable | Has Default
--- | --- | --- | --- | ---
`address` | text | &nbsp; | &bullet; | &nbsp;
`can_email` | boolean | &nbsp; | &nbsp; | &bullet;
`can_text` | boolean | &nbsp; | &nbsp; | &bullet;
`city` | text | &nbsp; | &bullet; | &nbsp;
`created` | timestamp | &nbsp; | &nbsp; | &bullet;
`email` | text | &nbsp; | &bullet; | &nbsp;
`first_name` | text | &nbsp; | &bullet; | &nbsp;
`id` | integer | &bullet; | &nbsp; | &bullet;
`language` | text | &nbsp; | &bullet; | &nbsp;
`last_login` | timestamp | &nbsp; | &nbsp; | &bullet;
`last_name` | text | &nbsp; | &bullet; | &nbsp;
`password` | text | &nbsp; | &bullet; | &nbsp;
`phone` | text | &nbsp; | &nbsp; | &nbsp;
`role` | text | &nbsp; | &nbsp; | &bullet;
`social_network` | text | &nbsp; | &bullet; | &nbsp;
`state` | text | &nbsp; | &bullet; | &nbsp;
`token` | text | &nbsp; | &bullet; | &nbsp;
`updated` | timestamp | &nbsp; | &nbsp; | &bullet;
`username` | text | &nbsp; | &bullet; | &nbsp;
`zipcode` | integer | &nbsp; | &bullet; | &nbsp;

List all user or clients of the business
------
<code request-method="GET">**GET** /user</code>

List all user or clients of the business

### Query Parameters

Parameter | Type | Description
--- | --- | ---
`id` | int | Returns user with specific id, you can provide more than one id, example: id=1&id=2>
`limit` | number | You can set limit return
`page` | number | page will go with limit, example limit=5&page=1
`search` | string | Search for employee first_name, last_name, email, or username



### Example
```http
GET http://localhost:1234/service/user?id=1&id=2
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
Date: Fri, 17 Nov 2017 20:37:44 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "address": "8625 N Wabash Ave", 
        "can_email": true, 
        "can_text": true, 
        "city": "Gladstone", 
        "created": "2017-11-17T19:42:26.299243+00:00", 
        "email": "thachrocky12345@gmail.com", 
        "first_name": "CustomerA", 
        "id": 2, 
        "language": null, 
        "last_login": "2017-11-17T19:42:26.299243+00:00", 
        "last_name": "Nguyen", 
        "password": "448ed7416fce2cb66c285d182b1ba3df1e90016d", 
        "phone": "816-803-1523", 
        "role": "EMPLOYEE", 
        "social_network": null, 
        "state": "MO", 
        "token": null, 
        "updated": "2017-11-17T19:42:26.299243+00:00", 
        "username": "nguyen2", 
        "zipcode": 64118
    }, 
    {
        "address": "8625 N Wabash Ave", 
        "can_email": true, 
        "can_text": true, 
        "city": "Gladstone", 
        "created": "2017-11-17T19:42:26.299243+00:00", 
        "email": "thachrocky12345@gmail.com", 
        "first_name": "CustomerA", 
        "id": 1, 
        "language": null, 
        "last_login": "2017-11-17T19:42:26.299243+00:00", 
        "last_name": "Nguyen", 
        "password": "448ed7416fce2cb66c285d182b1ba3df1e90016d", 
        "phone": "816-803-1523", 
        "role": "EMPLOYEE", 
        "social_network": null, 
        "state": "MO", 
        "token": null, 
        "updated": "2017-11-17T19:42:26.299243+00:00", 
        "username": "nguyen1", 
        "zipcode": 64118
    }
]
```


Show a user
------
<code request-method="GET">**GET** /user/&lt;user_id&gt;</code>

Show a user by id 

### Example
```http
GET http://localhost:1234/service/user/1
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
Date: Fri, 17 Nov 2017 20:37:44 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

{
    "address": "8625 N Wabash Ave", 
    "can_email": true, 
    "can_text": true, 
    "city": "Gladstone", 
    "created": "2017-11-17T19:42:26.299243+00:00", 
    "email": "thachrocky12345@gmail.com", 
    "first_name": "CustomerA", 
    "id": 1, 
    "language": null, 
    "last_login": "2017-11-17T19:42:26.299243+00:00", 
    "last_name": "Nguyen", 
    "password": "448ed7416fce2cb66c285d182b1ba3df1e90016d", 
    "phone": "816-803-1523", 
    "role": "EMPLOYEE", 
    "social_network": null, 
    "state": "MO", 
    "token": null, 
    "updated": "2017-11-17T19:42:26.299243+00:00", 
    "username": "nguyen1", 
    "zipcode": 64118
}
```


Insert User
------
<code request-method="POST">**POST** /user</code>

You can Insert a list of Users or 1 user

### Example
```http
POST http://localhost:1234/service/user
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Content-Length: 1063
Content-Type: application/json
Host: localhost:1234
Origin: http://localhost:1234/service

[
    {
        "address": "8625 N Wabash Ave", 
        "can_email": false, 
        "can_text": true, 
        "city": "Gladstone", 
        "email": "vuhoangnguyen@gmail.com", 
        "first_name": "VuOwner", 
        "id": 11, 
        "language": null, 
        "last_name": "Nguyen", 
        "password": "test12345", 
        "phone": "816-803-1523", 
        "role": "OWNER", 
        "social_network": null, 
        "state": "MO", 
        "token": null, 
        "username": "nguyen10", 
        "zipcode": 64118
    }, 
    {
        "address": "8625 N Wabash Ave", 
        "can_email": false, 
        "can_text": true, 
        "city": "Gladstone", 
        "email": "thach.bui@gmail.com", 
        "first_name": "Customer9", 
        "id": 12, 
        "language": null, 
        "last_name": "Nguyen", 
        "password": "test12345", 
        "phone": "816-803-1523", 
        "role": "CUSTOMER", 
        "social_network": null, 
        "state": "MO", 
        "token": null, 
        "username": "nguyen9", 
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
Date: Fri, 17 Nov 2017 20:37:44 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "address": "8625 N Wabash Ave", 
        "can_email": false, 
        "can_text": true, 
        "city": "Gladstone", 
        "created": "2017-11-17T20:37:44.300308+00:00", 
        "email": "vuhoangnguyen@gmail.com", 
        "first_name": "VuOwner", 
        "id": 11, 
        "language": null, 
        "last_login": "2017-11-17T20:37:44.300308+00:00", 
        "last_name": "Nguyen", 
        "password": "448ed7416fce2cb66c285d182b1ba3df1e90016d", 
        "phone": "816-803-1523", 
        "role": "OWNER", 
        "social_network": null, 
        "state": "MO", 
        "token": null, 
        "updated": "2017-11-17T20:37:44.300308+00:00", 
        "username": "nguyen10", 
        "zipcode": 64118
    }, 
    {
        "address": null, 
        "can_email": null, 
        "can_text": null, 
        "city": null, 
        "created": null, 
        "email": null, 
        "first_name": null, 
        "id": null, 
        "language": null, 
        "last_login": null, 
        "last_name": null, 
        "password": null, 
        "phone": null, 
        "role": null, 
        "social_network": null, 
        "state": null, 
        "token": null, 
        "updated": null, 
        "username": null, 
        "zipcode": null
    }
]
```


Update User
------
<code request-method="PUT">**PUT** /user</code>

You can Update a list of Users or 1 user, user's id must be included

### Example
```http
PUT http://localhost:1234/service/user
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Content-Length: 532
Content-Type: application/json
Host: localhost:1234
Origin: http://localhost:1234/service

[
    {
        "address": "8625 N Wabash Ave", 
        "can_email": false, 
        "can_text": true, 
        "city": "Gladstone", 
        "email": "thach.bui@gmail.com", 
        "first_name": "Customer9", 
        "id": 12, 
        "language": null, 
        "last_name": "Nguyen", 
        "password": "test12345", 
        "phone": "816-803-1523", 
        "role": "CUSTOMER", 
        "social_network": null, 
        "state": "MO", 
        "token": null, 
        "username": "nguyen9", 
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
Date: Fri, 17 Nov 2017 20:37:44 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "address": null, 
        "can_email": null, 
        "can_text": null, 
        "city": null, 
        "created": null, 
        "email": null, 
        "first_name": null, 
        "id": null, 
        "language": null, 
        "last_login": null, 
        "last_name": null, 
        "password": null, 
        "phone": null, 
        "role": null, 
        "social_network": null, 
        "state": null, 
        "token": null, 
        "updated": null, 
        "username": null, 
        "zipcode": null
    }
]
```


DELETE users
------
<code request-method="DELETE">**DELETE** /user</code>

You can DELETE a list of Users or 1 user, user's id must included

### Example
```http
DELETE http://localhost:1234/service/user
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Content-Length: 63
Content-Type: application/json
Host: localhost:1234
Origin: http://localhost:1234/service

[
    {
        "id": 11
    }, 
    {
        "id": 12
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
Date: Fri, 17 Nov 2017 20:37:44 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "address": "8625 N Wabash Ave", 
        "can_email": false, 
        "can_text": true, 
        "city": "Gladstone", 
        "created": "2017-11-17T20:37:44.300308+00:00", 
        "email": "vuhoangnguyen@gmail.com", 
        "first_name": "VuOwner", 
        "id": 11, 
        "language": null, 
        "last_login": "2017-11-17T20:37:44.300308+00:00", 
        "last_name": "Nguyen", 
        "password": "448ed7416fce2cb66c285d182b1ba3df1e90016d", 
        "phone": "816-803-1523", 
        "role": "OWNER", 
        "social_network": null, 
        "state": "MO", 
        "token": null, 
        "updated": "2017-11-17T20:37:44.300308+00:00", 
        "username": "nguyen10", 
        "zipcode": 64118
    }, 
    {
        "address": null, 
        "can_email": null, 
        "can_text": null, 
        "city": null, 
        "created": null, 
        "email": null, 
        "first_name": null, 
        "id": null, 
        "language": null, 
        "last_login": null, 
        "last_name": null, 
        "password": null, 
        "phone": null, 
        "role": null, 
        "social_network": null, 
        "state": null, 
        "token": null, 
        "updated": null, 
        "username": null, 
        "zipcode": null
    }
]
```

