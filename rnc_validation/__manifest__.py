# -*- coding: utf-8 -*-    
{
    'name': "RNC/Cedula Validation RD",

    'summary': """
            Localizacion Para Republica Dominicana
            Automatically creates customers and suppliers using the valid tax ID and the DGII.
        """,

    'description': """
        Pressing the create button in all for new partner will validate de fiscal identification, this module is connected directly to the form of validation of RNC / Cedula
        DGII valid if correct and automatically creates the associated name.
    """,

    'author': "Marcos Organizador de Negocios SRL - Write by Eneldo Serrata",
    'website': "http://marcos.do",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Localization',
    'version': '10.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views.xml',
        'data/data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
    
}
