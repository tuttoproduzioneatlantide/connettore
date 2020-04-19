from odoo import models,fields

class LogForAtlantide(models.Model):
    _name = 'x_log_changes_for_atlantide'
    
    x_model_name = fields.Char(string="model name", index=True, size=255)
    
    x_model_id    = fields.Integer(string="model idd", index=True)
    
    x_action_type  =  fields.Char(string="action type", index=True, size=1)
    
    x_action_timestamp    = fields.Datetime(string="action time")
    
    x_action_performed_by_user = fields.Integer(string="action was perform by user with this id")
    
    x_is_processed  = fields.Boolean(string="already processed by atlantide")
    
    x_atlantide_process_failed  = fields.Boolean(string="processed by atlantide with errors")
    
    x_process_error_description = fields.Text(string="description of atlantide process error")
    