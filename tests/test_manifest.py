from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

TOOL=Path(__file__).resolve().parents[1]/'scripts/artifact_manifest.py'

class ManifestTests(unittest.TestCase):
    def test_changed_source_invalidates_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);source=p/'source.drawio';export=p/'export.svg';record=p/'record.json'
            source.write_text('source version one');export.write_text('export version one')
            subprocess.run([sys.executable,str(TOOL),'record',str(source),str(export),'--manifest',str(record)],check=True,capture_output=True)
            self.assertEqual(subprocess.run([sys.executable,str(TOOL),'verify','--manifest',str(record)],capture_output=True).returncode,0)
            source.write_text('source version two')
            self.assertEqual(subprocess.run([sys.executable,str(TOOL),'verify','--manifest',str(record)],capture_output=True).returncode,1)
    def test_empty_manifest_is_not_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            record=Path(tmp)/'record.json';record.write_text('{"files": []}')
            self.assertNotEqual(subprocess.run([sys.executable,str(TOOL),'verify','--manifest',str(record)],capture_output=True).returncode,0)
