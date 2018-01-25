# timetracking

###### 1. Api to retrieve list of users:
        url → http://localhost:8000/apitest/user/
        method → GET
        response →
        
        
  ###### A user_list.html is rendered (Template Renderer)
  <html>
      <body>
          <h1>Users</h1>
          <ul>
              <li>User1</li>
          </ul>
      </body>
  </html>

###### 2. Api to retrieve insert user:
        url → http://localhost:8000/apitest/user/
        method → POST
        parameters → "username" : "User2"
        Content-Type → text/html
        response →
  ###### A user_list.html is rendered (Template Renderer)
  <html>
    <body>
        <h1>Users</h1>
        <ul>
            <li>User1</li>
            <li>User2</li>
        </ul>
    </body>
  </html>

###### 3. Api to retrieve insert Task:
###### Here when you create a Task it considers Task started from that time

        url → http://localhost:8000/apitest/task/
        method → POST
        parameters → "userid" : 1,"taskname": Task 1
        Content-Type → text/html
        response →
###### A task_list.html is rendered (Template Renderer)
<html>
  <body>
      <h1>Task</h1>
      <ul>
          <li>Task of User1 named as 
              <span>Task 1</span>, having duration
              <span>0</span> seconds
          </li>
      </ul>
  </body>
</html>
    

###### 4. Api to stop the Task:
###### This API restricts to stop already stopped Task, it returns 400
        url → http://localhost:8000/apitest/task/
        method → POST
        parameters → "userid" : 1,"taskid": Task 1,"action" :stop
        Content-Type → text/html
        response →
###### A task_list.html is rendered (Template Renderer)
<html>
  <body>
      <h1>Task</h1>
      <ul>
          <li>Task of User1 named as 
              <span>Task 1</span>, having duration
              <span>722</span> seconds
          </li>
      </ul>
  </body>
</html>
