#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `get_text` package."""
import os
import unittest
from get_text.core.get_article import Article


class TestGetText(unittest.TestCase):
    """Tests for `get_text` package."""

    def test_iz_ru(self):
        txt, html_text = self._get_fixture_page_and_result_text('iz.ru')
        article = Article(html_text, 'iz.ru').run_parse()
        self.assertEqual(txt, article.template_active())

    def test_1tv(self):
        txt, html_text = self._get_fixture_page_and_result_text('www.1tv.ru')
        article = Article(html_text, 'www.1tv.ru').run_parse()
        self.assertEqual(txt, article.template_active())

    def test_lenta_ru(self):
        txt, html_text = self._get_fixture_page_and_result_text('lenta.ru')
        article = Article(html_text, 'lenta.ru').run_parse()
        self.assertEqual(txt, article.template_active())

    def test_lenta_ru_2(self):
        txt, html_text = self._get_fixture_page_and_result_text('lenta.ru_2')
        article = Article(html_text, 'lenta.ru').run_parse()
        self.assertEqual(txt, article.template_active())

    def test_habr_com(self):
        txt, html_text = self._get_fixture_page_and_result_text('habr.com')
        article = Article(html_text, 'habr.com').run_parse()
        self.assertEqual(txt, article.template_active())

    @staticmethod
    def _get_fixture_page_and_result_text(site_host):
        cwd = os.getcwd()
        path = os.path.join(cwd, 'fixture', site_host)
        txt = ""
        html = ""
        for file in os.listdir(path):
            if file.endswith(".txt"):
                with open(os.path.join(path, file)) as f:
                    txt = f.read()
            if file.endswith(".html"):
                with open(os.path.join(path, file)) as f:
                    html = f.read()
        return txt, html


