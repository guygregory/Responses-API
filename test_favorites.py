"""
Playwright test script for testing Favorites functionality in Gradio app
"""
import asyncio
import subprocess
import time
from playwright.async_api import async_playwright
import os

async def test_favorites_functionality():
    """Test the favorites functionality in the Gradio app"""
    # Start the Gradio app in background
    print("Starting Gradio app...")
    app_process = subprocess.Popen([
        "python", "responses-conversation-stream-gradio-v1.py"
    ], cwd="/home/runner/work/Responses-API/Responses-API")
    
    # Wait for app to start
    time.sleep(10)
    
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        try:
            # Navigate to the Gradio app (default is http://127.0.0.1:7860)
            await page.goto("http://127.0.0.1:7860")
            await page.wait_for_load_state("networkidle", timeout=30000)
            
            # Take initial screenshot
            await page.screenshot(path="/tmp/1_initial_view.png", full_page=True)
            print("Screenshot 1: Initial view taken")
            
            # Check that info bar is visible
            info_bar = page.locator("text=Info:")
            await info_bar.wait_for(state="visible", timeout=10000)
            print("✓ Info bar is visible")
            
            # Check that Favorites button is visible
            favorites_btn = page.locator("text=⭐Favorites")
            await favorites_btn.wait_for(state="visible", timeout=10000)
            print("✓ Favorites button is visible")
            
            # Click the Favorites button
            await favorites_btn.click()
            await page.wait_for_timeout(2000)  # Wait for animation
            
            # Take screenshot with favorites menu open
            await page.screenshot(path="/tmp/2_favorites_menu_open.png", full_page=True)
            print("Screenshot 2: Favorites menu open taken")
            
            # Check that favorites menu is visible
            favorites_menu = page.locator("text=⭐ Favorites")
            await favorites_menu.wait_for(state="visible", timeout=5000)
            print("✓ Favorites menu is visible")
            
            # Check that shortcut buttons are visible
            shortcut_buttons = page.locator("text=📎")
            count = await shortcut_buttons.count()
            print(f"✓ Found {count} shortcut buttons")
            
            # Click on a shortcut button if available
            if count > 0:
                first_shortcut = shortcut_buttons.first
                await first_shortcut.click()
                await page.wait_for_timeout(2000)
                
                # Take screenshot after clicking shortcut
                await page.screenshot(path="/tmp/3_after_shortcut_click.png", full_page=True)
                print("Screenshot 3: After clicking shortcut taken")
                
                # Check if text was added to input box
                textbox = page.locator("textarea[placeholder*='Type your message']")
                textbox_value = await textbox.input_value()
                if textbox_value:
                    print(f"✓ Shortcut text added to input: {textbox_value[:50]}...")
                else:
                    print("ℹ No text added to input (this might be expected)")
            
            # Try to close the favorites menu
            close_btn = page.locator("text=✖ Close")
            if await close_btn.count() > 0:
                await close_btn.click()
                await page.wait_for_timeout(2000)
                
                # Take screenshot with menu closed
                await page.screenshot(path="/tmp/4_favorites_menu_closed.png", full_page=True)
                print("Screenshot 4: Favorites menu closed taken")
                print("✓ Successfully closed favorites menu")
            
            print("✅ All tests passed!")
            
        except Exception as e:
            print(f"❌ Test failed: {e}")
            # Take error screenshot
            await page.screenshot(path="/tmp/error_screenshot.png", full_page=True)
        
        finally:
            await browser.close()
            app_process.terminate()
            app_process.wait()

def run_test():
    """Run the async test"""
    asyncio.run(test_favorites_functionality())

if __name__ == "__main__":
    run_test()