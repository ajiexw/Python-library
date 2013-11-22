#coding=utf-8
from Model import Model

class Goods(Model):
    table_name = 'Goods'
    column_names = ['title']
    decorator = [('Pagination',{}),
        ('Search',{'index':'songshu', 'display_page':10, 'max': 1000, 'page_count': 30, 'firsttext':'第一页', 'lasttext':'末页'}),
    ]

    table_template = \
        '''CREATE TABLE IF NOT EXISTS {$table_name} (
            {$table_name}id       int unsigned                not null auto_increment,
            title                 varchar(100)  charset utf8  not null default '',
            created               timestamp                   not null default  current_timestamp,
            primary key ({$table_name}id)
        )ENGINE=InnoDB;'''
