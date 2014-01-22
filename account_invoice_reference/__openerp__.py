# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2014 Camptocamp SA
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

{'name' : 'Invoices Reference',
 'version' : '1.0',
 'author' : 'Camptocamp',
 'maintainer': 'Camptocamp',
 'license': 'AGPL-3',
 'category': 'category',
 'complexity': "easy",
 'depends' : ['account',
              ],
 'description': """
Invoices Reference
==================

Aims to simplify the "references" things on the invoices.  There is too
many fields on the invoices.  And it is very difficult to remember
which field goes in which field of the Journal Entries and under which
conditions.

Is follows this rule: the reference of a journal entry is
always the reference of the document which generated it to
be able to trace them in the accounting reports. That means the origin
of an invoice or if the invoice has been created manually without origin,
its number.

It particularly fits with other modules of the bank-statement-reconcile series
like account_advanced_reconcile_transaction_ref.

Use cases
---------

Customer invoices
  Journal Entry Reference is the Origin of the invoice if there,
  otherwise, it is the Number of the invoice.

Supplier invoices
  Journal Entry Reference is the Supplier Invoice Number of the invoice
  which is now mandatory.

 """,
 'website': 'http://www.camptocamp.com',
 'data': ['account_invoice_view.xml',
          ],
 'test': ['test/out_invoice_with_origin.yml',
          'test/out_invoice_without_origin.yml',
          'test/in_invoice_with_supplier_number.yml',
          'test/in_invoice_without_supplier_number.yml',
          'test/out_refund_with_origin.yml',
          'test/out_refund_without_origin.yml',
          'test/in_refund_with_supplier_number.yml',
          'test/in_refund_without_supplier_number.yml',

          ],
 'installable': True,
 'auto_install': False,
}
