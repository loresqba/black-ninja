# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

from openerp.osv import osv, fields


class sgs_partner_ruta(osv.Model):
    _inherit = 'res.partner'
    _columns = {
        'ruta_id': fields.many2one('sgs.rutas.ruta', 'Rutas'),
        'codigo': fields.char("Codigo Cliente", size=64, required=True),  
        'gironegocio_id': fields.many2one('sgs.rutas.gironegocio', 'Giro de Negocio'),
        'botella_id': fields.many2one('sgs.rutas.botella', 'Botella'),   
        'propiedad_id': fields.many2one('sgs.rutas.propiedad', 'Propiedad'),       
        'clasificacion_id': fields.many2one('sgs.rutas.clasificacion', 'Clasificacion'),
        'exclusividad_id': fields.many2one('sgs.rutas.exclusividad', 'Exclusividad'),
        'impacto_id': fields.many2one('sgs.rutas.impacto', 'Impacto'),
    } 
    _sql_constraints = [('codigo_unico','unique(codigo)','¡El código de debe ser único!')]
sgs_partner_ruta()

class sgs_rutas_ruta(osv.Model):
    _name = "sgs.rutas.ruta"
    _description = "Rutas"
    _rec_name = "nombre"
    _columns = {
        'nombre': fields.char("Nombre", size=64, required=True),
        'observacion': fields.text("Observacion", required=False),
        'cliente_ids': fields.one2many('res.partner','ruta_id','Cliente'),      
        'supervisor_id': fields.many2one('sgs.rutas.supervisor','Supervisor'),    
        'vendedor_id': fields.many2one('sgs.rutas.vendedor','Vendedor'),
    }
    _sql_constraints = [('nombre_unico','unique(nombre)','¡El nombre de la Propiedad debe ser único!'),
                        ('vendedor_unico','unique(vendedor_id)','¡Solo puede tener un vendedor!')]
sgs_rutas_ruta()

class sgs_rutas_supervisor(osv.Model):
    _name = "sgs.rutas.supervisor"
    _description = "Supervisor"
    _rec_name = "nombre"
    _columns = {
        'nombre': fields.char("Nombre", size=64, required=True),     
        'observacion': fields.text("Observacion", required=False),   
        'ruta_ids': fields.one2many('sgs.rutas.ruta','supervisor_id','Rutas'),
    }
sgs_rutas_supervisor()

class sgs_rutas_vendedor(osv.Model):
    _name = "sgs.rutas.vendedor"
    _description = "Vendedor"
    _rec_name = "nombre"
    _columns = {
        'nombre': fields.char("Nombre", size=64, required=True),  
        'observacion': fields.text("Observacion", required=False), 
        'ruta_ids': fields.one2many('sgs.rutas.ruta','vendedor_id','Rutas'),

    }  
    _sql_constraints = [('ruta_unico','unique(ruta_ids)','¡La Ruta debe ser única!')]
sgs_rutas_vendedor()

#Los Giros del Negocio del Cliente, almacenados en la BD
class sgs_rutas_gironegocio(osv.Model):
   _name= 'sgs.rutas.gironegocio'
   _description='Giros de Negocios del Cliente'
   _rec_name = "abreviatura"
   _columns = {      
      'abreviatura':fields.char('Abreviatura', size=4, required=True),
      'descripcion': fields.text("Descripcion", required=True),
      'cliente_ids': fields.one2many('res.partner','gironegocio_id','Cliente'), 
      # ... si necesitas más campos para otros propósitos
   }
   _sql_constraints = [('abreviatura_unico','unique(abreviatura)','¡La Abreviatura debe ser única!')]
sgs_rutas_gironegocio()

#Las Botellas almacenados en la BD
class sgs_rutas_botella(osv.Model):
   _name= 'sgs.rutas.botella'
   _description='Botellas del Cliente'
   _rec_name = "abreviatura"
   _columns = {      
      'abreviatura':fields.char('Abreviatura', size=4, required=True),
      'descripcion': fields.text("Descripcion", required=True),
      'cliente_ids': fields.one2many('res.partner','botella_id','Cliente'), 
      # ... si necesitas más campos para otros propósitos
   }
   _sql_constraints = [('abreviatura_unico','unique(abreviatura)','¡La Abreviatura debe ser única!')]
sgs_rutas_botella()

#Las Propiedades del Local almacenados en la BD
class sgs_rutas_propiedad(osv.Model):
   _name= 'sgs.rutas.propiedad'
   _description='Propiedad del Cliente'
   _rec_name = "abreviatura"
   _columns = {      
      'abreviatura':fields.char('Abreviatura', size=4, required=True),
      'descripcion': fields.text("Descripcion", required=True),
      'cliente_ids': fields.one2many('res.partner','propiedad_id','Cliente'), 
      # ... si necesitas más campos para otros propósitos
   }
   _sql_constraints = [('abreviatura_unico','unique(abreviatura)','¡La Abreviatura debe ser única!')]
sgs_rutas_propiedad()

#Las Clasificaciones del cliente en la BD
class sgs_rutas_clasificacion(osv.Model):
   _name= 'sgs.rutas.clasificacion'
   _description='Clasificacion del Cliente'
   _rec_name = "abreviatura"
   _columns = {      
      'abreviatura':fields.char('Abreviatura', size=4, required=True),
      'descripcion': fields.text("Descripcion", required=True),
      'cliente_ids': fields.one2many('res.partner','clasificacion_id','Cliente'), 
      # ... si necesitas más campos para otros propósitos
   }
   _sql_constraints = [('abreviatura_unico','unique(abreviatura)','¡La Abreviatura debe ser único!')]
sgs_rutas_clasificacion()

#Las Exclusividades del cliente en la BD
class sgs_rutas_exclusividad(osv.Model):
   _name= 'sgs.rutas.exclusividad'
   _description='Exclusividad del Cliente'
   _rec_name = "abreviatura"
   _columns = {      
      'abreviatura':fields.char('Abreviatura', size=4, required=True),
      'descripcion': fields.text("Descripcion", required=True),
      'cliente_ids': fields.one2many('res.partner','exclusividad_id','Cliente'), 
      # ... si necesitas más campos para otros propósitos
   }
   _sql_constraints = [('abreviatura_inico','unique(abreviatura)','¡La Abreviatura debe ser única!')]
sgs_rutas_exclusividad()

#Los Impactos del cliente en la BD
class sgs_rutas_impacto(osv.Model):
   _name= 'sgs.rutas.impacto'
   _description='Cliente de Impacto'
   _rec_name = "abreviatura"
   _columns = {      
      'abreviatura':fields.char('Abreviatura', size=2, required=True),
      'descripcion': fields.text("Descripcion", required=True),
      'cliente_ids': fields.one2many('res.partner','impacto_id','Cliente'), 
      # ... si necesitas más campos para otros propósitos
   }
   _sql_constraints = [('abreviatura_unico','unique(abreviatura)','¡La Abreviatura debe ser única!')]
sgs_rutas_impacto()
 





