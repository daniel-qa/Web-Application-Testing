
element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='ui-dialog-buttonset']/button[@class='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only']/span[contains(.,'Continue')]")))
driver.execute_script("arguments[0].click();", element)


element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='ui-dialog-buttonset']/button[@class='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only']/span[contains(.,'Continue')]")))
element.location_once_scrolled_into_view
element.click()
