from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import random

# Path to msedgedriver
EDGE_DRIVER_PATH = r"your\\path\\to\\msedgedriver.exe"

# Your full Google Form URL
FORM_URL = "https://docs.google.com/xxxxxxx/xxxxxxxx"

# Number of submissions
NUM_SUBMISSIONS = 150

for submission in range(NUM_SUBMISSIONS):
    print(f"\n📨 Submission {submission + 1}/{NUM_SUBMISSIONS}")

    
    options = Options()
    #options.add_argument('--headless')  # Uncomment to hide browser

    
    driver = webdriver.Edge(service=EdgeService(EDGE_DRIVER_PATH), options=options)
    driver.get(FORM_URL)
    time.sleep(3)  


    question_containers = driver.find_elements(By.XPATH, '//div[@class="Qr7Oae"]')
    submission_log = []  

    for i, container in enumerate(question_containers):
        try:
            
            question_label_element = container.find_element(By.XPATH, './/div[@class="geS5n"]/div/div/div[@role="heading"]/span[@class="M7eMe"]')
            question_text = question_label_element.text.strip()
            print(f"\n--- Processing Question {i + 1}: {question_text} ---")

            
            radio_group = container.find_elements(By.XPATH, './/div[@role="radiogroup"]')
            if radio_group:
                options = radio_group[0].find_elements(By.XPATH, './/div[@role="radio"]')
                if options:
                    choice = random.choice(options)
                    driver.execute_script("arguments[0].scrollIntoView(true);", choice)
                    time.sleep(0.3)
                    choice.click()
                    try:
                        selected_label_element = choice.find_element(By.XPATH, './/div[@class="geS5n"]/span')
                        selected_text = selected_label_element.text.strip()
                    except Exception as e_label:
                        selected_text = f"Could not retrieve radio label: {e_label}"
                    submission_log.append(f"Question {question_text}: {selected_text}")
                    print(f"✔ Radio: Selected - {selected_text}")
                    time.sleep(0.3)
                else:
                    print(f" Radio question {i + 1}: No options found.")

            
            checkbox_group = container.find_elements(By.XPATH, './/div[@role="list"]')
            if checkbox_group:
                try:
                    checkbox_items = checkbox_group[0].find_elements(By.XPATH, './/div[@role="listitem"]//div[@role="checkbox" and @tabindex="0"]')
                    if checkbox_items:
                        print(f" Checkbox question {i + 1}: Found {len(checkbox_items)} options.")
                        num_choices = random.randint(1, len(checkbox_items))
                        selected_items = random.sample(checkbox_items, num_choices)
                        selected_texts = []
                        
                        for item in selected_items:
                            try:
                                
                                driver.execute_script("arguments[0].scrollIntoView(true);", item)
                                time.sleep(0.3)
                                
                                
                                try:
                                    item.click()
                                except:
                                    driver.execute_script("arguments[0].click();", item)
                                    
                                
                                label = item.find_element(By.XPATH, '../../..//span[@class="aDTYNe snByac n5vBHf OIC90c"]')
                                selected_text = label.text.strip()
                                selected_texts.append(selected_text)
                                print(f"✔ Checkbox: Selected - {selected_text}")
                                time.sleep(0.3)
                            except Exception as e_checkbox_interact:
                                print(f" Error interacting with checkbox: {e_checkbox_interact}")
                        
                        if selected_texts:
                            submission_log.append(f"Question {question_text}: {', '.join(selected_texts)}")
                    else:
                        print(f" Checkbox question {i + 1}: No options found.")
                except Exception as e_checkbox:
                    print(f" Error processing checkbox question {i + 1}: {e_checkbox}")

        except Exception as e_question:
            print(f" Error processing question {i + 1} (finding container or parts): {e_question}")

    time.sleep(1)  

    
    try:
        submit_btn = driver.find_element(By.XPATH,
            '//span[contains(text(),"Submit") or contains(text(),"জমা দিন")]/ancestor::div[@role="button"]'
        )
        submit_btn.click()
        print(" Form submitted.")
    except Exception as e_submit:
        print(f" Could not find Submit button. Skipping this run. Error: {e_submit}")

    
    print("\n Submitted Answers:")
    for log_entry in submission_log:
        print(log_entry)

    time.sleep(2)
    driver.quit()  

    # Delay between submissions (adjust if needed)
    time.sleep(1)
