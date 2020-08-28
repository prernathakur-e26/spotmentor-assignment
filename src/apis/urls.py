from apis import views


api_urls = [
    ("/", views.index, ["GET"], "flask scaffolding index url"),
    ("/login",views.login,["GET","POST"],"flask scaffolding login url"),
    ("/user",views.get_all_users,["GET"],"flask scaffolding get_all_users url"),
    ("/user/<username>",views.get_one_user,["GET"],"flask scaffolding get_one_user url"),
    ("/create/user",views.create_user,["POST"],"flask scaffolding create_user url"),
    ("/update/user/<username>",views.update_user,["PUT"],"flask scaffolding update_user url"),
    ("/delete/user/<username>",views.delete_user,["DELETE"],"flask scaffolding delete_user url"),
]

other_urls = []

all_urls = api_urls + other_urls
