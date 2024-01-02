
class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver

        self.search_box = (By.ID, "navbar-query")
        self.search_type_dropdown = (By.ID, "navbar-search-category-select")
        self.search_button = (By.ID, "navbar-submit-button")

    def fill_search_data(self, search_query, search_type):
        search_box_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_box)
        )
        search_box_element.clear()
        search_box_element.send_keys(search_query)

        search_type_dropdown_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_type_dropdown)
        )
        search_type_dropdown_element.click()
        search_type_option = search_type_dropdown_element.find_element_by_xpath(f"//option[text()='{search_type}']")
        search_type_option.click()

    def click_search_button(self):
        search_button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button)
        )
        search_button_element.click()
driver = webdriver.Chrome()
driver.get("https://www.imdb.com/search/name/")
imdb_search_page = IMDbSearchPage(driver)
imdb_search_page.fill_search_data("Tom Hanks", "Actor")
imdb_search_page.click_search_button()
driver.quit()
