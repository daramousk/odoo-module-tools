# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    This module copyright:
#        (C) 2016 Cristian Moncho
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

# see: http://people.canonical.com/~mwh/bzrlibapi/bzrlib.html

from __future__ import absolute_import

from datetime import datetime
import logging

from . import ABCVcs


try:
    import bzrlib
    import bzrlib.plugin
except ImportError:
    raise Exception('Bazaar library not found.')

_logger = logging.getLogger(__name__)

if hasattr(bzrlib, 'initialize'):
    bzrlib.initialize()

bzrlib.plugin.load_plugins()

# bzrlib.ui.ui_factory = bzrlib.ui.SilentUIFactory()
if hasattr(bzrlib.ui.ui_factory, 'be_quiet'):
    bzrlib.ui.ui_factory.be_quiet(True)


class Bzr(ABCVcs):
    _vcs = 'bzr'
    _dir_structure = ('.bzr', 'branch')

    def init(self, source, branch=None, **kwargs):
        assert not self.is_initialized()
        _logger.debug('Initializing repo %s...', self._path)
        branch = bzrlib.branch.Branch.open(source)
        branch.create_checkout(self._path, revision_id=None, lightweight=True)

    def load(self, **kwargs):
        assert self._path and self.is_repo(self._path)
        _logger.debug('Loading repo %s...', self._path)
        self._repo = bzrlib.controldir.ControlDir.open(self._path)

    def info(self):
        _logger.debug('Getting info from repo %s...', self._path)
        branch = self._repo.open_branch()
        rev_id = branch.last_revision()
        rev = branch.repository.get_revision(rev_id)
        return dict(super(Bzr, self).info(), **{
            'source': self._repo.open_branch().user_url,
            # 'branch': None,
            'rev_id': branch.last_revision(),
            'rev_date': datetime.fromtimestamp(rev.timestamp),
        })

    def update(self):
        assert self.is_initialized() and self.is_clean()
        _logger.debug('Updating repo %s...', self._path)
        # [TODO] [TEST] has_workingtree
        self._repo.open_workingtree().update()

    def is_clean(self):
        """ True if there are no changes and no new files. """
        if not self.is_initialized():
            return False
        wt = self._repo.open_workingtree()
        return not (wt.has_changes() or next(wt.extras(), None))
