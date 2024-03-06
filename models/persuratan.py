from odoo import api, fields, models

class data_suratmasuk(models.Model):
    _name = 'surat.masuk'
    _description = 'surat masuk'

    no = fields.Integer(string='No')
    tanggal = fields.Date(string='Tanggal')
    nosurat = fields.Integer(string='Nomor')
    tanggalsurat = fields.Date(string='Tanggal')
    tofrom = fields.Char(string='Dari/Kepada')
    ringkasan = fields.Char(string='Ringkasan')
    keterangan = fields.Char(string='Keterangan')
    file_surat = fields.Binary(string='File Surat')
    
class data_suratkeluar(models.Model):
    _name = 'surat.keluar'
    _description = 'surat keluar'

class data_penugasan(models.Model):
    _name = 'data.penugasan'
    _description = 'data_penugasan'
    
    name = fields.Char(string='Nama')
    jabatan = fields.Char(string='Jabatan')
    niy = fields.Char(string='Niy')
    alamat = fields.Char(string='Alamat')
    tanggal = fields.Date(string='Tanggal')
    jam = fields.Datetime(string='Jam')
    tempat = fields.Char(string='Tempat')    