from openerp.tools.translate import _
import datetime
from openerp.osv import orm, fields

def float_or_zero(val):
    return float(val) if val else 0.0

class AccountStatementProfil(orm.Model):
    _inherit = "account.statement.profile"

    def _write_extra_statement_lines(
            self, cr, uid, parser, result_row_list, profile, statement_id, context):
        """Prepare the global commission line if there is one.
        """
        global_commission_amount = 0
        for row in parser.result_row_list:
            global_commission_amount += float_or_zero(row.get('commission_amount', '0.0'))
        if not global_commission_amount:
            return
        partner_id = profile.partner_id and profile.partner_id.id or False
        commission_account_id = profile.commission_account_id and profile.commission_account_id.id or False
        commission_analytic_id = profile.commission_analytic_id and profile.commission_analytic_id.id or False
        comm_values = {
            'name': 'IN ' + _('Commission line'),
            'date': datetime.datetime.now().date(),
            'amount': global_commission_amount,
            'partner_id': partner_id,
            'type': 'general',
            'statement_id': statement_id,
            'account_id': commission_account_id,
            'ref': 'commission',
            'analytic_account_id': commission_analytic_id,
            # !! We set the already_completed so auto-completion will not update those values!
            'already_completed': True,
        }
        statement_line_obj = self.pool.get('account.bank.statement.line')
        statement_line_obj.create(cr, uid, comm_values, context=context)

class AccountStatementLineWithCommission(orm.Model):
    _inherit = "account.bank.statement.line"
    _columns = {
        'commission_amount': fields.sparse(
            type='float',
            string='Line Commission Amount',
            serialization_field='additionnal_bank_fields'),
    }

class CreditPartnerStatementImporter(orm.TransientModel):
    _inherit = "credit.statement.import"

    _columns = {
        'commission_account_id': fields.many2one('account.account',
                                                 'Commission account'),
        'commission_analytic_id': fields.many2one('account.analytic.account',
                                                 'Commission analytic account'),
    }

    def onchange_profile_id(self, cr, uid, ids, profile_id, context=None):
        res = super(CreditPartnerStatementImporter, self).onchange_profile_id(
            cr, uid, ids, profile_id, context=context)
        if profile_id:
            c = self.pool.get("account.statement.profile").browse(
                    cr, uid, profile_id, context=context)
            res['value']['commission_account_id'] = \
                c.commission_account_id and c.commission_account_id.id or False
            res['value']['commission_a'] = \
                c.commission_analytic_id and c.commission_analytic_id.id or False
        return res