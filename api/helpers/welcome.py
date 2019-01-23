welcome_message = """
   <!DOCTYPE html>
     <html>
       <head>
         <title>iReporter API</title>
         <style type='text/css'>
           *{
               margin:0;
               padding:0;
           }
           body{
               width:80%;
               margin:0 auto;
           }
           .main-container{
               margin-top:45px;
           }
           h2{
               font-size:16pt;
               color:orange;
               text-align:center;
           }
           a{
               text-decoration:none;
           }
         </style>
       </head>
       <body>
         <div class='main-content'>
           <h2>iReporter</h2>
              Currently supported endpoints <br>
              <a href='https://nadralia-ireporter.herokuapp.com/api/v2/incidents'>Incidents</a> <br/>
              <a href='https://nadralia-ireporter.herokuapp.com/api/v1/auth/signup'>User Signup</a>
              <a href='https://nadralia-ireporter.herokuapp.com/api/v1/auth/login'>User Login</a>
         </div>
       </body>
     </html>
"""