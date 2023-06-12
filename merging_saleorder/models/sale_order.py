from odoo import models


class SalesOrder(models.Model):
    _inherit = 'sale.order'
    _description = "This model allows applying the commission in the sales"

    # @api.model
    def action_merge(self, *args):
        for i in self:
            # starts iterating over each instance in the salesperson
            order_line_dict = {}
            for j in i.order_line:
                # this line iterates over each order line in the current salesperson instances.
                considered = (j.product_template_id, j.price_unit)
                # assigns a tuple to the variable which act as an identifier
                print(j.product_template_id)
                if considered in order_line_dict:
                    # checks if the considered tuple exist in the order line dictionary
                    order_line_dict[considered] += j.product_uom_qty
                    # if exist this line increment the value by the quantity
                    j.unlink()
                else:
                    order_line_dict[considered] = j.product_uom_qty
            #         if the key is not present in the

            for j in i.order_line:
                considered = (j.product_template_id, j.price_unit)
                j.write({'product_uom_qty': order_line_dict.get(considered, j.product_uom_qty)})

        return True
