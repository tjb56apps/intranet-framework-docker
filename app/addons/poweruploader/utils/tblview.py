from importlib import import_module
from app.extensions.database import postgres_db, engine_postgres
from sqlalchemy import text, inspect

def get_values(table_name):

    try:
        tabel = getattr(import_module("app.addons.poweruploader.model.poweruploader"), table_name)
    except:
        return "<span>data not found</span>"
    
    users = postgres_db.query(tabel).all()
    
    tbs = []
    for row in users:
        d = {}
        for column in row.__table__.columns:
            if column.name != "id": # optional
                d[column.name] = str(getattr(row, column.name))
        
        tbs.append(d)

    # Extract Keys
    thead = ""
    try:
        for k in tbs[0].keys():
            thead+= f"<th>{k.capitalize()}</th>"
    except:
        return "<span>data not found</span>"
    
    # Extract Value
    kbody = "<tr>"
    for v in tbs:
        for ky in tbs[0].keys():
            kbody+= f"<td>{v[ky]}</td>"
        kbody+= "</tr>"

    return f'''
    <table class="table table-bordered table-striped">
        <thead>
            <tr>
            {thead}
            </tr>
        </thead>
        <tbody>
            {kbody}
        </tbody>
    </table>
    '''