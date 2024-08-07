from flask import render_template, redirect, url_for, session
from app.addons.blog import bp
from app.manifest import get_addon, get_child_path #, create_table
from app.addons.blog.model.blog import Blogpost
from app.auth.managementAuth import Users
from app.extensions.database import db

@bp.route("/")
def index():
    # print(Blogpost.query.statement.subquery().columns.keys())

    addon = get_addon(addondir="blog")
    if addon:
        if addon[1]:
            # return render_template("addons/blog/templates/index.html", addon_nav=addon[0], path=get_child_path())
            return render_template("addons/blog/templates/v2/index.html", addon_nav=addon[0], path=get_child_path())
    return redirect(url_for('main.index'))

@bp.route("/create-post")
def createPost():
    addon = get_addon(addondir="blog")
    if addon:
        if addon[1]:
            # return render_template("addons/blog/templates/create-post.html", addon_nav=addon[0], path=get_child_path())
            return render_template("addons/blog/templates/v2/create-post.html", addon_nav=addon[0], path=get_child_path())
    return redirect(url_for('main.index'))

@bp.route("/create-page")
def createPage():
    addon = get_addon(addondir="blog")
    if addon:
        if addon[1]:
            # return render_template("addons/blog/templates/create-page.html", addon_nav=addon[0], path=get_child_path())
            return render_template("addons/blog/templates/v2/create-page.html", addon_nav=addon[0], path=get_child_path())
    return redirect(url_for('main.index'))

@bp.route("/users")
def users():
    addon = get_addon(addondir="blog")
    if addon:
        if addon[1]:
            users = db.query(Users).where(Users.apps_id == "A001").all()

            # return render_template("addons/blog/templates/users.html", users=users, addon_nav=addon[0], path=get_child_path())
            return render_template("addons/blog/templates/v2/users.html", users=users, addon_nav=addon[0], path=get_child_path())
    return redirect(url_for('main.index'))

@bp.route("/setting")
def setting():
    addon = get_addon(addondir="blog")
    if addon:
        if addon[1]:
            # return render_template("addons/blog/templates/setting.html", addon_nav=addon[0], path=get_child_path())
            return render_template("addons/blog/templates/v2/setting.html", addon_nav=addon[0], path=get_child_path())
    return redirect(url_for('main.index'))