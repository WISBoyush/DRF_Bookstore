# DRF_Bookstore
paths:
  /bookstore/book/:
    get:
      operationId: bookstore_book_list
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            type: array
            items:
              $ref: '#/definitions/Book'
      tags:
        - bookstore
    post:
      operationId: bookstore_book_create
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Book'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/Book'
      tags:
        - bookstore
    parameters: []
  /bookstore/book/{id}/:
    get:
      operationId: bookstore_book_read
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Book'
      tags:
        - bookstore
    patch:
      operationId: bookstore_book_partial_update
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Book'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Book'
      tags:
        - bookstore
    parameters:
      - name: id
        in: path
        required: true
        type: string
  /bookstore/book/{id}/update_item/:
    patch:
      operationId: bookstore_book_update_item
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Book'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Book'
      tags:
        - bookstore
    parameters:
      - name: id
        in: path
        required: true
        type: string
  /bookstore/figure/:
    get:
      operationId: bookstore_figure_list
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            type: array
            items:
              $ref: '#/definitions/Figure'
      tags:
        - bookstore
    post:
      operationId: bookstore_figure_create
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Figure'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/Figure'
      tags:
        - bookstore
    parameters: []
  /bookstore/figure/{id}/:
    get:
      operationId: bookstore_figure_read
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Figure'
      tags:
        - bookstore
    patch:
      operationId: bookstore_figure_partial_update
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Figure'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Figure'
      tags:
        - bookstore
    parameters:
      - name: id
        in: path
        required: true
        type: string
  /bookstore/figure/{id}/update_item/:
    patch:
      operationId: bookstore_figure_update_item
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Figure'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Figure'
      tags:
        - bookstore
    parameters:
      - name: id
        in: path
        required: true
        type: string
  /bookstore/items/:
    get:
      operationId: bookstore_items_list
      description: ''
      parameters:
        - name: search
          in: query
          description: A search term.
          required: false
          type: string
        - name: title
          in: query
          description: ''
          required: false
          type: string
        - name: price
          in: query
          description: ''
          required: false
          type: number
        - name: ordering
          in: query
          description: Which field to use when ordering the results.
          required: false
          type: string
        - name: page
          in: query
          description: A page number within the paginated result set.
          required: false
          type: integer
      responses:
        '200':
          description: ''
      tags:
        - bookstore
    post:
      operationId: bookstore_items_create
      description: ''
      parameters: []
      responses:
        '201':
          description: ''
      tags:
        - bookstore
    parameters: []
  /bookstore/items/{id}/:
    get:
      operationId: bookstore_items_read
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
      tags:
        - bookstore
    parameters:
      - name: id
        in: path
        description: A unique integer value identifying this item.
        required: true
        type: integer
  /cart/:
    get:
      operationId: cart_list
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            type: array
            items:
              $ref: '#/definitions/Cart'
      tags:
        - cart
    post:
      operationId: cart_create
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Cart'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/Cart'
      tags:
        - cart
    parameters: []
  /cart/make_order/:
    post:
      operationId: cart_make_order
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Cart'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/Cart'
      tags:
        - cart
    parameters: []
  /cart/rent/:
    get:
      operationId: cart_rent_list
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            type: array
            items:
              $ref: '#/definitions/RentItem'
      tags:
        - cart
    post:
      operationId: cart_rent_create
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/RentItem'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/RentItem'
      tags:
        - cart
    parameters: []
  /cart/rent/create_entry/:
    patch:
      operationId: cart_rent_create_entry
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/RentItem'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/RentItem'
      tags:
        - cart
    parameters: []
  /cart/rent/make_order/:
    post:
      operationId: cart_rent_make_order
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/RentItem'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/RentItem'
      tags:
        - cart
    parameters: []
  /cart/rent/{id}/:
    get:
      operationId: cart_rent_read
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/RentItem'
      tags:
        - cart
    patch:
      operationId: cart_rent_partial_update
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/RentItem'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/RentItem'
      tags:
        - cart
    delete:
      operationId: cart_rent_delete
      description: ''
      parameters: []
      responses:
        '204':
          description: ''
      tags:
        - cart
    parameters:
      - name: id
        in: path
        required: true
        type: string
  /cart/update_cart/:
    patch:
      operationId: cart_update_cart
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Cart'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Cart'
      tags:
        - cart
    parameters: []
  /cart/{id}/:
    get:
      operationId: cart_read
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Cart'
      tags:
        - cart
    patch:
      operationId: cart_partial_update
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Cart'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Cart'
      tags:
        - cart
    delete:
      operationId: cart_delete
      description: ''
      parameters: []
      responses:
        '204':
          description: ''
      tags:
        - cart
    parameters:
      - name: id
        in: path
        required: true
        type: string
  /order/:
    get:
      operationId: order_list
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            type: array
            items:
              $ref: '#/definitions/OrderOuter'
      tags:
        - order
    post:
      operationId: order_create
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/OrderOuter'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/OrderOuter'
      tags:
        - order
    parameters: []
  /order/detail/:
    get:
      operationId: order_list_detail
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            type: array
            items:
              $ref: '#/definitions/OrderOuter'
      tags:
        - order
    parameters: []
  /order/pay/:
    post:
      operationId: order_pay
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/OrderOuter'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/OrderOuter'
      tags:
        - order
    parameters: []
  /order/{orders_id}/:
    get:
      operationId: order_read
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/OrderOuter'
      tags:
        - order
    patch:
      operationId: order_partial_update
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/OrderOuter'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/OrderOuter'
      tags:
        - order
    delete:
      operationId: order_delete
      description: ''
      parameters: []
      responses:
        '204':
          description: ''
      tags:
        - order
    parameters:
      - name: orders_id
        in: path
        required: true
        type: string
  /rent/:
    get:
      operationId: rent_list
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            type: array
            items:
              $ref: '#/definitions/Rent'
      tags:
        - rent
    post:
      operationId: rent_create
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Rent'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/Rent'
      tags:
        - rent
    parameters: []
  /rent/list_detail/:
    get:
      operationId: rent_list_detail
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            type: array
            items:
              $ref: '#/definitions/Rent'
      tags:
        - rent
    parameters: []
  /rent/{rents_id}/:
    get:
      operationId: rent_read
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Rent'
      tags:
        - rent
    patch:
      operationId: rent_partial_update
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Rent'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Rent'
      tags:
        - rent
    delete:
      operationId: rent_delete
      description: ''
      parameters: []
      responses:
        '204':
          description: ''
      tags:
        - rent
    parameters:
      - name: rents_id
        in: path
        required: true
        type: string
  /tag/:
    get:
      operationId: tag_list
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            type: array
            items:
              $ref: '#/definitions/Tag'
      tags:
        - tag
    post:
      operationId: tag_create
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Tag'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/Tag'
      tags:
        - tag
    parameters: []
  /tag/{id}/:
    get:
      operationId: tag_read
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Tag'
      tags:
        - tag
    patch:
      operationId: tag_partial_update
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Tag'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Tag'
      tags:
        - tag
    delete:
      operationId: tag_delete
      description: ''
      parameters: []
      responses:
        '204':
          description: ''
      tags:
        - tag
    parameters:
      - name: id
        in: path
        required: true
        type: string
  /tag/{id}/update_tag/:
    patch:
      operationId: tag_update_tag
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Tag'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Tag'
      tags:
        - tag
    parameters:
      - name: id
        in: path
        required: true
        type: string
  /token/:
    post:
      operationId: token_create
      description: |-
        Takes a set of user credentials and returns an access and refresh JSON web
        token pair to prove the authentication of those credentials.
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/TokenObtainPair'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/TokenObtainPair'
      tags:
        - token
    parameters: []
  /token/refresh/:
    post:
      operationId: token_refresh_create
      description: |-
        Takes a refresh type JSON web token and returns an access type JSON web
        token if the refresh token is valid.
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/TokenRefresh'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/TokenRefresh'
      tags:
        - token
    parameters: []
  /token/verify:
    post:
      operationId: token_verify_create
      description: |-
        Takes a token and indicates if it is valid.  This view provides no
        information about a token's fitness for a particular use.
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/TokenVerify'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/TokenVerify'
      tags:
        - token
    parameters: []
  /user/:
    get:
      operationId: user_list
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            type: array
            items:
              $ref: '#/definitions/User'
      tags:
        - user
    post:
      operationId: user_create
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/User'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/User'
      tags:
        - user
    parameters: []
  /user/{id}/:
    get:
      operationId: user_read
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/User'
      tags:
        - user
    parameters:
      - name: id
        in: path
        required: true
        type: string
  /user/{id}/profile/:
    get:
      operationId: user_profile_list
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            type: array
            items:
              $ref: '#/definitions/Profile'
      tags:
        - user
    post:
      operationId: user_profile_create
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Profile'
      responses:
        '201':
          description: ''
          schema:
            $ref: '#/definitions/Profile'
      tags:
        - user
    parameters:
      - name: id
        in: path
        required: true
        type: string
  /user/{id}/profile/{id}/:
    get:
      operationId: user_profile_read
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Profile'
      tags:
        - user
    put:
      operationId: user_profile_update
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Profile'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Profile'
      tags:
        - user
    patch:
      operationId: user_profile_partial_update
      description: ''
      parameters:
        - name: data
          in: body
          required: true
          schema:
            $ref: '#/definitions/Profile'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Profile'
      tags:
        - user
    delete:
      operationId: user_profile_delete
      description: ''
      parameters: []
      responses:
        '204':
          description: ''
      tags:
        - user
    parameters:
      - name: id
        in: path
        required: true
        type: string
