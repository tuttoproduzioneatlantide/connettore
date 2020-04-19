from odoo.addons.component.core import Component
from odoo.addons.component_event import skip_if
from datetime import datetime

class AtlantideListener(Component):
    _name = 'atlantide.event.listener'
    _inherit = 'base.connector.listener'
    _apply_on = ['res.users']

    @skip_if(lambda self, record, **kwargs: self.no_connector_export(record))
    def on_record_create(self, record, fields=None):
        """ Called when a record is created """
        f = open("mylog.txt", "a")
        f.write("Create! {0} Record: {1} Self: {2} Fields: {3}\n".format(record, type(record), type(self), type(fields)))
        f.close()

    @skip_if(lambda self, record, **kwargs: self.no_connector_export(record))
    def on_record_write(self, record, fields=None):
        #f = open("mylog.txt", "a")
        #f.write("Write! {0}  Record: {1} Self: {2} Fields: {3} Nostro: {4}\n".format(record, type(record), type(self), type(fields), type(self.env['x_log_changes_for_atlantide'])))
        #f.close()
        self.env['x_log_changes_for_atlantide'].create({
            'x_model_name': 'res.users.2',
            'x_model_id': 32,
            'x_action_type': 'u',
            'x_action_timestamp': datetime.now(),
            'x_action_performed_by_user': 1,
            'x_is_processed': False,
            'x_atlantide_process_failed': False,
            'x_process_error_description': ''
        })
    def on_record_unlink(self, record):
        f = open("mylog.txt", "a")
        f.write("Write! {0}  Record: {1} Self: {2} \n".format(record, type(record), type(self)))
        f.close()

