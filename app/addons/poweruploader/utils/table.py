import pandas as pd
import os
import app
from app.extensions.database import postgres_db, engine_postgres
from app.addons.poweruploader.model.poweruploader import Manual, Hsemanhour062024

def table(table_name, filename):
    if table_name == "Manual":
        df = pd.read_csv(os.path.join(app.app.config['UPLOAD_FOLDER'], "addons", "poweruploader", "static", filename), delimiter=";")

        df = pd.read_csv(os.path.join(app.app.config['UPLOAD_FOLDER'], "addons", "poweruploader", "static", filename), delimiter=";")
        df2 = pd.read_sql('SELECT name, address FROM "Manual"', con=engine_postgres)
        rows = df[~df.Name.isin([row[0] for row in df2.values.tolist()])]

        postgres_db.add_all([Manual(name=row[1], address=row[2]) for row in rows.values.tolist()])
        postgres_db.commit()

        return True

    elif table_name == "Hsemanhour062024":
        df = pd.read_csv(os.path.join(app.app.config['UPLOAD_FOLDER'], "addons", "poweruploader", "static", filename), delimiter=";")

        df = pd.read_csv(os.path.join(app.app.config['UPLOAD_FOLDER'], "addons", "poweruploader", "static", filename), delimiter=";")
        df2 = pd.read_sql('SELECT no, title, date, company, manpower, manhour, safemanhour, itemtype, path FROM "Hsemanhour062024"', con=engine_postgres)
        rows = df[~df.No.isin([row[0] for row in df2.values.tolist()])]

        postgres_db.add_all([ \
            Hsemanhour062024( \
                no=row[0], \
                title=row[1], \
                date=row[2], \
                company=row[3], \
                manpower=row[4], \
                manhour=row[5], \
                safemanhour=row[6], \
                itemtype=row[7], \
                path=row[8], \
                    ) for row in rows.values.tolist()])
        postgres_db.commit()

        return True

    else:
        return False
