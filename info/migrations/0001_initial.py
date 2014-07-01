# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SitewideContent'
        db.create_table(u'info_sitewidecontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phonenumber', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('logo', self.gf('mezzanine.core.fields.FileField')(max_length=200)),
        ))
        db.send_create_signal(u'info', ['SitewideContent'])


    def backwards(self, orm):
        # Deleting model 'SitewideContent'
        db.delete_table(u'info_sitewidecontent')


    models = {
        u'info.sitewidecontent': {
            'Meta': {'object_name': 'SitewideContent'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            'phonenumber': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['info']