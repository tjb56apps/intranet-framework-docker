from flask import render_template, redirect, url_for, session, request, flash
from app.addons.poweruploader import bp
from app.manifest import get_addon, get_child_path #, create_table
# from app.addons.blog.model.blog import Blogpost
from app.addons.poweruploader.model.poweruploader import Poweruploader, Table, Manual, Hsemanhour062024
from app.auth.managementAuth import Users
from app.extensions.database import db, postgres_db, engine_postgres
from importlib import import_module
from werkzeug.utils import secure_filename
from app.addons.poweruploader.utils.utils import allowed_file
from app.addons.poweruploader.utils.table import table
from app.addons.poweruploader.utils.tblview import get_values
import os
import app
import csv
import pandas as pd

# @bp.route("/")
# def index():
#     addon = get_addon(addondir="poweruploader")
#     if addon:
#         if addon[1]:
#             return render_template("addons/poweruploader/templates/index.html", addon_nav=addon[0], path=get_child_path())

#     return redirect(url_for('main.index'))

@bp.route("/")
def index():
    addon = get_addon(addondir="poweruploader")
    if addon:
        if addon[1]:
            # print(session["username"])
            options = db.query(Poweruploader.table).filter_by(username=session["username"]).first()
            if options is None:
                options__ = []
            else:
                options_ = [opt for opt in options]
                options__ = options_[0].split(",")
            return render_template("addons/poweruploader/templates/uploader.html", options=options__, addon_nav=addon[0], path=get_child_path())
    return redirect(url_for('main.index'))

@bp.route("/upload-to-table", methods=["GET", "POST"])
def upload_to_table():
    addon = get_addon(addondir="poweruploader")
    if addon:
        if addon[1]:
            # if session["leveling"] == "parent":
            if request.method == "POST":
                table_name = request.form["dtbase"]
                
                # Logic upload metode
                if request.files.get("file"):
                    file = request.files['file']
                    if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.app.config['UPLOAD_FOLDER'], "addons", "poweruploader", "static", filename))

                        try:
                            notif = table(table_name, filename)
                            flash(notif)

                            return redirect(url_for("poweruploader.index"))
                        except Exception as e:
                            print(e)
                            return redirect(url_for("poweruploader.index"))

                else:
                    print(False)
                    return redirect(url_for("poweruploader.index"))

                return redirect(url_for("poweruploader.index"))

    return redirect(url_for('main.index'))

@bp.route("/users")
def users():
    addon = get_addon(addondir="poweruploader")
    if addon:
        if addon[1]:
            if session["leveling"] == "parent":
                users = db.query(Users).filter(Users.apps_id.ilike("%B002%")).all()
                user_s = []
                for row in users:
                    root = {
                        "id": row.id,
                        "username": row.username,
                        "department": row.department,
                        "position": row.position,
                        "action": db.query(Poweruploader).filter_by(username=row.username).first()
                    }
                    user_s.append(root)
                # print(user_s)

                return render_template("addons/poweruploader/templates/users.html", users=user_s, addon_nav=addon[0], path=get_child_path())
            return redirect(url_for('poweruploader.index'))
    return redirect(url_for('main.index'))

@bp.route("/add")
def add_table():
    addon = get_addon(addondir="poweruploader")
    if addon:
        if addon[1]:
            users_tab = db.query(Users).filter_by(id=request.args.get("id")).first()
            
            # table query from poweruploader
            table = db.query(Poweruploader).filter_by(username=users_tab.username).first()
            if table is None:
                # record
                pwu = Poweruploader(username=users_tab.username, department=users_tab.department, position=users_tab.position, table="")
                db.add(pwu)
                db.commit()

                return redirect(url_for("poweruploader.users"))

            # table query from table db
            tables = db.query(Table).all()
            # print(tables)
            table_list = []
            for tb in tables:
                # print(table.table)
                root = {
                    "id": tb.id,
                    "table_name": tb.table_name,
                    "check": tb.table_name in table.table.split(",")
                }
                table_list.append(root)

            # print(table_list)
            
            return render_template("addons/poweruploader/templates/add_table.html", tables=table_list, users_tab=users_tab, addon_nav=addon[0], path=get_child_path())
    return redirect(url_for('main.index'))

@bp.route("/save", methods=["GET", "POST"])
def save():
    addon = get_addon(addondir="poweruploader")
    if addon:
        if addon[1]:

            tbl_str = ""
            for tbl in request.form.getlist("table"):
                tbl_str+=tbl+","
            table = (tbl_str[:-1])

            if db.query(Poweruploader).filter_by(username=request.form["username"]).first() is not None:
                update_table = db.query(Poweruploader).where(Poweruploader.username == request.form["username"])
                update_table.update({
                    Poweruploader.table: table# request.form["table"]
                })
                
                db.commit()
            else:
                username = (request.form["username"])
                department = (request.form["department"])
                position = (request.form["position"])
                # table = (request.form["table"])
                # table = (request.form.getlist("table"))

                new_user = Poweruploader(username=username, department=department, position=position, table=table)
                db.add(new_user)
                db.commit()

            return redirect(url_for("poweruploader.users"))
    return redirect(url_for('main.index'))

@bp.route("/table-view")
def table_view():
    addon = get_addon(addondir="poweruploader")
    if addon:
        if addon[1]:
            tables = get_values(request.args.get("table"))
            # print(tables)
            return render_template("addons/poweruploader/templates/table_view.html", table_html=tables, addon_nav=addon[0], path=get_child_path())

    return redirect(url_for('main.index'))