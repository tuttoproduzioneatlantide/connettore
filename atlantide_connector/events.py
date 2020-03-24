from odoo.addons.component.core import Component
from odoo.addons.component_event import skip_if

class AtlantideListener(Component):
    _name = 'atlantide.event.listener'
    _inherit = 'base.connector.listener'
    _apply_on = ['res.users']

    @skip_if(lambda self, record, **kwargs: self.no_connector_export(record))
    def on_record_create(self, record, fields=None):
        """ Called when a record is created """
        f = open("mylog.txt", "a")
        f.write("Create! {0} \n".format(record))
        f.close()		

    @skip_if(lambda self, record, **kwargs: self.no_connector_export(record))
    def on_record_write(self, record, fields=None):
        f = open("mylog.txt", "a")
        f.write("Write! {0} \n".format(record))
        f.close()		

    def on_record_unlink(self, record):
        with record.backend_id.work_on(record._name) as work:
            external_id = work.component(usage='binder').to_external(record)
            if external_id:
                f = open("mylog.txt", "a")
                f.write("Write! {0} \n".format(record))
                f.close()		

