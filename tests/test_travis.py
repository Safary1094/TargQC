from tests import BaseTargQC


class TravisTests(BaseTargQC):
    def test_01_bed3(self):
        self._test('bed3', bams=self.bams, bed=self.bed3, threads=2)

    def test_02_wgs(self):
        self._test('wgs', bams=self.bams, threads=2)
