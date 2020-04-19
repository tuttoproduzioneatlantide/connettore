# Copyright 2013-2017 Camptocamp SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

import hashlib
import logging
import struct

_logger = logging.getLogger(__name__)


def pg_try_advisory_lock(env, lock):
    hasher = hashlib.sha1(str(lock).encode())
    # pg_lock accepts an int8 so we build an hash composed with
    # contextual information and we throw away some bits
    int_lock = struct.unpack("q", hasher.digest()[:8])

    env.cr.execute("SELECT pg_try_advisory_xact_lock(%s);", (int_lock,))
    acquired = env.cr.fetchone()[0]
    return acquired
