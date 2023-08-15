import unittest
import urllib.request

class WebsiteTest(unittest.TestCase):
    def test_website_loading(self):
        url = "http://atg.world"
        response = urllib.request.urlopen(url)
        status_code = response.getcode()
        self.assertEqual(status_code, 200, f"Website failed to load. Status code: {status_code}")

        content = response.read()
        self.assertTrue(content, "Website content is empty.")

        title = content.decode('utf-8').split('<title>')[1].split("</title>")[0]
        print("Website loaded successfully!")
        print("Website Ttile:", title)

        self.assertNotEqual(len(content), 0, "Website content is empty.")


if __name__ == '__main__':
    unittest.main()


