# © 2016 Opener B.V. (<https://opener.am>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from lxml import etree

from odoo import api, models


class Base(models.AbstractModel):
    _inherit = "base"

    @api.model
    def _get_view(self, view_id=None, view_type="form", **options):
        """
        Retrieve and modify the view architecture for the given view ID or type.

        This method overrides the base `_get_view` method to customize the
        architecture of the view. It retrieves the view architecture, modifies
        it by replacing specific group identifiers, and then returns the modified
        architecture along with the original view record.

        :param int view_id: The ID of the view to retrieve. If None, defaults
                            to the specified view type.
        :param str view_type: The type of the view to return ('form', 'list', etc.).
        :param dict options: Additional options for fetching the view.

        :return: A tuple containing:
            - etree.Element: The modified view architecture as an etree node.
            - ir.ui.view: The original view record retrieved.
        """
        arch, view = super()._get_view(view_id=view_id, view_type=view_type, **options)
        arch_str = etree.tostring(arch, encoding="unicode")
        arch_str = arch_str.replace(
            "base.group_no_one", "base_technical_features.group_technical_features"
        )
        arch = etree.fromstring(arch_str)

        return arch, view
