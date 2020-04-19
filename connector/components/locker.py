# Copyright 2018 Camptocamp SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

import logging

import psycopg2

from odoo.addons.component.core import Component
from odoo.addons.connector.exception import RetryableJobError

_logger = logging.getLogger(__name__)


class RecordLocker(Component):
    """Component allowing to lock record(s) for the current transaction

    Example of usage::

        self.component('record.locker').lock(self.records)

    See the definition of :meth:`~lock` for details.
    """

    _name = "base.record.locker"
    _inherit = ["base.connector"]
    _usage = "record.locker"

    def lock(self, records, seconds=None, ignore_retry=True):
        sql = "SELECT id FROM %s WHERE ID IN %%s FOR UPDATE NOWAIT" % self.model._table
        try:
            self.env.cr.execute(sql, (tuple(records.ids),), log_exceptions=False)
        except psycopg2.OperationalError:
            _logger.info(
                "A concurrent job is already working on the same "
                "record (%s with one id in %s). Job delayed later.",
                self.model._name,
                tuple(records.ids),
            )
            raise RetryableJobError(
                "A concurrent job is already working on the same record "
                "(%s with one id in %s). The job will be retried later."
                % (self.model._name, tuple(records.ids)),
                seconds=seconds,
                ignore_retry=ignore_retry,
            )
