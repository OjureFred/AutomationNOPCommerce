import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL =ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info('*************** Test_001_Login ****************')
        self.logger.info('*************** Verifying Home Page Title ******')
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        

        if act_title == "Your store. Login":
            self.driver.close()
            assert True 
            self.logger.info('*************** Home Page Title Passed ****************')

        else:
            self.driver.save_screenshot('.\\Screenshots\\'  + 'test_homePageTitle.png')
            self.driver.close()
            assert False
            self.logger.info('*************** Home Page Title Failed ****************')
    
    def test_login(self, setup):
        self.logger.info('*************** Test_001_Login ****************')
        self.logger.info('*************** Verifying Login ******')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info('*************** Login Passed ****************')
        else: 
            self.driver.save_screenshot('.\\Screenshots\\'  + 'test_Login.png')
            self.driver.close()
            assert False
            self.logger.info('*************** Login Failed ****************')


