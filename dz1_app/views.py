from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    html_main = """
           <!DOCTYPE html>
           <html>
           <head>
               <title>Главная</title>
           </head>
           <body>
               <h1>Добро пожаловать, Пользователь!</h1>              
           </body>
           </html>
       """

    return HttpResponse(html_main)


def about(request):
    html_about = """
               <!DOCTYPE html>
               <html>
               <head>
                   <title>Наверху!</title>
               </head>
               <body>
                   <h1>Обо мне!</h1>
                   <p>Инфа тут</p>
                   tyt!!!    
                   jhhhh!!!          
               </body>
               </html>
           """
    return HttpResponse(html_about)
