# Generated by Django 2.2.10 on 2020-04-02 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0069_smsconfig_template_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='smsconfig',
            name='signature_i18n',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='国际-签名'),
        ),
        migrations.AddField(
            model_name='smsconfig',
            name='template_activate_i18n',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='国际-用户激活文案模板ID'),
        ),
        migrations.AddField(
            model_name='smsconfig',
            name='template_code_i18n',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='国际-验证码通用文案模板ID'),
        ),
        migrations.AddField(
            model_name='smsconfig',
            name='template_login_i18n',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='国际-登录文案模板ID'),
        ),
        migrations.AddField(
            model_name='smsconfig',
            name='template_register_i18n',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='国际-注册文案模板ID'),
        ),
        migrations.AddField(
            model_name='smsconfig',
            name='template_reset_mobile_i18n',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='国际-用户重置手机文案模板ID'),
        ),
        migrations.AddField(
            model_name='smsconfig',
            name='template_reset_pwd_i18n',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='国际-重置密码文案模板ID'),
        ),
    ]
