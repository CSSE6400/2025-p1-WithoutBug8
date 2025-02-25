[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18328249)

# CSSE6400 Week 1 Practical

### 项目简介
**Practical-1** 是一个简单的练习项目，旨在学习 **HTTP 协议**，并结合 **Flask 框架** 和 **REST API** 构建一个基础的 **Todo 应用**。

### 具体内容

- HTTP协议的四种请求；GET，POST，PUT，DELETE

  | 请求方法 | 作用         | 是否需要请求体          | 是否需要指定ID              | 主要用途 | 安全性🔒       |
  | -------- | ------------ | ----------------------- | --------------------------- | -------- | ------------- |
  | GET      | 获取资源     | 一般来说，参数都在URL中 | 不一定                      | 查询数据 | ❌不安全       |
  | POST     | 创建新资源   | 需要请求体              | 服务器自动生成ID/自己指定ID | 新增数据 | ⚠️相对来说安全 |
  | PUT      | 更新现有资源 | 需要请求体              | 必须指定ID                  | 修改数据 | ❓看实现方法   |
  | DELETE   | 删除资源     | 需要URL                 | 必须指定ID                  | 删除数据 | ❓看实现方法   |

  
1. GET请求：用于获取数据，通常用于查询操作；

   - 可通过 URL 传递参数，但是由于参数暴露在 URL 中，安全性较低

   ```python
   # 在路由routes页面配置
   @api.route('/todos',methods=['GET'])
   def get_todo():
       return jsonify([{
           "id": 1,
           "title": "Watch CSSE6400 Lecture",
           "description": "Watch CSSE6400 Lecture on ECHO360 for week1",
           "completed": True,
           "decline_at": "2025-02-25T00:00:00",
           "created_at": "2025-02-24T00:00:00",
           "updated_at": "2025-02-24T00:00:00"
       }])
   # 在endpoint.http上配置
   GET {{baseUrl}}/api/v1/todos
   ```

   

2. POST请求：用于创建新资源；

   - 通过请求体（body）提交数据，适用于创建新的数据项

   ```python
   # 在路由routes页面配置
   @api.route('/todos',methods=['POST'])
   def create_todo():
       return jsonify({
           "id": 2300847,
           "title": "Watch CSSE6400 Lecture",
           "description": "Watch CSSE6400 Lecture on ECHO360 for week1",
           "completed": True,
           "decline_at": "2025-02-25T00:00:00",
           "created_at": "2025-02-24T00:00:00",
           "updated_at": "2025-02-24T00:00:00"
       }), 201 
   # 在endpoint.http上配置
   POST {{baseUrl}}/api/v1/todos
   Content-Type: application/json
   {
       "title": "An exmaple Todo",
       "description": "This is an example todo"
   }
   ```

3. PUT请求：用于更新数据

   - 需要提供要更新的资源 id，若资源不存在，可能会创建新资源（根据具体实现）

   ```python
   # 在路由route页面配置
   @api.route('/todos/<int:id>',methods=['PUT'])
   def update_todo(id):
       return jsonify({
           "id": id,
           "title": "Watch CSSE6400 Lecture",
           "description": "Watch CSSE6400 Lecture on ECHO360 for week1",
           "completed": True,
           "decline_at": "2025-02-25T00:00:00",
           "created_at": "2025-02-24T00:00:00",
           "updated_at": "2025-02-24T00:00:00"
       })
   # 在endpoint.http上配置
   PUT {{baseUrl}}/api/v1/todos/1
   Content-Type: application/json
   {
       "title": "updated title",
   }
   ```

4. DELETE请求：用于删除数据；

   - 通过资源 id 确定要删除的对象，删除操作不可逆

   ```python
   # 在路由route页面配置
   @api.route('/todos/<int:id>',methods=['DELETE'])
   def delete_todo(id):
       return jsonify({
           "id": id,
           "title": "Watch CSSE6400 Lecture",
           "description": "Watch CSSE6400 Lecture on ECHO360 for week1",
           "completed": True,
           "decline_at": "2025-02-25T00:00:00",
           "created_at": "2025-02-24T00:00:00",
           "updated_at": "2025-02-24T00:00:00"
       })
   # 在endpoint.http上配置
   DELETE {{baseUrl}}/api/v1/todos/1
   ```

### 其他补充的内容

1. HTTP状态码

   - **200s（成功响应）**服务器成功处理了请求。
     - 200 OK（请求成功）
     - 201 Created（资源已成功创建）
   - **300s（重定向）**服务器告诉客户端要访问另一个 URL。
     - 301 Moved Permanently（永久重定向）
     - 302 Found（临时重定向）
   - **400s（客户端错误）**请求有问题，通常是客户端导致的错误。
     - 400 Bad Request（请求格式错误）
     - 401 Unauthorized（未授权）
     - 403 Forbidden（禁止访问）
     - 404 Not Found（请求的资源不存在）
   - **500s（服务器错误）**服务器无法正确处理请求。
     - 500 Internal Server Error（服务器内部错误）
     - 502 Bad Gateway（网关错误）
     - 503 Service Unavailable（服务器暂时不可用）

2. 启动后端服务Flask的指令，本项目的Flask文件是由poetry安装的，poetry 是一个 Python 依赖管理和打包工具，用于**简化包管理**、**虚拟环境管理**和**项目发布**。

   - 简化包管理：用 pyproject.toml 统一管理项目的 Python 依赖
   - 虚拟环境管理：自动创建和管理虚拟环境
   - 项目发布：可以轻松打包和发布 Python 包

   ```shell
   poetry run flask --app todo run
   ```
