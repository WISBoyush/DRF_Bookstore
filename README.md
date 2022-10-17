# DRF_Bookstore
### /bookstore/book/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Book](#Book) ] |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Book](#Book) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Book](#Book) |

### /bookstore/book/{id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Book](#Book) |

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |
| data | body |  | Yes | [Book](#Book) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Book](#Book) |

### /bookstore/book/{id}/update_item/

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |
| data | body |  | Yes | [Book](#Book) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Book](#Book) |

### /bookstore/figure/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Figure](#Figure) ] |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Figure](#Figure) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Figure](#Figure) |

### /bookstore/figure/{id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Figure](#Figure) |

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |
| data | body |  | Yes | [Figure](#Figure) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Figure](#Figure) |

### /bookstore/figure/{id}/update_item/

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |
| data | body |  | Yes | [Figure](#Figure) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Figure](#Figure) |

### /bookstore/items/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| search | query | A search term. | No | string |
| title | query |  | No | string |
| price | query |  | No | number |
| ordering | query | Which field to use when ordering the results. | No | string |
| page | query | A page number within the paginated result set. | No | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

### /bookstore/items/{id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this item. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /cart/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Cart](#Cart) ] |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Cart](#Cart) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Cart](#Cart) |

### /cart/make_order/

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Cart](#Cart) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Cart](#Cart) |

### /cart/rent/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [RentItem](#RentItem) ] |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [RentItem](#RentItem) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [RentItem](#RentItem) |

### /cart/rent/create_entry/

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [RentItem](#RentItem) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [RentItem](#RentItem) |

### /cart/rent/make_order/

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [RentItem](#RentItem) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [RentItem](#RentItem) |

### /cart/rent/{id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [RentItem](#RentItem) |

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |
| data | body |  | Yes | [RentItem](#RentItem) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [RentItem](#RentItem) |

#### DELETE
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /cart/update_cart/

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Cart](#Cart) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Cart](#Cart) |

### /cart/{id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Cart](#Cart) |

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |
| data | body |  | Yes | [Cart](#Cart) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Cart](#Cart) |

#### DELETE
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /order/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [OrderOuter](#OrderOuter) ] |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [OrderOuter](#OrderOuter) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [OrderOuter](#OrderOuter) |

### /order/detail/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [OrderOuter](#OrderOuter) ] |

### /order/pay/

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [OrderOuter](#OrderOuter) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [OrderOuter](#OrderOuter) |

### /order/{orders_id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| orders_id | path |  | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [OrderOuter](#OrderOuter) |

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| orders_id | path |  | Yes | string |
| data | body |  | Yes | [OrderOuter](#OrderOuter) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [OrderOuter](#OrderOuter) |

#### DELETE
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| orders_id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /rent/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Rent](#Rent) ] |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Rent](#Rent) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Rent](#Rent) |

### /rent/list_detail/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Rent](#Rent) ] |

### /rent/{rents_id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| rents_id | path |  | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Rent](#Rent) |

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| rents_id | path |  | Yes | string |
| data | body |  | Yes | [Rent](#Rent) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Rent](#Rent) |

#### DELETE
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| rents_id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /tag/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Tag](#Tag) ] |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Tag](#Tag) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Tag](#Tag) |

### /tag/{id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Tag](#Tag) |

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |
| data | body |  | Yes | [Tag](#Tag) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Tag](#Tag) |

#### DELETE
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /tag/{id}/update_tag/

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |
| data | body |  | Yes | [Tag](#Tag) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Tag](#Tag) |

### /token/

#### POST
##### Description:

Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [TokenObtainPair](#TokenObtainPair) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [TokenObtainPair](#TokenObtainPair) |

### /token/refresh/

#### POST
##### Description:

Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [TokenRefresh](#TokenRefresh) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [TokenRefresh](#TokenRefresh) |

### /token/verify

#### POST
##### Description:

Takes a token and indicates if it is valid.  This view provides no
information about a token's fitness for a particular use.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [TokenVerify](#TokenVerify) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [TokenVerify](#TokenVerify) |

### /user/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [User](#User) ] |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [User](#User) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [User](#User) |

### /user/{id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [User](#User) |

### /user/{id}/profile/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Profile](#Profile) ] |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |
| data | body |  | Yes | [Profile](#Profile) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Profile](#Profile) |

### /user/{id}/profile/{id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Profile](#Profile) |

#### PUT
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |
| data | body |  | Yes | [Profile](#Profile) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Profile](#Profile) |

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |
| data | body |  | Yes | [Profile](#Profile) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Profile](#Profile) |

#### DELETE
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |
