from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_product", views.createProduct, name="create_product"),
    path("product_detail/<listing_id>", views.productDetail, name="product_detail"),
    path("watchlist/add/<listing_id>", views.addWatchlist, name="add_watchlist"),
    path("watchlist/delete/<listing_id>", views.deleteWatchlist, name="delete_watchlist"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("category_detail/<category_id>", views.categoryDetail, name="category_detail"),
]
