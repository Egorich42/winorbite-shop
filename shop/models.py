#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

class Category(models.Model):
    icon = models.ImageField(upload_to='products/', blank=True, verbose_name="Изображение")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True,blank=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'        

    def  __unicode__(self): 
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/', blank=True, verbose_name="Изображение товара")
    parameter = models.CharField(max_length=200, db_index=True, blank=True, verbose_name="Параметр")
    parameter_value =  models.CharField(max_length=50, db_index=True, blank=True, verbose_name="значение параметра")
    second_parameter = models.CharField(max_length=200, db_index=True, blank=True, verbose_name="Параметр")
    second_parameter_value = models.CharField(max_length=50, db_index=True, blank=True, verbose_name="значение параметра")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена бел.рубли")
    price_rub = models.DecimalField(max_digits=10,  blank=True, default='1',  decimal_places=2, verbose_name="Цена рубли")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
   
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])


contacts_text = ['<h1>Наши контакты:</h1><br><ul><li><img src="/media/social-links/mail.png" alt="e-mail addres"><span>winterorbite@gmail.com</span></li><li><img src="/media/social-links/mail.png" alt="e-mail addres"><span>e.g.hutter@gmail.com</span></li><li><img src="/media/social-links/skype.png" alt="skype-contack"><span>bigegorich</span></li><li><img src="/media/social-links/velcom.png" alt="velcome-phone-number"><span>+375 44 749 01 87</span></li><li><img src="/media/social-links/mts.png" alt="mts-phone-number"><span>+375 333 516 975</span></li></ul>']
payment_text =['<p><h2>Доставка:</h2></p><ul><h3>По территории Беларуси:</h3><li>В течении 3 - 6 дней</li><li>Стоимость - 4 бел.рубля</li> <li>По Минску, а так же при заказе от 50 бел.рублей - бесплатно</li><h3>На территории России и Украины</h3><li>В течении 7 - 8 дней</li><li>Стоимость - 150 рублей</li> <li>При заказе от 2000 бел.рублей - бесплатно</li></ul></section><section class="payment"><p><h2>Способы оплаты:</h2></p><ul><li><h3>Наличный расчет</h3> При доставке курьером вы оплачиваете заказ наличными после проверки комплектности и качества товаров.</li> <li><h3>Наложенный платеж </h3>Наложенный платеж — это возможность оплаты заказа в отделении почтовой связи в момент его получения.</li></ul>']
privacy_text = ['<h3>Правила защиты информации о пользователях сайта <a href="http://winorbite.com/">  winorbite.com</a></h3><p>Настоящие Правила являются официальным документом интернет-магазина «Зимняя орбита», расположенного по адресу г. Минск, пер. Козлова, 7/г, каб.501, (далее – Администрация Сайта), и определяют порядок обработки и защиты информации о физических лицах, пользующихся услугами интернет-сайта<a href="http://winorbite.com/">   http://winorbite.com</a> (далее – Сайт) и его сервисов (далее – Пользователи). </p> <h4>Цели обработки информации</h4><p>Администрация Сайта осуществляет обработку информации о Пользователях, в том числе их персональных данных, в целях выполнения обязательств Администрации Сайта перед Пользователями в отношении использования Сайта и его сервисов. </p><h4>Персональные данные Пользователей</h4><p>Персональные данные Пользователей включают в себя предоставляемые Пользователями : имя, номер мобильного телефона и адрес электронной почты;</p><h4>Обработка персональных данных</h4><p>Обработка персональных данных осуществляется на основе принципов:<ul><li>законности целей и способов обработки персональных данных;</li><li>добросовестности;</li>  <li>соответствия целей обработки персональных данных целям, заранее определенным и заявленным при сборе персональных данных, а также полномочиям Администрации Сайта;</li>  <li>соответствия объема и характера обрабатываемых персональных данных, способов обработки персональных данных целям обработки персональных данных;</li>    <li>недопустимости объединения созданных для несовместимых между собой целей баз данных, содержащих персональные данные.</li></ul></p><h4>Сбор персональных данных</h4><p>Сбор персональных данных Пользователя осуществляется на Сайте при регистрации заказа.Персональные данные  предоставляются Пользователем и являются минимально необходимыми при регистрации заказа.</p><h4>Хранение и использование персональных данных</h4><p>Персональные данные пользователей хранятся исключительно на электронных носителях и обрабатываются с использованием автоматизированных систем, за исключением случаев, когда неавтоматизированная обработка персональных данных необходима в связи с исполнением требований законодательства.</p><p>Срок хранения персональных данных Пользователя - 120 дней со дня регистрации заказа.</p><h4>Передача персональных данных</h4><p>Персональные данные Пользователей не передаются каким-либо третьим лицам.</p><p>Предоставление персональных данных Пользователей по запросу государственных органов (органов местного самоуправления) осуществляется в порядке, предусмотренном законодательством.</p></section>']