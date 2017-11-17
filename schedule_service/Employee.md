
Employee
======

`/store/<store-id>/employee`

EMPLOYEE OVERVIEW

### Methods

Method | URL | Description
--- | --- | ---
**[GET](/documentation/endpoint/Employee#list-all-store-of-a-business-including-employees)** | `/store/<store-id>/employee` | List all store of a business including employees
**[GET](/documentation/endpoint/Employee#show-an-employee-by-id-including-schedule)** | `/store/<store_id>/employee/<employee-id>` | Show an employee by id including schedule
**[POST](/documentation/endpoint/Employee#insert-employee)** | `/store/<store-id>/employee` | Insert Employee
**[PUT](/documentation/endpoint/Employee#update-employee)** | `/store/<store-id>/employee` | Update Employee
**[DELETE](/documentation/endpoint/Employee#delete-employee)** | `/store/<store-id>/employee` | DELETE Employee

### Object Attributes

Attribute | Type | Readonly | Nullable | Has Default
--- | --- | --- | --- | ---
`address` | text | &nbsp; | &bullet; | &nbsp;
`allow_backup` | integer | &nbsp; | &nbsp; | &bullet;
`break_time` | integer | &nbsp; | &bullet; | &nbsp;
`city` | text | &nbsp; | &bullet; | &nbsp;
`created` | timestamp | &nbsp; | &nbsp; | &bullet;
`email` | text | &nbsp; | &bullet; | &nbsp;
`first_name` | text | &nbsp; | &nbsp; | &nbsp;
`id` | integer | &bullet; | &nbsp; | &bullet;
`last_name` | text | &nbsp; | &bullet; | &nbsp;
`phone` | text | &nbsp; | &bullet; | &nbsp;
`rate` | numeric | &nbsp; | &nbsp; | &bullet;
`session_in_minutes` | integer | &nbsp; | &nbsp; | &bullet;
`state` | text | &nbsp; | &bullet; | &nbsp;
`store_id` | integer | &nbsp; | &nbsp; | &nbsp;
`updated` | timestamp | &nbsp; | &nbsp; | &bullet;
`zipcode` | integer | &nbsp; | &bullet; | &nbsp;

List all store of a business including employees
------
<code request-method="GET">**GET** /store/&lt;store-id&gt;/employee</code>

List all store of a business including employees

### Query Parameters

Parameter | Type | Description
--- | --- | ---
`id` | int | Returns employee with specific id, you can provide more than one id, example: id=1&id=2>
`limit` | number | You can set limit return
`page` | number | page will go with limit, example limit=5&page=1
`search` | string | Search for employee first_name, last_name, email, or address



### Example
```http
GET http://localhost:1234/service/store/1/employee?limit=3&page=0
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
Date: Fri, 17 Nov 2017 00:08:45 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "address": "8625 N Wabash Ave", 
        "allow_backup": 2, 
        "break_time": 13, 
        "city": "Gladstone", 
        "created": "2017-11-17T00:05:48.224553+00:00", 
        "email": "vuhoangnguyen@gmail.com", 
        "first_name": "Employee1", 
        "id": 20, 
        "last_name": "Nguyen", 
        "phone": "816-803-1523", 
        "rate": 5.0, 
        "schedule": [
            {
                "available": false, 
                "employee_id": 20, 
                "id": 43, 
                "iso_weekday_id": 1, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.266537+00:00", 
                "weekday": "Monday"
            }, 
            {
                "available": false, 
                "employee_id": 20, 
                "id": 44, 
                "iso_weekday_id": 2, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.266537+00:00", 
                "weekday": "Tuesday"
            }, 
            {
                "available": false, 
                "employee_id": 20, 
                "id": 45, 
                "iso_weekday_id": 3, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.266537+00:00", 
                "weekday": "Wednesday"
            }, 
            {
                "available": false, 
                "employee_id": 20, 
                "id": 46, 
                "iso_weekday_id": 4, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.266537+00:00", 
                "weekday": "Thursday"
            }, 
            {
                "available": false, 
                "employee_id": 20, 
                "id": 47, 
                "iso_weekday_id": 5, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.266537+00:00", 
                "weekday": "Friday"
            }, 
            {
                "available": false, 
                "employee_id": 20, 
                "id": 48, 
                "iso_weekday_id": 6, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.266537+00:00", 
                "weekday": "Saturday"
            }, 
            {
                "available": false, 
                "employee_id": 20, 
                "id": 49, 
                "iso_weekday_id": 7, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.266537+00:00", 
                "weekday": "Sunday"
            }
        ], 
        "session_in_minutes": 20, 
        "state": "MO", 
        "store_id": 1, 
        "updated": "2017-11-17T00:05:48.224553+00:00", 
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
        "schedule": [
            {
                "available": false, 
                "employee_id": 3, 
                "id": 15, 
                "iso_weekday_id": 1, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.551765+00:00", 
                "weekday": "Monday"
            }, 
            {
                "available": false, 
                "employee_id": 3, 
                "id": 16, 
                "iso_weekday_id": 2, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.551765+00:00", 
                "weekday": "Tuesday"
            }, 
            {
                "available": false, 
                "employee_id": 3, 
                "id": 17, 
                "iso_weekday_id": 3, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.551765+00:00", 
                "weekday": "Wednesday"
            }, 
            {
                "available": false, 
                "employee_id": 3, 
                "id": 18, 
                "iso_weekday_id": 4, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.551765+00:00", 
                "weekday": "Thursday"
            }, 
            {
                "available": false, 
                "employee_id": 3, 
                "id": 19, 
                "iso_weekday_id": 5, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.551765+00:00", 
                "weekday": "Friday"
            }, 
            {
                "available": false, 
                "employee_id": 3, 
                "id": 20, 
                "iso_weekday_id": 6, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.551765+00:00", 
                "weekday": "Saturday"
            }, 
            {
                "available": false, 
                "employee_id": 3, 
                "id": 21, 
                "iso_weekday_id": 7, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.551765+00:00", 
                "weekday": "Sunday"
            }
        ], 
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
        "first_name": "Employee2", 
        "id": 2, 
        "last_name": "Bui", 
        "phone": "816-803-1523", 
        "rate": 5.0, 
        "schedule": [
            {
                "available": false, 
                "employee_id": 2, 
                "id": 8, 
                "iso_weekday_id": 1, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.344547+00:00", 
                "weekday": "Monday"
            }, 
            {
                "available": false, 
                "employee_id": 2, 
                "id": 9, 
                "iso_weekday_id": 2, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.344547+00:00", 
                "weekday": "Tuesday"
            }, 
            {
                "available": false, 
                "employee_id": 2, 
                "id": 10, 
                "iso_weekday_id": 3, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.344547+00:00", 
                "weekday": "Wednesday"
            }, 
            {
                "available": false, 
                "employee_id": 2, 
                "id": 11, 
                "iso_weekday_id": 4, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.344547+00:00", 
                "weekday": "Thursday"
            }, 
            {
                "available": false, 
                "employee_id": 2, 
                "id": 12, 
                "iso_weekday_id": 5, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.344547+00:00", 
                "weekday": "Friday"
            }, 
            {
                "available": false, 
                "employee_id": 2, 
                "id": 13, 
                "iso_weekday_id": 6, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.344547+00:00", 
                "weekday": "Saturday"
            }, 
            {
                "available": false, 
                "employee_id": 2, 
                "id": 14, 
                "iso_weekday_id": 7, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-16T23:51:56.344547+00:00", 
                "weekday": "Sunday"
            }
        ], 
        "session_in_minutes": 30, 
        "state": "MO", 
        "store_id": 1, 
        "updated": "2017-11-16T23:51:56.311145+00:00", 
        "zipcode": 64118
    }
]
```


Show an employee by id including schedule
------
<code request-method="GET">**GET** /store/&lt;store_id&gt;/employee/&lt;employee-id&gt;</code>

Show an employee by id including schedule

### Example
```http
GET http://localhost:1234/service/store/1/employee/1
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
Date: Fri, 17 Nov 2017 00:08:45 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

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
    "schedule": [
        {
            "available": false, 
            "employee_id": 1, 
            "id": 1, 
            "iso_weekday_id": 1, 
            "session_end": 17, 
            "session_start": 9, 
            "updated": "2017-11-16T23:51:56.343611+00:00", 
            "weekday": "Monday"
        }, 
        {
            "available": false, 
            "employee_id": 1, 
            "id": 2, 
            "iso_weekday_id": 2, 
            "session_end": 17, 
            "session_start": 9, 
            "updated": "2017-11-16T23:51:56.343611+00:00", 
            "weekday": "Tuesday"
        }, 
        {
            "available": false, 
            "employee_id": 1, 
            "id": 3, 
            "iso_weekday_id": 3, 
            "session_end": 17, 
            "session_start": 9, 
            "updated": "2017-11-16T23:51:56.343611+00:00", 
            "weekday": "Wednesday"
        }, 
        {
            "available": false, 
            "employee_id": 1, 
            "id": 4, 
            "iso_weekday_id": 4, 
            "session_end": 17, 
            "session_start": 9, 
            "updated": "2017-11-16T23:51:56.343611+00:00", 
            "weekday": "Thursday"
        }, 
        {
            "available": false, 
            "employee_id": 1, 
            "id": 5, 
            "iso_weekday_id": 5, 
            "session_end": 17, 
            "session_start": 9, 
            "updated": "2017-11-16T23:51:56.343611+00:00", 
            "weekday": "Friday"
        }, 
        {
            "available": false, 
            "employee_id": 1, 
            "id": 6, 
            "iso_weekday_id": 6, 
            "session_end": 17, 
            "session_start": 9, 
            "updated": "2017-11-16T23:51:56.343611+00:00", 
            "weekday": "Saturday"
        }, 
        {
            "available": false, 
            "employee_id": 1, 
            "id": 7, 
            "iso_weekday_id": 7, 
            "session_end": 17, 
            "session_start": 9, 
            "updated": "2017-11-16T23:51:56.343611+00:00", 
            "weekday": "Sunday"
        }
    ], 
    "session_in_minutes": 20, 
    "state": "MO", 
    "store_id": 1, 
    "updated": "2017-11-16T23:51:56.311145+00:00", 
    "zipcode": 64118
}
```


Insert Employee
------
<code request-method="POST">**POST** /store/&lt;store-id&gt;/employee</code>

You can Insert a list of employees or 1 only

### Example
```http
POST http://localhost:1234/service/store/1/employee
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Content-Length: 864
Content-Type: application/json
Host: localhost:1234
Origin: http://localhost:1234/service

[
    {
        "address": "8625 N Wabash Ave", 
        "allow_backup": 2, 
        "break_time": 13, 
        "city": "Gladstone", 
        "email": "vuhoangnguyen@gmail.com", 
        "first_name": "Employee1", 
        "id": 20, 
        "last_name": "Nguyen", 
        "phone": "816-803-1523", 
        "rate": 5, 
        "session_in_minutes": 20, 
        "state": "MO", 
        "store_id": 1, 
        "zipcode": 64118
    }, 
    {
        "address": "7625 N Wabash Ave", 
        "allow_backup": 3, 
        "break_time": 12, 
        "city": "Gladstone", 
        "email": "thachrocky@icloud.com", 
        "first_name": "Employee2", 
        "id": 21, 
        "last_name": "Bui", 
        "phone": "816-803-1523", 
        "rate": 5, 
        "session_in_minutes": 30, 
        "state": "MO", 
        "store_id": 1, 
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
Date: Fri, 17 Nov 2017 00:08:46 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "address": null, 
        "allow_backup": null, 
        "break_time": null, 
        "city": null, 
        "created": null, 
        "email": null, 
        "first_name": null, 
        "id": null, 
        "last_name": null, 
        "phone": null, 
        "rate": null, 
        "schedule": [], 
        "session_in_minutes": null, 
        "state": null, 
        "store_id": null, 
        "updated": null, 
        "zipcode": null
    }, 
    {
        "address": null, 
        "allow_backup": null, 
        "break_time": null, 
        "city": null, 
        "created": null, 
        "email": null, 
        "first_name": null, 
        "id": null, 
        "last_name": null, 
        "phone": null, 
        "rate": null, 
        "schedule": [], 
        "session_in_minutes": null, 
        "state": null, 
        "store_id": null, 
        "updated": null, 
        "zipcode": null
    }
]
```


Update Employee
------
<code request-method="PUT">**PUT** /store/&lt;store-id&gt;/employee</code>

You can Update a list of Employees or 1 Employee, Employee's id must be included

### Example
```http
PUT http://localhost:1234/service/store/1/employee
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Content-Length: 430
Content-Type: application/json
Host: localhost:1234
Origin: http://localhost:1234/service

[
    {
        "address": "7625 N Wabash Ave", 
        "allow_backup": 3, 
        "break_time": 12, 
        "city": "Gladstone", 
        "email": "thachrocky@icloud.com", 
        "first_name": "Employee2", 
        "id": 21, 
        "last_name": "Bui", 
        "phone": "816-803-1523", 
        "rate": 5, 
        "session_in_minutes": 30, 
        "state": "MO", 
        "store_id": 1, 
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
Date: Fri, 17 Nov 2017 00:08:46 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

[
    {
        "address": "7625 N Wabash Ave", 
        "allow_backup": 3, 
        "break_time": 12, 
        "city": "Gladstone", 
        "created": "2017-11-17T00:05:48.224553+00:00", 
        "email": "thachrocky@icloud.com", 
        "first_name": "Employee2", 
        "id": 21, 
        "last_name": "Bui", 
        "phone": "816-803-1523", 
        "rate": 5.0, 
        "schedule": [
            {
                "available": false, 
                "employee_id": 21, 
                "id": 36, 
                "iso_weekday_id": 1, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.265635+00:00", 
                "weekday": "Monday"
            }, 
            {
                "available": false, 
                "employee_id": 21, 
                "id": 37, 
                "iso_weekday_id": 2, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.265635+00:00", 
                "weekday": "Tuesday"
            }, 
            {
                "available": false, 
                "employee_id": 21, 
                "id": 38, 
                "iso_weekday_id": 3, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.265635+00:00", 
                "weekday": "Wednesday"
            }, 
            {
                "available": false, 
                "employee_id": 21, 
                "id": 39, 
                "iso_weekday_id": 4, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.265635+00:00", 
                "weekday": "Thursday"
            }, 
            {
                "available": false, 
                "employee_id": 21, 
                "id": 40, 
                "iso_weekday_id": 5, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.265635+00:00", 
                "weekday": "Friday"
            }, 
            {
                "available": false, 
                "employee_id": 21, 
                "id": 41, 
                "iso_weekday_id": 6, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.265635+00:00", 
                "weekday": "Saturday"
            }, 
            {
                "available": false, 
                "employee_id": 21, 
                "id": 42, 
                "iso_weekday_id": 7, 
                "session_end": 17, 
                "session_start": 9, 
                "updated": "2017-11-17T00:05:48.265635+00:00", 
                "weekday": "Sunday"
            }
        ], 
        "session_in_minutes": 30, 
        "state": "MO", 
        "store_id": 1, 
        "updated": "2017-11-16T18:08:46.407816+00:00", 
        "zipcode": 64118
    }
]
```


DELETE Employee
------
<code request-method="DELETE">**DELETE** /store/&lt;store-id&gt;/employee</code>

You can DELETE a list of Employees or 1  Employee, Employee's id must be included

### Example
```http
DELETE http://localhost:1234/service/store/1/employee
Authorization: Basic dnVuZ3V5ZW46dnVuZ3V5ZW4xMjM0NSE=
Content-Length: 63
Content-Type: application/json
Host: localhost:1234
Origin: http://localhost:1234/service

[
    {
        "id": 20
    }, 
    {
        "id": 21
    }
]
```

```http
HTTP/1.1 400 Bad Request
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Suppress-WWW-Authenticate, Content-Type, Authorization, Vary
Access-Control-Allow-Methods: GET, PUT, POST, DELETE, HEAD, OPTIONS
Access-Control-Allow-Origin: http://localhost:1234/service
Access-Control-Max-Age: 3600
Cache-Control: no-store, must-revalidate
Content-Type: application/json
Date: Fri, 17 Nov 2017 00:08:46 GMT
Expires: 0
Server: TwistedWeb/16.6.0
Transfer-Encoding: chunked
Vary: Origin

{
    "attribute": null, 
    "error_info": "update or delete on table \"employee\" violates foreign key constraint \"schedule_employee_id_fkey\" on table \"schedule\"\nDETAIL:  Key (id)=(20) is still referenced from table \"schedule\".\n", 
    "type_error": "ValueError"
}
```

