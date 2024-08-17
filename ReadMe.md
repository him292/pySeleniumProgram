### Selenium - Web Automation

- WHat is Selenium: open source suite which helps automate browser. It contains:
  - Selenium IDE
    - a firefox extension whixh is used to record and playback
    - Problems:
      - maintaining test cases
      - code duplicates
      - you need to learn selenium IDE language
      - whenever window size changes -> test case fails
  - Selenium Webdriver
      - it supports many languages
      - Selenium RC (remote control) + wedrive -> Selenium 3
      - ![img.png](img.png)
  - Selenium Grid (Grid is multiple machines connected to each other)
- 2 versions:
  - Version 3 - Old -> JSON wire protcol
  - Version 4 ( released 2023 -> W3C protocol, selenium manager, relative)
- Selenium vs Playwright vs cypress
  - No reporting tool
  - multi tab support
  - Cross domain support
  - Drag and drop
  - Statuc waits but not dynamic
  - parallel test eexecution
  - Support for java, js, python
  - Though Playwright is the best tool but still Selenium is used widely
    - Playwright is owned by Microsoft
- Webdriver architecture
  - 
- Selenium not used in:
  - Load/Performance testing as it can slow down the system
  - not suitable when testing mobile apps
  - has difficulty interaCTING WITH CUSTOM controls or non-standard UI elements
  - cannot automate captchas
  - Audio or Video streaming
  - Security testing
  - API testing, mobile testing cannot be do

- Selenium 4 (W3C) version removed the "JSON wire protocol" (which adds the HTTP request and send to Server)
and tells the webdriver to handle everything
- Upgrade can also be done from Selenium 3 to 4

### Selenium Webdriver Architecture (9th AuG)

- Webdriver API is a set of classes and methods that allows you to interact with the browser using the code

- Headless browser - used when?
  - When we dont need to use UI
  - if there are alot test cases to cover (Ex: 5000)
    - These many test cases takes a lot of memory if we go with UI

### WAITS

- Time.sleep() - we dont use it much, its without any condition
- ImplicitWait() - not used much, because it adds wait to all the elements within the script
- Explicit Wait() - Mostly used. It waits until a certain condition is met
- Fluent Wait() - Used with a paramater (poll_frequency=value) when you want to wait for an element in certain
  interval (like after every second)


### Working with Dropdowns

2 Types:
- Static dropdown
- Dynamic Dropdown

- Static dropdown

element_select = driver.find_element(By.ID, "dropdown")
select = Select(element_select
select.select_by_visible_text("Option 2))


- Dynamic Dropdown 
  - Static with custom controls - controlled by JS executor
  - Pure dynamic - handled by JS executor, Action classes and Logic