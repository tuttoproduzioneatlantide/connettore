# Copyright 2012-2017 Camptocamp SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

# Connector related errors


class ConnectorException(Exception):
    """ Base Exception for the connectors """


class NoConnectorUnitError(ConnectorException):
    """ No ConnectorUnit has been found """


class InvalidDataError(ConnectorException):
    """ Data Invalid """


# Job related errors


class MappingError(ConnectorException):
    """ An error occurred during a mapping transformation. """


