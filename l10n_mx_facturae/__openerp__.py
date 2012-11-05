# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2010 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
############################################################################
#    Coded by: moylop260 (moylop260@vauxoo.com)
#    Launchpad Project Manager for Publication: Nhomar Hernandez - nhomar@vauxoo.com
############################################################################
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

{
    "name" : "Creacion de Factura Electronica para Mexico (CFD)",
    "version" : "1.0",
    "author" : "Vauxoo",
    "category" : "Localization/Mexico",
    "description" : """This module creates e-invoice files from invoices with standard CFD-2010 of Mexican SAT.
Requires the following programs:
  xsltproc
    Ubuntu insall with:
        sudo apt-get install xsltproc

  openssl
      Ubuntu insall with:
        sudo apt-get install openssl
    """,
    "website" : "http://www.vauxoo.com/",
    "license" : "AGPL-3",
    "depends" : ["account", "base_vat", "document",
            "l10n_mx_facturae_lib", "l10n_mx_partner_address",
            "l10n_mx_facturae_cer",
            "l10n_mx_invoice_datetime",
            "l10n_mx_invoice_tax_ref",
            "l10n_mx_facturae_seq",
            "l10n_mx_company_cif",
            "l10n_mx_partner_address",
            "l10n_mx_invoice_amount_to_text",
            "sale",#no depende de "sale" directamente, pero marca error en algunas versiones
        ],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
        'security/l10n_mx_facturae_security.xml',
        #'security/ir.model.access.csv',
        "l10n_mx_facturae_report.xml",
        "wizard/wizard_invoice_facturae_txt_v6_view.xml",
        "wizard/wizard_invoice_facturae_xml_v6_view.xml",
        "wizard/installer_view.xml",
        #"ir_sequence_view.xml",
        #"res_company_view6.xml",
        "invoice_view.xml",
        #"partner_address_view.xml",
    ],
    "installable" : True,
    "active" : False,
}
