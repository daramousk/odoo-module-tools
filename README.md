Odoo Module Tools
=================

About
-----

This repository aims to offer a faster way to manage and deploy all the non-official *OpenERP/Odoo* modules.


Installation
------------

The recommended installation way is to clone this repository under your Odoo's **data_path**, this way it will be able to upgrade itself. Assuming that you are logged as **root** user and that the service is launched by the **odoo** user (who also must have his own $HOME directory), the next commands will do it:

```
# su - odoo -c "mkdir -p ~/.local/share/Odoo/repositories/8.0"
# su - odoo -c "git clone https://github.com/crimoniv/odoo-module-tools -b 8.0 ~/.local/share/Odoo/repositories/8.0/odoo_module_tools
```

Once the repository is completely cloned, its absolute path must be included in the **addons_path** parameter, in *OpenERP/Odoo*'s config file (e.g. `/etc/odoo/openerp-server.conf`).

```
addons_path = <path1>,<path2>,/home/odoo/.local/share/Odoo/repositories/8.0/odoo_module_tools
```

\**If the previous parameter does not exists, it is safe to declare it with only one path.*


Included Modules
----------------

addon | version | summary
--- | --- | ---
[repository_management](repository_management/)* | 8.0.1.0 | Manage external repositories.
[module_external](module_external/)* | 8.0.1.0 | Upload and install modules from external sources.

\**Both methods should not be used interchangeably to install the same module.*


Disclaimer
----------

* I do not assume any responsibility for any consequence of using the modules found in this repository.
* These modules are deployed with the purpose of helping developers to develop and test modules in a faster and easier way.
* It is highly discouraged their usage in a production environments, for security and stability reasons.
* Experienced and skilled users may use them for other purposes at their own risk.

Licenses
--------

* The content of this project itself is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE (Version 3). To view a copy of this license, see [LICENSE](LICENSE) or visit http://www.gnu.org/licenses/agpl-3.0.html.
* The icons [box] and [wrench] are licensed under a [Creative Commons (Attribution 3.0 Unported) License]. They are attributed to [Pixel Buddha].

[box]: https://www.iconfinder.com/icons/289621/archive_box_bundle_cargo_delivery_package_products_icon#size=128
[wrench]: https://www.iconfinder.com/icons/416405/service_setting_tool_tools_work_wrench_icon#size=128
[Creative Commons (Attribution 3.0 Unported) License]: http://creativecommons.org/licenses/by/3.0/
[Pixel Buddha]: https://www.iconfinder.com/PixelBuddha
