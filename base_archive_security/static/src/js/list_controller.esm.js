/** @odoo-module **/

import {ListController} from "@web/views/list/list_controller";
import {onWillStart} from "@odoo/owl";
import {patch} from "@web/core/utils/patch";
import {useService} from "@web/core/utils/hooks";

patch(ListController.prototype, "base_archive_security.ListControllerPatch", {
    setup() {
        this._super();
        this.userService = useService("user");
        onWillStart(async () => {
            this.archiveEnabled = await this.userService.hasGroup(
                "base_archive_security.group_can_archive"
            );
        });
    },
});
