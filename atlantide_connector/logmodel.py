from odoo import models,fields

class LogForAtlantide(models.Model):
    _name = 'atlantide.changes_for_atlantide'
    
    model_name = fields.Char(string="model name", index=True, size=255)
    model_id    = fields.Integer(string="model idd", index=True)
    action_type    fields.Char(string="action type", index=True, size=1)
    action_timestamp    = fields.Datetime(string="action time")
    action_performed_by_user = fields.Integer(string="action was perform by user with this id")
    is_processed  = fields.Boolean(string="already processed by atlantide")
    atlantide_process_failed  = fields.Boolean(string="processed by atlantide with errors")
    process_error_description = fields.Text(string="description of atlantide process error")
    