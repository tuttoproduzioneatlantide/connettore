from odoo.addons.component.core import AbstractComponent


class BaseConnectorComponent(AbstractComponent):
    """ Base component for the connector

    Is inherited by every components of the Connector (Binder, Mapper, ...)
    and adds a few methods which are of common usage in the connectors.

    """

    _name = "base.connector"

    @property
    def backend_record(self):
        """ Backend record we are working with """
        # backward compatibility
        return self.work.collection

    def binder_for(self, model=None):
        """ Shortcut to get Binder for a model

        Equivalent to: ``self.component(usage='binder', model_name='xxx')``

        """
        return self.component(usage="binder", model_name=model)

