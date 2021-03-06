## 1）getCart-查看购物车

#### URL
POST http://[address]/order/getcart

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:
```
{
    "username":"$user name"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N

#### Response

Status Code:


码 | 描述
--- | ---
200 | 访问成功 
401 | 访问失败，token错误 

body：

```
{ 
	"errormsg":"$Access failed, token error",
	"goodssum":"$goods sum",
	"goodsamount":"$goods amount",
	"buylist":[{"merchantname":"$merchant name",
				"goodsname":"$goods name",
				"goodsnumber":"$goods number",
				"goodsimage":"$goods image",
				"saleprice":"$sale price" },{......}]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 errormsg | string | 失败时，为错误信息描述，且以下变量不输出；<br />成功时，此变量为空，且输出以下变量 | Y          
 goodssum | string | 总商品数 | N 
 goodsamount | string | 总金额 | N 
 **buylist** |        | 购物车中的所有商品，且每件商品都应包含如下信息 |            
 merchantname | string | 商家名 | N 
 goodsname | string | 商品名 | N 
 goodsnumber | string | 商品数量 | N 
 goodsimage | string | 商品图片 | N 
 saleprice | string | 活动价 | N 



## 2）delCart-删除购物车中的商品

#### URL
POST http://[address]/order/delcart

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:
```
{
    "goodsid":"$good id",
    "goodsnumber":"$goods number"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 goodsid | string | 商品编号 | N          
 goodsnumber | string | 商品数量 | N 

#### Response

Status Code:


码 | 描述
--- | ---
200 | 删除成功 
401 | 删除失败，token错误 


Body:
```
{
	"errormsg":"$Delete failed, token error"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
errormsg | string | 错误信息描述，成功返回"ok" | Y 

#### 接口描述

某一商品在购物车中可能数量大于一，因此删除的时候要传入需要删除的数量



## 3）addCart-添加商品到购物车

#### URL
POST http://[address]/order/addcart

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:
```
{
    "username":"$user name",
    “orderamount":"$order amount",
    "merchantname":"$merchant name",
	"goodsname":"$goods name",
	"goodsnumber":"$goods number",
	"goodsimage":"$goods image",
	"saleprice":"$sale price" 
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
orderamount | string | 总金额 | N
 merchantname | string | 商家名   | N          
 goodsname    | string | 商品名   | N          
 goodsnumber  | string | 商品数量 | N          
 goodsimage   | string | 商品图片 | N          
 saleprice    | string | 活动价   | N          

#### Response

Status Code:

码 | 描述
--- | ---
200 | 添加成功 
401 | 添加失败，token错误 

Body:
```
{
	"errormsg":"$addition failed, token error"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
errormsg | string | 错误信息描述，成功返回"ok" | Y 



## 4）createOrder-创建订单

#### URL
POST http://[address]/order/createorder

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:
```
{
	"username":"$user name",
	"orderamount":"$goods amount",
    "buylist":[{"merchantname":"$merchant name",
    		   "goodsname":"$goods name",
    		   "goodsnumber":"$goods number"，
    		   "saleprice":"$sale price"},{......} ]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
orderamount | string | 总金额 | N 
buylist |  | 购买的所有商品<br />(同接口"getCart"的buylist) |  

#### Response

Status Code:

码 | 描述| 
--- | ---|--- 
200 | 订单生成成功 | 
401 | 订单生成失败，token错误 | 
501 | 订单生成失败，商品暂无 | 

Body:
```
{
	"result":"$status code",	
    "errormsg":"$order generation failed，token error/order generation failed，no goods"，
    "orderid":"$order number"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 errormsg | string | 失败时，为错误信息描述，且以下变量不输出；<br />成功时，此变量为空，且输出以下变量 | Y          
 orderid | sring  | 订单号       | N          



## 5）cancelOrder-取消订单

#### URL：

POST http://[address]/order/cancelorder

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:

```
{
    “orderid":"$order number"
}
```

| 变量名  | 类型 | 描述   | 是否可为空 |
| ------- | ---- | ------ | ---------- |
| orderid | int  | 订单号 | N          |

#### Response

Status Code:

| 码   | 描述                |
| ---- | ------------------- |
| 200  | 取消成功            |
| 401  | 取消失败，token错误 |

Body:

```
{
	"errormsg":"$cancel failed, token error"
}
```

| 变量名   | 类型   | 描述                       | 是否可为空 |
| -------- | ------ | -------------------------- | ---------- |
| errormsg | string | 错误信息描述，成功时为"ok" | N          |



## 6）paymentOrder-订单支付

#### URL：

POST http://[address]/order/paymentorder

#### Request

Headers:

| key   | 类型   | 描述      |
| ----- | ------ | --------- |
| token | string | 访问token |

Body:

```
{
    "balance":"$user balance",
    "orderamount":"$goods amount",
    “orderid":"$order number"
}
```

| 变量名      | 类型   | 描述   | 是否可为空 |
| ----------- | ------ | ------ | ---------- |
| balance     | string | 用余额 | N          |
| orderamount | string | 总金额 | N          |
| orderid     | string | 订单号 | N          |

#### Response

Status Code:

| 码   | 描述                   |
| ---- | ---------------------- |
| 200  | 支付成功               |
| 401  | 支付失败，token错误    |
| 501  | 支付失败，账户余额不足 |

Body:

```
{
	"errormsg":"$payment failed, token error/payment failed, insufficient account balance"
}
```

| 变量名   | 类型   | 描述                       | 是否可为空 |
| -------- | ------ | -------------------------- | ---------- |
| errormsg | string | 错误信息描述，成功时为"ok" | N          |



## 7）allOrder-查看全部订单

#### URL：

POST http://[address]/order/allorder

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:

```
{
    "userid":"$user id"
}
```

| 变量名 | 类型   | 描述     | 是否可为空 |
| ------ | ------ | -------- | ---------- |
| userid | string | 用户编号 | N          |

#### Response

Status Code:

| 码   | 描述                |
| ---- | ------------------- |
| 200  | 查询成功            |
| 401  | 查询失败，token错误 |
| 501  | 查询失败，暂无订单  |

Body:

```
{
	"errormsg":"$Inquiry failed, token error/Inquiry failed, no order",
	"orderlist":[{"orderid":"$order number",
    			 "orderstatus":"$order status",
    			 "orderamount":"$order amount",
    			 "buylist":[{ "merchantname":"$merchant name",
				             "goodsname":"$goods name",
						    "goodsnumber":"$goods number",
						    "goodsimage":"$goods image",
				  			"saleprice":"$sale price" },{......}]},
				  {......}]	  	
}
```

| 变量名        | 类型   | 描述                                                         | 是否可为空 |
| ------------- | ------ | ------------------------------------------------------------ | ---------- |
| errormsg      | string | 失败时，为错误信息描述，且以下变量不输出；<br />成功时，此变量为空，且输出以下变量 | Y          |
| **orderlist** |        | 用户的所有订单，且每单应该包含以下信息                       |            |
| orderid       | string | 订单号                                                       | N          |
| orderstatus   | string | 订单状态，可以是：交易成功、待支付、交易失败                 | N          |
| orderamount   | string | 总金额                                                       | N          |
| buylist       |        | (同接口"getCart"的buylist)                                   | N          |

#### 接口描述

a."orderlist"表示一个用户可能拥有多个订单；

b.单个订单可能包含多个商品，即"buylist"展示在同一个订单中的商品信息。