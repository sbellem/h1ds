# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ShotRange'
        db.create_table(u'h1ds_shotrange', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('min_shot', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('max_shot', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'h1ds', ['ShotRange'])

        # Adding M2M table for field shot_ranges on 'Tree'
        db.create_table(u'h1ds_tree_shot_ranges', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tree', models.ForeignKey(orm[u'h1ds.tree'], null=False)),
            ('shotrange', models.ForeignKey(orm[u'h1ds.shotrange'], null=False))
        ))
        db.create_unique(u'h1ds_tree_shot_ranges', ['tree_id', 'shotrange_id'])


    def backwards(self, orm):
        # Deleting model 'ShotRange'
        db.delete_table(u'h1ds_shotrange')

        # Removing M2M table for field shot_ranges on 'Tree'
        db.delete_table('h1ds_tree_shot_ranges')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'h1ds.device': {
            'Meta': {'object_name': 'Device'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'latest_shot': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['h1ds.Shot']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'h1ds.filter': {
            'Meta': {'object_name': 'Filter'},
            'code': ('python_field.fields.PythonCodeField', [], {}),
            'data_dim': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['h1ds.FilterDim']", 'symmetrical': 'False'}),
            'data_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['h1ds.FilterDtype']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'h1ds.filterdim': {
            'Meta': {'object_name': 'FilterDim'},
            'code': ('python_field.fields.PythonCodeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'h1ds.filterdtype': {
            'Meta': {'object_name': 'FilterDtype'},
            'code': ('python_field.fields.PythonCodeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'h1ds.h1dssignal': {
            'Meta': {'object_name': 'H1DSSignal'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'h1ds.h1dssignalinstance': {
            'Meta': {'ordering': "('-time',)", 'object_name': 'H1DSSignalInstance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['h1ds.H1DSSignal']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'})
        },
        u'h1ds.node': {
            'Meta': {'object_name': 'Node'},
            'children': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'children_rel_+'", 'to': u"orm['h1ds.Node']"}),
            'dtype': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'has_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'n_channels': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'n_dimensions': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'subtree_hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        },
        u'h1ds.nodepath': {
            'Meta': {'object_name': 'NodePath'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nodes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['h1ds.Node']", 'through': u"orm['h1ds.PathMap']", 'symmetrical': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['h1ds.NodePath']", 'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'tree': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'h1ds.pagelet': {
            'Meta': {'object_name': 'Pagelet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'pagelet_type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '2048'})
        },
        u'h1ds.pageletcoordinates': {
            'Meta': {'object_name': 'PageletCoordinates'},
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pagelet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['h1ds.Pagelet']"}),
            'worksheet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['h1ds.Worksheet']"})
        },
        u'h1ds.pathmap': {
            'Meta': {'object_name': 'PathMap'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['h1ds.Node']"}),
            'node_path': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['h1ds.NodePath']"}),
            'shot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['h1ds.Shot']"})
        },
        u'h1ds.shot': {
            'Meta': {'object_name': 'Shot'},
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['h1ds.Device']", 'on_delete': 'models.PROTECT'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'h1ds.shotrange': {
            'Meta': {'object_name': 'ShotRange'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_shot': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_shot': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'h1ds.tree': {
            'Meta': {'object_name': 'Tree'},
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['h1ds.Device']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'shot_ranges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['h1ds.ShotRange']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'h1ds.usersignal': {
            'Meta': {'object_name': 'UserSignal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '2048'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'h1ds.worksheet': {
            'Meta': {'object_name': 'Worksheet'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pagelets': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['h1ds.Pagelet']", 'through': u"orm['h1ds.PageletCoordinates']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['h1ds']