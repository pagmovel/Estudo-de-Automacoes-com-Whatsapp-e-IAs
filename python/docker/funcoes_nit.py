import lxml

# import locale
import xlsxwriter
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import numpy as np
import psycopg2
import datetime
from datetime import date
import logging
import sys
import os
from time import sleep
from datetime import date, timedelta
from pytz import timezone
from typing import Any
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import psycopg2.extras as extras
from sqlalchemy import create_engine
import sqlalchemy.types as sqltypes
from sqlalchemy.exc import SQLAlchemyError
import glob
import skimpy
from skimpy import clean_columns
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from anticaptchaofficial.recaptchav2proxyless import *

# from selenium.webdriver.chrome.options import Options

sys.path.append("../")
# import usuario as user
# from funcoesbb import FuncoesBB

import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from decouple import config
import mimetypes
from bs4 import BeautifulSoup
import locale

import fasteners


class Nit:

    def __init__(
        self, robo="painel", show_browser=True, db_prod=False, v_browser="chrome"
    ):

        self.Keys = Keys
        self.v_browser = v_browser

        if v_browser == "chrome":
            self.option = webdriver.ChromeOptions()
            #             self.option.page_load_strategy='none'
            self.option.add_argument("--disable-dev-shm-usage")
            self.option.add_argument("--no-sandbox")

            if show_browser:
                self.option.add_argument("--window-size=1700,1500")
                self.option.add_argument("--force-device-scale-factor=0.65")
            else:
                self.option.add_argument("--headless")
                self.option.add_argument("--window-size=1920,1200")

                # pass

            self.option.add_argument("--default-shm-size=32m")
            self.option.add_argument("--proxy-bypass-list=*")
            self.option.add_argument("--proxy-server='direct://'")

            self.option.add_argument("--allow-insecure-localhost")
            self.option.add_argument("--log-level=3")
            self.option.add_argument("--incognito")  # 🔹 Ativa o modo anônimo

        #     browser = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()),options=option)
        #             self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)

        elif v_browser == "edge":
            from selenium.webdriver.edge.options import Options

            self.options = Options()
            self.options.page_load_strategy = "none"

            if show_browser == False:
                self.options.add_argument("--headless")
                # option.add_argument("--window-size=1920,1200")

            self.options.add_argument("--no-sandbox")
            self.options.add_argument("--disable-dev-shm-usage")
            self.options.page_load_strategy = "none"

    #             self.browser = webdriver.Edge(options = options)

    def horarioAtual(self):
        fuso_horario = timezone("America/Fortaleza")
        return str(datetime.now().astimezone(fuso_horario))

    def setLoginParams(self, username, password):
        self.username = username
        self.password = password

    def openBrowser(self):
        if self.v_browser == "edge":
            self.browser = webdriver.Edge(options=self.options)
        elif self.v_browser == "chrome":
            self.browser = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=self.option
            )
            print("abrindo o chrome")

    def closeBrowser(self):
        self.browser.close()

    def getUrl(self, url):
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url  # Adiciona "https://" se o prefixo estiver ausente
        self.browser.get(url)

    def alertas(self, text, mensagem_saida=False, timeout=10):
        try:
            # Aguarda que o alert seja exibido (timeout de 10 segundos)
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present())

            # Alterna para o alert
            alert = self.browser.switch_to.alert

            # Obtem o texto do alert
            alert_text = alert.text

            # Aceita o alert (confirma o botão OK)
            if alert_text == text:
                alert.accept()
                if mensagem_saida:
                    print(mensagem_saida)
                else:
                    print("Alert confirmado.")
            else:
                return False

        except TimeoutException:
            print("Nenhum alert foi exibido dentro do tempo limite.")
            return False

    def findElement(self, obj=None, tipo="XPATH", xpath=None, timeout=15):
        tipo = self.tipoXpath(tipo)
        try:
            #             return obj.find_elements(tipo, xpath)
            return WebDriverWait(obj, timeout).until(
                EC.visibility_of_element_located((tipo, xpath))
            )

        except TimeoutException:
            return False
        except Exception as e:
            return e

    def tipoXpath(self, tipo):
        if tipo == "XPATH":
            tipo = By.XPATH
        elif tipo == "ID":
            tipo = By.ID
        elif tipo == "CSS_SELECTOR":
            tipo = By.CSS_SELECTOR
        elif tipo == "CLASS_NAME":
            tipo = By.CLASS_NAME
        else:
            return False

        return tipo
    
    
    def getElementJavascript(self, tipo="XPATH", xpath=None, timout=15, click=False):
        tipo = self.tipoXpath(tipo)
        wait = WebDriverWait(self.browser, timout)
        elemento = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

        # Emula o clique via JavaScript
        self.browser.execute_script("arguments[0].click();", elemento)
        

    def getElement(self, tipo="XPATH", xpath=None, timeout=15, click=False):
        tipo = self.tipoXpath(tipo)

        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located((tipo, xpath))
            )

            if element:
                if click:
                    element.click()
                else:
                    return element

        except TimeoutException:
            return False
        except Exception as e:
            return False

    def checkText(self, tipo="XPATH", attribute="*", text=None, timeout=5, logs=False):
        """
        Verifica se existe um determinado texto na tela.

        :param tipo: Tipo de localizador ('XPATH', 'ID', etc.). Padrão: 'XPATH'.
        :param attribute: Nome da tag HTML ou '*' para qualquer tag. Padrão: '*'.
        :param text: Texto a ser verificado. Obrigatório.
        :param timeout: Tempo máximo de espera em segundos. Padrão: 5.
        :return: True se o texto for encontrado; False caso contrário.
        """
        if text is None:
            raise ValueError("[checkText] O parâmetro 'text' é obrigatório.")

        if not attribute or not isinstance(attribute, str):
            raise ValueError(
                "[checkText] O parâmetro 'attribute' deve ser uma string válida."
            )

        try:
            # Constrói um XPath mais robusto para capturar o texto em qualquer posição dentro do <td>
            xpath = f'//{attribute}[contains(., "{text}")]'
            tipo_id = self.tipoXpath(
                tipo
            )  # Converte o tipo para o formato esperado pelo Selenium

            if logs:
                print(f"[checkText] TIPO: {tipo_id} | XPATH: {xpath}")

            # Aguarda a presença do elemento (independente de estar visível)
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((tipo_id, xpath))
            )

            # Busca todos os elementos que podem conter o texto
            elements = self.browser.find_elements(tipo_id, xpath)

            # Depuração: imprime os elementos encontrados
            if logs:
                print(
                    f"[checkText] Encontrados {len(elements)} elementos com XPath '{xpath}'"
                )
                for el in elements:
                    print(
                        f"[checkText] Texto encontrado: {el.text.strip()} | HTML: {el.get_attribute('outerHTML')}"
                    )

            # Verifica se o texto está realmente presente em algum dos elementos encontrados
            if any(text in el.text for el in elements):
                return True

            if logs:
                print(
                    f"[checkText] O texto '{text}' não foi encontrado em nenhum dos elementos identificados."
                )
            return False

        except TimeoutException:
            if logs:
                print(
                    f"[checkText] Timeout ao procurar o texto '{text}' com o XPath '{xpath}'."
                )
            return False
        except NoSuchElementException:
            if logs:
                print(f"[checkText] Elemento não encontrado com o XPath '{xpath}'.")
            return False
        except Exception as e:
            if logs:
                print(f"[checkText] Erro inesperado: {e}")
            return False

    def login(self, xpath_user, xpath_passw, xpath_btn):
        # Campo usuario
        input_user = self.getElement(xpath=xpath_user)
        if input_user:
            input_user.clear()
            input_user.send_keys(self.username)
        else:
            print("Não encontrei campo usuario.")

        # campo senha
        input_password = self.getElement(xpath=xpath_passw)
        if input_password:
            input_password.clear()
            input_password.send_keys(self.password)
        else:
            print("Não encontrei campo senha.")

        # botão para logar
        btn_login = self.getElement(xpath=xpath_btn, click=True)
        #         if btn_login:
        #             btn_login.click()
        #         else:
        if btn_login == False:
            print("Não encontrei botão para logar.")
