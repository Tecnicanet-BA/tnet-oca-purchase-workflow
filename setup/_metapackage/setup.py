import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-purchase-workflow",
    description="Meta package for oca-purchase-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-procurement_purchase_no_grouping',
        'odoo12-addon-product_form_purchase_link',
        'odoo12-addon-product_supplier_code_purchase',
        'odoo12-addon-product_supplierinfo_qty_multiplier',
        'odoo12-addon-purchase_add_products_from_bom',
        'odoo12-addon-purchase_allowed_product',
        'odoo12-addon-purchase_analytic_global',
        'odoo12-addon-purchase_blanket_order',
        'odoo12-addon-purchase_commercial_partner',
        'odoo12-addon-purchase_date_planned_manual',
        'odoo12-addon-purchase_default_terms_conditions',
        'odoo12-addon-purchase_delivery_split_date',
        'odoo12-addon-purchase_deposit',
        'odoo12-addon-purchase_discount',
        'odoo12-addon-purchase_exception',
        'odoo12-addon-purchase_force_invoiced',
        'odoo12-addon-purchase_invoice_plan',
        'odoo12-addon-purchase_invoice_plan_deposit',
        'odoo12-addon-purchase_landed_cost',
        'odoo12-addon-purchase_last_price_info',
        'odoo12-addon-purchase_line_procurement_group',
        'odoo12-addon-purchase_location_by_line',
        'odoo12-addon-purchase_manual_delivery',
        'odoo12-addon-purchase_minimum_amount',
        'odoo12-addon-purchase_no_rfq',
        'odoo12-addon-purchase_open_qty',
        'odoo12-addon-purchase_order_analytic_search',
        'odoo12-addon-purchase_order_approval_block',
        'odoo12-addon-purchase_order_approved',
        'odoo12-addon-purchase_order_archive',
        'odoo12-addon-purchase_order_general_discount',
        'odoo12-addon-purchase_order_line_deep_sort',
        'odoo12-addon-purchase_order_line_description',
        'odoo12-addon-purchase_order_line_packaging_qty',
        'odoo12-addon-purchase_order_line_price_history',
        'odoo12-addon-purchase_order_line_price_history_discount',
        'odoo12-addon-purchase_order_line_sequence',
        'odoo12-addon-purchase_order_line_stock_available',
        'odoo12-addon-purchase_order_product_recommendation',
        'odoo12-addon-purchase_order_product_recommendation_brand',
        'odoo12-addon-purchase_order_product_recommendation_forecast',
        'odoo12-addon-purchase_order_product_recommendation_secondary_unit',
        'odoo12-addon-purchase_order_secondary_unit',
        'odoo12-addon-purchase_order_type',
        'odoo12-addon-purchase_order_uninvoiced_amount',
        'odoo12-addon-purchase_picking_state',
        'odoo12-addon-purchase_price_recalculation',
        'odoo12-addon-purchase_product_usage',
        'odoo12-addon-purchase_propagate_qty',
        'odoo12-addon-purchase_quick',
        'odoo12-addon-purchase_reception_notify',
        'odoo12-addon-purchase_reception_status',
        'odoo12-addon-purchase_request',
        'odoo12-addon-purchase_request_department',
        'odoo12-addon-purchase_request_order_approved',
        'odoo12-addon-purchase_request_product_usage',
        'odoo12-addon-purchase_request_tier_validation',
        'odoo12-addon-purchase_request_usage_department',
        'odoo12-addon-purchase_requisition_auto_rfq',
        'odoo12-addon-purchase_requisition_line_description',
        'odoo12-addon-purchase_requisition_tier_validation',
        'odoo12-addon-purchase_security',
        'odoo12-addon-purchase_start_end_dates',
        'odoo12-addon-purchase_stock_price_unit_sync',
        'odoo12-addon-purchase_stock_return_request',
        'odoo12-addon-purchase_tier_validation',
        'odoo12-addon-purchase_triple_discount',
        'odoo12-addon-purchase_work_acceptance',
        'odoo12-addon-purchase_work_acceptance_evaluation',
        'odoo12-addon-subcontracted_service',
        'odoo12-addon-supplier_calendar',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
