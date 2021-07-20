import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class Ratification(models.Model):
    id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=250)


class Sector(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    name_ar = models.CharField(max_length=50)

    def __str__(self):
        return self.name_ar


class Device(models.Model):
    id = models.AutoField(primary_key=True, help_text=_("Id"), verbose_name=_("مسلسل"))
    entry_date = models.DateField(default=datetime.date.today, verbose_name=_("تاريخ الدخول"))
    delivery_entity = models.ForeignKey(Sector, on_delete=models.PROTECT, verbose_name=_("شعبة/فرع"))
    delivery_engineer = models.CharField(max_length=50, verbose_name=_("المندوب"))
    type = models.CharField(max_length=50, verbose_name=_("اسم الصنف"))
    serial_number = models.CharField(max_length=50, help_text=_("Serial Number"), verbose_name=_("سريال"))
    _is_custody = models.BooleanField(default=False, verbose_name=_("عهدة"))
    receiver_engineer = models.CharField(max_length=50, verbose_name=_("مهندس الاستقبال"))
    fixing_engineer = models.CharField(max_length=50, verbose_name=_("مهندس الصيانة"))
    action = models.CharField(max_length=250, verbose_name=_("الاجراء المتخذ"))
    maintenance_date = models.DateField(null=True, blank=True, verbose_name=_("تاريخ الاصلاح"))
    maintenance_state = models.CharField(max_length=50, choices=[(' تم الأصلاح من الفرع', 'تم الأصلاح من الفرع'),
                                                                 (' تم الأصلاح من الورشة', 'تم الأصلاح من الورشة'),
                                                                 (' تم التكهين من الورشة', 'تم التكهين من الورشة'),
                                                                 ('عاطل', 'عاطل')], verbose_name=_("تمام الأصلاح"),
                                         blank=True)
    receiver_name = models.CharField(max_length=50, verbose_name=_("أسم المندوب"), blank=True)
    sender_name = models.CharField(max_length=50, verbose_name=_("القائم بالتسليم"), blank=True)
    sending_date = models.DateField(verbose_name=_("تاريخ التسليم"), null=True, blank=True)
    register_date = models.DateField(verbose_name=_("تاريخ تسجيل العهدة"), blank=True, null=True)
    register_person = models.CharField(max_length=50, verbose_name=_("القائم بالتسجيل"), blank=True)
    ratification_doc = models.CharField(max_length=50, choices=[('صح', 'صح'), ('خطأ', 'خطأ')],
                                        verbose_name=_("طباعة طلب التصديق"), blank=True)
    ratification_date = models.DateField(verbose_name=_("تاريخ التصديق"), blank=True, null=True)
    register_number = models.CharField(max_length=50, verbose_name=_("رقم التصديق"), blank=True)
    exiting_date_1 = models.DateField(verbose_name=_("تاريخ الخروج إلى الورشة"), blank=True, null=True)
    responsible_person_1 = models.CharField(max_length=50, verbose_name=_("القائم بالمأمورية"), blank=True)
    exiting_date_2 = models.DateField(verbose_name=_("تاريخ الاستلام من الورشة"), blank=True, null=True)
    responsible_person_2 = models.CharField(max_length=50, verbose_name=_("القائم بالمأمورية"), blank=True)
    exiting_date_3 = models.DateField(verbose_name=_("تاريخ الرجوع من الورشة"), blank=True, null=True)
    responsible_person_3 = models.CharField(max_length=50, verbose_name=_("القائم بالمأمورية"), blank=True)
    exiting_date_4 = models.DateField(verbose_name=_("تاريخ الدخول إلى الفرع"), blank=True, null=True)
    responsible_person_4 = models.CharField(max_length=50, verbose_name=_("القائم بالمأمورية"), blank=True)

    class Meta:
        verbose_name = _("Device")
        verbose_name_plural = _("Devices")

    def save(self, *args, **kwargs):
        try:
            Ratification.objects.get(serial_number=self.serial_number)
            self._is_custody = True
        except Ratification.DoesNotExist:
            self._is_custody = False
        super(Device, self).save(*args, **kwargs)
