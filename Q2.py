import unittest

class TestNormalizeCompanyName(unittest.TestCase):

    def test_basic_variants(self):
        self.assertEqual(
            normalize_company_name("CAF softsol"),
            "CAF SoftSol India Pvt Ltd."
        )

        self.assertEqual(
            normalize_company_name("CAF solution"),
            "CAF SoftSol India Pvt Ltd."
        )

        self.assertEqual(
            normalize_company_name("CAF           softSolution  India Pvt Limited"),
            "CAF SoftSol India Pvt Ltd."
        )

    def test_case_and_spacing(self):
        self.assertEqual(
            normalize_company_name("  caf   SoftSol "),
            "CAF SoftSol India Pvt Ltd."
        )

    def test_empty_and_none(self):
        self.assertIsNone(normalize_company_name(""))
        self.assertIsNone(normalize_company_name("   "))
        self.assertIsNone(normalize_company_name(None))

    def test_unrelated_company(self):
        self.assertEqual(
            normalize_company_name("Google India Private Limited"),
            "Google India Private Limited"
        )

if __name__ == "__main__":
    unittest.main()
