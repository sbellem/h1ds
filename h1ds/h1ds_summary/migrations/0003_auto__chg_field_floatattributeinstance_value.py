# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'FloatAttributeInstance.value'
        db.alter_column('h1ds_summary_floatattributeinstance', 'value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True))


    def backwards(self, orm):
        
        # Changing field 'FloatAttributeInstance.value'
        db.alter_column('h1ds_summary_floatattributeinstance', 'value', self.gf('django.db.models.fields.FloatField')())


    models = {
        'h1ds_summary.floatattributeinstance': {
            'Meta': {'object_name': 'FloatAttributeInstance'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['h1ds_summary.SummaryAttribute']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['h1ds_summary.Shot']"}),
            'value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'h1ds_summary.shot': {
            'Meta': {'object_name': 'Shot'},
            'shot': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'h1ds_summary.summaryattribute': {
            'Meta': {'object_name': 'SummaryAttribute'},
            'data_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['h1ds_summary']
