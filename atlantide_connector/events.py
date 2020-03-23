from odoo.addons.connector.event import on_record_create

@on_record_create()

def procesa_creacion_de_usuarios(session, model_name, record_id, vals):
        f = open("mylog.txt", "a")
        f.write("Create!")
        f.close()
