"""Optional rendered-check tests. Run with DRS_BROWSER_TESTS=1 after browser setup."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]

@unittest.skipUnless(os.environ.get('DRS_BROWSER_TESTS')=='1','Optional: set DRS_BROWSER_TESTS=1 with Playwright/Chromium available')
class BrowserTests(unittest.TestCase):
    def inspect(self,body):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'fixture.svg';report=Path(tmp)/'result.json'
            path.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="240" height="120" viewBox="0 0 240 120">'+body+'</svg>')
            result=subprocess.run(['node',str(ROOT/'scripts/review_svg.mjs'),str(path),'--report',str(report)],capture_output=True,text=True)
            self.assertTrue(report.exists(),result.stderr)
            return result.returncode,json.loads(report.read_text())
    def test_visible_svg_text(self):
        code,report=self.inspect('<text x="20" y="40" font-size="16">Readable</text>')
        self.assertEqual(code,0);self.assertEqual(report['labels'],1)
    def test_text_overlap_is_rejected(self):
        code,report=self.inspect('<text x="20" y="40" font-size="16">First label</text><text x="20" y="40" font-size="16">Second label</text>')
        self.assertEqual(code,1);self.assertTrue(report['textOverlaps'])
    def test_frame_contact_is_rejected(self):
        code,report=self.inspect('<rect x="20" y="20" width="100" height="60" fill="none" stroke="black" stroke-width="2"/><text x="15" y="45" font-size="16">Touches</text>')
        self.assertEqual(code,1);self.assertTrue(report['ruleContacts'])
    def test_no_text_is_not_success(self):
        code,report=self.inspect('<rect x="20" y="20" width="100" height="60"/>')
        self.assertEqual(code,1);self.assertEqual(report['labels'],0)
