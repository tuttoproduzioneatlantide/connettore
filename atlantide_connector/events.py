from odoo.addons.component.core import Component
from odoo.addons.component_event import skip_if
from datetime import datetime

class AtlantideListener(Component):
    _name = 'atlantide.event.listener'
    _inherit = 'base.connector.listener'
    _apply_on = ['res.partner','sale.order.line','sale.order','product.product','purchase.order.line','purchase.order','waste.rds.line','waste.rds','res.users','waste.waste']

    @skip_if(lambda self, record, **kwargs: self.no_connector_export(record))
    def on_record_create(self, record, fields=None):
        self.env['x_log_changes_for_atlantide'].create({
            'x_model_name': record._name,
            'x_model_id': record.id,
            'x_action_type': 'a',
            'x_action_timestamp': datetime.now(),
            'x_action_performed_by_user': record.write_uid.ids[0],
            'x_is_processed': False,
            'x_atlantide_process_failed': False,
            'x_process_error_description': ''
        })

    @skip_if(lambda self, record, **kwargs: self.no_connector_export(record))
    def on_record_write(self, record, fields=None):
        self.env['x_log_changes_for_atlantide'].create({
            'x_model_name': record._name,
            'x_model_id': record.id,
            'x_action_type': 'u',
            'x_action_timestamp': datetime.now(),
            'x_action_performed_by_user': record.write_uid.ids[0],
            'x_is_processed': False,
            'x_atlantide_process_failed': False,
            'x_process_error_description': ''
        })
    def on_record_unlink(self, record):
        self.env['x_log_changes_for_atlantide'].create({
            'x_model_name': record._name,
            'x_model_id': record.id,
            'x_action_type': 'r',
            'x_action_timestamp': datetime.now(),
            'x_action_performed_by_user': record.write_uid.ids[0],
            'x_is_processed': False,
            'x_atlantide_process_failed': False,
            'x_process_error_description': ''
        })

