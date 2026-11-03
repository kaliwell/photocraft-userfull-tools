import threading
import unittest
from unittest.mock import Mock
from photocraft_ai.native import NativeWorker

class ReferenceRemovalTests(unittest.TestCase):
    def test_old_clients_cannot_submit_reference_images(self):
        worker=NativeWorker(None)
        with self.assertRaisesRegex(ValueError,'Codex AI'):
            worker.submit({'mode':'generate','prompt':'test','references':[{'name':'old.png','data':'AAAA'}]})
        self.assertFalse(worker.snapshot()['busy'])

    def test_normal_generation_request_remains_available(self):
        service=Mock(); service.lock=threading.Lock()
        target=Mock(index=0); target.name='test'
        service.bridge.active_image.return_value=target
        service.bridge._revision.return_value=1
        worker=NativeWorker(service)
        worker._run({'mode':'generate','prompt':'test','document':{'index':0,'name':'test','revision':1}})
        self.assertFalse(worker.snapshot()['error'])
        self.assertNotIn('references',service.prepare.call_args.kwargs)
        service.apply.assert_called_once()
