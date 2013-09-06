# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'ConfigDBLoadingDir.folder'
        db.alter_column('h1ds_configdb_configdbloadingdir', 'folder', self.gf('django.db.models.fields.CharField')(max_length=1024))


    def backwards(self, orm):
        
        # Changing field 'ConfigDBLoadingDir.folder'
        db.alter_column('h1ds_configdb_configdbloadingdir', 'folder', self.gf('django.db.models.fields.FilePathField')(max_length=100))


    models = {
        'h1ds_configdb.configdbfile': {
            'Meta': {'object_name': 'ConfigDBFile'},
            'dbfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'filetype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['h1ds_configdb.ConfigDBFileType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'md5sum': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'h1ds_configdb.configdbfiletype': {
            'Meta': {'object_name': 'ConfigDBFileType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mimetype': ('django.db.models.fields.CharField', [], {'max_length': '126'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'h1ds_configdb.configdbloadingdir': {
            'Meta': {'object_name': 'ConfigDBLoadingDir'},
            'folder': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'force_overwrite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'h1ds_configdb.configdbproperty': {
            'Meta': {'object_name': 'ConfigDBProperty'},
            'configdb_file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['h1ds_configdb.ConfigDBFile']"}),
            'configdb_propertytype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['h1ds_configdb.ConfigDBPropertyType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value_float': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'value_integer': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'value_string': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'h1ds_configdb.configdbpropertytype': {
            'Meta': {'object_name': 'ConfigDBPropertyType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'value_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['h1ds_configdb']
