import base64
import importlib.util
from pathlib import Path
import tempfile
import unittest
import urllib.parse
import xml.etree.ElementTree as E
import zlib

spec=importlib.util.spec_from_file_location("audit",Path(__file__).resolve().parents[1]/"scripts/audit_drawio.py")
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)

class AuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.path=Path(self.tmp.name)/"fixture.drawio"
        self.model=E.fromstring('''<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><mxCell id="start" parent="1" vertex="1" value="Start"><mxGeometry x="10" y="10" width="0" height="0"/></mxCell><mxCell id="end" parent="1" vertex="1"><mxGeometry x="40" y="10" width="0" height="0"/></mxCell><mxCell id="flow" parent="1" edge="1" source="start" target="end" drsRole="workflow"><mxGeometry relative="1"/></mxCell></root></mxGraphModel>''')
    def tearDown(self):self.tmp.cleanup()
    def result(self):
        E.ElementTree(self.model).write(self.path)
        return a.audit(self.path)
    def test_valid(self):
        r=self.result();self.assertFalse(r['errors']);self.assertEqual(r['pages'][0]['workflow_routes_checked'],1)
    def test_missing_endpoint(self):
        self.model.find(".//mxCell[@id='flow']").set('target','absent')
        self.assertTrue(any('missing target' in x for x in self.result()['errors']))
    def test_duplicate_id(self):
        E.SubElement(self.model.find('root'),'mxCell',id='start')
        self.assertTrue(any('duplicate' in x for x in self.result()['errors']))
    def test_parent_cycle(self):
        self.model.find(".//mxCell[@id='1']").set('parent','start')
        self.assertTrue(any('cycle' in x for x in self.result()['errors']))
    def test_short_arrow(self):
        self.model.find(".//mxCell[@id='end']/mxGeometry").set('x','15')
        self.assertTrue(any('shorter' in x for x in self.result()['errors']))
    def test_diagonal(self):
        self.model.find(".//mxCell[@id='end']/mxGeometry").set('y','30')
        self.assertTrue(any('diagonal' in x for x in self.result()['errors']))
    def test_missing_route_coverage(self):
        self.model.find(".//mxCell[@id='flow']").set('drsRole','wire')
        self.assertTrue(any('coverage absent' in x for x in self.result()['warnings']))
    def test_compressed_page(self):
        raw=urllib.parse.quote(E.tostring(self.model,encoding='unicode'),safe="~()*!.'").encode()
        compressor=zlib.compressobj(wbits=-15);encoded=base64.b64encode(compressor.compress(raw)+compressor.flush()).decode()
        root=E.Element('mxfile');E.SubElement(root,'diagram',name='Compressed').text=encoded
        E.ElementTree(root).write(self.path)
        self.assertFalse(a.audit(self.path)['errors'])
    def test_wrapped_cell(self):
        root=self.model.find('root');cell=root.find("mxCell[@id='start']");root.remove(cell);cell.attrib.pop('id')
        wrapper=E.SubElement(root,'object',id='start',label='Wrapped label');wrapper.append(cell)
        r=self.result();self.assertFalse(r['errors']);self.assertEqual(r['pages'][0]['labels'],1)
    def test_outside_frame(self):
        self.model.find(".//mxCell[@id='start']").set('parent','frame')
        root=self.model.find('root');frame=E.SubElement(root,'mxCell',id='frame',parent='1',vertex='1',drsRole='frame')
        E.SubElement(frame,'mxGeometry',x='0',y='0',width='5',height='5')
        self.assertTrue(any('outside' in x for x in self.result()['errors']))
    def test_nonfinite_geometry(self):
        self.model.find(".//mxCell[@id='end']/mxGeometry").set('x','nan')
        self.assertTrue(any('nonfinite' in x for x in self.result()['errors']))

if __name__=='__main__':unittest.main()
