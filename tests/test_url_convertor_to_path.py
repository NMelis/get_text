#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `url_convert_to_path` function."""

import unittest
from get_text.helper.url_convertor import url_query_convert_to_path


class TestUrlConvertToPath(unittest.TestCase):
    """Tests for `url_convert_to_path` function."""

    def test_url_with_type_web_page_file_txt(self):
        """TTests for `url_convert_to_path` function with some urls"""
        path, file_name = url_query_convert_to_path(
            'https://lenta.ru/news/2019/03/15/new_watch/', 'txt')
        self.assertEqual(path, 'lenta.ru/news/2019/03/15')
        self.assertEqual(file_name, 'new_watch.txt')

        path, file_name = url_query_convert_to_path(
            'https://moslenta.ru/city/'
            'pogoda-v-moskve-vzyala-kurs-na-poteplenie-17-03-2019.htm', 'txt')
        self.assertEqual(path, 'moslenta.ru/city')
        self.assertEqual(file_name, 'pogoda-v-moskve-vzyala-kurs-na-poteplenie'
                         '-17-03-2019.txt')

        path, file_name = url_query_convert_to_path(
            'https://moslenta.ru/razvlecheniya/udivitelnoe-ryadom.htm', 'txt')
        self.assertEqual(path, 'moslenta.ru/razvlecheniya')
        self.assertEqual(file_name, 'udivitelnoe-ryadom.txt')

        path, file_name = url_query_convert_to_path(
            'https://www.gazeta.ru/politics/2019/03/17_a_1224872.shtml/', 'txt')
        self.assertEqual(path, 'www.gazeta.ru/politics/2019/03')
        self.assertEqual(file_name, '17_a_1224872.txt')

        path, file_name = url_query_convert_to_path(
            'https://www.1tv.ru/news/2019-03-16/32045-v_novoy', 'txt')
        self.assertEqual(path, 'www.1tv.ru/news/2019-03-16')
        self.assertEqual(file_name, '32045-v_novoy.txt')

        path, file_name = url_query_convert_to_path(
            'https://www.1tv.ru/super_news.php', 'txt')
        self.assertEqual(path, 'www.1tv.ru/')
        self.assertEqual(file_name, 'super_news.txt')

