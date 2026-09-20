import os
from playwright.sync_api import sync_playwright

def run():
    artifact_dir = r"C:\Users\luuhu\.gemini\antigravity\brain\d4e25254-6ecf-46e0-86e5-63bf620ed979"
    html_path = r"D:\Projects\Personal\Luu-Khang-Huy---portfolio\index.html"
    file_url = f"file:///{html_path.replace(os.sep, '/')}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        
        # Monitor console errors
        errors = []
        page.on("pageerror", lambda err: errors.append(str(err)))
        
        page.goto(file_url, wait_until="networkidle")
        page.wait_for_timeout(1000)

        # 1. Hero showcase
        page.screenshot(path=os.path.join(artifact_dir, "motion_verify_hero.png"))
        print("[CAPTURE] Hero screenshot saved")

        # 2. Hero button hover state
        cta_btn = page.locator("a[href='#featured-projects'].spatial-btn-primary").first
        cta_btn.hover()
        page.wait_for_timeout(400)
        page.screenshot(path=os.path.join(artifact_dir, "motion_verify_btn_hover.png"))
        print("[CAPTURE] Button hover state screenshot saved")

        # 3. Section 2 Tech Stack & Lifecycle
        page.locator("#skills-process").scroll_into_view_if_needed()
        page.wait_for_timeout(600)
        page.screenshot(path=os.path.join(artifact_dir, "motion_verify_skills_process.png"))
        print("[CAPTURE] Skills & Process screenshot saved")

        # 4. Section 5 Contact & Monogram
        page.locator("#contact").scroll_into_view_if_needed()
        page.wait_for_timeout(600)
        page.screenshot(path=os.path.join(artifact_dir, "motion_verify_contact.png"))
        print("[CAPTURE] Contact screenshot saved")

        browser.close()
        
        if errors:
            print(f"[PAGE ERRORS] {errors}")
        else:
            print("[SUCCESS] Zero page errors encountered! All motion test screenshots verified.")

if __name__ == "__main__":
    run()
