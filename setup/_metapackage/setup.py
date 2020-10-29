import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-sale-workflow",
    description="Meta package for oca-sale-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-partner_contact_sale_info_propagation',
        'odoo12-addon-partner_prospect',
        'odoo12-addon-partner_sale_pivot',
        'odoo12-addon-portal_sale_personal_data_only',
        'odoo12-addon-product_form_sale_link',
        'odoo12-addon-product_supplierinfo_for_customer_sale',
        'odoo12-addon-sale_automatic_workflow',
        'odoo12-addon-sale_automatic_workflow_job',
        'odoo12-addon-sale_automatic_workflow_payment_mode',
        'odoo12-addon-sale_blanket_order',
        'odoo12-addon-sale_cancel_reason',
        'odoo12-addon-sale_commercial_partner',
        'odoo12-addon-sale_commitment_lead_time',
        'odoo12-addon-sale_contact_type',
        'odoo12-addon-sale_disable_inventory_check',
        'odoo12-addon-sale_discount_display_amount',
        'odoo12-addon-sale_double_validation',
        'odoo12-addon-sale_elaboration',
        'odoo12-addon-sale_exception',
        'odoo12-addon-sale_fixed_discount',
        'odoo12-addon-sale_force_invoiced',
        'odoo12-addon-sale_generator',
        'odoo12-addon-sale_global_discount',
        'odoo12-addon-sale_invoice_group_method',
        'odoo12-addon-sale_invoice_plan',
        'odoo12-addon-sale_invoice_policy',
        'odoo12-addon-sale_isolated_quotation',
        'odoo12-addon-sale_last_price_info',
        'odoo12-addon-sale_merge_draft_invoice',
        'odoo12-addon-sale_milestone_profile_invoicing',
        'odoo12-addon-sale_mrp_bom',
        'odoo12-addon-sale_mrp_link',
        'odoo12-addon-sale_order_action_invoice_create_hook',
        'odoo12-addon-sale_order_archive',
        'odoo12-addon-sale_order_digitized_signature',
        'odoo12-addon-sale_order_general_discount',
        'odoo12-addon-sale_order_incoterm_place',
        'odoo12-addon-sale_order_invoicing_finished_task',
        'odoo12-addon-sale_order_line_date',
        'odoo12-addon-sale_order_line_description',
        'odoo12-addon-sale_order_line_input',
        'odoo12-addon-sale_order_line_price_history',
        'odoo12-addon-sale_order_line_sequence',
        'odoo12-addon-sale_order_lot_generator',
        'odoo12-addon-sale_order_lot_selection',
        'odoo12-addon-sale_order_min_qty',
        'odoo12-addon-sale_order_price_recalculation',
        'odoo12-addon-sale_order_product_recommendation',
        'odoo12-addon-sale_order_product_recommendation_secondary_unit',
        'odoo12-addon-sale_order_revision',
        'odoo12-addon-sale_order_secondary_unit',
        'odoo12-addon-sale_order_tag',
        'odoo12-addon-sale_order_transmit_method',
        'odoo12-addon-sale_order_type',
        'odoo12-addon-sale_partner_incoterm',
        'odoo12-addon-sale_procurement_group_by_commitment_date',
        'odoo12-addon-sale_procurement_group_by_line',
        'odoo12-addon-sale_product_category_menu',
        'odoo12-addon-sale_product_multi_add',
        'odoo12-addon-sale_product_returnable',
        'odoo12-addon-sale_product_set',
        'odoo12-addon-sale_product_set_variant',
        'odoo12-addon-sale_quotation_number',
        'odoo12-addon-sale_rental',
        'odoo12-addon-sale_require_po_doc',
        'odoo12-addon-sale_shipping_info_helper',
        'odoo12-addon-sale_start_end_dates',
        'odoo12-addon-sale_stock_delivery_address',
        'odoo12-addon-sale_stock_picking_blocking',
        'odoo12-addon-sale_stock_picking_note',
        'odoo12-addon-sale_stock_return_request',
        'odoo12-addon-sale_stock_secondary_unit',
        'odoo12-addon-sale_stock_sourcing_address',
        'odoo12-addon-sale_tier_validation',
        'odoo12-addon-sale_triple_discount',
        'odoo12-addon-sale_validity',
        'odoo12-addon-sale_wishlist',
        'odoo12-addon-sales_team_security',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
